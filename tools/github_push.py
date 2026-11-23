# -*- coding: utf-8 -*-
"""用 GitHub Git Data API 推送整个仓库（绕过卡住的 HTTPS git 传输栈）。
复用本机 jingji 项目已验证的凭据获取方式：git credential fill。
"""
import subprocess, urllib.request, urllib.error, ssl, json, base64, sys, time

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

OWNER, REPO, BRANCH = "TianDiHuAng", "shenhua", "main"
API = "https://api.github.com"
ctx = ssl._create_unverified_context()

out = subprocess.run(
    ["D:/Git/Git/bin/git.exe", "credential", "fill"],
    input=b"protocol=https\nhost=github.com\n\n", capture_output=True
).stdout.decode("utf-8", "ignore")
cred = dict(l.split("=", 1) for l in out.strip().splitlines() if "=" in l)
TOKEN = cred.get("password", "")
if not TOKEN:
    print("未取到 GitHub 凭据"); sys.exit(1)
print("凭据已获取（用户 %s）" % cred.get("username", "?"))

def api(method, path, payload=None):
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    headers = {
        "User-Agent": "ShenhuaPush/1.0",
        "Authorization": "Bearer " + TOKEN,
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if data:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(API + path, data=data, headers=headers, method=method)
    for attempt in range(5):
        try:
            r = urllib.request.urlopen(req, timeout=25, context=ctx)
            return json.loads(r.read())
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "ignore")
            print("HTTP", e.code, path, body[:300], file=sys.stderr)
            raise
        except Exception as e:
            if attempt == 2:
                raise
            time.sleep(1 + attempt)

files = [f for f in subprocess.run(["git", "ls-files"], capture_output=True).stdout.decode("utf-8").strip().splitlines() if f.strip()]
print("待推送文件:", len(files))

# 空仓库需先用 Contents API 提交一个文件来初始化，否则 Git Data API 返回 409
try:
    api("GET", "/repos/%s/%s/git/ref/heads/%s" % (OWNER, REPO, BRANCH))
except urllib.error.HTTPError:
    seed = "README.md" if "README.md" in files else files[0]
    with open(seed, "rb") as f:
        seed_content = f.read()
    api("PUT", "/repos/%s/%s/contents/%s" % (OWNER, REPO, seed),
        {"message": "init: 初始化仓库", "content": base64.b64encode(seed_content).decode(), "branch": BRANCH})
    print("空仓库已用 Contents API 初始化（%s）" % seed)
    time.sleep(2)

tree = []
for i, path in enumerate(files, 1):
    with open(path, "rb") as f:
        content = f.read()
    print("  blob %d/%d %s (%d B)" % (i, len(files), path, len(content)))
    blob = api("POST", "/repos/%s/%s/git/blobs" % (OWNER, REPO),
               {"content": base64.b64encode(content).decode(), "encoding": "base64"})
    mode = "100755" if ".sh" in path else "100644"
    tree.append({"path": path, "mode": mode, "type": "blob", "sha": blob["sha"]})
    if i % 40 == 0 or i == len(files):
        print("blobs", i, "/", len(files))

t = api("POST", "/repos/%s/%s/git/trees" % (OWNER, REPO), {"base_tree": None, "tree": tree})
print("tree:", t["sha"][:12])

parent = None
try:
    ref = api("GET", "/repos/%s/%s/git/ref/heads/%s" % (OWNER, REPO, BRANCH))
    parent = ref["object"]["sha"]
    print("parent commit:", parent[:12])
except urllib.error.HTTPError:
    print("空仓库或分支不存在，无 parent")

msg = "宗教与神话比较库：118条目/122来源/零JS静态站点/双源与待核实校验"
payload = {"message": msg, "tree": t["sha"]}
if parent:
    payload["parents"] = [parent]
commit = api("POST", "/repos/%s/%s/git/commits" % (OWNER, REPO), payload)
print("commit:", commit["sha"][:12])

try:
    api("GET", "/repos/%s/%s/git/ref/heads/%s" % (OWNER, REPO, BRANCH))
    api("PATCH", "/repos/%s/%s/git/refs/heads/%s" % (OWNER, REPO, BRANCH),
        {"sha": commit["sha"], "force": False})
    print("ref updated")
except urllib.error.HTTPError:
    api("POST", "/repos/%s/%s/git/refs" % (OWNER, REPO),
        {"ref": "refs/heads/%s" % BRANCH, "sha": commit["sha"]})
    print("ref created")

print("PUSH DONE: https://github.com/%s/%s (branch %s)" % (OWNER, REPO, BRANCH))
