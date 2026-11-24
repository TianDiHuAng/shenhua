#!/bin/bash
# 网络不稳时的补推脚本：重试推送并用远端哈希核验。
# 用法：bash tools/push_retry.sh
cd "$(dirname "$0")/.." || exit 1
LOCAL=$(git rev-parse HEAD)
for i in 1 2 3 4 5; do
  echo "push 尝试 $i ..."
  timeout 120 git -c http.sslBackend=schannel -c http.connectTimeout=20 push -u origin HEAD 2>&1 | tail -2
  REMOTE=$(timeout 40 git -c http.sslBackend=schannel ls-remote origin master 2>/dev/null | cut -f1)
  if [ "$REMOTE" = "$LOCAL" ]; then
    echo "OK: 远端已是 $LOCAL"
    exit 0
  fi
  echo "远端=$REMOTE 本地=$LOCAL，30 秒后重试"
  sleep 30
done
echo "FAIL: 仍未同步"
exit 1
