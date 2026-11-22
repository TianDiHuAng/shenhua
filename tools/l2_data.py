# -*- coding: utf-8 -*-
"""L2 深度升级内容池。每条七节：来源文本/故事梗概已在L1/版本差异/解读/比较/SVG/待核实。
纪律：学者与学派必须真实可考；比较必须有 sources.json 中的 basis_source；不编造数字与引文。
"""

L2_DATA = {
    "myth-norse": {
        "level": "L2",
        "source_text": "北欧神话主要见于中世纪冰岛文献：《诗体埃达》保存古老众神诗歌，《散文埃达》由斯诺里·斯蒂德吕松系统化叙述并以欧赫墨罗斯主义（Euhemerism，神祇历史化）方式解释诸神，另有萨迦与《贝奥武甫》等日耳曼材料。这些文本多经基督教时代抄写者记录，其原始形态与成文年代存在学术讨论。",
        "versions": [
            "《诗体埃达》的预言诗与神祇诗歌较少系统化叙述，保留较古老的众神形象与宇宙末日（诸神的黄昏）意象。",
            "《散文埃达》把诗歌材料整理为连贯的创世与神祇谱系，并明确提出诸神原为古代英雄/君王的历史化解释，属于作者的系统化处理。",
            "萨克索·格拉玛提库斯《丹麦人的业绩》以拉丁文改写北欧传说，同样带有历史化与基督教时代立场，与冰岛材料形成对照。"
        ],
        "interpretations": [
            {"holder": "Georges Dumézil", "school": "印欧比较神话学（三功能假说）", "view": "以主权、战争、丰产三功能解析印欧神系，北欧的奥丁、托尔、弗雷被作为三功能的对应案例；此为学派模型，非唯一解释。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "把宇宙树与诸神的黄昏置于宇宙周期与“永恒回归”（eternal return）的框架中理解，强调神话时间与仪式的关联。"},
            {"holder": "John Lindow", "school": "北欧神话与民俗研究", "view": "强调现存文本的中世纪语境与口传—书写过渡，主张区分诗歌材料与后世的系统化叙述。"}
        ],
        "comparisons": [
            {"tradition": "希腊神话", "basis_source": "aca-comparative-myth", "note": "印欧比较神话学（Dumézil、Puhvel）在天父/风暴神等功能位置上比较北欧与希腊神系，属有文献依据的学派比较，不主张直接同源。"},
            {"tradition": "印度神话（吠陀）", "basis_source": "aca-gods-indo-europeans", "note": "Dumézil 的三功能模型将北欧与吠陀神系并置比较；此为理论框架下的对照，学界对其适用性仍有讨论。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>北欧神话结构示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>北欧神话结构示意（尤弥尔—诸神—宇宙树）</text><line x1='380' y1='118' x2='380' y2='170' stroke='currentColor' opacity='0.5'/><line x1='180' y1='170' x2='580' y2='170' stroke='currentColor' opacity='0.5'/><line x1='180' y1='170' x2='180' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='170' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='580' y1='170' x2='580' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='246' x2='380' y2='292' stroke='currentColor' opacity='0.5'/><rect x='280' y='82' width='200' height='36' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='106' text-anchor='middle' fill='var(--svg-text)' font-size='14'>原初巨人 尤弥尔</text><rect x='100' y='212' width='160' height='34' fill='var(--svg-node)' stroke='currentColor'/><text x='180' y='234' text-anchor='middle' fill='var(--svg-text)' font-size='14'>奥丁（主权）</text><rect x='300' y='212' width='160' height='34' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='234' text-anchor='middle' fill='var(--svg-text)' font-size='14'>托尔（战争）</text><rect x='500' y='212' width='160' height='34' fill='var(--svg-node)' stroke='currentColor'/><text x='580' y='234' text-anchor='middle' fill='var(--svg-text)' font-size='14'>弗雷（丰产）</text><rect x='270' y='292' width='220' height='40' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='318' text-anchor='middle' fill='var(--svg-text)' font-size='14'>宇宙树 尤克特拉希尔</text></svg>",
        "pending_notes": "1) 《诗体埃达》诸诗的确切成文年代有争论；2) 斯诺里的历史化解释是否忠实于更早传统，学界有分歧；3) John Lindow 与萨克索《丹麦人的业绩》均未录入 sources.json，其观点/材料作为学界代表列举，待补来源条目；4) 三功能模型为学派框架，不替读者下结论。",
        "needs_verification": True
    },
    "myth-egyptian": {
        "level": "L2",
        "source_text": "埃及神话的材料跨越数千年，主要包括古王国金字塔文、中王国棺椁文与新王国《亡灵书》，另有神庙铭文与希腊罗马时期记录。不同时期与地点的创世叙事并不统一，赫利奥波利斯、孟菲斯、底比斯等地各有传统。",
        "versions": [
            "赫利奥波利斯传统以阿图姆（或拉）为原初神，经舒与泰芙努特、盖布与努特展开为九柱神谱系。",
            "孟菲斯神学把创世归于普塔神的思想与言语，属神学中心转移后的系统化表达。",
            "底比斯传统抬高阿蒙并与拉结合为阿蒙—拉；新王国时期的阿肯那顿改革短暂推行阿顿崇拜，改革后恢复旧有神系。"
        ],
        "interpretations": [
            {"holder": "Henri Frankfort", "school": "古代近东思想研究", "view": "主张埃及与美索不达米亚的创世叙事以神话意象把握宇宙秩序，与现代抽象哲学的因果推演方式不同，不应以后者标准误读。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "把创世叙事与尼罗河泛滥的季节性循环、王权仪式的重演相联系，视神话为对宇宙秩序的周期性确认。"},
            {"holder": "James P. Allen", "school": "埃及学（宗教文本研究）", "view": "强调埃及创世文本的多元并存，主张各中心传统是并行的神学表达而非单线演进。"}
        ],
        "comparisons": [
            {"tradition": "美索不达米亚神话", "basis_source": "aca-before-philosophy", "note": "Frankfort 等对近东两大传统的宇宙观作并置比较，指出二者均以神话意象表达秩序，但侧重不同；此为有文献依据的比较。"},
            {"tradition": "希腊神话", "basis_source": "aca-golden-bough", "note": "Frazer 讨论奥西里斯与地中海地区死而复生神祇的相似性，属早期比较宗教学的经典议题，其具体结论在学界有争论。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>埃及创世传统对照示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>埃及创世传统对照（三大中心）</text><line x1='160' y1='150' x2='160' y2='200' stroke='currentColor' opacity='0.5'/><line x1='380' y1='150' x2='380' y2='200' stroke='currentColor' opacity='0.5'/><line x1='600' y1='150' x2='600' y2='200' stroke='currentColor' opacity='0.5'/><rect x='60' y='92' width='200' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='160' y='116' text-anchor='middle' fill='var(--svg-text)' font-size='14'>赫利奥波利斯</text><text x='160' y='138' text-anchor='middle' fill='var(--svg-text)' font-size='13'>阿图姆—九柱神</text><rect x='280' y='92' width='200' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='116' text-anchor='middle' fill='var(--svg-text)' font-size='14'>孟菲斯</text><text x='380' y='138' text-anchor='middle' fill='var(--svg-text)' font-size='13'>普塔—言语创世</text><rect x='500' y='92' width='200' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='600' y='116' text-anchor='middle' fill='var(--svg-text)' font-size='14'>底比斯</text><text x='600' y='138' text-anchor='middle' fill='var(--svg-text)' font-size='13'>阿蒙—拉</text><rect x='60' y='200' width='200' height='58' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='160' y='224' text-anchor='middle' fill='var(--svg-text)' font-size='13'>金字塔文—棺椁文</text><text x='160' y='246' text-anchor='middle' fill='var(--svg-text)' font-size='13'>亡灵书</text><rect x='280' y='200' width='200' height='58' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='224' text-anchor='middle' fill='var(--svg-text)' font-size='13'>神庙铭文</text><text x='380' y='246' text-anchor='middle' fill='var(--svg-text)' font-size='13'>王权仪式</text><rect x='500' y='200' width='200' height='58' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='600' y='224' text-anchor='middle' fill='var(--svg-text)' font-size='13'>阿肯那顿改革</text><text x='600' y='246' text-anchor='middle' fill='var(--svg-text)' font-size='13'>阿顿崇拜（短暂）</text><text x='380' y='318' text-anchor='middle' fill='var(--svg-text)' font-size='13'>说明：三大中心的传统并存，非单线演进</text></svg>",
        "pending_notes": "1) 阿肯那顿改革的确切年代与影响范围学界有不同估计，正文未列具体数字；2) James P. Allen 的著作未录入 sources.json，待补；3) Frazer 的比较结论属早期学派观点，已标注争论。",
        "needs_verification": True
    },
    "myth-mesopotamian": {
        "level": "L2",
        "source_text": "美索不达米亚神话主要保存在楔形文字泥板中，包括苏美尔语与阿卡德语文献。创世史诗、洪水叙事、王表与史诗《吉尔伽美什》构成核心材料，不同时期与城邦的传统并不统一，且大量文本仍有残缺。",
        "versions": [
            "《巴比伦创世史诗》以马尔杜克与提亚马特的斗争为中心，叙述天地与人类的建立，并抬高巴比伦主神的地位。",
            "《阿特拉哈西斯》叙述洪水与人类再生，与《吉尔伽美什史诗》中的洪水段落存在情节对应，二者关系为学界研究议题。",
            "苏美尔王表把王权起源归于天降，与创世史诗的王权观形成对照；苏美尔语与阿卡德语版本在神名与重点上存在差异。"
        ],
        "interpretations": [
            {"holder": "Thorkild Jacobsen", "school": "美索不达米亚宗教史", "view": "以 Circuit of the gods 等概念分析苏美尔—阿卡德的神祇组织与城邦政治的对应，强调神话叙事与政治秩序的关联。"},
            {"holder": "Samuel Noah Kramer", "school": "苏美尔学", "view": "通过泥板翻译与整理指出苏美尔创世思想的独特性，强调其与后世闪族传统的承继与差异。"},
            {"holder": "Henri Frankfort", "school": "古代近东思想研究", "view": "把美索不达米亚宇宙观作为与希腊哲学思想对照的类型，主张前者以神话意象而非抽象推演表达秩序。"}
        ],
        "comparisons": [
            {"tradition": "埃及神话", "basis_source": "aca-before-philosophy", "note": "Frankfort 将美索不达米亚与埃及的宇宙观并置比较，指出二者同属近东神话思维但气质不同；有文献依据。"},
            {"tradition": "希腊神话", "basis_source": "aca-comparative-myth", "note": "比较神话学讨论近东创世/洪水母题与希腊神话的关系，学界对影响路径与程度有争论，此处并列呈现不作定论。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>美索不达米亚神话文本群示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>美索不达米亚神话文本群（创世·洪水·王权）</text><line x1='380' y1='120' x2='380' y2='168' stroke='currentColor' opacity='0.5'/><line x1='160' y1='168' x2='600' y2='168' stroke='currentColor' opacity='0.5'/><line x1='160' y1='168' x2='160' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='168' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='600' y1='168' x2='600' y2='212' stroke='currentColor' opacity='0.5'/><rect x='280' y='84' width='200' height='36' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='108' text-anchor='middle' fill='var(--svg-text)' font-size='14'>楔形文字泥板</text><rect x='60' y='212' width='200' height='56' fill='var(--svg-node)' stroke='currentColor'/><text x='160' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>巴比伦创世史诗</text><text x='160' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='13'>马尔杜克—提亚马特</text><rect x='280' y='212' width='200' height='56' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>洪水叙事</text><text x='380' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='13'>阿特拉哈西斯—吉尔伽美什</text><rect x='500' y='212' width='200' height='56' fill='var(--svg-node)' stroke='currentColor'/><text x='600' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>苏美尔王表</text><text x='600' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='13'>天降王权</text><rect x='230' y='312' width='300' height='40' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='338' text-anchor='middle' fill='var(--svg-text)' font-size='13'>苏美尔语 / 阿卡德语版本并存，文本多有残缺</text></svg>",
        "pending_notes": "1) 洪水叙事两版本的关系与先后学界仍有讨论；2) 大量泥板文本残缺，正文未给具体数字；3) Jacobsen、Kramer 的具体论点以其代表著作概括，细节待逐条核对引文。",
        "needs_verification": True
    },
    "myth-chinese": {
        "level": "L2",
        "source_text": "中国神话散见于《山海经》《楚辞》《庄子》等典籍，系统性的创世叙述出现较晚（如三国时期文献中的盘古传说，其辑佚性质与年代待核实）。与部分拥有长篇创世史诗的传统不同，中国上古神话多以片段形式保存，后经整理与再叙述。",
        "versions": [
            "《山海经》保存大量神话地理与神祇片段，叙事简短，多不交代完整情节脉络。",
            "《楚辞》中的《天问》以疑问形式列举宇宙与神话传说，保留了若干远古母题的线索。",
            "盘古、女娲等创世与造人神话的系统叙述多见于较晚文献，其形成年代与早期口传关系是研究议题。"
        ],
        "interpretations": [
            {"holder": "袁珂", "school": "中国神话学（神话整理与研究）", "view": "通过辑录与整理散见文献，指出中国神话具有片段化特征，并强调神话与上古社会意识的关联；其整理工作影响深远。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "以宇宙创生与“永恒回归”（eternal return）的框架理解创世神话的一般结构，可作为比较参照，不直接等同于对中国材料的专门结论。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "主张神话思维具有普遍的逻辑结构，为分析神话中的对立与中介提供方法论参照；此为该学派的一般立场。"}
        ],
        "comparisons": [
            {"tradition": "印度神话", "basis_source": "aca-eternal-return", "note": "以 Eliade 的创世母题框架作现象学层面的对照，属于比较宗教学的一般框架，不主张具体文本间的传播关系。"},
            {"tradition": "北欧神话", "basis_source": "aca-eternal-return", "note": "以 Eliade 的创世母题框架把盘古化生与北欧原初巨人躯体化生作现象学层面的并置；此为纯框架性参照，Puhvel 的印欧比较材料不直接涵盖中国，不推断源流。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>中国神话文献与母题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>中国神话文献与母题（片段化传统）</text><line x1='150' y1='150' x2='150' y2='204' stroke='currentColor' opacity='0.5'/><line x1='380' y1='150' x2='380' y2='204' stroke='currentColor' opacity='0.5'/><line x1='610' y1='150' x2='610' y2='204' stroke='currentColor' opacity='0.5'/><rect x='70' y='96' width='160' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='150' y='120' text-anchor='middle' fill='var(--svg-text)' font-size='14'>山海经</text><text x='150' y='140' text-anchor='middle' fill='var(--svg-text)' font-size='13'>神话地理</text><rect x='300' y='96' width='160' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='120' text-anchor='middle' fill='var(--svg-text)' font-size='14'>楚辞·天问</text><text x='380' y='140' text-anchor='middle' fill='var(--svg-text)' font-size='13'>疑问形式</text><rect x='530' y='96' width='160' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='610' y='120' text-anchor='middle' fill='var(--svg-text)' font-size='14'>庄子</text><text x='610' y='140' text-anchor='middle' fill='var(--svg-text)' font-size='13'>哲学化引用</text><rect x='70' y='204' width='160' height='54' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='150' y='228' text-anchor='middle' fill='var(--svg-text)' font-size='13'>神祇与异物</text><text x='150' y='248' text-anchor='middle' fill='var(--svg-text)' font-size='13'>片段叙事</text><rect x='300' y='204' width='160' height='54' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='228' text-anchor='middle' fill='var(--svg-text)' font-size='13'>宇宙诸问</text><text x='380' y='248' text-anchor='middle' fill='var(--svg-text)' font-size='13'>母题线索</text><rect x='530' y='204' width='160' height='54' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='610' y='228' text-anchor='middle' fill='var(--svg-text)' font-size='13'>寓言化</text><text x='610' y='248' text-anchor='middle' fill='var(--svg-text)' font-size='13'>哲学转用</text><rect x='230' y='310' width='300' height='44' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='338' text-anchor='middle' fill='var(--svg-text)' font-size='13'>盘古·女娲：系统叙述多见于较晚文献</text></svg>",
        "pending_notes": "1) 盘古传说最早文献出处的辑佚性质与年代待核实；2) 袁珂的具体论点未录入 sources.json；Lévi-Strauss 仅录入《结构人类学》方法论通论，其中国神话相关具体论点待核；3) 神话片段化的判断为学界通行看法，具体材料需逐条核对。",
        "needs_verification": True
    },
    "myth-hindu": {
        "level": "L2",
        "source_text": "印度神话的材料包括吠陀颂歌、两大史诗与往世书等，跨越漫长的形成期。吠陀诸神与后世往世书的三相神体系在重点与神学上差异显著，奥义书与史诗则构成重要的过渡与转折。",
        "versions": [
            "吠陀颂歌以因陀罗、阿耆尼、苏摩等神祇为中心，侧重祭祀与赞颂，未形成后世的三相神格局。",
            "奥义书把讨论重心转向梵与自我的哲学问题，神话叙事在此被重新阐释。",
            "史诗与往世书确立梵天、毗湿奴、湿婆的三相神框架，并发展出化身与 Bhakti（虔信）等主题。"
        ],
        "interpretations": [
            {"holder": "Georges Dumézil", "school": "印欧比较神话学（三功能假说）", "view": "把吠陀神系作为印欧三功能结构的重要证据，并与伊朗、北欧材料比较；该模型在学界影响大但也有批评。"},
            {"holder": "Wendy Doniger", "school": "芝加哥学派（宗教史与文本研究）", "view": "强调印度神话的多义性与阐释史，关注文本如何在不同语境中被重读；主张警惕单一化解读。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "从宇宙轴、神话时间与现代性的对照理解印度宇宙观，为跨文化比较提供现象学框架。"}
        ],
        "comparisons": [
            {"tradition": "波斯神话", "basis_source": "aca-gods-indo-europeans", "note": "Dumézil 的印欧比较把印度与伊朗（波斯）材料并置，属有文献依据的学派比较；具体对应关系学界有讨论。"},
            {"tradition": "北欧神话", "basis_source": "aca-comparative-myth", "note": "比较神话学在印欧语系框架内对照印度与北欧神系，不主张直接文本传播，仅记录学术比较。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>印度神话发展阶段示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>印度神话发展阶段（吠陀—奥义书—史诗往世书）</text><line x1='140' y1='150' x2='380' y2='150' stroke='currentColor' opacity='0.5'/><line x1='380' y1='150' x2='620' y2='150' stroke='currentColor' opacity='0.5'/><line x1='140' y1='150' x2='140' y2='196' stroke='currentColor' opacity='0.5'/><line x1='380' y1='150' x2='380' y2='196' stroke='currentColor' opacity='0.5'/><line x1='620' y1='150' x2='620' y2='196' stroke='currentColor' opacity='0.5'/><rect x='60' y='96' width='160' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='140' y='120' text-anchor='middle' fill='var(--svg-text)' font-size='14'>吠陀</text><text x='140' y='140' text-anchor='middle' fill='var(--svg-text)' font-size='13'>自然神·祭祀</text><rect x='300' y='96' width='160' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='120' text-anchor='middle' fill='var(--svg-text)' font-size='14'>奥义书</text><text x='380' y='140' text-anchor='middle' fill='var(--svg-text)' font-size='13'>梵我·哲学转向</text><rect x='540' y='96' width='160' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='620' y='120' text-anchor='middle' fill='var(--svg-text)' font-size='14'>史诗·往世书</text><text x='620' y='140' text-anchor='middle' fill='var(--svg-text)' font-size='13'>三相神·化身</text><rect x='60' y='196' width='160' height='54' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='140' y='220' text-anchor='middle' fill='var(--svg-text)' font-size='13'>因陀罗</text><text x='140' y='240' text-anchor='middle' fill='var(--svg-text)' font-size='13'>阿耆尼·苏摩</text><rect x='300' y='196' width='160' height='54' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='220' text-anchor='middle' fill='var(--svg-text)' font-size='13'>梵与自我</text><text x='380' y='240' text-anchor='middle' fill='var(--svg-text)' font-size='13'>神话重释</text><rect x='540' y='196' width='160' height='54' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='620' y='220' text-anchor='middle' fill='var(--svg-text)' font-size='13'>梵天·毗湿奴</text><text x='620' y='240' text-anchor='middle' fill='var(--svg-text)' font-size='13'>湿婆·虔信</text><text x='380' y='322' text-anchor='middle' fill='var(--svg-text)' font-size='13'>阶段为叙述便利而划分，各传统实际并存且相互交叠</text></svg>",
        "pending_notes": "1) 吠陀、奥义书、史诗与往世书的形成年代跨度大且难以精确，正文未列具体年数；2) Dumézil 三功能模型与 Doniger 的阐释立场均有学界争论；3) 细分阶段为叙述便利之划分，不表示严格的时间先后顺序。",
        "needs_verification": True
    },
    "myth-japanese": {
        "level": "L2",
        "source_text": "日本神话主要见于《古事记》与《日本书纪》，二者成书于奈良时代，以天皇世系为中心整理神话与历史传说；另有序、祝词等口传材料。两部书在记事与措辞上存在差异，均带有编纂时代的政治语境。",
        "versions": [
            "《古事记》以散文与诗歌混用，叙述从宇宙生成到天皇世系的连续谱系，语言与叙事更具文学性。",
            "《日本书纪》采用汉文编年体，部分神话记录附异文，显示编纂时对多种材料的取舍。",
            "祝词等口传材料与两部正史的记述并不完全一致，为研究地方与仪式传统提供旁证。"
        ],
        "interpretations": [
            {"holder": "本居宣长", "school": "国学（Japanology/国文学）", "view": "主张区分中国式道德化解读与日本古典的固有精神，强调以文本语言本身理解神话；此立场在思想史上有影响也有批评。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "可从创世、太阳神与王权神话的一般结构作跨文化对照，属现象学框架的比较参照。"},
            {"holder": "Donald L. Philippi", "school": "日本神话译介与研究", "view": "强调《古事记》作为文学与神话文本的独特性，指出其叙事与编纂意图的复杂性。"}
        ],
        "comparisons": [
            {"tradition": "中国神话", "basis_source": "aca-comparative-myth", "note": "比较研究常就东亚创世与王权神话作对照，此处仅记录有文献依据的母题层面比较，不主张具体传播路径。"},
            {"tradition": "希腊神话", "basis_source": "aca-eternal-return", "note": "以创世与王权神话的现象学框架作一般对照，属比较宗教学的框架性参照。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>日本神话文本与谱系示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>日本神话文本与谱系（示意）</text><rect x='80' y='82' width='260' height='56' fill='var(--svg-node)' stroke='currentColor'/><text x='210' y='106' text-anchor='middle' fill='var(--svg-text)' font-size='14'>古事记</text><text x='210' y='126' text-anchor='middle' fill='var(--svg-text)' font-size='13'>散文诗歌混用·文学性</text><rect x='420' y='82' width='260' height='56' fill='var(--svg-node)' stroke='currentColor'/><text x='550' y='106' text-anchor='middle' fill='var(--svg-text)' font-size='14'>日本书纪</text><text x='550' y='126' text-anchor='middle' fill='var(--svg-text)' font-size='13'>汉文编年·附异文</text><line x1='210' y1='138' x2='210' y2='182' stroke='currentColor' opacity='0.5'/><line x1='550' y1='138' x2='550' y2='182' stroke='currentColor' opacity='0.5'/><line x1='210' y1='182' x2='550' y2='182' stroke='currentColor' opacity='0.5'/><line x1='380' y1='182' x2='380' y2='222' stroke='currentColor' opacity='0.5'/><rect x='280' y='222' width='200' height='40' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='248' text-anchor='middle' fill='var(--svg-text)' font-size='14'>天照大神·皇祖神话</text><line x1='380' y1='262' x2='380' y2='302' stroke='currentColor' opacity='0.5'/><rect x='230' y='302' width='300' height='40' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='328' text-anchor='middle' fill='var(--svg-text)' font-size='13'>两书记事有差异，均带编纂时代语境</text></svg>",
        "pending_notes": "1) 两部正史的编纂年代与材料来源学界有讨论；2) 本居宣长、Philippi 的具体论点待逐条核对原文，著作未完整录入 sources.json；3) 祝词等口传材料与正史的对应关系尚需专门研究。",
        "needs_verification": True
    },
    "myth-maya": {
        "level": "L2",
        "source_text": "玛雅神话的材料包括殖民时期记录的《波波尔·乌》、考古铭文、编年史与民族志资料。不同时期与城邦的信仰并不统一，且大量材料经殖民时代转录，解读依赖语言学、图像学与考古学的综合。",
        "versions": [
            "《波波尔·乌》以基切玛雅语叙述创世、玉米人的造就与英雄双子传说，是现存最系统的玛雅神话文本之一。",
            "古典期铭文与陶器图像反映的是城邦王权与祭仪语境，与殖民时期文本之间隔着漫长时段，不能直接等同。",
            "不同玛雅群体的口传与民族志材料显示地方差异，研究者谨慎地把它们与古代材料对应。"
        ],
        "interpretations": [
            {"holder": "Linda Schele", "school": "玛雅碑铭与艺术史研究", "view": "通过铭文与图像解读玛雅王权与宇宙观，强调视觉材料与文字材料互证；其具体解读在学界有讨论。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "可从创世与宇宙轴的一般母题对玛雅材料作现象学层面的对照，属框架性参照而非专门结论。"},
            {"holder": "Karl A. Taube", "school": "中美洲考古与图像学", "view": "强调图像与考古证据对理解玛雅神祇的重要性，主张跨区域比较需以材料为基础。"}
        ],
        "comparisons": [
            {"tradition": "阿兹特克神话", "basis_source": "aca-short-history-myth", "note": "比较神话学通论常把中美洲两大传统并置，此处仅记录母题层面的一般比较，不主张细节同源。"},
            {"tradition": "美索不达米亚神话", "basis_source": "aca-eternal-return", "note": "以创世母题的现象学框架作对照，属比较宗教学的一般参照，非具体传播关系的论断。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>玛雅神话材料来源示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>玛雅神话材料来源（互证关系）</text><rect x='80' y='96' width='180' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='120' text-anchor='middle' fill='var(--svg-text)' font-size='14'>波波尔·乌</text><text x='170' y='142' text-anchor='middle' fill='var(--svg-text)' font-size='13'>殖民期转录</text><rect x='290' y='96' width='180' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='120' text-anchor='middle' fill='var(--svg-text)' font-size='14'>古典期铭文</text><text x='380' y='142' text-anchor='middle' fill='var(--svg-text)' font-size='13'>城邦王权</text><rect x='500' y='96' width='180' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='120' text-anchor='middle' fill='var(--svg-text)' font-size='14'>考古与图像</text><text x='590' y='142' text-anchor='middle' fill='var(--svg-text)' font-size='13'>陶器·石刻</text><line x1='170' y1='156' x2='380' y2='218' stroke='currentColor' opacity='0.5'/><line x1='380' y1='156' x2='380' y2='218' stroke='currentColor' opacity='0.5'/><line x1='590' y1='156' x2='380' y2='218' stroke='currentColor' opacity='0.5'/><rect x='270' y='218' width='220' height='48' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='248' text-anchor='middle' fill='var(--svg-text)' font-size='14'>综合解读</text><rect x='230' y='308' width='300' height='42' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='334' text-anchor='middle' fill='var(--svg-text)' font-size='13'>不同时期与城邦传统不一，不可直接等同</text></svg>",
        "pending_notes": "1) 《波波尔·乌》的转录年代与文本层次学界有讨论；2) 铭文解读依赖语言学进展，具体读法可能更新；3) Schele、Taube 的具体论点待逐条核对原文，著作未完整录入 sources.json。",
        "needs_verification": True
    },
    "myth-aztec": {
        "level": "L2",
        "source_text": "阿兹特克（墨西卡）神话主要依靠殖民时期记录、少量前殖民抄本与考古材料重建，核心母题包括太阳神、第五太阳纪与羽蛇神传说。材料多经后世转录，且带有记录者的立场，需与其他证据互证。",
        "versions": [
            "关于宇宙纪元，现存文献记载此前太阳纪的更替，第五太阳纪至今的叙事在不同文献中细节有出入。",
            "羽蛇神（魁札尔科亚特尔）在神话与历史传说中的身份并不单一，既有神祇也有祭司—统治者的叙事层次。",
            "西班牙征服者与本土编年史的记录立场不同，对同一神祇与仪式的描述存在明显差异。"
        ],
        "interpretations": [
            {"holder": "Miguel León-Portilla", "school": "纳瓦特尔文学与思想史", "view": "以本土语言材料重建阿兹特克思想，强调其宇宙观与伦理观念的复杂性，反对把献祭简单化解释。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "可从宇宙周期与末世母题作现象学对照，属一般性框架参照。"},
            {"holder": "Inga Clendinnen", "school": "历史人类学", "view": "强调仪式与政治秩序的关联，并指出殖民记录的中介性与解读困难。"}
        ],
        "comparisons": [
            {"tradition": "玛雅神话", "basis_source": "aca-short-history-myth", "note": "通论性著作常把中美洲两大传统并列，此处仅记录母题层面的一般比较。"},
            {"tradition": "埃及神话", "basis_source": "aca-eternal-return", "note": "以太阳神与宇宙秩序母题作现象学层面的对照，属比较宗教学的框架性参照。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>阿兹特克宇宙纪元与材料示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>阿兹特克宇宙纪元与材料（示意）</text><rect x='60' y='90' width='180' height='56' fill='var(--svg-node)' stroke='currentColor'/><text x='150' y='114' text-anchor='middle' fill='var(--svg-text)' font-size='13'>前四个太阳纪</text><text x='150' y='134' text-anchor='middle' fill='var(--svg-text)' font-size='12'>文献记载有出入</text><rect x='290' y='90' width='180' height='56' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='114' text-anchor='middle' fill='var(--svg-text)' font-size='13'>第五太阳纪</text><text x='380' y='134' text-anchor='middle' fill='var(--svg-text)' font-size='12'>现存世界</text><rect x='520' y='90' width='180' height='56' fill='var(--svg-node)' stroke='currentColor'/><text x='610' y='114' text-anchor='middle' fill='var(--svg-text)' font-size='13'>太阳神崇拜</text><text x='610' y='134' text-anchor='middle' fill='var(--svg-text)' font-size='12'>王权与祭仪</text><line x1='240' y1='118' x2='290' y2='118' stroke='currentColor' opacity='0.5'/><line x1='470' y1='118' x2='520' y2='118' stroke='currentColor' opacity='0.5'/><rect x='100' y='204' width='240' height='56' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='220' y='228' text-anchor='middle' fill='var(--svg-text)' font-size='13'>殖民期记录·抄本</text><text x='220' y='248' text-anchor='middle' fill='var(--svg-text)' font-size='12'>立场各异，需互证</text><rect x='420' y='204' width='240' height='56' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='540' y='228' text-anchor='middle' fill='var(--svg-text)' font-size='13'>考古与图像材料</text><text x='540' y='248' text-anchor='middle' fill='var(--svg-text)' font-size='12'>独立旁证</text><text x='380' y='322' text-anchor='middle' fill='var(--svg-text)' font-size='13'>羽蛇神兼具神祇与历史叙事层次</text></svg>",
        "pending_notes": "1) 现存文献多经殖民时代转录，记录立场差异明显；2) 宇宙纪元的细节在不同文献中不一致，正文未列具体年数；3) León-Portilla、Clendinnen 的论点待逐条核对原文，著作未完整录入 sources.json。",
        "needs_verification": True
    },
    "rel-christianity": {
        "level": "L2",
        "source_text": "基督教以《圣经》新约为核心经典，并在历史中形成天主教、东正教与新教等主要传统。早期教父著作、公会议文献与宗教改革文本构成研究其历史与教义分歧的重要材料；不同宗派对经典与传统的权重理解不同。",
        "versions": [
            "天主教、东正教与新教在圣事、教会权威与圣经—传统关系上存在长期分歧，这些分歧是历史形成的结果。",
            "新约各卷成书背景与作者归属存在学术讨论，文本批判研究对这些问题的结论并不完全一致。",
            "早期诺斯替文献的发现为理解早期基督教的多样性提供了材料，其与正典文献的关系为学界研究议题。"
        ],
        "interpretations": [
            {"holder": "Elaine Pagels", "school": "早期基督教与诺斯替研究", "view": "通过诺斯替福音与正典文本的对照，指出早期基督教内部的多样性；其观点在学界有讨论。"},
            {"holder": "Max Weber", "school": "宗教社会学", "view": "在《新教伦理与资本主义精神》中讨论新教教义与近代经济伦理的关联，属社会学层面的分析，不宣教。"},
            {"holder": "Émile Durkheim", "school": "宗教社会学", "view": "从宗教的社会功能与集体表征角度分析宗教现象，为比较宗教学提供理论框架。"}
        ],
        "comparisons": [
            {"tradition": "犹太教", "basis_source": "aca-myth-legend-custom", "note": "学界就犹太教与基督教在经典与律法理解上的承继与分歧有大量研究，此处仅记录有文献依据的比较。"},
            {"tradition": "伊斯兰教", "basis_source": "aca-god-is-not-one", "note": "亚伯拉罕诸教的比较研究有专门文献，Prothero 的比较为通俗学术读物，细节待进一步核对。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>基督教主要传统分支示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>基督教主要传统分支（示意）</text><rect x='300' y='84' width='160' height='44' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='112' text-anchor='middle' fill='var(--svg-text)' font-size='14'>早期基督教</text><line x1='380' y1='128' x2='380' y2='166' stroke='currentColor' opacity='0.5'/><line x1='160' y1='166' x2='600' y2='166' stroke='currentColor' opacity='0.5'/><line x1='160' y1='166' x2='160' y2='208' stroke='currentColor' opacity='0.5'/><line x1='380' y1='166' x2='380' y2='208' stroke='currentColor' opacity='0.5'/><line x1='600' y1='166' x2='600' y2='208' stroke='currentColor' opacity='0.5'/><rect x='80' y='208' width='160' height='48' fill='var(--svg-node)' stroke='currentColor'/><text x='160' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='14'>天主教</text><rect x='300' y='208' width='160' height='48' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='14'>东正教</text><rect x='520' y='208' width='160' height='48' fill='var(--svg-node)' stroke='currentColor'/><text x='600' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='14'>新教</text><rect x='230' y='310' width='300' height='44' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='338' text-anchor='middle' fill='var(--svg-text)' font-size='13'>分歧为历史形成，本站不作真伪判断</text></svg>",
        "pending_notes": "1) 新约各卷成书与作者归属存在学术争论，正文未列具体年份；2) Pagels、Weber、Durkheim 的观点为其代表著作的概括，细节待逐条核对；3) 宗派分歧的表述采用学界通行描述，不评判信仰真伪。",
        "needs_verification": True
    },
    "rel-islam": {
        "level": "L2",
        "source_text": "伊斯兰教以《古兰经》为最高经典，以圣训为重要辅助文献，并发展出法学、教义学与苏菲传统。经典以阿拉伯语传述，译本在语义上存在差异；不同教法学派与神学流派对同一经文的理解并不一致。",
        "versions": [
            "逊尼派与什叶派在历史传承与伊玛目观念上存在差异，是历史形成的教义分歧，本站只作描述性记录。",
            "《古兰经》的读法与注释传统多样，不同注释学派对经文的解释重点有所不同。",
            "苏菲传统强调修行与内在体验，与教法学者的侧重形成对照，历史上二者的关系复杂且随地区而异。"
        ],
        "interpretations": [
            {"holder": "Stephen Prothero", "school": "比较宗教学", "view": "在亚伯拉罕诸教的比较框架中强调各传统的独特目标与实践，反对把不同宗教简化为同一本质；属通俗学术著作的观点。"},
            {"holder": "Max Weber", "school": "宗教社会学", "view": "从宗教伦理与经济社会结构的关联角度分析宗教，为理解宗教与社会的关系提供理论框架，不涉及信仰真伪判断。"},
            {"holder": "Émile Durkheim", "school": "宗教社会学", "view": "把宗教视为集体表征与社会事实，强调仪式与共同体的功能，为比较研究提供方法论基础。"}
        ],
        "comparisons": [
            {"tradition": "基督教", "basis_source": "aca-god-is-not-one", "note": "亚伯拉罕诸教的比较有专门文献，Prothero 的比较为通俗学术读物，具体教义差异待进一步核对。"},
            {"tradition": "犹太教", "basis_source": "enc-brit-judaism", "note": "以权威百科的犹太教条目作为亚伯拉罕诸教一般关联的参照（该来源未在线核验，见 pending_notes）；具体教义差异待专门文献核对。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>伊斯兰教传统结构示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>伊斯兰教传统结构（描述性示意）</text><rect x='280' y='82' width='200' height='44' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='110' text-anchor='middle' fill='var(--svg-text)' font-size='14'>古兰经</text><line x1='380' y1='126' x2='380' y2='162' stroke='currentColor' opacity='0.5'/><line x1='180' y1='162' x2='580' y2='162' stroke='currentColor' opacity='0.5'/><line x1='180' y1='162' x2='180' y2='204' stroke='currentColor' opacity='0.5'/><line x1='380' y1='162' x2='380' y2='204' stroke='currentColor' opacity='0.5'/><line x1='580' y1='162' x2='580' y2='204' stroke='currentColor' opacity='0.5'/><rect x='100' y='204' width='160' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='180' y='232' text-anchor='middle' fill='var(--svg-text)' font-size='13'>圣训</text><rect x='300' y='204' width='160' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='232' text-anchor='middle' fill='var(--svg-text)' font-size='13'>教法学派</text><rect x='500' y='204' width='160' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='580' y='232' text-anchor='middle' fill='var(--svg-text)' font-size='13'>教义学</text><line x1='380' y1='250' x2='380' y2='292' stroke='currentColor' opacity='0.5'/><rect x='270' y='292' width='220' height='44' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>逊尼 / 什叶 · 苏菲传统</text></svg>",
        "pending_notes": "1) 教义与教派分歧采用学界通行描述，不评判信仰真伪；2) 经文译本差异与注释学派的具体论点待逐条核对原文；3) Prothero、Weber、Durkheim 的观点为概括，细节待核对。",
        "needs_verification": True
    },
    "myth-celtic": {
        "level": "L2",
        "source_text": "凯尔特神话的材料分散且多为中世纪抄本：《马比诺吉昂》保存威尔士的神话故事集，《侵略之书》汇编爱尔兰的伪史与神祇传说。更早的高卢人信仰主要依靠古典作者记载与考古铭文重建，材料与后世爱尔兰、威尔士传统之间隔着漫长时段。",
        "versions": [
            "爱尔兰的神话循环以达努神族与米列斯人入侵传说为核心，现存形态经过中世纪修道院的整理与基督教化改写。",
            "威尔士《马比诺吉昂》的四个分支以威尔士地方传说为底本，与爱尔兰材料有若干对应人物，但各自独立成篇。",
            "古典时代高卢神祇（如凯撒《高卢战记》所记者）与中世纪岛屿凯尔特材料不能简单等同，研究者强调其间的时空距离。"
        ],
        "interpretations": [
            {"holder": "Proinsias Mac Cana", "school": "凯尔特文学与神话研究", "view": "强调凯尔特神话的地方性、口传底色与中世纪文本的中介性，主张在文本语境中理解神祇叙事，而非重建统一的神话体系。"},
            {"holder": "Marie-Louise Sjoestedt", "school": "凯尔特宗教研究", "view": "以宗教史与语言学方法分析爱尔兰神祇，指出神祇形象与王权、地域的关联；其结论基于当时的材料，部分细节已被后续研究修订。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "可就宇宙轴、英雄与丰产母题作现象学层面的框架性参照，不构成对凯尔特材料的专门结论。"}
        ],
        "comparisons": [
            {"tradition": "北欧神话", "basis_source": "aca-gods-indo-europeans", "note": "印欧比较神话学在语系框架内并置凯尔特与北欧材料，属有文献依据的学派比较，不主张直接文本同源。"},
            {"tradition": "希腊神话", "basis_source": "aca-comparative-myth", "note": "比较神话学把凯尔特神祇与地中海传统作功能层面的对照，学界对具体对应有争论，此处并列呈现。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>凯尔特神话材料来源示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>凯尔特神话材料来源（岛屿与大陆）</text><rect x='80' y='96' width='240' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='200' y='120' text-anchor='middle' fill='var(--svg-text)' font-size='14'>爱尔兰传统</text><text x='200' y='142' text-anchor='middle' fill='var(--svg-text)' font-size='13'>侵略之书·神话循环</text><rect x='440' y='96' width='240' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='560' y='120' text-anchor='middle' fill='var(--svg-text)' font-size='14'>威尔士传统</text><text x='560' y='142' text-anchor='middle' fill='var(--svg-text)' font-size='13'>马比诺吉昂</text><rect x='260' y='210' width='240' height='60' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='234' text-anchor='middle' fill='var(--svg-text)' font-size='14'>中世纪抄本</text><text x='380' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='13'>经修道院整理改写</text><rect x='260' y='312' width='240' height='44' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='340' text-anchor='middle' fill='var(--svg-text)' font-size='13'>大陆高卢材料：古典记载与考古</text></svg>",
        "pending_notes": "1) 高卢与岛屿凯尔特材料之间的时空距离大，不能简单等同；2) Mac Cana、Sjoestedt 的具体论点待逐条核对，其著作未录入 sources.json；3) 本土知识传统的细节以学界通行为限，不作真伪评判。",
        "needs_verification": True
    },
    "rel-judaism": {
        "level": "L2",
        "source_text": "犹太教的核心经典为《托拉》与《塔木德》，并在历史中发展出律法、神秘主义与礼仪传统。本站对经典的引用使用公共领域译本，不同译本在语义上存在差异；教义与实践的描述均采用学术与描述性立场，不评判信仰真伪。",
        "versions": [
            "拉比犹太教以《塔木德》诠释律法，强调口传传统与律法实践，是第二圣殿时期之后犹太教的主流形态之一。",
            "卡巴拉与哈西德主义强调神秘体验与虔敬，与侧重律法研究的传统在侧重上不同，历史上二者关系复杂。",
            "近现代犹太教内部出现多个宗派，对律法权威与现代性的回应各异，是历史发展的结果。"
        ],
        "interpretations": [
            {"holder": "Theodor H. Gaster", "school": "圣经民俗与比较宗教学", "view": "在《旧约中的神话、传说与习俗》中以民俗与神话学方法分析旧约材料，指出其与近东传统的关联；属学术分析，不作信仰判断。"},
            {"holder": "Gershom Scholem", "school": "犹太神秘主义研究", "view": "以历史与文本研究方法梳理卡巴拉传统，强调神秘主义在犹太历史中的位置；其框架影响深远，具体论点学界有讨论。"},
            {"holder": "Stephen Prothero", "school": "比较宗教学", "view": "在亚伯拉罕诸教比较中强调各传统独特目标，反对把不同宗教简化为同一本质，属通俗学术著作的观点。"}
        ],
        "comparisons": [
            {"tradition": "基督教", "basis_source": "aca-god-is-not-one", "note": "比较宗教学就犹太教与基督教在经典与律法理解上的承继与分歧有大量研究，此处记录有文献依据的一般比较。"},
            {"tradition": "古代近东神话", "basis_source": "aca-myth-legend-custom", "note": "Gaster 以民俗学方法比较旧约与近东神话材料，属专门研究；此处仅记录学界已有的比较，不推断信仰源流。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>犹太教经典与传统结构示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>犹太教经典与传统结构（描述性示意）</text><rect x='290' y='84' width='180' height='44' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='112' text-anchor='middle' fill='var(--svg-text)' font-size='14'>托拉</text><line x1='380' y1='128' x2='380' y2='164' stroke='currentColor' opacity='0.5'/><line x1='170' y1='164' x2='590' y2='164' stroke='currentColor' opacity='0.5'/><line x1='170' y1='164' x2='170' y2='206' stroke='currentColor' opacity='0.5'/><line x1='380' y1='164' x2='380' y2='206' stroke='currentColor' opacity='0.5'/><line x1='590' y1='164' x2='590' y2='206' stroke='currentColor' opacity='0.5'/><rect x='90' y='206' width='160' height='50' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='228' text-anchor='middle' fill='var(--svg-text)' font-size='13'>塔木德</text><text x='170' y='246' text-anchor='middle' fill='var(--svg-text)' font-size='12'>律法诠释</text><rect x='300' y='206' width='160' height='50' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='228' text-anchor='middle' fill='var(--svg-text)' font-size='13'>礼仪实践</text><text x='380' y='246' text-anchor='middle' fill='var(--svg-text)' font-size='12'>日常与节期</text><rect x='510' y='206' width='160' height='50' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='228' text-anchor='middle' fill='var(--svg-text)' font-size='13'>神秘主义</text><text x='590' y='246' text-anchor='middle' fill='var(--svg-text)' font-size='12'>卡巴拉·哈西德</text><rect x='230' y='308' width='300' height='44' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='336' text-anchor='middle' fill='var(--svg-text)' font-size='13'>内部传统多样，本站不作真伪评判</text></svg>",
        "pending_notes": "1) 不同译本的语义差异与具体教义细节待逐条核对原文；2) Gaster、Scholem、Prothero 的观点为概括，Scholem 著作未录入 sources.json；3) 全部表述采用描述性立场，不替信仰表态。",
        "needs_verification": True
    },
    "rel-buddhism": {
        "level": "L2",
        "source_text": "佛教以佛陀的教导为核心，经典结集为三藏，不同部派与大乘传统在经典与修行目标上各有发展。《法句经》为流传广的早期经典之一，本站引用使用公共领域译本；教义描述采用学术立场，不评判信仰真伪。",
        "versions": [
            "早期部派佛教侧重阿罗汉道与戒定慧的修持，不同部派在戒律与教义细节上存在差异。",
            "大乘佛教发展出菩萨道与空性等主题，并形成多部经典传统，与早期部派在侧重点上不同。",
            "藏传、汉传与南传佛教在制度、仪轨与经典语言上各自发展，是历史与地域条件的结果。"
        ],
        "interpretations": [
            {"holder": "Richard Gombrich", "school": "早期佛教研究（语文学与历史方法）", "view": "以巴利文经典与历史语言学方法研究早期佛教，强调在文本语境中理解教义，反对过度现代化的投射；结论学界有讨论。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "从神话时间、宇宙轴与修行实践的角度把佛教置于比较宗教学框架，属现象学层面的参照。"},
            {"holder": "Peter Harvey", "school": "佛教伦理与哲学研究", "view": "系统梳理佛教伦理与心性学说，强调不同传统间的连续性；其著作为学术通论，细节待核对。"}
        ],
        "comparisons": [
            {"tradition": "印度教", "basis_source": "enc-brit-hinduism", "note": "以权威百科的印度教条目作为佛教与印度教背景关联的一般参照（该来源未在线核验，见待核实）；具体教义差异待专门文献核对。"},
            {"tradition": "耆那教", "basis_source": "enc-brit-buddhism", "note": "以权威百科条目作为与耆那教同属印度宗教背景的一般参照（该来源未在线核验，见待核实）；具体差异待专门文献核对。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>佛教传统分支示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>佛教传统分支（描述性示意）</text><rect x='290' y='84' width='180' height='44' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='112' text-anchor='middle' fill='var(--svg-text)' font-size='14'>佛陀教导</text><line x1='380' y1='128' x2='380' y2='166' stroke='currentColor' opacity='0.5'/><line x1='160' y1='166' x2='600' y2='166' stroke='currentColor' opacity='0.5'/><line x1='160' y1='166' x2='160' y2='208' stroke='currentColor' opacity='0.5'/><line x1='380' y1='166' x2='380' y2='208' stroke='currentColor' opacity='0.5'/><line x1='600' y1='166' x2='600' y2='208' stroke='currentColor' opacity='0.5'/><rect x='80' y='208' width='160' height='50' fill='var(--svg-node)' stroke='currentColor'/><text x='160' y='230' text-anchor='middle' fill='var(--svg-text)' font-size='13'>南传</text><text x='160' y='248' text-anchor='middle' fill='var(--svg-text)' font-size='12'>早期部派</text><rect x='300' y='208' width='160' height='50' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='230' text-anchor='middle' fill='var(--svg-text)' font-size='13'>汉传</text><text x='380' y='248' text-anchor='middle' fill='var(--svg-text)' font-size='12'>大乘诸宗</text><rect x='520' y='208' width='160' height='50' fill='var(--svg-node)' stroke='currentColor'/><text x='600' y='230' text-anchor='middle' fill='var(--svg-text)' font-size='13'>藏传</text><text x='600' y='248' text-anchor='middle' fill='var(--svg-text)' font-size='12'>金刚乘</text><rect x='230' y='310' width='300' height='44' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='338' text-anchor='middle' fill='var(--svg-text)' font-size='13'>分支为历史发展结果，不作真伪评判</text></svg>",
        "pending_notes": "1) 部派与大乘的形成年代跨度大，正文未列具体年数；2) Gombrich、Harvey 的论点待逐条核对原文，其著作未录入 sources.json；3) 全部教义描述采用学术立场，不替信仰表态。",
        "needs_verification": True
    },
    "rel-hinduism": {
        "level": "L2",
        "source_text": "印度教是多种传统的复合体，其文本包括吠陀、奥义书、史诗与往世书，不同传统在神祇、修行与哲学上差异显著。本站引用使用公共领域译本，并以学术与描述性立场整理，不评判任何信仰的真伪。",
        "versions": [
            "吠陀传统以祭祀与颂神为中心，奥义书转向梵与自我的哲学探究，二者在关注点上不同。",
            "史诗与往世书发展出三相神与化身叙事，并形成虔信（bhakti）传统，与早期祭祀传统并重。",
            "哲学上有吠檀多、数论、瑜伽等多个体系，对梵、自我与解脱的关系理解各异。"
        ],
        "interpretations": [
            {"holder": "Wendy Doniger", "school": "芝加哥学派（印度宗教与文本研究）", "view": "强调印度传统的多义性与阐释史，警惕把多样实践简化为单一体系；其具体解读在学界有争论。"},
            {"holder": "Georges Dumézil", "school": "印欧比较神话学", "view": "以三功能假说解析吠陀神系并与印欧其他传统比较，属学派模型，学界对其适用范围有批评。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "以宇宙轴、轮回与修行实践的比较框架理解印度宗教，属现象学层面的参照。"}
        ],
        "comparisons": [
            {"tradition": "佛教", "basis_source": "aca-god-is-not-one", "note": "比较宗教学就印度教与佛教的背景关联有专门研究，此处记录有文献依据的一般比较，不作信仰判断。"},
            {"tradition": "波斯传统", "basis_source": "aca-gods-indo-europeans", "note": "Dumézil 的印欧比较把印度与伊朗材料并置，属学派框架下的对照，学界对对应关系有讨论。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>印度教文本与哲学传统示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>印度教文本与哲学传统（示意）</text><rect x='70' y='96' width='180' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='160' y='120' text-anchor='middle' fill='var(--svg-text)' font-size='14'>吠陀</text><text x='160' y='140' text-anchor='middle' fill='var(--svg-text)' font-size='13'>祭祀·颂神</text><rect x='290' y='96' width='180' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='120' text-anchor='middle' fill='var(--svg-text)' font-size='14'>奥义书</text><text x='380' y='140' text-anchor='middle' fill='var(--svg-text)' font-size='13'>梵我探究</text><rect x='510' y='96' width='180' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='600' y='120' text-anchor='middle' fill='var(--svg-text)' font-size='14'>史诗·往世书</text><text x='600' y='140' text-anchor='middle' fill='var(--svg-text)' font-size='13'>三相神·虔信</text><line x1='160' y1='154' x2='160' y2='204' stroke='currentColor' opacity='0.5'/><line x1='380' y1='154' x2='380' y2='204' stroke='currentColor' opacity='0.5'/><line x1='600' y1='154' x2='600' y2='204' stroke='currentColor' opacity='0.5'/><rect x='130' y='204' width='500' height='56' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='228' text-anchor='middle' fill='var(--svg-text)' font-size='13'>哲学体系：吠檀多 · 数论 · 瑜伽</text><text x='380' y='248' text-anchor='middle' fill='var(--svg-text)' font-size='12'>对梵·自我·解脱的理解各异</text><text x='380' y='322' text-anchor='middle' fill='var(--svg-text)' font-size='13'>传统多元并存，本站不作真伪评判</text></svg>",
        "pending_notes": "1) 各传统与哲学体系形成年代跨度大，正文未列具体年数；2) Doniger、Dumézil 的观点为学派立场，学界有争论；3) 全部描述采用学术立场，不替信仰表态。",
        "needs_verification": True
    },
    "rel-taoism": {
        "level": "L2",
        "source_text": "道教以《道德经》《庄子》等典籍为重要文本资源，并在历史中发展出炼养、科仪与宫观制度等实践形态。道家哲学与制度化宗教之间既有联系又有区别，本站以学术立场描述，不评判信仰真伪。",
        "versions": [
            "道家哲学侧重对道、自然与治身的思考，是先秦思想的重要一支，与后世的宗教组织形态有别。",
            "汉魏以后的道教逐渐形成教团、科仪与炼养体系，经典结集与祖师谱系也随之发展。",
            "全真与正一等宗派在修行方式、戒律与组织上各有侧重，是历史演变的结果。"
        ],
        "interpretations": [
            {"holder": "刘笑敢", "school": "道家哲学研究", "view": "以文献考证与哲学分析研究《庄子》与老子思想，强调区分原始文本与后世诠释；具体结论学界有讨论。"},
            {"holder": "Isabelle Robinet", "school": "道教与道家研究", "view": "系统梳理道教的冥想、经典与历史脉络，强调道家思想与道教实践之间的连续与转化；其著作为学术通论。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "可从宇宙对应、修身实践与“永恒回归”（eternal return）等主题作现象学层面的参照，不构成对道教材料的专门结论。"}
        ],
        "comparisons": [
            {"tradition": "儒家", "basis_source": "enc-brit-taoism", "note": "以权威百科条目作为道家与儒家在中国思想史中关系的一般参照（该来源未在线核验，见待核实）；具体思想差异待专门文献核对。"},
            {"tradition": "佛教", "basis_source": "enc-brit-buddhism", "note": "以权威百科的佛教条目作为本土传统与传入宗教互动背景的一般参照（该来源未在线核验）；来源库暂无专门研究佛教东传的著作，此处属待核实的弱参照，具体过程待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>道家哲学与道教形态示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>道家哲学与道教形态（示意）</text><rect x='80' y='100' width='260' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='210' y='124' text-anchor='middle' fill='var(--svg-text)' font-size='14'>道家哲学</text><text x='210' y='146' text-anchor='middle' fill='var(--svg-text)' font-size='13'>道德经·庄子</text><rect x='420' y='100' width='260' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='550' y='124' text-anchor='middle' fill='var(--svg-text)' font-size='14'>制度道教</text><text x='550' y='146' text-anchor='middle' fill='var(--svg-text)' font-size='13'>教团·科仪·炼养</text><line x1='340' y1='130' x2='420' y2='130' stroke='currentColor' opacity='0.5'/><rect x='150' y='226' width='200' height='52' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='250' y='248' text-anchor='middle' fill='var(--svg-text)' font-size='13'>全真 · 内丹修行</text><text x='250' y='266' text-anchor='middle' fill='var(--svg-text)' font-size='12'>出家·戒律</text><rect x='410' y='226' width='200' height='52' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='510' y='248' text-anchor='middle' fill='var(--svg-text)' font-size='13'>正一 · 符箓科仪</text><text x='510' y='266' text-anchor='middle' fill='var(--svg-text)' font-size='12'>居家·法事</text><text x='380' y='336' text-anchor='middle' fill='var(--svg-text)' font-size='13'>哲学与宗教形态有别，本站不作真伪评判</text></svg>",
        "pending_notes": "1) 道家哲学与制度化道教的关系为学界讨论议题，正文谨慎区分；2) 刘笑敢、Robinet 的论点待逐条核对，其著作未录入 sources.json；3) 全部表述采用学术立场，不替信仰表态。",
        "needs_verification": True
    },
    "rel-confucianism": {
        "level": "L2",
        "source_text": "儒家以《论语》所载孔子言行与《易经》等经典为重要文本资源，并在历史中发展出经学、理学与礼学传统。本站引用使用公共领域译本，以学术与描述性立场整理，不评判信仰真伪。",
        "versions": [
            "先秦儒家侧重伦理、礼乐与政治秩序，孔子与其后学在重点上各有发展。",
            "汉代经学强调章句训诂与天人感应，宋明理学则转向心性与天理的哲学探讨，二者问题意识不同。",
            "近现代新儒家在回应现代性问题上提出新的诠释，与古典经学形成对照。"
        ],
        "interpretations": [
            {"holder": "Herbert Fingarette", "school": "比较哲学与儒家研究", "view": "以《论语》的礼仪维度解读孔子，主张“世俗即神圣”的解释路径；其读法在学界有支持也有批评。"},
            {"holder": "朱熹", "school": "宋明理学", "view": "以天理、格物致知与存天理灭人欲等命题重构儒家义理，对后世影响深远；此处为思想史描述，非信仰判断。"},
            {"holder": "Stephen Prothero", "school": "比较宗教学", "view": "把儒家的修身与秩序实践列为宗教比较的一个案例，强调各传统目标不同，属通俗学术著作的观点。"}
        ],
        "comparisons": [
            {"tradition": "道教", "basis_source": "enc-brit-taoism", "note": "以权威百科条目作为儒道在中国思想史中关系的一般参照（该来源未在线核验，见待核实）；具体差异待专门文献核对。"},
            {"tradition": "东亚礼仪传统", "basis_source": "aca-god-is-not-one", "note": "比较宗教学就礼仪与修身传统有一般研究，此处记录有文献依据的比较，不作信仰判断。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>儒家思想发展阶段示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>儒家思想发展阶段（示意）</text><rect x='60' y='112' width='190' height='62' fill='var(--svg-node)' stroke='currentColor'/><text x='155' y='136' text-anchor='middle' fill='var(--svg-text)' font-size='14'>先秦儒家</text><text x='155' y='158' text-anchor='middle' fill='var(--svg-text)' font-size='13'>伦理·礼乐</text><rect x='285' y='112' width='190' height='62' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='136' text-anchor='middle' fill='var(--svg-text)' font-size='14'>汉代经学</text><text x='380' y='158' text-anchor='middle' fill='var(--svg-text)' font-size='13'>训诂·天人</text><rect x='510' y='112' width='190' height='62' fill='var(--svg-node)' stroke='currentColor'/><text x='605' y='136' text-anchor='middle' fill='var(--svg-text)' font-size='14'>宋明理学</text><text x='605' y='158' text-anchor='middle' fill='var(--svg-text)' font-size='13'>心性·天理</text><line x1='250' y1='143' x2='285' y2='143' stroke='currentColor' opacity='0.5'/><line x1='475' y1='143' x2='510' y2='143' stroke='currentColor' opacity='0.5'/><rect x='270' y='232' width='220' height='54' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='13'>近现代新儒家</text><text x='380' y='274' text-anchor='middle' fill='var(--svg-text)' font-size='12'>回应现代性</text><text x='380' y='340' text-anchor='middle' fill='var(--svg-text)' font-size='13'>阶段为叙述便利而划分，非严格断代</text></svg>",
        "pending_notes": "1) 思想史分期为叙述便利，具体年代与学派界限学界有讨论；2) Fingarette 的“世俗即神圣”译法为其著作观点概括，著作未录入 sources.json；3) 全部表述采用学术立场，不替信仰表态。",
        "needs_verification": True
    },
    "rel-shinto": {
        "level": "L2",
        "source_text": "神道教的神话材料主要见于《古事记》与《日本书纪》，实践层面以神社、祭祀与洁净观念为中心。神道与佛教在历史上长期共存并相互影响，本站以学术与描述性立场整理，不评判信仰真伪。",
        "versions": [
            "早期神道以自然神与氏族祭祀为中心，缺乏统一教义文本，其形态多从典籍与习俗中重建。",
            "佛教传入后形成神佛习合的长期过程，神祇与佛菩萨在信仰实践中被关联理解。",
            "近代国家神道曾被制度化，战后制度格局发生显著变化，是历史政治条件的产物。"
        ],
        "interpretations": [
            {"holder": "本居宣长", "school": "国学（日本古典研究）", "view": "主张以日本古典语言的固有精神理解神话，反对道德化的外来解读；其立场在思想史上有影响也有批评。"},
            {"holder": "Donald L. Philippi", "school": "日本神话译介与研究", "view": "强调《古事记》作为神话文本的文学性与独特性，指出其编纂意图的复杂性；见其英译导论。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "可从太阳神话、神圣中心（sacred center）与王权仪式作现象学层面的参照，不构成对神道材料的专门结论。"}
        ],
        "comparisons": [
            {"tradition": "日本神话", "basis_source": "pri-kojiki", "note": "《古事记》既是神话文本也是神道教的重要经典，此处以原典为依据记录文本与信仰实践的关联。"},
            {"tradition": "佛教", "basis_source": "enc-brit-buddhism", "note": "以权威百科条目作为神佛习合历史背景的一般参照（该来源未在线核验，见待核实）；具体过程待专门文献核对。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>神道教结构与历史层次示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>神道教结构与历史层次（示意）</text><rect x='80' y='104' width='200' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='180' y='128' text-anchor='middle' fill='var(--svg-text)' font-size='14'>神话文本</text><text x='180' y='148' text-anchor='middle' fill='var(--svg-text)' font-size='13'>古事记·日本书纪</text><rect x='280' y='104' width='200' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='128' text-anchor='middle' fill='var(--svg-text)' font-size='14'>实践核心</text><text x='380' y='148' text-anchor='middle' fill='var(--svg-text)' font-size='13'>神社·祭祀·洁净</text><rect x='480' y='104' width='200' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='580' y='128' text-anchor='middle' fill='var(--svg-text)' font-size='14'>历史互动</text><text x='580' y='148' text-anchor='middle' fill='var(--svg-text)' font-size='13'>神佛习合</text><line x1='180' y1='162' x2='180' y2='214' stroke='currentColor' opacity='0.5'/><line x1='380' y1='162' x2='380' y2='214' stroke='currentColor' opacity='0.5'/><line x1='580' y1='162' x2='580' y2='214' stroke='currentColor' opacity='0.5'/><rect x='130' y='214' width='500' height='58' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>近代制度化与战后变化：历史政治条件的产物</text><text x='380' y='258' text-anchor='middle' fill='var(--svg-text)' font-size='12'>本站仅作描述，不评判信仰真伪</text><text x='380' y='336' text-anchor='middle' fill='var(--svg-text)' font-size='13'>神道无统一教义文本，形态多从典籍与习俗重建</text></svg>",
        "pending_notes": "1) 早期神道形态依赖典籍与习俗重建，具体细节学界有讨论；2) 本居宣长、Philippi 的论点待逐条核对原文，其著作未录入 sources.json；3) 术语已统一：“神圣中心”（sacred center）采用中文为主、英文括注；4) 全部表述采用学术立场，不替信仰表态。",
        "needs_verification": True
    },
    "motif-flood": {
        "level": "L2",
        "source_text": "洪水母题见于多个传统的一手文献：美索不达米亚的《阿特拉哈西斯》与《吉尔伽美什史诗》洪水段落保存了较早的叙事，其他地区亦有各自的大洪水传说。学界对其间的传播关系有长期研究但无定论，本站只记录有文献依据的比较。",
        "versions": [
            "《阿特拉哈西斯》叙述洪水由神议决定、人类得以延续的情节，是现存较早的洪水叙事之一。",
            "《吉尔伽美什史诗》中的洪水段落与前者有情节对应，二者关系为学界研究议题，先后与依赖关系仍在讨论。",
            "不同地区的洪水叙事在起因、幸存方式与神意解释上各异，不宜直接等同或推断单一起源。"
        ],
        "interpretations": [
            {"holder": "Samuel Noah Kramer", "school": "苏美尔学", "view": "通过泥板整理指出苏美尔洪水叙事材料的独特性及其与后世版本的承继关系，强调文本考证的基础作用。"},
            {"holder": "James George Frazer", "school": "早期比较宗教学", "view": "在跨文化框架中讨论洪水传说，属早期学派的观点，其具体结论与资料使用在现代学界受到修订。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "把洪水叙事置于宇宙毁灭与重生的母题框架中理解，强调其与宇宙循环观念的联系，属现象学参照。"}
        ],
        "comparisons": [
            {"tradition": "希伯来经典传统", "basis_source": "aca-myth-legend-custom", "note": "Gaster 以民俗与神话学方法比较旧约与近东洪水材料，属专门研究；此处仅记录学界已有的比较，不推断信仰源流。"},
            {"tradition": "希腊神话", "basis_source": "aca-comparative-myth", "note": "比较神话学在近东与地中海框架内讨论洪水母题，学界对传播路径有争论，此处并列呈现不作定论。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>洪水母题跨传统示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>洪水母题跨传统（仅示意，不表示源流）</text><rect x='70' y='104' width='190' height='62' fill='var(--svg-node)' stroke='currentColor'/><text x='165' y='128' text-anchor='middle' fill='var(--svg-text)' font-size='13'>阿特拉哈西斯</text><text x='165' y='150' text-anchor='middle' fill='var(--svg-text)' font-size='12'>美索不达米亚</text><rect x='285' y='104' width='190' height='62' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='128' text-anchor='middle' fill='var(--svg-text)' font-size='13'>吉尔伽美什</text><text x='380' y='150' text-anchor='middle' fill='var(--svg-text)' font-size='12'>洪水段落</text><rect x='500' y='104' width='190' height='62' fill='var(--svg-node)' stroke='currentColor'/><text x='595' y='128' text-anchor='middle' fill='var(--svg-text)' font-size='13'>其他传统</text><text x='595' y='150' text-anchor='middle' fill='var(--svg-text)' font-size='12'>多地各有叙事</text><line x1='260' y1='135' x2='285' y2='135' stroke='currentColor' opacity='0.5'/><line x1='475' y1='135' x2='500' y2='135' stroke='currentColor' opacity='0.5'/><rect x='200' y='232' width='360' height='60' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='13'>共同关注：毁灭·幸存·重生</text><text x='380' y='276' text-anchor='middle' fill='var(--svg-text)' font-size='12'>起因与神意解释各异，不作同源断言</text><text x='380' y='346' text-anchor='middle' fill='var(--svg-text)' font-size='13'>学界对传播关系有长期研究但无定论</text></svg>",
        "pending_notes": "1) 洪水叙事的先后与传播关系学界无定论，正文未列具体年数；2) Kramer、Frazer 的具体论点以其代表著作概括，细节待核对；3) 不推断单一起源，符合比较学术规范。",
        "needs_verification": True
    },
    "motif-underworld": {
        "level": "L2",
        "source_text": "冥界母题见于多传统的一手文献：古埃及的《亡灵书》详述死后旅程，其他传统亦有各自的亡者居所与冥界旅行叙事。学界对冥界观念的比较有专门研究，本站只记录有文献依据的对照。",
        "versions": [
            "古埃及的冥界叙事与《亡灵书》仪式文本相联，涉及审判与重生的观念，文本形态随时期演变。",
            "希腊神话中的冥界由哈迪斯掌管，英雄与亡者的冥界旅行构成叙事母题，见诸史诗与悲剧。",
            "不同传统的冥界在方位、审判与回归可能性上差异显著，不宜直接等同。"
        ],
        "interpretations": [
            {"holder": "Jean-Pierre Vernant", "school": "巴黎学派（古希腊神话与思想）", "view": "把希腊冥界与献祭、城邦秩序的图像体系联系起来分析，强调神话形象的历史语境，属学派研究。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "把冥界旅行置于通过仪式与宇宙论的框架中理解，强调其为跨文化的结构母题，属现象学参照。"},
            {"holder": "James George Frazer", "school": "早期比较宗教学", "view": "在死而复生神话的框架中讨论冥界主题，属早期学派观点，其资料使用已被现代学界修订。"}
        ],
        "comparisons": [
            {"tradition": "希腊神话", "basis_source": "aca-greek-myth-thought", "note": "Vernant 等对希腊冥界与献祭图像有专门研究，此处以该学术著作为依据记录有文献依据的比较。"},
            {"tradition": "北欧神话", "basis_source": "aca-comparative-myth", "note": "比较神话学在印欧框架内讨论冥界观念，学界对具体对应有争论，此处并列呈现不作定论。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>冥界母题对照示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>冥界母题对照（仅示意，不表示源流）</text><rect x='80' y='106' width='180' height='62' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='130' text-anchor='middle' fill='var(--svg-text)' font-size='13'>古埃及</text><text x='170' y='152' text-anchor='middle' fill='var(--svg-text)' font-size='12'>亡灵书·审判</text><rect x='290' y='106' width='180' height='62' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='130' text-anchor='middle' fill='var(--svg-text)' font-size='13'>希腊</text><text x='380' y='152' text-anchor='middle' fill='var(--svg-text)' font-size='12'>哈迪斯·冥界行</text><rect x='500' y='106' width='180' height='62' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='130' text-anchor='middle' fill='var(--svg-text)' font-size='13'>北欧</text><text x='590' y='152' text-anchor='middle' fill='var(--svg-text)' font-size='12'>亡者居所</text><line x1='170' y1='168' x2='170' y2='222' stroke='currentColor' opacity='0.5'/><line x1='380' y1='168' x2='380' y2='222' stroke='currentColor' opacity='0.5'/><line x1='590' y1='168' x2='590' y2='222' stroke='currentColor' opacity='0.5'/><rect x='140' y='222' width='480' height='56' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='246' text-anchor='middle' fill='var(--svg-text)' font-size='13'>共同关注：亡者归宿·审判·回归可能</text><text x='380' y='266' text-anchor='middle' fill='var(--svg-text)' font-size='12'>方位与观念差异显著，不直接等同</text><text x='380' y='340' text-anchor='middle' fill='var(--svg-text)' font-size='13'>比较需有文献依据，本站不自行牵强类比</text></svg>",
        "pending_notes": "1) 各传统冥界观念差异大，不作直接等同；2) Vernant、Frazer 的具体论点以其代表著作概括，细节待核对；3) 术语已统一：正文采用“英雄”译法。",
        "needs_verification": True
    },
    "motif-herojourney": {
        "level": "L2",
        "source_text": "英雄之旅母题指英雄离家、历险、归来的叙事结构，Joseph Campbell 在《千面英雄》中对其作了系统阐述。该模型影响广泛，但学界对其过度概括与材料取舍有批评，本站把它作为一种分析框架而非普遍定律来呈现。",
        "versions": [
            "Campbell 的“单一神话”把英雄旅程概括为若干阶段，属比较神话学的分析模型，非对每一具体文本的精确描述。",
            "《奥德赛》常作为该母题的经典案例，但其叙事细节与模型阶段并不逐一对应。",
            "其他传统的英雄叙事（如《吉尔伽美什》）在结构上既有相似也有差异，学界对模型的适用范围有讨论。"
        ],
        "interpretations": [
            {"holder": "Joseph Campbell", "school": "比较神话学（单一神话模型）", "view": "提出英雄旅程的普遍结构，强调其心理与仪式意涵；该模型影响广泛，但被批评为过度概括。"},
            {"holder": "Carl Jung", "school": "分析心理学（原型理论）", "view": "把英雄形象理解为集体无意识的原型表现，为 Campbell 提供心理学背景；其理论在学界有争论。"},
            {"holder": "Northrop Frye", "school": "文学原型批评", "view": "在文学类型与原型框架中分析英雄叙事的循环结构，属文学批评路径。"}
        ],
        "comparisons": [
            {"tradition": "美索不达米亚神话", "basis_source": "aca-hero-faces", "note": "Campbell 的著作把《吉尔伽美什》等纳入英雄旅程讨论，此处以该著作为依据记录比较，并标注模型的概括性。"},
            {"tradition": "印度史诗", "basis_source": "aca-archetypes", "note": "以荣格原型理论与史诗英雄叙事作框架性参照，属学界已有的分析路径，不主张文本同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>英雄旅程母题结构示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>英雄旅程母题（Campbell 模型的示意）</text><rect x='60' y='180' width='130' height='52' fill='var(--svg-node)' stroke='currentColor'/><text x='125' y='204' text-anchor='middle' fill='var(--svg-text)' font-size='13'>离家</text><text x='125' y='222' text-anchor='middle' fill='var(--svg-text)' font-size='12'>召唤·启程</text><line x1='190' y1='206' x2='225' y2='206' stroke='currentColor' opacity='0.5'/><rect x='225' y='180' width='130' height='52' fill='var(--svg-node)' stroke='currentColor'/><text x='290' y='204' text-anchor='middle' fill='var(--svg-text)' font-size='13'>历险</text><text x='290' y='222' text-anchor='middle' fill='var(--svg-text)' font-size='12'>试炼·伙伴</text><line x1='355' y1='206' x2='390' y2='206' stroke='currentColor' opacity='0.5'/><rect x='390' y='180' width='130' height='52' fill='var(--svg-node)' stroke='currentColor'/><text x='455' y='204' text-anchor='middle' fill='var(--svg-text)' font-size='13'>危机</text><text x='455' y='222' text-anchor='middle' fill='var(--svg-text)' font-size='12'>深渊·转化</text><line x1='520' y1='206' x2='555' y2='206' stroke='currentColor' opacity='0.5'/><rect x='555' y='180' width='140' height='52' fill='var(--svg-node)' stroke='currentColor'/><text x='625' y='204' text-anchor='middle' fill='var(--svg-text)' font-size='13'>归来</text><text x='625' y='222' text-anchor='middle' fill='var(--svg-text)' font-size='12'>带回馈赠</text><rect x='200' y='292' width='360' height='46' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>为分析模型，非对每部作品的精确描述</text></svg>",
        "pending_notes": "1) Campbell 模型被批评为过度概括，正文已标注；2) Jung、Frye 的具体论点以其代表著作概括，Frye 著作未录入 sources.json，细节待核对；3) “单一神话”译法与术语统一待办；本站不把它当作普遍定律。",
        "needs_verification": True
    },
    "motif-sun": {
        "level": "L2",
        "source_text": "太阳母题见于多传统的一手文献：古埃及的金字塔文与《亡灵书》以太阳神拉为核心，吠陀颂歌礼赞太阳神苏利耶。学界对太阳崇拜的比较有长期研究，本站只记录有文献依据的对照。",
        "versions": [
            "古埃及传统中拉居于创世与王权叙事核心，太阳的每日运行被赋予宇宙论意义，文本形态随时期演变。",
            "吠陀颂歌以苏利耶等太阳神为礼赞对象，太阳与秩序、光明的关联在颂诗中反复出现。",
            "不同传统的太阳神在性别、职能与谱系上差异显著，不宜直接等同或推断单一起源。"
        ],
        "interpretations": [
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "把太阳运行与宇宙循环、仪式时间相联系，视太阳崇拜为对宇宙秩序的周期性确认，属现象学层面的参照。"},
            {"holder": "Henri Frankfort", "school": "古代近东思想研究", "view": "以神话意象分析埃及太阳神与王权的关联，主张不以现代抽象标准误读古代宇宙观，属专门研究。"},
            {"holder": "James George Frazer", "school": "早期比较宗教学", "view": "在跨文化框架中讨论太阳神话，属早期学派观点，其具体结论在现代学界多经修订。"}
        ],
        "comparisons": [
            {"tradition": "埃及神话", "basis_source": "pri-pyramid-texts", "note": "以金字塔文原典为依据，记录太阳神拉在古埃及宇宙观中的核心地位，属文本层面的对照。"},
            {"tradition": "印度神话", "basis_source": "pri-rigveda", "note": "以《梨俱吠陀》太阳颂歌为依据，记录吠陀太阳神崇拜，不推断与埃及传统的传播关系。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>太阳母题跨传统示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>太阳母题跨传统（仅示意，不表示源流）</text><circle cx='380' cy='150' r='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='156' text-anchor='middle' fill='var(--svg-text)' font-size='14'>太阳</text><line x1='380' y1='196' x2='380' y2='234' stroke='currentColor' opacity='0.5'/><line x1='170' y1='234' x2='590' y2='234' stroke='currentColor' opacity='0.5'/><line x1='170' y1='234' x2='170' y2='272' stroke='currentColor' opacity='0.5'/><line x1='380' y1='234' x2='380' y2='272' stroke='currentColor' opacity='0.5'/><line x1='590' y1='234' x2='590' y2='272' stroke='currentColor' opacity='0.5'/><rect x='90' y='272' width='160' height='52' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='294' text-anchor='middle' fill='var(--svg-text)' font-size='13'>埃及·拉</text><text x='170' y='312' text-anchor='middle' fill='var(--svg-text)' font-size='12'>王权与创世</text><rect x='300' y='272' width='160' height='52' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='294' text-anchor='middle' fill='var(--svg-text)' font-size='13'>吠陀·苏利耶</text><text x='380' y='312' text-anchor='middle' fill='var(--svg-text)' font-size='12'>光明与秩序</text><rect x='510' y='272' width='160' height='52' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='294' text-anchor='middle' fill='var(--svg-text)' font-size='13'>其他传统</text><text x='590' y='312' text-anchor='middle' fill='var(--svg-text)' font-size='12'>职能各异</text></svg>",
        "pending_notes": "1) 各传统太阳神的职能与谱系差异大，不作直接等同；2) Eliade、Frazer 的具体论点以其代表著作概括，细节待核对；3) 不推断单一起源，比较需有文献依据。",
        "needs_verification": True
    },
    "motif-mother-goddess": {
        "level": "L2",
        "source_text": "母神母题指以生育、丰产与大地为特征的女神形象，见于多个传统的文献与考古材料。Frazer《金枝》与 Eliade《比较宗教的模式》对丰产女神与大地母题有专门讨论，本站只记录有文献依据的对照。",
        "versions": [
            "近东与地中海传统中有多位丰产与爱情女神，其职能与神话叙事各有不同，不能简单归并为一个女神原型。",
            "印度传统的性力派以女神为最高神格之一，与三相神体系中的男神形成不同的神学侧重。",
            "考古材料中的女性神像常被解读为丰产象征，但具体含义在学界存在争论，需谨慎对待。"
        ],
        "interpretations": [
            {"holder": "James George Frazer", "school": "早期比较宗教学", "view": "在《金枝》中把丰产女神与植物、季节仪式联系起来，属早期学派观点，其泛化结论在现代学界受到修订。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "在《比较宗教的模式》中分析大地、丰产与女神的宇宙论意涵，强调神话意象的结构，属现象学参照。"},
            {"holder": "Wendy Doniger", "school": "芝加哥学派（印度宗教与文本研究）", "view": "强调女神传统的多义性，警惕把多样女神简化为单一“大母神”原型；其解读在学界有讨论。"}
        ],
        "comparisons": [
            {"tradition": "印度神话", "basis_source": "aca-patterns-religion", "note": "以 Eliade《比较宗教的模式》为依据，记录丰产与大地女神母题的一般比较，不推断具体传播关系。"},
            {"tradition": "美索不达米亚神话", "basis_source": "aca-golden-bough", "note": "以 Frazer《金枝》为早期学派参照，记录近东丰产女神的比较，其结论已被现代学界修订，此处并列呈现。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>母神母题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>母神母题（仅示意，不表示同源）</text><rect x='280' y='88' width='200' height='48' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='118' text-anchor='middle' fill='var(--svg-text)' font-size='14'>母神母题</text><line x1='380' y1='136' x2='380' y2='176' stroke='currentColor' opacity='0.5'/><line x1='160' y1='176' x2='600' y2='176' stroke='currentColor' opacity='0.5'/><line x1='160' y1='176' x2='160' y2='216' stroke='currentColor' opacity='0.5'/><line x1='380' y1='176' x2='380' y2='216' stroke='currentColor' opacity='0.5'/><line x1='600' y1='176' x2='600' y2='216' stroke='currentColor' opacity='0.5'/><rect x='80' y='216' width='160' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='160' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>生育</text><text x='160' y='258' text-anchor='middle' fill='var(--svg-text)' font-size='12'>人类繁衍</text><rect x='300' y='216' width='160' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>丰产</text><text x='380' y='258' text-anchor='middle' fill='var(--svg-text)' font-size='12'>土地收获</text><rect x='520' y='216' width='160' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='600' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>大地</text><text x='600' y='258' text-anchor='middle' fill='var(--svg-text)' font-size='12'>宇宙论</text><rect x='230' y='312' width='300' height='44' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='340' text-anchor='middle' fill='var(--svg-text)' font-size='13'>多为不同功能女神，不宜并为单一原型</text></svg>",
        "pending_notes": "1) Frazer 的泛化结论已标为早期学派观点；2) Doniger 的具体论点以其著作概括，细节待核对；3) 考古女性神像的含义有争议，正文谨慎表述。",
        "needs_verification": True
    },
    "motif-dragon": {
        "level": "L2",
        "source_text": "龙与巨蛇母题见于多传统的文本与图像材料：欧洲的恶龙传说、中国的龙与水神及降雨信仰、中美洲的羽蛇神等。学界对不同文化中龙的解读有大量研究，本站只记录有文献依据的对照。",
        "versions": [
            "欧洲中世纪传统的龙多为需被英雄制服的怪物形象，与基督教象征体系有联系。",
            "中国传统的龙与水、降雨与王权相关，形象与欧洲的恶龙差异显著，不宜混同。",
            "中美洲的羽蛇神兼具神祇与王权叙事层次，与欧亚的龙在文化语境上不同。"
        ],
        "interpretations": [
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "把巨蛇／龙与混沌、宇宙秩序的确立联系起来，视为英雄制服混沌的母题，属现象学层面的参照。"},
            {"holder": "Joseph Campbell", "school": "比较神话学（单一神话模型）", "view": "在英雄旅程框架中把屠龙作为关键试炼环节，属分析模型，学界对其概括性有批评。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "主张神话动物常作为二元对立的中介，为分析龙的形象提供方法论参照，属学派一般立场。"}
        ],
        "comparisons": [
            {"tradition": "中国神话", "basis_source": "aca-comparative-myth", "note": "比较神话学在跨文化框架内讨论龙／蛇母题，此处记录一般学术对照，不推断欧亚与中国的传播关系。"},
            {"tradition": "中美洲神话", "basis_source": "enc-wiki-dragon", "note": "以权威百科条目作为羽蛇神与龙形象的一般参照（该来源未在线核验）；文化语境差异大，属弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>龙母题跨传统示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>龙／巨蛇母题（仅示意，不表示同源）</text><rect x='70' y='104' width='190' height='62' fill='var(--svg-node)' stroke='currentColor'/><text x='165' y='128' text-anchor='middle' fill='var(--svg-text)' font-size='13'>欧洲</text><text x='165' y='150' text-anchor='middle' fill='var(--svg-text)' font-size='12'>恶龙·待制服</text><rect x='285' y='104' width='190' height='62' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='128' text-anchor='middle' fill='var(--svg-text)' font-size='13'>中国</text><text x='380' y='150' text-anchor='middle' fill='var(--svg-text)' font-size='12'>水·降雨·王权</text><rect x='500' y='104' width='190' height='62' fill='var(--svg-node)' stroke='currentColor'/><text x='595' y='128' text-anchor='middle' fill='var(--svg-text)' font-size='13'>中美洲</text><text x='595' y='150' text-anchor='middle' fill='var(--svg-text)' font-size='12'>羽蛇神</text><rect x='200' y='232' width='360' height='60' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='13'>共同母题：巨蛇／龙</text><text x='380' y='276' text-anchor='middle' fill='var(--svg-text)' font-size='12'>文化语境差异显著，不宜混同</text><text x='380' y='346' text-anchor='middle' fill='var(--svg-text)' font-size='13'>比较需有文献依据，不推断同源</text></svg>",
        "pending_notes": "1) 不同文化龙的形象与职能差异大，不作直接等同；2) Lévi-Strauss 的中介说为学派立场，学界有讨论；3) 中美洲比较属弱参照，待补专门文献。",
        "needs_verification": True
    },
    "motif-worldtree": {
        "level": "L2",
        "source_text": "世界树（宇宙轴）母题以连接天、地与下界的巨树为特征，北欧的尤克特拉希尔是文献中记载较详的案例，见《诗体埃达》与《散文埃达》。学界对其跨文化比较有研究，本站只记录有文献依据的对照。",
        "versions": [
            "北欧传统中尤克特拉希尔联结诸界，诸神与命运在其上展开，是宇宙秩序的象征。",
            "其他传统中的宇宙轴也可能表现为柱、山或梯，功能上与世界树相近但形态不同。",
            "把不同文化的宇宙轴意象并置属母题层面的比较，不宜据此推断直接接触或同源。"
        ],
        "interpretations": [
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "把世界树作为“宇宙轴”与“世界中心”的典型意象，强调其沟通诸界与仪式的象征功能，属现象学参照。"},
            {"holder": "Georges Dumézil", "school": "印欧比较神话学", "view": "在印欧材料框架内讨论北欧宇宙观，属学派比较，具体到世界树的结论学界有讨论。"},
            {"holder": "John Lindow", "school": "北欧神话与民俗研究", "view": "强调北欧宇宙树材料的中世纪文本语境，主张区分诗歌证据与后世系统化叙述，其著作未录入来源库。"}
        ],
        "comparisons": [
            {"tradition": "北美原住民传统", "basis_source": "aca-eternal-return", "note": "以 Eliade 的宇宙轴框架作母题层面的一般参照，不主张具体传播关系。"},
            {"tradition": "美索不达米亚神话", "basis_source": "pri-poetic-eddas", "note": "以北欧原典为世界树母题的文本依据，与美索不达米亚宇宙观作框架性对照，待补专门比较文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>世界树宇宙轴示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>世界树：连接诸界的宇宙轴（示意）</text><line x1='380' y1='96' x2='380' y2='330' stroke='currentColor' opacity='0.7'/><line x1='250' y1='150' x2='510' y2='150' stroke='currentColor' opacity='0.4'/><line x1='250' y1='230' x2='510' y2='230' stroke='currentColor' opacity='0.4'/><line x1='250' y1='310' x2='510' y2='310' stroke='currentColor' opacity='0.4'/><rect x='540' y='126' width='170' height='48' fill='var(--svg-node)' stroke='currentColor'/><text x='625' y='156' text-anchor='middle' fill='var(--svg-text)' font-size='13'>上方：天界</text><rect x='540' y='206' width='170' height='48' fill='var(--svg-node)' stroke='currentColor'/><text x='625' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>中间：人间</text><rect x='540' y='286' width='170' height='48' fill='var(--svg-node)' stroke='currentColor'/><text x='625' y='316' text-anchor='middle' fill='var(--svg-text)' font-size='13'>下方：冥界</text><text x='380' y='360' text-anchor='middle' fill='var(--svg-text)' font-size='13'>尤克特拉希尔为文献记载较详的案例</text></svg>",
        "pending_notes": "1) 不同文化宇宙轴形态不同，比较仅限母题层面；2) Lindow 著作未录入 sources.json，已声明；3) 与北美、美索不达米亚的对照为框架性弱参照，待补专门文献。",
        "needs_verification": True
    },
    "motif-eschatology": {
        "level": "L2",
        "source_text": "末世母题叙述世界的终结与再生，见于一手文献如北欧的诸神黄昏诗歌与多种宗教经典。Eliade《永恒回归的神话》对宇宙周期与末世主题有讨论，本站只记录有文献依据的对照。",
        "versions": [
            "北欧传统中的诸神黄昏叙述诸神的败亡与世界更新，是末世母题的重要案例。",
            "亚伯拉罕诸教中的末世论涉及审判与救赎，与宇宙周期型末世在结构上不同。",
            "不同传统的末世叙事在是否循环、如何再生上差异显著，不宜直接等同。"
        ],
        "interpretations": [
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "在《永恒回归的神话》中讨论宇宙毁灭与重生的循环模式，视末世叙事为宇宙论的组成部分，属现象学参照。"},
            {"holder": "John Lindow", "school": "北欧神话与民俗研究", "view": "强调诸神黄昏材料主要见于基督教时代抄本，解读需考虑记录语境，其著作未录入来源库。"},
            {"holder": "Stephen Prothero", "school": "比较宗教学", "view": "强调各宗教末世目标不同，反对把不同传统的终末论简化为同一模式，属通俗学术著作的观点。"}
        ],
        "comparisons": [
            {"tradition": "北欧神话", "basis_source": "pri-poetic-eddas", "note": "以《诗体埃达》原典为依据，记录诸神黄昏母题，属文本层面的对照。"},
            {"tradition": "亚伯拉罕诸教", "basis_source": "aca-eternal-return", "note": "以 Eliade 的宇宙周期框架作一般参照，指出其与线性末世论的结构差异，不主张同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>末世母题结构示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>末世母题：终结与再生（示意）</text><rect x='70' y='150' width='150' height='56' fill='var(--svg-node)' stroke='currentColor'/><text x='145' y='174' text-anchor='middle' fill='var(--svg-text)' font-size='13'>现有秩序</text><text x='145' y='192' text-anchor='middle' fill='var(--svg-text)' font-size='12'>稳定期</text><line x1='220' y1='178' x2='270' y2='178' stroke='currentColor' opacity='0.5'/><rect x='270' y='150' width='150' height='56' fill='var(--svg-node)' stroke='currentColor'/><text x='345' y='174' text-anchor='middle' fill='var(--svg-text)' font-size='13'>终结</text><text x='345' y='192' text-anchor='middle' fill='var(--svg-text)' font-size='12'>毁灭·审判</text><line x1='420' y1='178' x2='470' y2='178' stroke='currentColor' opacity='0.5'/><rect x='470' y='150' width='150' height='56' fill='var(--svg-node)' stroke='currentColor'/><text x='545' y='174' text-anchor='middle' fill='var(--svg-text)' font-size='13'>再生</text><text x='545' y='192' text-anchor='middle' fill='var(--svg-text)' font-size='12'>更新·救赎</text><path d='M545 216 Q545 270 145 270 Q145 270 145 206' fill='none' stroke='currentColor' opacity='0.4'/><text x='380' y='300' text-anchor='middle' fill='var(--svg-text)' font-size='13'>部分传统为循环模式，部分为线性终末</text><text x='380' y='340' text-anchor='middle' fill='var(--svg-text)' font-size='12'>差异显著，不作直接等同</text></svg>",
        "pending_notes": "1) 循环与线性末世模式差异大，不作直接等同；2) Lindow 著作未录入 sources.json，已声明；3) 与亚伯拉罕诸教的比较为框架性参照，细节待核。",
        "needs_verification": True
    },
    "motif-trickster": {
        "level": "L2",
        "source_text": "诡计者母题以机智、欺骗与越界的角色为特征，见于多传统的神话与口传。比较神话学与民俗学对其有专门研究，本站只记录有文献依据的对照。",
        "versions": [
            "北欧的洛基兼具诡计与变形能力，其形象在《诗体埃达》与《散文埃达》中略有差异。",
            "其他传统中的诡计者可能兼具文化英雄与欺骗者两面，职能复合，不宜单一化。",
            "把不同文化的诡计者并置属母题层面的比较，需有文献依据，不推断同源。"
        ],
        "interpretations": [
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "把诡计者视为中介性角色，用以调和二元对立，属结构主义的一般立场，为分析提供方法论参照。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "可从越界与秩序重建的角度理解诡计者叙事，属现象学层面的框架参照。"},
            {"holder": "Jaan Puhvel", "school": "印欧比较神话学", "view": "在印欧材料框架内讨论相关角色，属学派比较，其适用范围学界有讨论。"}
        ],
        "comparisons": [
            {"tradition": "北欧神话", "basis_source": "pri-prose-eddas", "note": "以《散文埃达》原典为依据，记录洛基的诡计者形象，属文本层面的对照。"},
            {"tradition": "中国叙事传统", "basis_source": "aca-comparative-myth", "note": "以比较神话学通论作母题层面的一般参照，不推断与北欧材料的传播关系。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>诡计者母题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>诡计者母题（仅示意，不表示同源）</text><rect x='290' y='94' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='124' text-anchor='middle' fill='var(--svg-text)' font-size='14'>诡计者</text><line x1='380' y1='140' x2='380' y2='180' stroke='currentColor' opacity='0.5'/><line x1='180' y1='180' x2='580' y2='180' stroke='currentColor' opacity='0.5'/><line x1='180' y1='180' x2='180' y2='218' stroke='currentColor' opacity='0.5'/><line x1='380' y1='180' x2='380' y2='218' stroke='currentColor' opacity='0.5'/><line x1='580' y1='180' x2='580' y2='218' stroke='currentColor' opacity='0.5'/><rect x='90' y='218' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='180' y='240' text-anchor='middle' fill='var(--svg-text)' font-size='13'>机智</text><text x='180' y='258' text-anchor='middle' fill='var(--svg-text)' font-size='12'>以智取胜</text><rect x='290' y='218' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='240' text-anchor='middle' fill='var(--svg-text)' font-size='13'>欺骗</text><text x='380' y='258' text-anchor='middle' fill='var(--svg-text)' font-size='12'>越界行事</text><rect x='490' y='218' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='580' y='240' text-anchor='middle' fill='var(--svg-text)' font-size='13'>中介</text><text x='580' y='258' text-anchor='middle' fill='var(--svg-text)' font-size='12'>调和两极</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>常兼具文化英雄与欺骗者两面</text></svg>",
        "pending_notes": "1) 诡计者形象复合，不宜单一化；2) Lévi-Strauss 的中介说为学派立场，学界有讨论；3) 与中国叙事传统的比较为框架性弱参照，待补专门文献。",
        "needs_verification": True
    },
    "fig-zeus": {
        "level": "L2",
        "source_text": "宙斯是希腊神话的奥林匹斯主神，主要见于赫西俄德《神谱》与荷马《伊利亚特》《奥德赛》，另在阿波罗多洛斯《书库》与保萨尼亚斯《希腊志》中有地方传说记载。不同文献中的形象并不完全一致。",
        "versions": [
            "《神谱》叙述宙斯在神权更替中击败克洛诺斯，确立奥林匹斯秩序，侧重谱系与权力继承。",
            "荷马史诗中的宙斯是既成秩序的主宰，其权威需与其他神祇协商，更多参与人间事务。",
            "地方崇拜中的宙斯有不同称号与职能，与泛希腊版本并存，不宜视为单一形象。"
        ],
        "interpretations": [
            {"holder": "Jean-Pierre Vernant", "school": "巴黎学派（古希腊神话与思想）", "view": "把宙斯的权威与城邦公共秩序的图像体系联系起来分析，属有文献依据的学派研究。"},
            {"holder": "Walter Burkert", "school": "宗教史学派", "view": "强调希腊宗教的祭祀实践核心与近东影响，将宙斯置于历史宗教史语境，属学术研究。"},
            {"holder": "Georges Dumézil", "school": "印欧比较神话学", "view": "以三功能假说把宙斯与印欧天父神功能对照，属学派模型，学界对其适用性有讨论。"}
        ],
        "comparisons": [
            {"tradition": "北欧神话", "basis_source": "aca-gods-indo-europeans", "note": "Dumézil 的印欧比较把宙斯与奥丁等作功能对照，属学派框架，不主张直接同源。"},
            {"tradition": "罗马神话", "basis_source": "pri-virgil-aeneid", "note": "以《埃涅阿斯纪》等罗马文学为依据，记录宙斯与朱庇特的传统对应，属文本层面的对照。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>宙斯形象来源示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>宙斯形象的主要文献来源</text><rect x='280' y='88' width='200' height='48' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='118' text-anchor='middle' fill='var(--svg-text)' font-size='14'>宙斯</text><line x1='380' y1='136' x2='380' y2='172' stroke='currentColor' opacity='0.5'/><line x1='150' y1='172' x2='610' y2='172' stroke='currentColor' opacity='0.5'/><line x1='150' y1='172' x2='150' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='172' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='610' y1='172' x2='610' y2='212' stroke='currentColor' opacity='0.5'/><rect x='70' y='212' width='160' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='150' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>神谱</text><text x='150' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>谱系·神权更替</text><rect x='300' y='212' width='160' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>荷马史诗</text><text x='380' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>既成秩序</text><rect x='530' y='212' width='160' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='610' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>地方传说</text><text x='610' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>书库·希腊志</text><text x='380' y='322' text-anchor='middle' fill='var(--svg-text)' font-size='13'>不同文献中的形象并不完全一致</text></svg>",
        "pending_notes": "1) 三功能模型为学派框架，学界有争论；2) 各文献形象差异已并列呈现，不替读者下结论；3) 比较需有文献依据，不主张直接同源。",
        "needs_verification": True
    },
    "fig-odin": {
        "level": "L2",
        "source_text": "奥丁是北欧神话的至高神之一，主要见于《诗体埃达》与《散文埃达》，另在萨迦中有所记载。现存文本多经中世纪基督教抄写者记录，其原始形象与后世叙述之间的关系为学界讨论议题。",
        "versions": [
            "《诗体埃达》的诗歌中奥丁兼具智慧、战争与亡灵管理等职能，形象较为复合。",
            "《散文埃达》把奥丁置于系统化的神谱与历史化解释框架中，属于作者的系统化处理。",
            "斯诺里的历史化解释把诸神追溯到古代君王，与诗歌材料的神话叙述形成对照。"
        ],
        "interpretations": [
            {"holder": "Georges Dumézil", "school": "印欧比较神话学", "view": "以三功能假说把奥丁归为主权功能，与托尔、弗雷对应，属学派模型，学界对其适用性有讨论。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "可从智慧、战争与亡灵的复合职能作现象学层面的参照，属框架性对照。"},
            {"holder": "John Lindow", "school": "北欧神话与民俗研究", "view": "强调奥丁材料的中世纪文本语境与口传—书写过渡，主张区分诗歌证据与后世系统化叙述，其著作未录入来源库。"}
        ],
        "comparisons": [
            {"tradition": "希腊神话", "basis_source": "aca-gods-indo-europeans", "note": "Dumézil 的印欧比较把奥丁与宙斯等作功能对照，属学派框架，不主张直接同源。"},
            {"tradition": "印度神话", "basis_source": "aca-comparative-myth", "note": "比较神话学在印欧语系框架内并置北欧与印度神系，属学术对照，具体对应关系有讨论。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>奥丁形象与文献示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>奥丁形象的主要文献来源</text><rect x='280' y='88' width='200' height='48' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='118' text-anchor='middle' fill='var(--svg-text)' font-size='14'>奥丁</text><line x1='380' y1='136' x2='380' y2='172' stroke='currentColor' opacity='0.5'/><line x1='150' y1='172' x2='610' y2='172' stroke='currentColor' opacity='0.5'/><line x1='150' y1='172' x2='150' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='172' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='610' y1='172' x2='610' y2='212' stroke='currentColor' opacity='0.5'/><rect x='70' y='212' width='160' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='150' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>诗体埃达</text><text x='150' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>古老诗歌</text><rect x='300' y='212' width='160' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>散文埃达</text><text x='380' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>系统化叙述</text><rect x='530' y='212' width='160' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='610' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>萨迦</text><text x='610' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>历史传说</text><text x='380' y='322' text-anchor='middle' fill='var(--svg-text)' font-size='13'>材料多经中世纪记录，形象复合</text></svg>",
        "pending_notes": "1) 现存文本的中世纪记录语境已标注；2) Lindow 著作未录入 sources.json，已声明；3) 三功能模型为学派框架，不替读者下结论。",
        "needs_verification": True
    },
    "fig-ra": {
        "level": "L2",
        "source_text": "拉是古埃及的太阳神，在金字塔文、棺椁文与《亡灵书》中居核心地位，并与王权叙事相联。不同时期与地点的传统并不统一，拉的职能与形象随历史演变。",
        "versions": [
            "古王国金字塔文中拉与王权、太阳运行紧密关联，是创世与死后重生叙事的核心神祇。",
            "中王国与新王国时期拉与阿蒙结合为阿蒙—拉，神学中心发生转移。",
            "阿肯那顿改革短暂推行阿顿崇拜，改革后恢复旧有神系，反映宗教与政治的互动。"
        ],
        "interpretations": [
            {"holder": "Henri Frankfort", "school": "古代近东思想研究", "view": "以神话意象分析拉与王权、宇宙秩序的关联，主张不以现代抽象标准误读埃及宇宙观，属专门研究。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "把太阳神的每日运行与宇宙循环、仪式时间相联系，属现象学层面的参照。"},
            {"holder": "James P. Allen", "school": "埃及学（宗教文本研究）", "view": "强调埃及创世与太阳神传统的多元并存，主张各中心表述为并行而非单线演进，其著作未录入来源库。"}
        ],
        "comparisons": [
            {"tradition": "印度神话", "basis_source": "pri-rigveda", "note": "以《梨俱吠陀》太阳颂歌为依据，记录埃及拉与吠陀太阳神的母题对照，不推断传播关系。"},
            {"tradition": "日本神话", "basis_source": "enc-brit-shinto", "note": "以权威百科条目作太阳神母题的一般参照（该来源未在线核验），文化语境差异大，属弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>拉的神学与历史演变示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>拉：太阳神与王权（示意）</text><circle cx='380' cy='132' r='40' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='138' text-anchor='middle' fill='var(--svg-text)' font-size='14'>拉</text><line x1='380' y1='172' x2='380' y2='210' stroke='currentColor' opacity='0.5'/><line x1='150' y1='210' x2='610' y2='210' stroke='currentColor' opacity='0.5'/><line x1='150' y1='210' x2='150' y2='248' stroke='currentColor' opacity='0.5'/><line x1='380' y1='210' x2='380' y2='248' stroke='currentColor' opacity='0.5'/><line x1='610' y1='210' x2='610' y2='248' stroke='currentColor' opacity='0.5'/><rect x='70' y='248' width='160' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='150' y='272' text-anchor='middle' fill='var(--svg-text)' font-size='13'>金字塔文</text><text x='150' y='292' text-anchor='middle' fill='var(--svg-text)' font-size='12'>王权·创世</text><rect x='300' y='248' width='160' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='272' text-anchor='middle' fill='var(--svg-text)' font-size='13'>阿蒙—拉</text><text x='380' y='292' text-anchor='middle' fill='var(--svg-text)' font-size='12'>神学中心转移</text><rect x='530' y='248' width='160' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='610' y='272' text-anchor='middle' fill='var(--svg-text)' font-size='13'>亡灵书</text><text x='610' y='292' text-anchor='middle' fill='var(--svg-text)' font-size='12'>冥界·重生</text><text x='380' y='346' text-anchor='middle' fill='var(--svg-text)' font-size='12'>各时期传统并存，非单线演进</text></svg>",
        "pending_notes": "1) 各时期神学中心的演变年代有争论，正文未列具体年数；2) Allen 著作未录入 sources.json，已声明；3) 与日本太阳神的比较为弱参照，待补专门文献。",
        "needs_verification": True
    },
    "fig-pangu": {
        "level": "L2",
        "source_text": "盘古是中国神话中的创世神，以身躯化生天地的叙事著称。其系统记载见于较晚文献（如三国时期典籍的辑佚引文），早期形态与口传关系是学界讨论议题，本站如实标注待核实。",
        "versions": [
            "盘古开天地的叙事在较晚文献中才有系统记载，其最早出处的辑佚性质与年代待核实。",
            "盘古身体化生天地万物的母题，与典籍中其他创世叙述并存，二者关系为研究议题。",
            "后世的民间叙述与文献记载在细节上有所差异，反映神话的流传演变。"
        ],
        "interpretations": [
            {"holder": "袁珂", "school": "中国神话学（神话整理与研究）", "view": "通过辑录散见文献整理中国神话，指出其片段化特征，其著作未录入 sources.json。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "以宇宙创生与“永恒回归”（eternal return）框架理解化生型创世，属现象学参照，不直接等同于对中国材料的专门结论。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "为分析化生神话中的对立与中介提供方法论参照，属学派一般立场。"}
        ],
        "comparisons": [
            {"tradition": "北欧神话", "basis_source": "aca-eternal-return", "note": "以 Eliade 的创世母题框架把盘古化生与北欧原初巨人化生作现象学层面的并置，属纯框架性参照，不推断源流。"},
            {"tradition": "印度神话", "basis_source": "aca-short-history-myth", "note": "以通论性神话著作作创世母题的一般参照，具体文本关联待专门文献核对。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>盘古化生母题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>盘古化生天地万物（示意）</text><rect x='300' y='92' width='160' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>盘古</text><line x1='380' y1='138' x2='380' y2='178' stroke='currentColor' opacity='0.5'/><line x1='150' y1='178' x2='610' y2='178' stroke='currentColor' opacity='0.5'/><line x1='150' y1='178' x2='150' y2='216' stroke='currentColor' opacity='0.5'/><line x1='380' y1='178' x2='380' y2='216' stroke='currentColor' opacity='0.5'/><line x1='610' y1='178' x2='610' y2='216' stroke='currentColor' opacity='0.5'/><rect x='70' y='216' width='160' height='52' fill='var(--svg-node)' stroke='currentColor'/><text x='150' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>天</text><text x='150' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>清气上升</text><rect x='300' y='216' width='160' height='52' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>地</text><text x='380' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>浊气下沉</text><rect x='530' y='216' width='160' height='52' fill='var(--svg-node)' stroke='currentColor'/><text x='610' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>万物</text><text x='610' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>身躯化生</text><rect x='230' y='312' width='300' height='44' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='340' text-anchor='middle' fill='var(--svg-text)' font-size='13'>最早出处辑佚性质与年代待核实</text></svg>",
        "pending_notes": "1) 盘古传说最早出处的辑佚性质与年代待核实，已标注；2) 袁珂、Lévi-Strauss 的具体论点待逐条核对，袁珂著作未录入 sources.json；3) 与北欧、印度的比较为框架性参照，不推断源流。",
        "needs_verification": True
    }
}
