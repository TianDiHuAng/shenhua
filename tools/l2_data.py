# -*- coding: utf-8 -*-
"""L2 深度升级内容池。每条七节：来源文本/故事梗概已在L1/版本差异/解读/比较/SVG/待核实。
纪律：学者与学派必须真实可考；比较必须有 sources.json 中的 basis_source；不编造数字与引文。
"""

L2_DATA = {
    "myth-norse": {
        "level": "L3",
        "controversies": [
            {"issue": "诸神黄昏是否受基督教末世观影响", "views": [
                {"holder": "部分学者", "basis": "认为诸神黄昏的末世—重生结构与基督教启示文学存在可比性，且文本成于基督教时代，可能受其影响。"},
                {"holder": "另一些学者", "basis": "主张宇宙周期观源于异教传统，基督教影响有限且难确证，须区分抄写语境与材料来源。"}]},
            {"issue": "Dumézil 三功能模型对北欧神系的适用性", "views": [
                {"holder": "Georges Dumézil 及支持者", "basis": "以奥丁—托尔—弗雷对应主权、战争、丰产三功能（见《印欧人的神》）。"},
                {"holder": "批评者", "basis": "认为三功能划分是事后套用，北欧材料未必严格符合，存在简化与选择性取材之嫌。"}]}
        ],
        "data_points": [
            {"claim": "《诗体埃达》主要保存于13世纪冰岛抄本（如 Codex Regius），其诗歌成文年代多早于抄本。", "basis_source": "pri-poetic-eddas"},
            {"claim": "《散文埃达》由斯诺里·斯图鲁松约13世纪编纂，以历史化方式解释诸神。", "basis_source": "pri-prose-eddas"}
        ],
        "source_text": "北欧神话主要见于中世纪冰岛文献：《诗体埃达》保存古老众神诗歌，《散文埃达》由斯诺里·斯蒂德吕松系统化叙述并以欧赫墨罗斯主义（Euhemerism，神祇历史化）方式解释诸神，另有萨迦与《贝奥武甫》等日耳曼材料。这些文本多经基督教时代抄写者记录，其原始形态与成文年代存在学术讨论。",
        "versions": [
            "《诗体埃达》的预言诗与神祇诗歌较少系统化叙述，保留较古老的众神形象与宇宙末日（诸神的黄昏）意象。",
            "《散文埃达》把诗歌材料整理为连贯的创世与神祇谱系，并明确提出诸神原为古代英雄/君王的历史化解释，属于作者的系统化处理。",
            "萨克索·格拉玛提库斯《丹麦人的业绩》以拉丁文改写北欧传说，同样带有历史化与基督教时代立场，与冰岛材料形成对照。"
        ],
        "interpretations": [
            {"holder": "Georges Dumézil", "school": "印欧比较神话学（三功能假说）", "view": "（据《印欧人的神》）以主权、战争、丰产三功能解析印欧神系，北欧的奥丁、托尔、弗雷被作为三功能的对应案例；此为学派模型，非唯一解释。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "（据《永恒回归的神话》）把宇宙树与诸神的黄昏置于宇宙周期与“永恒回归”（eternal return）的框架中理解，强调神话时间与仪式的关联。"},
            {"holder": "John Lindow", "school": "北欧神话与民俗研究", "view": "强调现存文本的中世纪语境与口传—书写过渡，主张区分诗歌材料与后世的系统化叙述；其著作未录入来源库。"}
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
        "level": "L3",
        "controversies": [
            {"issue": "埃及创世叙事是多元并立还是单线演进", "views": [
                {"holder": "James P. Allen 等", "basis": "认为赫利奥波利斯、孟菲斯、底比斯等创世传统是并行的神学表达，各有中心，非单线演进。"},
                {"holder": "部分旧说", "basis": "曾倾向按时间顺序把不同中心传统排成演进序列，现代学界多不采。"}]},
            {"issue": "阿肯那顿宗教改革的性质", "views": [
                {"holder": "一解释", "basis": "视为接近一神教的阿顿崇拜革命。"},
                {"holder": "另一解释", "basis": "认为仍属王权操纵的单一主神崇拜，未否定其他神祇，须区分宫廷神学与民间实践。"}]}
        ],
        "data_points": [
            {"claim": "金字塔文是现存最早的埃及宗教文本群之一，见于古王国金字塔内壁。", "basis_source": "pri-pyramid-texts"},
            {"claim": "《亡灵书》诸版本随新王国时期流行，内容因时期与墓主而异。", "basis_source": "pri-book-dead"}
        ],
        "source_text": "埃及神话的材料跨越数千年，主要包括古王国金字塔文、中王国棺椁文与新王国《亡灵书》，另有神庙铭文与希腊罗马时期记录。不同时期与地点的创世叙事并不统一，赫利奥波利斯、孟菲斯、底比斯等地各有传统。",
        "versions": [
            "赫利奥波利斯传统以阿图姆（或拉）为原初神，经舒与泰芙努特、盖布与努特展开为九柱神谱系。",
            "孟菲斯神学把创世归于普塔神的思想与言语，属神学中心转移后的系统化表达。",
            "底比斯传统抬高阿蒙并与拉结合为阿蒙—拉；新王国时期的阿肯那顿改革短暂推行阿顿崇拜，改革后恢复旧有神系。"
        ],
        "interpretations": [
            {"holder": "Henri Frankfort", "school": "古代近东思想研究", "view": "（据《哲学之前》）主张埃及与美索不达米亚的创世叙事以神话意象把握宇宙秩序，与现代抽象哲学的因果推演方式不同，不应以后者标准误读。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "（据《永恒回归的神话》）把创世叙事与尼罗河泛滥的季节性循环、王权仪式的重演相联系，视神话为对宇宙秩序的周期性确认。"},
            {"holder": "James P. Allen", "school": "埃及学（宗教文本研究）", "view": "强调埃及创世文本的多元并存，主张各中心传统是并行的神学表达而非单线演进；其著作未录入来源库。"}
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
        "level": "L3",
        "controversies": [
            {"issue": "洪水叙事两版本（阿特拉哈西斯 vs 吉尔伽美什）的先后与依赖关系", "views": [
                {"holder": "承袭说", "basis": "认为《吉尔伽美什》洪水段落承袭较早的《阿特拉哈西斯》。"},
                {"holder": "共同源头说", "basis": "认为二者共享更早的口传传统，彼此无直接依赖，年代先后难定。"}]},
            {"issue": "《巴比伦创世史诗》的性质", "views": [
                {"holder": "政治神学解释", "basis": "认为是巴比伦抬升马尔杜克、确立城邦神学地位的产物。"},
                {"holder": "神庙神学解释", "basis": "认为更多是神庙祭祀语境下的文学编纂，政治功能为次。"}]}
        ],
        "data_points": [
            {"claim": "《巴比伦创世史诗》(Enuma Elish) 约成书于公元前12—11世纪，以马尔杜克为中心。", "basis_source": "pri-enuma-elish"},
            {"claim": "《吉尔伽美什史诗》有多种版本，巴比伦标准版约公元前13—10世纪编定。", "basis_source": "pri-gilgamesh"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "中国神话是否“零散化”、缺乏系统创世史诗", "views": [
                {"holder": "袁珂等整理派", "basis": "认为中国神话多片段保存，需辑佚整理才能显出脉络。"},
                {"holder": "部分学者", "basis": "认为“片段化”部分是近代整理框架造成，古代材料本就以散见为常态。"}]},
            {"issue": "盘古神话的来源与年代", "views": [
                {"holder": "本土晚出说", "basis": "盘古系统记载最早见于三国徐整《三五历纪》的辑佚引文，属较晚出。"},
                {"holder": "比较关联说", "basis": "有比较学者提出盘古化生与印度原人/宇宙卵母题的可能关联，学界有争论，未定论。"}]}
        ],
        "data_points": [
            {"claim": "盘古神话的系统记载最早见于三国时期文献的辑佚引文（原书已佚）。", "basis_source": "aca-short-history-myth"},
            {"claim": "《山海经》为神话地理与神祇材料的汇编，非一时一人所作。", "basis_source": "pri-shan-hai-jing"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "吠陀传统进入南亚的解释（移民论 vs 本土连续论）", "views": [
                {"holder": "移民说", "basis": "认为说印欧语的群体约公元前二千纪迁入南亚，带来吠陀传统。"},
                {"holder": "本土连续说", "basis": "强调南亚本地文化连续性，主张外来影响与本土传统长期融合，具体程度有争论。"}]},
            {"issue": "三相神的形成", "views": [
                {"holder": "自然发展说", "basis": "认为梵天—毗湿奴—湿婆由吠陀神系自然演化而来。"},
                {"holder": "后世整合说", "basis": "认为三相神格局主要成形于史诗—往世书时期，是后期的重新整合。"}]}
        ],
        "data_points": [
            {"claim": "《梨俱吠陀》被认为成书于约公元前1500—1200年，是现存最早的印度宗教文本之一。", "basis_source": "pri-rigveda"},
            {"claim": "两大史诗《摩诃婆罗多》《罗摩衍那》成书跨度长，经历长期增补。", "basis_source": "pri-mahabharata"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "《古事记》《日本书纪》的编纂意图与史料价值", "views": [
                {"holder": "政治编纂说", "basis": "认为两书为确立天皇世系合法性而编纂，神话被纳入王统叙事。"},
                {"holder": "材料分层说", "basis": "认为两书仍保存大量早期神话与口传材料，须区分原始层次与编纂加工。"}]},
            {"issue": "天照大神与皇祖神、伊势崇拜结合的年代", "views": [
                {"holder": "早期既有说", "basis": "认为太阳女神崇拜起源甚早。"},
                {"holder": "后世整合说", "basis": "认为其与皇祖神、伊势神宫的结合主要完成于律令国家时期，含政治整合。"}]}
        ],
        "data_points": [
            {"claim": "《古事记》成书于712年，《日本书纪》于720年，均属奈良时代官修。", "basis_source": "pri-kojiki"},
            {"claim": "两书记事与措辞存在差异，《日本书纪》附有异文。", "basis_source": "pri-nihon-shoki"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "《波波尔·乌》的文本层次与殖民记录的影响", "views": [
                {"holder": "传统保存说", "basis": "认为其保存了前殖民的基切玛雅创世与英雄双子传统。"},
                {"holder": "中介影响说", "basis": "认为文本经殖民早期转录，可能受记录者与基督教语境影响，须分辨层次。"}]},
            {"issue": "古典期铭文与殖民期文本能否直接对应", "views": [
                {"holder": "谨慎对应说", "basis": "认为图像与铭文可与后世神话母题谨慎互证。"},
                {"holder": "时段区隔说", "basis": "认为古典期城邦材料与殖民期文本相隔甚远，不能直接等同。"}]}
        ],
        "data_points": [
            {"claim": "《波波尔·乌》以基切玛雅语记录，成文于殖民早期（约16世纪中叶）。", "basis_source": "pri-popol-vuh"},
            {"claim": "玛雅神话材料包括殖民期文本、古典期铭文与考古图像，需互证。", "basis_source": "ins-world-history"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "宇宙纪元（前四个太阳纪）的细节", "views": [
                {"holder": "文献甲", "basis": "不同编年史对各纪元名称、结局的记载互有出入。"},
                {"holder": "文献乙", "basis": "另一系记录强调不同的毁灭方式与时长，难统一。"}]},
            {"issue": "羽蛇神兼具神祇与历史祭司—统治者层次", "views": [
                {"holder": "神祇说", "basis": "主要作为风、智慧与文明赐予之神。"},
                {"holder": "历史神化说", "basis": "认为与托尔特克统治者（如 Topiltzin Quetzalcoatl）的传说相互叠合，属历史人物的神化。"}]}
        ],
        "data_points": [
            {"claim": "阿兹特克神话多经殖民时期记录与前殖民抄本重建，记录立场各异。", "basis_source": "ins-world-history"},
            {"claim": "太阳神崇拜与王权、祭仪紧密相关。", "basis_source": "ins-british-museum"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "新约各卷的成书年代与作者归属", "views": [
                {"holder": "传统归属说", "basis": "按教会传统把福音书归于马太、马可、路加、约翰。"},
                {"holder": "现代文本批评", "basis": "认为福音书作者多不可考、成书于公元1世纪后期、相互有承继，作者归属为后世追认。"}]},
            {"issue": "诺斯替文献与正统正典的关系", "views": [
                {"holder": "Elaine Pagels 等", "basis": "认为早期基督教内部存在多样传统，诺斯替亦属其一，正典化含权力选择（见《诺斯替福音》）。"},
                {"holder": "正统派立场/批评者", "basis": "主张正典形成有信仰与使徒传承依据，诺斯替属后期偏离。"}]}
        ],
        "data_points": [
            {"claim": "新约正典的形成经历数世纪，各地教会对书卷的接受程度不一。", "basis_source": "aca-gnostic-gospels"},
            {"claim": "《圣经》钦定本（KJV）1611年刊行，属公共领域英文译本。", "basis_source": "pri-bible-kjv"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "《古兰经》的成文与汇编过程", "views": [
                {"holder": "传统叙述", "basis": "认为经文在哈里发时期被统一搜集为定本、抄本标准化。"},
                {"holder": "现代文本研究", "basis": "据早期抄本（如萨那抄本）变异等材料，主张早期文本存在书写层面差异，具体过程仍有讨论。"}]},
            {"issue": "圣训的真实性与甄别方法", "views": [
                {"holder": "传统圣训学", "basis": "以传述链（isnad）与传述者诚信为核心标准甄别真伪。"},
                {"holder": "现代历史批判", "basis": "对部分圣训的传述链可靠性与年代存疑，主张结合历史语境审慎使用。"}]}
        ],
        "data_points": [
            {"claim": "《古兰经》以阿拉伯语传述，共114章，不同译本语义有差异。", "basis_source": "pri-quran"},
            {"claim": "逊尼与什叶的分野源于早期继承问题，形成于数世纪的历史过程。", "basis_source": "enc-brit-islam"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "凯尔特神话是否存在可重建的统一体系", "views": [
                {"holder": "统一体系说", "basis": "认为可据语言与母题重建共同的凯尔特神系。"},
                {"holder": "地方性说", "basis": "如 Mac Cana 强调地方性、口传底色与中世纪文本中介，反对统一化重建。"}]},
            {"issue": "高卢（大陆）与岛屿凯尔特材料的连续性", "views": [
                {"holder": "延续说", "basis": "认为大陆与岛屿传统在母题上有延续。"},
                {"holder": "区隔说", "basis": "认为二者时空距离大，高卢材料主要靠古典记载与考古，不能与中世纪岛屿文本直接等同。"}]}
        ],
        "data_points": [
            {"claim": "《马比诺吉昂》保存威尔士神话故事集，成文于中世纪（约12—14世纪）。", "basis_source": "pri-mabinogion"},
            {"claim": "《侵略之书》汇编爱尔兰伪史与神祇传说。", "basis_source": "pri-lebor-gabala"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "托拉（摩西五经）的成书", "views": [
                {"holder": "传统说", "basis": "按传统归于摩西。"},
                {"holder": "底本假说（文本批评）", "basis": "以来源分析提出 JEDP 等底本，认为五经为长期编纂，学界主流采底本说但细节仍有争论。"}]},
            {"issue": "卡巴拉的历史起源", "views": [
                {"holder": "古代口传说", "basis": "视卡巴拉为自古代延续的秘传传统。"},
                {"holder": "中世纪成型说", "basis": "如 Scholem 等主张卡巴拉主要成型于中世纪（如《光辉之书》13世纪），古代渊源难以确证。"}]}
        ],
        "data_points": [
            {"claim": "犹太教核心经典为《托拉》，并以《塔木德》诠释律法。", "basis_source": "pri-bible-kjv"},
            {"claim": "犹太教内部存在正统、保守、改革等宗派，对律法权威的回应各异。", "basis_source": "enc-brit-judaism"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "大乘经典是否为历史佛陀亲说", "views": [
                {"holder": "大乘传统立场", "basis": "视大乘经为佛陀教说（依法身/传承理解，非仅历史肉身所说）。"},
                {"holder": "现代学界主流", "basis": "多认为大乘经典成于佛灭后数世纪，非历史佛陀亲口所说，属教团发展产物。"}]},
            {"issue": "“无我”与轮回主体的关系", "views": [
                {"holder": "无我论", "basis": "主张诸法无我，轮回依缘起相续而无实体主体。"},
                {"holder": "补特伽罗/相续解释", "basis": "不同部派以“补特伽罗”或心识相续解释轮回的连续性与业力承担。"}]}
        ],
        "data_points": [
            {"claim": "佛教经典结集为三藏（经、律、论），不同部派传承有别。", "basis_source": "pri-dhammapada"},
            {"claim": "佛教分南传、汉传、藏传三大系统，经典语言与制度各异。", "basis_source": "enc-brit-buddhism"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "印度教是否为单一宗教", "views": [
                {"holder": "统一传统说", "basis": "视印度教为有共同经典与观念的统一宗教传统。"},
                {"holder": "多元建构说", "basis": "如 Doniger 等强调其内部多元，“印度教”部分为近代统称，涵盖差异极大的实践。"}]},
            {"issue": "种姓制度的经典依据与历史形成", "views": [
                {"holder": "传统依据说", "basis": "以《梨俱吠陀》原人歌等为种姓的经典依据。"},
                {"holder": "历史建构说", "basis": "认为种姓的具体形态随历史演变，经典文本与实际制度之间有复杂落差。"}]}
        ],
        "data_points": [
            {"claim": "印度教经典包括吠陀、奥义书、史诗与往世书，跨越长时段。", "basis_source": "pri-rigveda"},
            {"claim": "印度教内部有毗湿奴派、湿婆派、性力派等多元传统。", "basis_source": "enc-brit-hinduism"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "道家哲学与制度化道教的关系", "views": [
                {"holder": "连续发展说", "basis": "认为道家思想经发展演化为道教实践。"},
                {"holder": "性质区分说", "basis": "如刘笑敢等主张区分原始哲学文本与后世宗教诠释，二者性质不同。"}]},
            {"issue": "《道德经》的作者与成书年代", "views": [
                {"holder": "传统说", "basis": "归于老子（李耳）。"},
                {"holder": "现代考据说", "basis": "多认为成书于战国、非一时一人，编者与年代有争论。"}]}
        ],
        "data_points": [
            {"claim": "《道德经》约五千言，分《道经》《德经》，有公共领域译本。", "basis_source": "pri-tao-te-ching"},
            {"claim": "《庄子》为道家重要文本，兼具哲学与寓言，成书亦非一人一时。", "basis_source": "pri-zhuangzi"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "儒家是否为“宗教”（“儒教”定性之争）", "views": [
                {"holder": "宗教性传统说", "basis": "强调其祭祀、天道与终极关怀，可视为宗教性传统。"},
                {"holder": "伦理政治哲学说", "basis": "认为儒家主要是伦理与政治哲学，是否称“教”学界有争论。"}]},
            {"issue": "《论语》的可信度", "views": [
                {"holder": "辑录可信说", "basis": "视为孔子及其弟子言行辑录，可据以重建孔子思想。"},
                {"holder": "层次不一说的谨慎立场", "basis": "认为成书分层、部分记载经后学加工，须分辨。"}]}
        ],
        "data_points": [
            {"claim": "《论语》为孔子及其弟子言行的辑录，成书约在战国前期。", "basis_source": "pri-analects"},
            {"claim": "《易经》为占筮经典，后被儒家列为经典，成书年代有争议。", "basis_source": "pri-i-ching"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "神道教是“宗教”还是“祭祀传统”", "views": [
                {"holder": "宗教说", "basis": "视其具备神祇、祭祀与世界观，为一种宗教。"},
                {"holder": "实践传统说", "basis": "认为其以神社祭祀与洁净为核心、缺乏统一教义，与制度化宗教有别。"}]},
            {"issue": "近代国家神道的性质与角色", "views": [
                {"holder": "制度批判说", "basis": "认为国家神道曾被制度化以服务国家主义，战时角色须批判审视。"},
                {"holder": "区隔说", "basis": "主张区分国家神道与民间神道，避免以偏概全。"}]}
        ],
        "data_points": [
            {"claim": "神道教神话材料主要见于《古事记》《日本书纪》，实践以神社祭祀为中心。", "basis_source": "pri-kojiki"},
            {"claim": "神道与佛教历史上长期共存、相互影响（神佛习合）。", "basis_source": "enc-brit-shinto"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "洪水叙事的传播关系（近东→希腊/希伯来 vs 独立发生）", "views": [
                {"holder": "影响/传播说", "basis": "认为近东洪水叙事向周边传播、被改写吸收。"},
                {"holder": "独立发生说", "basis": "认为多地洪水传说可就地产生，传播关系难确证。"}]},
            {"issue": "《阿特拉哈西斯》与《吉尔伽美什》洪水段落的先后", "views": [
                {"holder": "阿特拉哈西斯较早说", "basis": "认为吉尔伽美什洪水段承袭前者。"},
                {"holder": "共同源头说", "basis": "认为二者共享更早传统，先后难定。"}]}
        ],
        "data_points": [
            {"claim": "《阿特拉哈西斯》与《吉尔伽美什》洪水段落存在情节对应，二者关系为研究议题。", "basis_source": "pri-atrahasis"},
            {"claim": "洪水母题见于多个传统的一手文献，起因与神意解释各异。", "basis_source": "pri-gilgamesh"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "冥界观念的跨文化比较是否成立", "views": [
                {"holder": "结构母题说", "basis": "认为亡者居所、审判、回归等构成可比的结构母题。"},
                {"holder": "差异优先说", "basis": "认为各传统冥界在方位、审判与回归可能性上差异显著，不宜直接等同。"}]},
            {"issue": "冥界旅行的仪式性解读", "views": [
                {"holder": "通过仪式说", "basis": "以“通过仪式”解释由生到死再到重生的过渡结构。"},
                {"holder": "文本语境说", "basis": "强调须在具体文本与崇拜语境中理解，避免过度普适化。"}]}
        ],
        "data_points": [
            {"claim": "古埃及《亡灵书》详述死后旅程与审判，文本随时期演变。", "basis_source": "pri-book-dead"},
            {"claim": "希腊冥界由哈迪斯掌管，亡者与英雄的冥界旅行见于史诗与悲剧。", "basis_source": "pri-theogony"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "Campbell 单一神话模型的普适性", "views": [
                {"holder": "普遍结构说", "basis": "认为英雄旅程是跨文化的普遍叙事结构，具心理与仪式意义。"},
                {"holder": "批评者", "basis": "认为该模型过度概括、选择性取材，可证伪性不足，不适用于所有文本。"}]},
            {"issue": "英雄旅程模型的性别与跨文化适用性", "views": [
                {"holder": "可扩展说", "basis": "认为模型可扩展至女性英雄与非西方叙事。"},
                {"holder": "修正说", "basis": "认为模型以男性英雄为原型，用于其他传统需大幅修正。"}]}
        ],
        "data_points": [
            {"claim": "《千面英雄》1949年提出英雄旅程模型，影响广泛。", "basis_source": "aca-hero-faces"},
            {"claim": "《奥德赛》常被作为英雄旅程案例，但其细节与模型阶段并不逐一对应。", "basis_source": "pri-odyssey"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "太阳崇拜是否构成最早宗教形式之一", "views": [
                {"holder": "太阳中心论（早期自然神话学）", "basis": "曾主张太阳神话是宗教的早期核心（如 Müller 一系）。"},
                {"holder": "现代批评", "basis": "否定单一太阳起源，认为太阳神崇拜与其他自然崇拜并存，起源多元。"}]},
            {"issue": "太阳神的性别与职能跨文化可比性", "views": [
                {"holder": "母题可比说", "basis": "认为太阳运行与宇宙秩序的关联在多地可比。"},
                {"holder": "差异优先说", "basis": "认为各传统太阳神在性别、职能与谱系上差异显著，不宜等同。"}]}
        ],
        "data_points": [
            {"claim": "古埃及金字塔文与《亡灵书》以太阳神拉为核心；吠陀颂歌礼赞苏利耶。", "basis_source": "pri-rigveda"},
            {"claim": "金字塔文是现存的埃及太阳神—王权叙事早期文本之一。", "basis_source": "pri-pyramid-texts"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "是否存在统一的“大母神”原型", "views": [
                {"holder": "大母神论（Frazer/Gimbutas 一系）", "basis": "认为丰产女神可归为普遍的“大母神”原型。"},
                {"holder": "批评者（如 Doniger）", "basis": "反对把多样女神简化为单一原型，强调各自的文本与地域语境。"}]},
            {"issue": "史前女神像的解读", "views": [
                {"holder": "丰产女神说", "basis": "把女性神像多解读为丰产与生育象征。"},
                {"holder": "谨慎说", "basis": "认为含义多样、证据有限，不能一概视为“母神”。"}]}
        ],
        "data_points": [
            {"claim": "近东与地中海有多位丰产/爱情女神，职能各异。", "basis_source": "aca-patterns-religion"},
            {"claim": "Frazer《金枝》把丰产女神与植物、季节仪式相联系，属早期学派观点。", "basis_source": "aca-golden-bough"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "龙/巨蛇母题的跨文化比较", "views": [
                {"holder": "混沌制服母题说", "basis": "认为英雄制服巨蛇象征秩序战胜混沌，多地可比。"},
                {"holder": "差异优先说", "basis": "认为欧洲恶龙、中国水龙、中美洲羽蛇等文化语境不同，形象职能差异大。"}]},
            {"issue": "中国龙与欧洲龙是否同源", "views": [
                {"holder": "独立发展说", "basis": "认为两地龙形象各自独立形成，文化内涵不同。"},
                {"holder": "交流影响说", "basis": "认为可能存在间接交流，但缺乏确证，学界多倾向独立。"}]}
        ],
        "data_points": [
            {"claim": "欧洲恶龙、中国水龙、中美洲羽蛇在形象与职能上差异显著。", "basis_source": "enc-wiki-dragon"},
            {"claim": "Eliade 把巨蛇/龙与混沌及宇宙秩序的确立相联系。", "basis_source": "aca-eternal-return"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "世界树是否为印欧共有母题", "views": [
                {"holder": "印欧比较说", "basis": "认为宇宙轴/世界树是印欧共有母题（Dumézil/Puhvel 一系）。"},
                {"holder": "独立母题说", "basis": "认为宇宙轴意象广泛见于非印欧传统，属更普遍的独立母题。"}]},
            {"issue": "尤克特拉希尔材料的年代与基督教影响", "views": [
                {"holder": "古层说", "basis": "认为其宇宙树观念源自异教传统。"},
                {"holder": "文本语境说", "basis": "认为现存描述出自基督教时代抄本，须分辨记录语境。"}]}
        ],
        "data_points": [
            {"claim": "北欧尤克特拉希尔联结诸界，见《诗体埃达》《散文埃达》。", "basis_source": "pri-poetic-eddas"},
            {"claim": "宇宙轴也表现为柱、山、梯，功能相近而形态不同。", "basis_source": "enc-wiki-world-tree"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "末世是循环还是线性", "views": [
                {"holder": "循环说", "basis": "以宇宙周期、毁灭—重生解释末世（如 Eliade 的永恒回归框架）。"},
                {"holder": "线性终末说", "basis": "亚伯拉罕诸教的末世论为一次性审判与救赎，属线性终末。"}]},
            {"issue": "诸神黄昏是否受基督教末世观影响", "views": [
                {"holder": "影响说", "basis": "认为末世—重生结构与基督教启示文学可比，且成于基督教时代。"},
                {"holder": "独立说", "basis": "认为宇宙周期观源于异教传统，基督教影响有限难确证。"}]}
        ],
        "data_points": [
            {"claim": "北欧诸神黄昏叙述诸神败亡与世界更新，见《诗体埃达》。", "basis_source": "pri-poetic-eddas"},
            {"claim": "亚伯拉罕诸教末世论涉及审判与救赎，与宇宙周期型不同。", "basis_source": "aca-eternal-return"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "诡计者是否是可跨文化统一的原型", "views": [
                {"holder": "原型说（Jung/Campbell 一系）", "basis": "认为诡计者是普遍的心理原型，见于多文化。"},
                {"holder": "批评者", "basis": "认为各地诡计者语境与功能不同，过度普适化会抹平差异。"}]},
            {"issue": "诡计者是文化英雄还是破坏者", "views": [
                {"holder": "两面说", "basis": "诡计者常兼具助益与破坏两面。"},
                {"holder": "反派说", "basis": "在部分叙事中被视为单一反派或越界者。"}]}
        ],
        "data_points": [
            {"claim": "北欧洛基兼具诡计与变形，见《诗体埃达》《散文埃达》。", "basis_source": "pri-prose-eddas"},
            {"claim": "Lévi-Strauss 把诡计者视为神话思维的中介角色。", "basis_source": "aca-structural-anthro"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "宙斯形象是否主要源自印欧天父神", "views": [
                {"holder": "印欧说", "basis": "Dumézil 以三功能把宙斯归为主权/天父功能，与印欧天父神对应。"},
                {"holder": "多元来源说", "basis": "强调近东与地方传统的影响，主张宙斯形象为多元融合，非单一印欧来源。"}]},
            {"issue": "荷马与赫西俄德笔下宙斯的差异", "views": [
                {"holder": "谱系优先说", "basis": "《神谱》以神权更替与谱系塑造宙斯。"},
                {"holder": "秩序协商说", "basis": "荷马史诗把宙斯视为需与诸神协商的既成秩序之主。"}]}
        ],
        "data_points": [
            {"claim": "《神谱》叙述宙斯击败克洛诺斯确立奥林匹斯秩序。", "basis_source": "pri-theogony"},
            {"claim": "荷马史诗中宙斯权威需与其他神祇协商。", "basis_source": "pri-iliad"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "奥丁形象的历史层次（智慧/战争/亡灵复合）", "views": [
                {"holder": "复合古层说", "basis": "认为其智慧、战争与亡灵职能有古老根源。"},
                {"holder": "文本整合说", "basis": "认为现存形象经中世纪（尤其斯诺里）系统化与基督教时代改写。"}]},
            {"issue": "Dumézil 三功能中奥丁的位置", "views": [
                {"holder": "主权功能说", "basis": "把奥丁归为主权功能（与托尔战争、弗雷丰产对应）。"},
                {"holder": "批评者", "basis": "认为三功能划分对北欧材料有简化与套用之嫌。"}]}
        ],
        "data_points": [
            {"claim": "奥丁主要见于《诗体埃达》《散文埃达》，经中世纪记录。", "basis_source": "pri-poetic-eddas"},
            {"claim": "斯诺里在《散文埃达》把诸神作历史化解释。", "basis_source": "pri-prose-eddas"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "拉与阿蒙的结合及太阳神神学中心的转移", "views": [
                {"holder": "神学融合说", "basis": "新王国时期拉与阿蒙结合为阿蒙—拉，反映底比斯神学中心的抬升。"},
                {"holder": "地方传统并存说", "basis": "认为各中心太阳神传统长期并存，融合是政治—神学整合的一面。"}]},
            {"issue": "阿肯那顿阿顿崇拜与拉传统的关系", "views": [
                {"holder": "革命说", "basis": "视为对传统阿蒙—拉祭司体系的激进改革。"},
                {"holder": "延续说", "basis": "认为阿顿崇拜仍与太阳神传统有连续性，改革性质学界有争论。"}]}
        ],
        "data_points": [
            {"claim": "拉在金字塔文、亡灵书中居核心，与王权相联。", "basis_source": "pri-pyramid-texts"},
            {"claim": "新王国时期拉与阿蒙结合为阿蒙—拉。", "basis_source": "pri-book-dead"}
        ],
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
        "level": "L3",
        "controversies": [
            {"issue": "盘古神话的最早出处与年代", "views": [
                {"holder": "晚出说", "basis": "系统记载最早见于三国徐整《三五历纪》的辑佚引文（原书已佚），属较晚出。"},
                {"holder": "更早口传说", "basis": "推测有更早口传根源，但缺乏确证文献，待考。"}]},
            {"issue": "盘古化生与印度原人/宇宙卵母题的关系", "views": [
                {"holder": "比较关联说", "basis": "有比较学者提出与印度原人（Purusha）/宇宙卵母题的可能关联。"},
                {"holder": "独立说", "basis": "认为中国化生创世可独立产生，关联缺乏直接证据，学界有争论。"}]}
        ],
        "data_points": [
            {"claim": "盘古神话系统记载最早见于三国文献的辑佚引文。", "basis_source": "aca-short-history-myth"},
            {"claim": "盘古以身躯化生天地的叙事多见于较晚文献。", "basis_source": "enc-wiki-mythology"}
        ],
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
    },
    "fig-nuwa": {
        "level": "L3",
        "controversies": [
            {"issue": "女娲神话的早期形态与造人/补天母题年代", "views": [
                {"holder": "散见早期说", "basis": "《楚辞·天问》等已提及女娲，保留早期线索。"},
                {"holder": "系统晚出说", "basis": "造人、补天的系统叙述多见于较晚文献，其形成年代待考。"}]},
            {"issue": "女娲与伏羲的关系", "views": [
                {"holder": "兄妹/配偶说", "basis": "后世图像与传说多以女娲、伏羲为对偶的始祖。"},
                {"holder": "并列始祖说", "basis": "文献中二者常并称人文始祖，具体关联形态因时代与文本而异。"}]}
        ],
        "data_points": [
            {"claim": "女娲传说散见《楚辞》《淮南子》等，系统叙述多见于较晚文献。", "basis_source": "pri-chu-ci"},
            {"claim": "女娲与伏羲常并称人文始祖，关联形态不一。", "basis_source": "aca-short-history-myth"}
        ],
        "source_text": "女娲是中国神话中的造人与补天女神，材料散见于《楚辞》《淮南子》等典籍（其中《淮南子》未录入来源库）。相关传说的系统叙述多见于较晚文献，早期形态与辑佚性质为学界讨论议题，本站如实标注待核实。",
        "versions": [
            "《楚辞·天问》以疑问形式提及女娲，保留神话线索但未展开完整情节。",
            "较晚文献叙述女娲造人与补天的故事，细节在不同版本间有差异，反映神话的流传演变。",
            "女娲与伏羲常被并称为人文始祖，二者的关联在文献与图像材料中形态不一。"
        ],
        "interpretations": [
            {"holder": "袁珂", "school": "中国神话学（神话整理与研究）", "view": "通过辑录散见文献整理中国神话，指出女娲神话的造人与补天母题；其著作未录入 sources.json。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "可从宇宙修复与母神母题作现象学层面的参照，不直接等同于对中国材料的专门结论。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "为分析造人神话中的对立与中介提供方法论参照，属学派一般立场。"}
        ],
        "comparisons": [
            {"tradition": "希腊神话", "basis_source": "aca-golden-bough", "note": "以 Frazer《金枝》为早期学派参照，记录造人母题的一般比较，其结论已被现代学界修订，不构成同源断言。"},
            {"tradition": "美索不达米亚神话", "basis_source": "aca-short-history-myth", "note": "以通论性神话著作作造人母题的一般参照，具体文本关联待专门文献核对。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>女娲神话母题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>女娲神话母题（造人·补天）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>女娲</text><line x1='380' y1='138' x2='380' y2='178' stroke='currentColor' opacity='0.5'/><line x1='200' y1='178' x2='560' y2='178' stroke='currentColor' opacity='0.5'/><line x1='200' y1='178' x2='200' y2='216' stroke='currentColor' opacity='0.5'/><line x1='560' y1='178' x2='560' y2='216' stroke='currentColor' opacity='0.5'/><rect x='110' y='216' width='180' height='56' fill='var(--svg-node)' stroke='currentColor'/><text x='200' y='240' text-anchor='middle' fill='var(--svg-text)' font-size='13'>造人</text><text x='200' y='260' text-anchor='middle' fill='var(--svg-text)' font-size='12'>人类起源</text><rect x='470' y='216' width='180' height='56' fill='var(--svg-node)' stroke='currentColor'/><text x='560' y='240' text-anchor='middle' fill='var(--svg-text)' font-size='13'>补天</text><text x='560' y='260' text-anchor='middle' fill='var(--svg-text)' font-size='12'>宇宙修复</text><rect x='230' y='316' width='300' height='44' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='344' text-anchor='middle' fill='var(--svg-text)' font-size='13'>系统叙述多见于较晚文献，出处待核实</text></svg>",
        "pending_notes": "1) 女娲材料的早期形态与辑佚性质待核实；2) 袁珂著作未录入 sources.json，已声明；《淮南子》未录入来源库，正文已注明；3) 跨传统比较为学派/框架性参照，不推断同源。",
        "needs_verification": True
    },
    "fig-buddha": {
        "level": "L3",
        "controversies": [
            {"issue": "佛陀生平中史实与传说的区分", "views": [
                {"holder": "历史研究", "basis": "主张从早期经典提取核心史实，把神通、成道细节等视为后世传说层。"},
                {"holder": "信仰叙述", "basis": "传统将生平视为具宗教意义的整体叙事，不宜简单以“史实/传说”二分。"}]},
            {"issue": "大乘经典是否为历史佛陀亲说", "views": [
                {"holder": "大乘传统立场", "basis": "视大乘经为佛陀教说（依法身/传承理解）。"},
                {"holder": "现代学界主流", "basis": "多认为大乘经典成于佛灭后数世纪，非历史佛陀亲说。"}]}
        ],
        "data_points": [
            {"claim": "佛陀（乔达摩·悉达多）教导见于早期经典结集，《法句经》为流传较广的早期经典。", "basis_source": "pri-dhammapada"},
            {"claim": "关于佛陀生平的记载掺杂后世传说，须区分历史与叙事。", "basis_source": "enc-brit-buddhism"}
        ],
        "source_text": "释迦牟尼（乔达摩·悉达多）是佛教创始人，其教导见于早期经典结集，《法句经》为流传较广的早期经典之一。关于其生平的记载掺杂后世传说，历史与叙事层面需区分；本站采用学术描述性立场，不评判信仰真伪。",
        "versions": [
            "早期经典侧重其教导（如四圣谛、八正道），生平叙述较为简略。",
            "后世传记与部派传统对出生、出家、成道等节点有更详细的叙事，不同传统在细节上存在差异。",
            "大乘传统对佛陀的理解与早期部派在佛身、菩萨道等教义上侧重不同。"
        ],
        "interpretations": [
            {"holder": "Richard Gombrich", "school": "早期佛教研究（语文学与历史方法）", "view": "以巴利文经典与历史方法研究佛陀教导，强调在文本语境中理解，反对过度现代化投射；其著作未录入 sources.json。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "可从圣者、宇宙轴与修行实践的比较框架理解佛陀形象，属现象学参照。"},
            {"holder": "Stephen Prothero", "school": "比较宗教学", "view": "在宗教比较中强调佛教目标的独特性，反对把不同宗教简化为同一本质，属通俗学术著作观点。"}
        ],
        "comparisons": [
            {"tradition": "耆那教", "basis_source": "aca-god-is-not-one", "note": "Prothero 的宗教比较含印度宗教传统背景，此处作一般参照（通俗学术著作，未在线核验）；两教教义差异待专门文献核对，不主张同源。"},
            {"tradition": "基督教", "basis_source": "aca-god-is-not-one", "note": "Prothero 比较各宗教独特目标的框架仅作通俗学术参照，不主张教义同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>释迦牟尼生平与教导示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>释迦牟尼：生平节点与教导（示意）</text><rect x='60' y='180' width='150' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='135' y='204' text-anchor='middle' fill='var(--svg-text)' font-size='13'>出生</text><text x='135' y='222' text-anchor='middle' fill='var(--svg-text)' font-size='12'>迦毗罗卫</text><line x1='210' y1='207' x2='245' y2='207' stroke='currentColor' opacity='0.5'/><rect x='245' y='180' width='150' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='320' y='204' text-anchor='middle' fill='var(--svg-text)' font-size='13'>出家</text><text x='320' y='222' text-anchor='middle' fill='var(--svg-text)' font-size='12'>舍俗修行</text><line x1='395' y1='207' x2='430' y2='207' stroke='currentColor' opacity='0.5'/><rect x='430' y='180' width='150' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='505' y='204' text-anchor='middle' fill='var(--svg-text)' font-size='13'>成道</text><text x='505' y='222' text-anchor='middle' fill='var(--svg-text)' font-size='12'>菩提树下</text><rect x='230' y='286' width='300' height='50' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='310' text-anchor='middle' fill='var(--svg-text)' font-size='13'>教导：四圣谛·八正道（法句经）</text><text x='380' y='356' text-anchor='middle' fill='var(--svg-text)' font-size='12'>生平记载含后世传说，历史与叙事需区分</text></svg>",
        "pending_notes": "1) 生平记载掺杂传说，正文已区分历史与叙事；2) Gombrich 著作未录入 sources.json，已声明；3) 教义描述采用学术立场，不替信仰表态。",
        "needs_verification": True
    },
    "fig-jesus": {
        "level": "L3",
        "controversies": [
            {"issue": "耶稣生平的历史研究（福音书年代、作者、神迹）", "views": [
                {"holder": "历史耶稣研究", "basis": "以文本批评区分历史层与信仰叙述，认为福音书成于公元1世纪后期、作者多不可考。"},
                {"holder": "信仰叙述", "basis": "传统以福音书为信仰见证，神迹与复活属信仰核心，非纯历史记录。"}]},
            {"issue": "耶稣的神人二性", "views": [
                {"holder": "迦克墩定义立场", "basis": "主张基督一位格、神人二性不分不离。"},
                {"holder": "其他古代传统", "basis": "如聂斯脱利、一性论等对神人关系有不同表述，反映教义史分歧。"}]}
        ],
        "data_points": [
            {"claim": "耶稣事迹主要见于新约四福音书，另有早期教父与教外文献提及。", "basis_source": "pri-bible-kjv"},
            {"claim": "早期诺斯替文献为理解早期基督教多样性提供材料。", "basis_source": "aca-gnostic-gospels"}
        ],
        "source_text": "耶稣是基督教信仰的中心人物，其事迹主要见于新约四福音书，另有早期教父与教外文献提及。关于其生平的历史研究与信仰叙述层次不同，本站采用学术描述性立场，不评判信仰真伪。",
        "versions": [
            "四福音书对同一事件的表述各有侧重，文本批评研究关注其成书背景与相互关系。",
            "早期诺斯替文献的发现为理解早期基督教的多样性提供了材料，其与正典的关系为学界议题。",
            "不同宗派对耶稣的神人关系与救赎教义理解各异，是历史形成的结果。"
        ],
        "interpretations": [
            {"holder": "Elaine Pagels", "school": "早期基督教与诺斯替研究", "view": "通过诺斯替福音与正典对照指出早期基督教内部的多样性，属学术研究，其具体结论学界有讨论。"},
            {"holder": "Bart D. Ehrman", "school": "新约文本批评", "view": "以文本批评方法研究新约的传抄与成书，强调历史研究的局限，其著作未录入 sources.json。"},
            {"holder": "Stephen Prothero", "school": "比较宗教学", "view": "在宗教比较中强调基督教目标的独特性，反对简化，属通俗学术著作观点。"}
        ],
        "comparisons": [
            {"tradition": "犹太教", "basis_source": "aca-myth-legend-custom", "note": "Gaster 以民俗与神话学方法研究旧约材料，此处仅作历史背景的一般参照，不推断信仰关系。"},
            {"tradition": "伊斯兰教", "basis_source": "aca-god-is-not-one", "note": "Prothero 的亚伯拉罕诸教比较为通俗学术框架，不主张教义同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>耶稣研究材料层次示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>耶稣研究材料层次（描述性示意）</text><rect x='280' y='90' width='200' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='120' text-anchor='middle' fill='var(--svg-text)' font-size='14'>耶稣</text><line x1='380' y1='136' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='160' y1='174' x2='600' y2='174' stroke='currentColor' opacity='0.5'/><line x1='160' y1='174' x2='160' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='600' y1='174' x2='600' y2='212' stroke='currentColor' opacity='0.5'/><rect x='70' y='212' width='180' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='160' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>四福音书</text><text x='160' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>正典文本</text><rect x='290' y='212' width='180' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>诺斯替文献</text><text x='380' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>早期多样性</text><rect x='510' y='212' width='180' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='600' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>教父与教外</text><text x='600' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>旁证材料</text><text x='380' y='322' text-anchor='middle' fill='var(--svg-text)' font-size='13'>历史研究与信仰叙述层次不同</text><text x='380' y='348' text-anchor='middle' fill='var(--svg-text)' font-size='12'>本站不作真伪评判</text></svg>",
        "pending_notes": "1) 新约成书与文本问题有学术争论，正文未列具体年份；2) Ehrman 著作未录入 sources.json，已声明；3) 宗派分歧采用描述性立场，不替信仰表态。",
        "needs_verification": True
    },
    "fig-muhammad": {
        "level": "L3",
        "controversies": [
            {"issue": "穆罕默德生平的史料层次（古兰经/圣训/早期传记）", "views": [
                {"holder": "传统叙述", "basis": "以古兰经、圣训与早期传记（西拉）综合呈现生平。"},
                {"holder": "现代历史研究", "basis": "强调各史料年代与可靠性不一，须分层审慎使用，部分细节存疑。"}]},
            {"issue": "圣训的真实性与甄别", "views": [
                {"holder": "传统圣训学", "basis": "以传述链与传述者诚信甄别真伪。"},
                {"holder": "现代历史批判", "basis": "对部分圣训的传述链与年代存疑，主张结合历史语境审慎使用。"}]}
        ],
        "data_points": [
            {"claim": "《古兰经》被视为穆罕默德传达的启示；圣训保存其言行传统。", "basis_source": "pri-quran"},
            {"claim": "早期传记（西拉）与历史记载对生平细节有不同叙述。", "basis_source": "enc-brit-islam"}
        ],
        "source_text": "穆罕默德是伊斯兰教的先知，《古兰经》被视为其传达的启示，圣训保存了其言行传统。关于其生平的历史研究与信仰叙述层次不同，本站采用学术描述性立场，不评判信仰真伪。",
        "versions": [
            "《古兰经》作为核心经典，其成文与汇编过程为学界研究议题。",
            "圣训的收集与甄别形成专门学科，不同学派对圣训的采信标准存在差异。",
            "早期传记（西拉）与历史记载对生平细节有不同叙述，需区分史料层次。"
        ],
        "interpretations": [
            {"holder": "Stephen Prothero", "school": "比较宗教学", "view": "在亚伯拉罕诸教比较中强调伊斯兰教目标的独特性，反对简化，属通俗学术著作观点。"},
            {"holder": "Max Weber", "school": "宗教社会学", "view": "从宗教伦理与社会结构关联角度分析宗教，为理解宗教与社会关系提供框架，不涉及信仰真伪。"},
            {"holder": "Émile Durkheim", "school": "宗教社会学", "view": "把宗教视为社会事实与集体表征，强调仪式与共同体功能，为比较研究提供方法论。"}
        ],
        "comparisons": [
            {"tradition": "犹太教", "basis_source": "aca-god-is-not-one", "note": "Prothero 的亚伯拉罕诸教比较为通俗学术框架，不主张先知传统同源。"},
            {"tradition": "基督教", "basis_source": "enc-brit-islam", "note": "以权威百科条目作两教关系的一般参照（该来源未在线核验）；具体教义差异待专门文献核对。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>穆罕默德研究材料示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>穆罕默德研究材料（描述性示意）</text><rect x='280' y='92' width='200' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>穆罕默德</text><line x1='380' y1='138' x2='380' y2='176' stroke='currentColor' opacity='0.5'/><line x1='170' y1='176' x2='590' y2='176' stroke='currentColor' opacity='0.5'/><line x1='170' y1='176' x2='170' y2='214' stroke='currentColor' opacity='0.5'/><line x1='380' y1='176' x2='380' y2='214' stroke='currentColor' opacity='0.5'/><line x1='590' y1='176' x2='590' y2='214' stroke='currentColor' opacity='0.5'/><rect x='80' y='214' width='180' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>古兰经</text><text x='170' y='258' text-anchor='middle' fill='var(--svg-text)' font-size='12'>核心经典</text><rect x='290' y='214' width='180' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>圣训</text><text x='380' y='258' text-anchor='middle' fill='var(--svg-text)' font-size='12'>言行传统</text><rect x='500' y='214' width='180' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>早期传记</text><text x='590' y='258' text-anchor='middle' fill='var(--svg-text)' font-size='12'>西拉</text><text x='380' y='322' text-anchor='middle' fill='var(--svg-text)' font-size='13'>史料层次需区分，本站不作真伪评判</text></svg>",
        "pending_notes": "1) 经典汇编与圣训甄别为学术议题，正文未列具体年份；2) 三位学者观点为概括，细节待核对；3) 全部采用描述性立场，不替信仰表态。",
        "needs_verification": True
    },
    "fig-moses": {
        "level": "L3",
        "controversies": [
            {"issue": "出埃及事件的史实性", "views": [
                {"holder": "缺乏确证说", "basis": "考古与埃及文献缺乏与出埃及叙事直接对应的确证，史实性有争议。"},
                {"holder": "传统叙述", "basis": "传统视出埃及为核心救赎史事件，具有信仰与身份意义。"}]},
            {"issue": "摩西五经的作者", "views": [
                {"holder": "传统说", "basis": "按传统归于摩西。"},
                {"holder": "底本假说", "basis": "文本批评以 JEDP 等底本解释五经为长期编纂，细节仍有争论。"}]}
        ],
        "data_points": [
            {"claim": "摩西的核心叙述见于《圣经》五经。", "basis_source": "pri-bible-kjv"},
            {"claim": "考古与历史研究对出埃及事件的史实性有讨论。", "basis_source": "aca-myth-legend-custom"}
        ],
        "source_text": "摩西是犹太教传统中的律法颁布者与出埃及领导者，其核心叙述见于《圣经》五经，另有教外文献与考古研究提供旁证。历史研究与信仰叙述层次不同，本站采用学术描述性立场，不评判信仰真伪。",
        "versions": [
            "五经对出埃及与律法颁布的叙述是犹太教与基督教共同的重要文本传统。",
            "文本批评研究关注五经的成书层次与来源，学界对其形成过程有不同模型。",
            "考古与历史研究对出埃及事件的史实性有讨论，正文不下定论。"
        ],
        "interpretations": [
            {"holder": "Theodor H. Gaster", "school": "圣经民俗与比较宗教学", "view": "以民俗与神话学方法分析旧约材料，指出其与近东传统的关联，属学术分析，不作信仰判断。"},
            {"holder": "Henri Frankfort", "school": "古代近东思想研究", "view": "以神话意象分析近东与埃及思想，主张不以现代抽象标准误读，属专门研究。"},
            {"holder": "Stephen Prothero", "school": "比较宗教学", "view": "在亚伯拉罕诸教比较中强调各传统独特目标，属通俗学术著作观点。"}
        ],
        "comparisons": [
            {"tradition": "古埃及宗教", "basis_source": "aca-before-philosophy", "note": "Frankfort 的近东思想研究作一般背景参照，不推断出埃及叙事与埃及文本的直接对应。"},
            {"tradition": "基督教", "basis_source": "aca-myth-legend-custom", "note": "Gaster 的旧约研究作文本传统参照，具体神学差异待专门文献核对。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>摩西传统材料示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>摩西传统材料（描述性示意）</text><rect x='280' y='92' width='200' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>摩西</text><line x1='380' y1='138' x2='380' y2='176' stroke='currentColor' opacity='0.5'/><line x1='170' y1='176' x2='590' y2='176' stroke='currentColor' opacity='0.5'/><line x1='170' y1='176' x2='170' y2='214' stroke='currentColor' opacity='0.5'/><line x1='380' y1='176' x2='380' y2='214' stroke='currentColor' opacity='0.5'/><line x1='590' y1='176' x2='590' y2='214' stroke='currentColor' opacity='0.5'/><rect x='80' y='214' width='180' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>五经</text><text x='170' y='258' text-anchor='middle' fill='var(--svg-text)' font-size='12'>律法·出埃及</text><rect x='290' y='214' width='180' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>文本批评</text><text x='380' y='258' text-anchor='middle' fill='var(--svg-text)' font-size='12'>成书层次</text><rect x='500' y='214' width='180' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>考古旁证</text><text x='590' y='258' text-anchor='middle' fill='var(--svg-text)' font-size='12'>史实性讨论</text><text x='380' y='322' text-anchor='middle' fill='var(--svg-text)' font-size='13'>历史研究与信仰叙述层次不同</text></svg>",
        "pending_notes": "1) 五经成书与出埃及史实性有学术争论，正文未下结论；2) 三位学者观点为概括，细节待核对；3) 描述性立场，不替信仰表态。",
        "needs_verification": True
    },
    "fig-vishnu": {
        "level": "L3",
        "controversies": [
            {"issue": "毗湿奴化身谱系的历史形成", "views": [
                {"holder": "渐进形成说", "basis": "认为化身数目与谱系在往世书—史诗时期逐步扩充。"},
                {"holder": "传统说", "basis": "视化身谱系为既有教义，各化身有既定次序与职能。"}]},
            {"issue": "毗湿奴派与湿婆派的最高神格", "views": [
                {"holder": "毗湿奴派", "basis": "以毗湿奴为至高神。"},
                {"holder": "湿婆派", "basis": "以湿婆为至高神，两派并存，神学侧重不同。"}]}
        ],
        "data_points": [
            {"claim": "毗湿奴为三相神中的保护神，化身叙事见往世书与史诗。", "basis_source": "pri-vishnu-purana"},
            {"claim": "化身包括罗摩、黑天等，谱系因传统而异。", "basis_source": "pri-mahabharata"}
        ],
        "source_text": "毗湿奴是印度教三相神中的保护神，其形象见于往世书与两大史诗，并以化身叙事著称。不同教派与地区传统对其职能神学理解各异，本站采用学术描述性立场，不评判信仰真伪。",
        "versions": [
            "往世书系统中毗湿奴与梵天、湿婆构成三相神，侧重保护与维持。",
            "化身叙事把毗湿奴与罗摩、黑天（Krishna）等形象关联，不同传统的化身谱系与重点不一。",
            "毗湿奴派内部在神学与实践上多样，与湿婆派等传统形成不同的侧重。"
        ],
        "interpretations": [
            {"holder": "Wendy Doniger", "school": "芝加哥学派（印度宗教与文本研究）", "view": "强调印度神祇的多义性与阐释史，警惕把多样传统简化为单一体系，其解读在学界有讨论。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "可从宇宙维持与化身母题作现象学层面的参照，属框架性对照。"},
            {"holder": "Georges Dumézil", "school": "印欧比较神话学", "view": "以三功能假说作印欧框架下的比较参照，属学派模型，学界对其适用性有讨论。"}
        ],
        "comparisons": [
            {"tradition": "希腊神话", "basis_source": "aca-comparative-myth", "note": "比较神话学在印欧框架内作功能层面的一般参照，不主张具体神祇同源。"},
            {"tradition": "佛教", "basis_source": "aca-patterns-religion", "note": "以 Eliade《比较宗教的模式》作印度宗教背景的框架性参照，具体教义关联待专门文献核对。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>毗湿奴神学结构示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>毗湿奴：三相神与化身（示意）</text><rect x='300' y='88' width='160' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='118' text-anchor='middle' fill='var(--svg-text)' font-size='14'>三相神</text><line x1='380' y1='134' x2='380' y2='170' stroke='currentColor' opacity='0.5'/><line x1='170' y1='170' x2='590' y2='170' stroke='currentColor' opacity='0.5'/><line x1='170' y1='170' x2='170' y2='208' stroke='currentColor' opacity='0.5'/><line x1='380' y1='170' x2='380' y2='208' stroke='currentColor' opacity='0.5'/><line x1='590' y1='170' x2='590' y2='208' stroke='currentColor' opacity='0.5'/><rect x='90' y='208' width='160' height='52' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='230' text-anchor='middle' fill='var(--svg-text)' font-size='13'>梵天</text><text x='170' y='248' text-anchor='middle' fill='var(--svg-text)' font-size='12'>创造</text><rect x='300' y='208' width='160' height='52' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='230' text-anchor='middle' fill='var(--svg-text)' font-size='13'>毗湿奴</text><text x='380' y='248' text-anchor='middle' fill='var(--svg-text)' font-size='12'>保护</text><rect x='510' y='208' width='160' height='52' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='230' text-anchor='middle' fill='var(--svg-text)' font-size='13'>湿婆</text><text x='590' y='248' text-anchor='middle' fill='var(--svg-text)' font-size='12'>毁灭再生</text><rect x='230' y='308' width='300' height='46' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='336' text-anchor='middle' fill='var(--svg-text)' font-size='13'>化身叙事：罗摩·黑天等</text></svg>",
        "pending_notes": "1) 化身谱系与教派差异大，正文不作单一化；2) Doniger、Dumézil 观点为学派立场，学界有争论；3) 比较为框架性参照，不主张同源。",
        "needs_verification": True
    },
    "fig-shiva": {
        "level": "L3",
        "controversies": [
            {"issue": "湿婆与吠陀鲁德罗的关系", "views": [
                {"holder": "继承说", "basis": "认为湿婆承袭吠陀风暴神鲁德罗的形象与职能。"},
                {"holder": "独立发展说", "basis": "认为湿婆神格有独立来源，与鲁德罗的关联为后世整合。"}]},
            {"issue": "湿婆形象的解读（苦行 vs 情欲）", "views": [
                {"holder": "张力说（如 Doniger）", "basis": "认为苦行与情欲的对立统一是理解湿婆神格的关键。"},
                {"holder": "单一化批评", "basis": "反对以单一主题概括其多面性，须结合具体文本与崇拜。"}]}
        ],
        "data_points": [
            {"claim": "湿婆为三相神中的毁灭与再生之神，见往世书、史诗与考古材料。", "basis_source": "enc-brit-hinduism"},
            {"claim": "早期风暴神鲁德罗与后世湿婆的关系为学界讨论议题。", "basis_source": "pri-rigveda"}
        ],
        "source_text": "湿婆是印度教三相神中的毁灭与再生之神，其形象见往来世书、史诗与考古材料，并以苦行、舞蹈与林伽崇拜等面向著称。不同教派与地区传统对其理解多样，本站采用学术描述性立场。",
        "versions": [
            "往世书系统中湿婆与梵天、毗湿奴构成三相神，兼具毁灭与再生职能。",
            "湿婆派内部有不同流派，对湿婆的绝对性与与其他神祇的关系理解不一。",
            "考古与图像材料中的湿婆形象（如舞王像）为研究其崇拜提供旁证，但解读需谨慎。"
        ],
        "interpretations": [
            {"holder": "Wendy Doniger", "school": "芝加哥学派（印度宗教与文本研究）", "view": "强调湿婆形象的多义性与阐释史，警惕单一化解读，其观点在学界有讨论。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "可从毁灭—再生与宇宙循环母题作现象学层面的参照，属框架性对照。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "为分析神祇的对立与中介关系提供方法论参照，属学派一般立场。"}
        ],
        "comparisons": [
            {"tradition": "印度神话（吠陀）", "basis_source": "pri-rigveda", "note": "以《梨俱吠陀》为依据，记录早期风暴神鲁德罗与后世湿婆关系的学术讨论，不主张简单等同。"},
            {"tradition": "希腊神话", "basis_source": "aca-comparative-myth", "note": "比较神话学作功能层面的一般参照，不主张具体神祇同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>湿婆形象面向示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>湿婆形象的主要面向（示意）</text><rect x='300' y='92' width='160' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>湿婆</text><line x1='380' y1='138' x2='380' y2='176' stroke='currentColor' opacity='0.5'/><line x1='150' y1='176' x2='610' y2='176' stroke='currentColor' opacity='0.5'/><line x1='150' y1='176' x2='150' y2='214' stroke='currentColor' opacity='0.5'/><line x1='380' y1='176' x2='380' y2='214' stroke='currentColor' opacity='0.5'/><line x1='610' y1='176' x2='610' y2='214' stroke='currentColor' opacity='0.5'/><rect x='70' y='214' width='160' height='56' fill='var(--svg-node)' stroke='currentColor'/><text x='150' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>苦行</text><text x='150' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>瑜伽·冥想</text><rect x='300' y='214' width='160' height='56' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>舞王</text><text x='380' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>宇宙之舞</text><rect x='530' y='214' width='160' height='56' fill='var(--svg-node)' stroke='currentColor'/><text x='610' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>林伽</text><text x='610' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>崇拜象征</text><text x='380' y='322' text-anchor='middle' fill='var(--svg-text)' font-size='13'>毁灭与再生并存，教派理解多样</text></svg>",
        "pending_notes": "1) 早期鲁德罗与湿婆关系为学术讨论，正文未下结论；2) Doniger、Lévi-Strauss 观点为学派立场；3) 描述性立场，不替信仰表态。",
        "needs_verification": True
    },
    "fig-indra": {
        "level": "L3",
        "controversies": [
            {"issue": "因陀罗与印欧风暴神的对应", "views": [
                {"holder": "印欧说", "basis": "Dumézil 以三功能把因陀罗归为战争功能，与北欧托尔等对应。"},
                {"holder": "批评者", "basis": "认为三功能模型对具体神祇的套用有简化与争论。"}]},
            {"issue": "因陀罗在史诗—往世书时期地位的下降", "views": [
                {"holder": "地位下降说", "basis": "认为三相神兴起后因陀罗地位相对下降，成为次位神。"},
                {"holder": "功能转化说", "basis": "认为其职能被重新安置，仍以其他形式在叙事中出现。"}]}
        ],
        "data_points": [
            {"claim": "因陀罗在《梨俱吠陀》居显要，以击败弗栗多著称。", "basis_source": "pri-rigveda"},
            {"claim": "后世其地位相对下降，三相神成为叙述中心。", "basis_source": "aca-gods-indo-europeans"}
        ],
        "source_text": "因陀罗是吠陀神话中的风暴与战争之神，在《梨俱吠陀》中居显要地位，后世文献中其地位有所变化。学界对其与印欧风暴神的比较有研究，本站只记录有文献依据的对照。",
        "versions": [
            "《梨俱吠陀》中因陀罗以击败弗栗多、释放河流等功绩著称，颂歌数量众多。",
            "史诗与往世书时期因陀罗的地位相对下降，三相神成为叙述中心。",
            "因陀罗在佛教与耆那教文献中亦有出现，形象与职能与吠陀传统不同。"
        ],
        "interpretations": [
            {"holder": "Georges Dumézil", "school": "印欧比较神话学", "view": "以三功能假说把因陀罗归为战争功能，与北欧托尔等对照，属学派模型，学界有讨论。"},
            {"holder": "Jaan Puhvel", "school": "印欧比较神话学", "view": "在印欧语系框架内比较风暴神，属学术对照，具体对应关系有讨论。"},
            {"holder": "Wendy Doniger", "school": "芝加哥学派（印度宗教与文本研究）", "view": "强调神话形象的多义性与阐释史，警惕单一化解读。"}
        ],
        "comparisons": [
            {"tradition": "北欧神话", "basis_source": "aca-gods-indo-europeans", "note": "Dumézil 的印欧比较把因陀罗与托尔作功能对照，属学派框架，不主张直接同源。"},
            {"tradition": "波斯传统", "basis_source": "aca-comparative-myth", "note": "比较神话学在印欧框架内并置印度与伊朗材料，属学术对照，学界对对应关系有讨论。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>因陀罗形象与文献示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>因陀罗：吠陀风暴神（示意）</text><rect x='300' y='92' width='160' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>因陀罗</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='150' y1='174' x2='610' y2='174' stroke='currentColor' opacity='0.5'/><line x1='150' y1='174' x2='150' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='610' y1='174' x2='610' y2='212' stroke='currentColor' opacity='0.5'/><rect x='70' y='212' width='160' height='56' fill='var(--svg-node)' stroke='currentColor'/><text x='150' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>风暴</text><text x='150' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>雷霆·降雨</text><rect x='300' y='212' width='160' height='56' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>战争</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>击败弗栗多</text><rect x='530' y='212' width='160' height='56' fill='var(--svg-node)' stroke='currentColor'/><text x='610' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>地位变化</text><text x='610' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>后世下降</text><text x='380' y='322' text-anchor='middle' fill='var(--svg-text)' font-size='13'>三功能模型为学派框架，不替读者下结论</text></svg>",
        "pending_notes": "1) 因陀罗地位变化为学界通行描述，具体年代待核；2) Dumézil 三功能模型有争论；3) 比较为学派框架，不主张同源。",
        "needs_verification": True
    },
    "myth-roman": {
        "level": "L2",
        "source_text": "罗马神话的材料包括奥维德《变形记》、维吉尔《埃涅阿斯纪》与李维《罗马史》等，罗马神祇常与希腊神祇对应，但本土传统与希腊影响的关系为学界讨论议题。本站只记录有文献依据的对照。",
        "versions": [
            "罗马早期宗教以功能神祇与仪式为主，后期大量吸收希腊神话的叙事与形象。",
            "《埃涅阿斯纪》把特洛伊传说与罗马建城叙事联结，是罗马神话文学化的代表。",
            "《变形记》汇集大量神话故事，其中不少源自希腊传统但经罗马诗人重述。"
        ],
        "interpretations": [
            {"holder": "Walter Burkert", "school": "宗教史学派", "view": "强调希腊宗教的祭祀实践核心与对罗马的影响，将罗马神话置于历史宗教史语境，属学术研究。"},
            {"holder": "Jean-Pierre Vernant", "school": "巴黎学派（古希腊神话与思想）", "view": "为神话与城邦秩序的关系研究提供框架，属学派参照，具体罗马材料结论待核。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "可从建城神话与宇宙秩序母题作现象学层面的参照，属框架性对照。"}
        ],
        "comparisons": [
            {"tradition": "希腊神话", "basis_source": "aca-greek-religion", "note": "Burkert 的希腊宗教研究为罗马—希腊神话关系的有文献依据参照，不主张简单复制。"},
            {"tradition": "伊特鲁里亚神话", "basis_source": "enc-wiki-list-myth", "note": "以权威百科条目作意大利本土背景的一般参照（该来源未在线核验，见待核实）；具体影响待专门文献核对。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>罗马神话来源示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>罗马神话的主要文献来源</text><rect x='280' y='90' width='200' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='120' text-anchor='middle' fill='var(--svg-text)' font-size='14'>罗马神话</text><line x1='380' y1='136' x2='380' y2='172' stroke='currentColor' opacity='0.5'/><line x1='150' y1='172' x2='610' y2='172' stroke='currentColor' opacity='0.5'/><line x1='150' y1='172' x2='150' y2='210' stroke='currentColor' opacity='0.5'/><line x1='380' y1='172' x2='380' y2='210' stroke='currentColor' opacity='0.5'/><line x1='610' y1='172' x2='610' y2='210' stroke='currentColor' opacity='0.5'/><rect x='70' y='210' width='160' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='150' y='234' text-anchor='middle' fill='var(--svg-text)' font-size='13'>变形记</text><text x='150' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>奥维德</text><rect x='300' y='210' width='160' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='234' text-anchor='middle' fill='var(--svg-text)' font-size='13'>埃涅阿斯纪</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>维吉尔</text><rect x='530' y='210' width='160' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='610' y='234' text-anchor='middle' fill='var(--svg-text)' font-size='13'>罗马史</text><text x='610' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>李维</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>本土传统与希腊影响的关系为学术议题</text></svg>",
        "pending_notes": "1) 罗马与希腊神话的关系学界有讨论，正文未简单等同；2) Vernant、Burkert 具体论点为概括，细节待核；3) 伊特鲁里亚比较为弱参照，待补专门文献。",
        "needs_verification": True
    },
    "rel-jainism": {
        "level": "L2",
        "source_text": "耆那教是起源于古印度的宗教传统，以非暴力（ahimsa）与苦行实践著称，经典结集与教义发展有自身历史。本站采用学术描述性立场，不评判信仰真伪。",
        "versions": [
            "耆那教传统对第23、24位祖师的记述构成其历史叙事，不同教派在经典与戒律理解上有差异。",
            "白衣派与天衣派在戒律与实践上各有侧重，是历史形成的分歧。",
            "非暴力与不执著等教义在不同时期被重新阐释，与社会语境相关。"
        ],
        "interpretations": [
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "可从苦行与解脱母题作现象学层面的参照，属框架性对照，不构成专门结论。"},
            {"holder": "Wendy Doniger", "school": "芝加哥学派（印度宗教与文本研究）", "view": "Doniger 强调印度宗教传统的多义性，提醒耆那教的非暴力与苦行应在自身教义脉络中理解，不宜化约为印度教或佛教的变体。"},
            {"holder": "Stephen Prothero", "school": "比较宗教学", "view": "在其宗教比较框架中，耆那教的非暴力与苦行被作为独特的修行目标对待，不宜化约为其他印度宗教的分支；属通俗学术著作观点。"}
        ],
        "comparisons": [
            {"tradition": "印度教", "basis_source": "enc-brit-hinduism", "note": "以权威百科条目作印度宗教背景的一般参照（该来源未在线核验，见待核实）；具体教义差异待专门文献核对。"},
            {"tradition": "佛教", "basis_source": "enc-brit-hinduism", "note": "以权威百科的印度教条目作两教同属印度宗教背景的一般参照（该来源未在线核验，见待核实）；属弱参照，具体教义差异待专门文献核对。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>耆那教实践与教义示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>耆那教实践与教义（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>耆那教</text><line x1='380' y1='138' x2='380' y2='176' stroke='currentColor' opacity='0.5'/><line x1='170' y1='176' x2='590' y2='176' stroke='currentColor' opacity='0.5'/><line x1='170' y1='176' x2='170' y2='214' stroke='currentColor' opacity='0.5'/><line x1='380' y1='176' x2='380' y2='214' stroke='currentColor' opacity='0.5'/><line x1='590' y1='176' x2='590' y2='214' stroke='currentColor' opacity='0.5'/><rect x='80' y='214' width='180' height='56' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>非暴力</text><text x='170' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>不害</text><rect x='290' y='214' width='180' height='56' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>苦行</text><text x='380' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>戒律实践</text><rect x='500' y='214' width='180' height='56' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>教派</text><text x='590' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>白衣·天衣</text><text x='380' y='322' text-anchor='middle' fill='var(--svg-text)' font-size='13'>描述性立场，不评判信仰真伪</text></svg>",
        "pending_notes": "1) 教派分歧的具体形成年代待核实，正文仅作历史描述；2) 非暴力、不执著等教义在不同时期的阐释差异待专门文献核对；3) 与印度教、佛教比较为弱参照，待补专门文献；4) 三位解读学者的代表著作未逐条录入 sources.json，细节待核。",
        "needs_verification": True
    },
    "myth-sumerian": {
        "level": "L2",
        "source_text": "苏美尔神话保存在楔形文字泥板中，主要来自公元前三千纪至二千纪的美索不达米亚南部城邦，内容包括神祇颂歌、创世与洪水叙事、王表等。《苏美尔王表》与 Kramer 的整理是研究基础，大量文本仍有残缺。",
        "versions": [
            "苏美尔诸神（如安、恩利尔、伊南娜）与城邦政治密切相关，不同城邦有各自的主神与神庙传统。",
            "洪水叙事在苏美尔泥板与后世阿卡德语版本间存在对应关系，二者的先后与改编关系为学界研究议题。",
            "《苏美尔王表》把王权起源归于天降，与创世史诗的王权观形成对照。"
        ],
        "interpretations": [
            {"holder": "Samuel Noah Kramer", "school": "苏美尔学", "view": "通过泥板翻译与整理指出苏美尔创世思想的独特性，强调其与后世闪族传统的承继与差异。"},
            {"holder": "Thorkild Jacobsen", "school": "美索不达米亚宗教史", "view": "以神祇组织与城邦政治的关联分析苏美尔宗教，强调神话叙事与政治秩序的关系。"},
            {"holder": "Henri Frankfort", "school": "古代近东思想研究", "view": "把苏美尔—美索不达米亚宇宙观作为与希腊哲学思想对照的类型，属专门研究。"}
        ],
        "comparisons": [
            {"tradition": "阿卡德神话", "basis_source": "aca-sumerian-mythology", "note": "Kramer 的苏美尔神话研究记录了苏美尔与阿卡德传统在神名与叙事上的承继关系，属有文献依据的对照。"},
            {"tradition": "埃及神话", "basis_source": "aca-before-philosophy", "note": "Frankfort 将美索不达米亚与埃及宇宙观并置比较，属近东思想研究的一般参照。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>苏美尔神话材料示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>苏美尔神话材料群（示意）</text><rect x='290' y='90' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='120' text-anchor='middle' fill='var(--svg-text)' font-size='14'>楔形文字泥板</text><line x1='380' y1='136' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>神祇颂歌</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>安·恩利尔·伊南娜</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>洪水叙事</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>与后世版本对应</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>苏美尔王表</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>天降王权</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>大量泥板残缺，正文未给具体年代</text></svg>",
        "pending_notes": "1) 大量泥板文本残缺，具体年代未列；2) 洪水叙事两版本的先后学界有讨论；3) Kramer、Jacobsen 论点以其代表著作为概括，细节待逐条核对。",
        "needs_verification": True
    },
    "myth-akkadian": {
        "level": "L2",
        "source_text": "阿卡德神话以闪族语言的美索不达米亚传统为主，《吉尔伽美什史诗》与《阿特拉哈西斯》是其核心文献，与苏美尔传统有承继关系。学界对二者文本关系有长期研究，本站只记录有文献依据的对照。",
        "versions": [
            "《吉尔伽美什史诗》有多种版本，巴比伦标准版本与更早的苏美尔故事在情节与主题上存在差异。",
            "《阿特拉哈西斯》叙述洪水与人类再生，与《吉尔伽美什》中的洪水段落存在情节对应，二者关系为研究议题。",
            "阿卡德传统在继承苏美尔神祇的同时，也抬升了本地主神（如马尔杜克）的地位。"
        ],
        "interpretations": [
            {"holder": "Thorkild Jacobsen", "school": "美索不达米亚宗教史", "view": "以神祇组织与政治秩序的关联分析阿卡德—巴比伦神话，强调叙事与王权的联系。"},
            {"holder": "Samuel Noah Kramer", "school": "苏美尔学", "view": "通过泥板整理指出苏美尔与闪族传统的承继与差异，为阿卡德神话研究提供背景。"},
            {"holder": "Henri Frankfort", "school": "古代近东思想研究", "view": "以神话意象分析美索不达米亚宇宙观，主张不以现代抽象标准误读。"}
        ],
        "comparisons": [
            {"tradition": "苏美尔神话", "basis_source": "aca-sumerian-mythology", "note": "Kramer 的苏美尔神话研究记录了苏美尔—阿卡德传统在神名与叙事上的承继关系，属有文献依据的对照。"},
            {"tradition": "希腊神话", "basis_source": "aca-comparative-myth", "note": "Puhvel 的比较神话学通论在近东—地中海框架内讨论洪水与英雄母题，属框架性弱参照而非具体文献实证，学界对传播路径有争论，待补专门文献，此处并列呈现。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>阿卡德神话核心文献示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>阿卡德神话核心文献（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>阿卡德传统</text><line x1='380' y1='138' x2='380' y2='176' stroke='currentColor' opacity='0.5'/><line x1='200' y1='176' x2='560' y2='176' stroke='currentColor' opacity='0.5'/><line x1='200' y1='176' x2='200' y2='214' stroke='currentColor' opacity='0.5'/><line x1='560' y1='176' x2='560' y2='214' stroke='currentColor' opacity='0.5'/><rect x='110' y='214' width='180' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='200' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>吉尔伽美什</text><text x='200' y='258' text-anchor='middle' fill='var(--svg-text)' font-size='12'>多版本史诗</text><rect x='470' y='214' width='180' height='58' fill='var(--svg-node)' stroke='currentColor'/><text x='560' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>阿特拉哈西斯</text><text x='560' y='258' text-anchor='middle' fill='var(--svg-text)' font-size='12'>洪水叙事</text><rect x='230' y='306' width='300' height='54' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='328' text-anchor='middle' fill='var(--svg-text)' font-size='13'>继承苏美尔传统</text><text x='380' y='348' text-anchor='middle' fill='var(--svg-text)' font-size='12'>抬升本地主神</text></svg>",
        "pending_notes": "1) 洪水两版本关系与先后学界有讨论；2) 史诗版本的确切年代未列；3) Jacobsen、Kramer 论点细节待逐条核对。",
        "needs_verification": True
    },
    "myth-persian": {
        "level": "L2",
        "source_text": "波斯神话材料包括前琐罗亚斯德时期的伊朗传统与《阿维斯陀》中的传说，主要经后世文献保存。学界对其与印欧神话的关系有比较研究，本站只记录有文献依据的对照，不评判任何信仰真伪。",
        "versions": [
            "前琐罗亚斯德时期的伊朗神祇与仪式材料零散，多经后世文献与考古间接重建。",
            "《阿维斯陀》中的神祇与宇宙观与琐罗亚斯德教的改革密切相关，前后传统的关系为学界议题。",
            "波斯神话与印度吠陀传统在印欧语系框架内有可比之处，具体对应关系有讨论。"
        ],
        "interpretations": [
            {"holder": "Georges Dumézil", "school": "印欧比较神话学", "view": "以三功能假说把伊朗与印度材料并置比较，属学派模型，学界对其适用范围有批评。"},
            {"holder": "Jaan Puhvel", "school": "印欧比较神话学", "view": "在印欧语系框架内比较伊朗与相关神话，属学术对照，具体对应关系有讨论。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "可从宇宙秩序与善恶母题作现象学层面的参照，属框架性对照。"}
        ],
        "comparisons": [
            {"tradition": "印度神话（吠陀）", "basis_source": "aca-gods-indo-europeans", "note": "Dumézil 的印欧比较把伊朗与吠陀材料并置，属学派框架，不主张直接同源。"},
            {"tradition": "希腊神话", "basis_source": "aca-comparative-myth", "note": "比较神话学在印欧框架内作一般参照，具体对应关系有讨论，本站不下定论。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>波斯神话材料层次示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>波斯神话材料层次（示意）</text><rect x='280' y='92' width='200' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>波斯神话</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>前琐罗亚斯德</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>材料零散</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>阿维斯陀</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>宇宙观·神祇</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>考古旁证</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>间接重建</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>印欧比较为学派框架，不主张同源</text></svg>",
        "pending_notes": "1) 前琐罗亚斯德材料零散，重建依赖后世文献，具体年代未列；2) Dumézil 三功能模型有争论；3) 比较为学派框架，不替读者下结论。",
        "needs_verification": True
    },
    "myth-finnish": {
        "level": "L2",
        "source_text": "芬兰神话的核心材料是《卡勒瓦拉》，由 Elias Lönnrot 据芬兰—卡累利阿口传诗歌编纂而成，并非单一作者的原创。口传材料的地域变体与编纂者的取舍为学界讨论议题，本站如实标注。",
        "versions": [
            "《卡勒瓦拉》1835 年初版、1849 年增订版，编纂者把不同地区与歌手演唱的诗歌连缀成篇。",
            "口传诗歌在流传中存在地域与演唱者差异，与编纂本的叙述并非一一对应。",
            "芬兰神话与波罗的海、北欧传统有可比母题，具体关系为学界讨论议题。"
        ],
        "interpretations": [
            {"holder": "Elias Lönnrot", "school": "芬兰口传文学编纂", "view": "通过采集与编纂口传诗歌建构芬兰民族叙事，其取舍与连缀方式影响后世对芬兰神话的理解，属文学史研究。"},
            {"holder": "Jaan Puhvel", "school": "印欧比较神话学", "view": "在印欧框架内比较芬兰—乌戈尔与其他神话，属学术对照；芬兰语非印欧语，适用性需谨慎。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "可从英雄与宇宙母题作现象学层面的参照，属框架性对照。"}
        ],
        "comparisons": [
            {"tradition": "北欧神话", "basis_source": "aca-comparative-myth", "note": "比较神话学在波罗的海—北欧框架内讨论母题相似性，芬兰语系归属特殊，不主张同源。"},
            {"tradition": "爱沙尼亚/乌戈尔传统", "basis_source": "enc-wiki-list-myth", "note": "以权威百科条目作乌拉尔语系背景的一般参照（该来源未在线核验，见待核实）；属弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>卡勒瓦拉与芬兰神话示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>卡勒瓦拉：从口传到编纂（示意）</text><rect x='70' y='150' width='170' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='155' y='174' text-anchor='middle' fill='var(--svg-text)' font-size='13'>口传诗歌</text><text x='155' y='194' text-anchor='middle' fill='var(--svg-text)' font-size='12'>地域变体</text><line x1='240' y1='180' x2='330' y2='180' stroke='currentColor' opacity='0.5'/><rect x='330' y='150' width='170' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='415' y='174' text-anchor='middle' fill='var(--svg-text)' font-size='13'>Lönnrot 编纂</text><text x='415' y='194' text-anchor='middle' fill='var(--svg-text)' font-size='12'>连缀成篇</text><line x1='500' y1='180' x2='590' y2='180' stroke='currentColor' opacity='0.5'/><rect x='590' y='150' width='120' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='650' y='184' text-anchor='middle' fill='var(--svg-text)' font-size='13'>卡勒瓦拉</text><rect x='230' y='282' width='300' height='48' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='304' text-anchor='middle' fill='var(--svg-text)' font-size='13'>1835初版 / 1849增订版</text><text x='380' y='356' text-anchor='middle' fill='var(--svg-text)' font-size='12'>芬兰语属乌拉尔语系，印欧比较需谨慎</text></svg>",
        "pending_notes": "1) 编纂本的取舍与口传原貌的关系为学界议题，正文未列具体细节；2) 芬兰语系归属特殊，Puhvel 印欧比较的适用性已标注需谨慎；3) 乌戈尔比较为弱参照，待补专门文献。",
        "needs_verification": True
    },
    "myth-slavic": {
        "level": "L2",
        "source_text": "斯拉夫神话的材料较为零散，主要经中世纪文献、民间传说与民族志记录保存，东斯拉夫与南斯拉夫传统各有差异。本站只记录有文献依据的对照，不推断同源。",
        "versions": [
            "东斯拉夫的神话材料多见于编年史与民间仪式记录，神祇形象经基督教时代改写。",
            "南斯拉夫与西斯拉夫的传说保留若干母题，与东斯拉夫材料既有相似也有地方差异。",
            "民族志记录的口传材料与中世纪文献之间隔着漫长时段，直接对应需谨慎。"
        ],
        "interpretations": [
            {"holder": "Aleksander Gieysztor", "school": "波兰历史学与斯拉夫神话研究", "view": "Gieysztor 认为东斯拉夫的佩伦（Perun）与雷电、誓约及王权仪式相关联，据编年史与民俗材料重建其职能；此为学术观点，其著作未录入 sources.json。"},
            {"holder": "Roman Jakobson", "school": "结构主义语言学与斯拉夫研究", "view": "Jakobson 从语言与神话结构的关系分析斯拉夫神祇，强调佩伦—维莱斯（Veles）等对立在神话思维中的位置，属学派框架，其著作未录入 sources.json。"},
            {"holder": "Åke Hultkrantz", "school": "宗教民族学", "view": "Hultkrantz 主张口传与民族志材料是重建斯拉夫等区域传统的首要依据，但指出这些记录多经后世转写、语境已变，直接追溯古代信仰须谨慎，其区域研究方法为此类重建设定了证据边界。"}
        ],
        "comparisons": [
            {"tradition": "北欧神话", "basis_source": "aca-comparative-myth", "note": "比较神话学在印欧框架内作一般参照，不主张具体神祇同源。"},
            {"tradition": "波罗的海神话", "basis_source": "enc-wiki-list-myth", "note": "以权威百科条目作区域背景的一般参照（该来源未在线核验，见待核实）；此为背景线索而非实质比较依据，属弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>斯拉夫神话材料示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>斯拉夫神话材料与区域差异（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>斯拉夫神话</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='160' y1='174' x2='600' y2='174' stroke='currentColor' opacity='0.5'/><line x1='160' y1='174' x2='160' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='600' y1='174' x2='600' y2='212' stroke='currentColor' opacity='0.5'/><rect x='70' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='160' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>东斯拉夫</text><text x='160' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>编年史·仪式</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>南斯拉夫</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>民间传说</text><rect x='510' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='600' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>西斯拉夫</text><text x='600' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>地方母题</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>口传与文献相隔漫长时段，对应需谨慎</text></svg>",
        "pending_notes": "1) 斯拉夫神话材料零散，重建依赖多类记录；2) 区域传统的具体差异待专门文献核对；3) Gieysztor、Jakobson 著作未录入 sources.json，已标注；4) 波罗的海比较为弱参照。",
        "needs_verification": True
    },
    "myth-hittite": {
        "level": "L2",
        "source_text": "赫梯神话保存在安纳托利亚的楔形文字泥板中，以风暴神与创世传说为核心，材料的解读依赖赫梯语与语言学进展。Gary Beckman 的《赫梯神话》译注是重要参考，部分文本仍有残缺。",
        "versions": [
            "赫梯的风暴神与王权仪式密切相关，神祇体系受到美索不达米亚与本土传统的双重影响。",
            "创世与神祇斗争的文本在赫梯语与阿卡德语版本间有对应，具体读法随语言学进展更新。",
            "赫梯材料与后来的安纳托利亚传统之间的关系为学界讨论议题。"
        ],
        "interpretations": [
            {"holder": "Gary Beckman", "school": "赫梯学与近东研究", "view": "通过泥板译注重建赫梯神话，强调文本的语言学细节与近东文化背景，属专门研究。"},
            {"holder": "Henri Frankfort", "school": "古代近东思想研究", "view": "为理解近东神话思维提供比较框架，具体到赫梯材料的结论待专门文献核对。"},
            {"holder": "Jaan Puhvel", "school": "印欧比较神话学", "view": "赫梯语属印欧语系，可在印欧框架内比较，属学术对照，具体对应关系有讨论。"}
        ],
        "comparisons": [
            {"tradition": "美索不达米亚神话", "basis_source": "aca-hittite-myths", "note": "Beckman 的译注指出赫梯材料受美索不达米亚传统影响，属有文献依据的对照。"},
            {"tradition": "希腊神话", "basis_source": "aca-comparative-myth", "note": "赫梯语属印欧语系，比较神话学在印欧框架内作一般参照，不主张直接同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>赫梯神话材料示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>赫梯神话材料与影响（示意）</text><rect x='280' y='92' width='200' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>楔形文字泥板</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='180' y1='174' x2='580' y2='174' stroke='currentColor' opacity='0.5'/><line x1='180' y1='174' x2='180' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='580' y1='174' x2='580' y2='212' stroke='currentColor' opacity='0.5'/><rect x='90' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='180' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>风暴神</text><text x='180' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>王权仪式</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>创世传说</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>多语版本</text><rect x='490' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='580' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>双重影响</text><text x='580' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>本土·近东</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>部分文本残缺，读法随语言学进展更新</text></svg>",
        "pending_notes": "1) 部分泥板文本残缺，具体读法待语言学进展更新；2) 与后世安纳托利亚传统的关系为学界议题；3) 比较为学术框架，不主张同源。",
        "needs_verification": True
    },
    "myth-yoruba": {
        "level": "L2",
        "source_text": "约鲁巴神话以奥里莎（orisha）神系与创世传说为核心，传统主要经口传与仪式保存，也有文字记录。大英博物馆等机构提供文物与背景资料，本站只记录有文献依据的对照，不评判信仰真伪。",
        "versions": [
            "约鲁巴传统中最高神与奥里莎神祇的谱系在不同地区与家族间存在差异，口传版本不一。",
            "创世与人类起源的叙事经文字记录与学术研究整理，记录者的立场需考虑。",
            "约鲁巴传统随移民传播到其他地区，在海地与美洲的宗教中有相关但不等同的形态。"
        ],
        "interpretations": [
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "可从创世与神系母题作现象学层面的一般参照，不构成对约鲁巴材料的专门结论。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "为分析神话中的对立与中介提供方法论参照，属学派一般立场。"},
            {"holder": "James George Frazer", "school": "早期比较宗教学", "view": "在跨文化框架中讨论神祇与仪式，属早期学派观点，其泛化结论在现代学界受到修订。"}
        ],
        "comparisons": [
            {"tradition": "非洲其他传统", "basis_source": "ins-british-museum", "note": "以机构藏品与背景资料作非洲宗教背景的一般参照（该机构页未在线核验，见待核实）；属弱参照，具体差异待专门文献核对。"},
            {"tradition": "大洋洲神话", "basis_source": "enc-wiki-list-myth", "note": "以权威百科条目作跨区域母题的一般参照（该来源未在线核验），属弱参照，不推断同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>约鲁巴神话结构示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>约鲁巴神话结构（示意）</text><rect x='280' y='92' width='200' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>至高神</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='180' y1='174' x2='580' y2='174' stroke='currentColor' opacity='0.5'/><line x1='180' y1='174' x2='180' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='580' y1='174' x2='580' y2='212' stroke='currentColor' opacity='0.5'/><rect x='90' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='180' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>奥里莎</text><text x='180' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>神祇谱系</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>创世</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>人类起源</text><rect x='490' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='580' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>口传·仪式</text><text x='580' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>传统载体</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>地区与家族版本有差异</text></svg>",
        "pending_notes": "1) 口传与记录者的立场需考虑，具体神系差异待专门文献核对；2) 机构与百科来源未在线核验，已标弱参照；3) “奥里莎（orisha）”采用中文为主、英文括注；来源未在线核验已标弱参照。",
        "needs_verification": True
    },
    "myth-dogon": {
        "level": "L2",
        "source_text": "多贡神话的材料主要来自20世纪人类学家记录的多贡人口传传统，涉及创世与天象观念。材料的记录语境与解读争议为学界讨论议题（如 Griaule 的记录方法曾受质疑），本站如实标注待核实。",
        "versions": [
            "多贡创世叙事经殖民时期与20世纪的人类学记录保存，不同记录者所得版本存在差异。",
            "关于天象知识的口传内容，学界对其记录可靠性与解读有长期争论。",
            "口传材料的翻译与语境依赖强，直接与现代天文学知识对应需谨慎。"
        ],
        "interpretations": [
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "为分析神话中的分类与对立结构提供方法论参照，属学派一般立场，不构成对多贡材料的专门结论。"},
            {"holder": "Michel Leiris", "school": "民族学与神话研究", "view": "对多贡材料的记录与解读持审慎态度，强调语境与记录方法的重要性，其著作未录入来源库。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "可从创世与宇宙观母题作现象学层面的参照，属框架性对照。"}
        ],
        "comparisons": [
            {"tradition": "非洲其他传统", "basis_source": "ins-british-museum", "note": "以机构背景资料作区域参照（该机构页未在线核验，见待核实）；属弱参照，具体差异待专门文献核对。"},
            {"tradition": "约鲁巴神话", "basis_source": "enc-wiki-list-myth", "note": "以权威百科条目作非洲神话背景的一般参照（该来源未在线核验）；此为区域背景线索而非多贡—约鲁巴之间具体母题的实证依据，属弱参照，待补专门民族志文献，不主张同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>多贡神话材料与争议示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>多贡神话材料与记录争议（示意）</text><line x1='155' y1='180' x2='305' y2='180' stroke='currentColor' opacity='0.5'/><line x1='455' y1='180' x2='605' y2='180' stroke='currentColor' opacity='0.5'/><rect x='70' y='150' width='170' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='155' y='174' text-anchor='middle' fill='var(--svg-text)' font-size='13'>口传传统</text><text x='155' y='194' text-anchor='middle' fill='var(--svg-text)' font-size='12'>多贡人</text><rect x='305' y='150' width='150' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='174' text-anchor='middle' fill='var(--svg-text)' font-size='13'>人类学记录</text><text x='380' y='194' text-anchor='middle' fill='var(--svg-text)' font-size='12'>20世纪</text><rect x='455' y='150' width='170' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='540' y='174' text-anchor='middle' fill='var(--svg-text)' font-size='13'>学术解读</text><text x='540' y='194' text-anchor='middle' fill='var(--svg-text)' font-size='12'>存争议</text><rect x='230' y='282' width='300' height='54' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='304' text-anchor='middle' fill='var(--svg-text)' font-size='13'>记录方法与解读存争议</text><text x='380' y='322' text-anchor='middle' fill='var(--svg-text)' font-size='12'>如实标注待核实</text><text x='380' y='368' text-anchor='middle' fill='var(--svg-text)' font-size='12'>口传与现代知识对应需谨慎</text></svg>",
        "pending_notes": "1) 多贡材料的记录可靠性与解读有长期争论，正文已标注；2) Leiris 著作未录入 sources.json，已声明；3) 与天象知识的对应需谨慎，不下定论。",
        "needs_verification": True
    },
    "myth-polynesian": {
        "level": "L2",
        "source_text": "波利尼西亚神话包括毛利、夏威夷等地的创世与航海传统，主要经口传与19世纪以来的记录保存。不同岛屿群体在传统上有联系也有差异，本站只记录有文献依据的对照。",
        "versions": [
            "毛利与夏威夷的创世叙事共享若干母题，但神名与细节因地域而异。",
            "航海与祖先传说反映波利尼西亚人的海洋文化背景，口传版本随移民而演变。",
            "殖民时期记录与当代口传之间存在语境差异，解读需考虑记录立场。"
        ],
        "interpretations": [
            {"holder": "Marshall Sahlins", "school": "历史人类学（夏威夷研究）", "view": "Sahlins 认为夏威夷的神话叙事与王权政治相互建构，Māui 等人物传说与岛屿社会的历史变迁相关；其分析基于具体岛屿材料，著作未录入 sources.json。"},
            {"holder": "Patrick V. Kirch", "school": "太平洋考古学与波利尼西亚研究", "view": "Kirch 通过考古与语言材料重建波利尼西亚人的迁徙与航海社会，指出航海传统与祖先叙事的物质基础；其著作为专门研究，未录入 sources.json。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 可从创世与宇宙轴母题作现象学层面的参照，不直接等同于对波利尼西亚材料的专门结论。"}
        ],
        "comparisons": [
            {"tradition": "澳大利亚原住民神话", "basis_source": "enc-wiki-list-myth", "note": "以权威百科条目作大洋洲背景的一般参照（该来源未在线核验，见待核实）；属弱参照，不推断同源。"},
            {"tradition": "非洲传统", "basis_source": "ins-world-history", "note": "以机构资料作跨区域母题的一般参照（该来源未在线核验），属弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>波利尼西亚神话示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>波利尼西亚神话（示意）</text><rect x='280' y='92' width='200' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>波利尼西亚神话</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>创世</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>共享母题</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>航海传说</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>海洋文化</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>祖先叙事</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>随移民演变</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>地域差异与记录立场需考虑</text></svg>",
        "pending_notes": "1) 不同岛屿版本差异待专门文献核对；2) Sahlins、Kirch 著作未录入 sources.json，已标注；3) 殖民记录语境已标注；4) 与非洲传统比较为弱参照，待补专门文献。",
        "needs_verification": True
    },
    "myth-australian": {
        "level": "L2",
        "source_text": "澳大利亚原住民神话以“梦创时代”（Dreaming）的祖先叙事与宇宙观为核心，主要通过口传、仪式与岩画传统保存。材料记录涉及殖民语境与文化敏感性，本站以学术描述性立场整理，不评判信仰真伪。",
        "versions": [
            "不同原住民群体的梦创叙事各有地方差异，祖先神话与特定地域紧密关联。",
            "口传与仪式知识多为社群内部传承，外部记录的完整性与准确性有限。",
            "殖民时期记录与当代原住民社群的叙述之间存在语境差异，解读需谨慎。"
        ],
        "interpretations": [
            {"holder": "W. E. H. Stanner", "school": "澳大利亚人类学与原住民宗教研究", "view": "Stanner 认为“梦创时代”并非遥远的过去，而是持续作用于当下的宇宙论，强调其时间观的特殊性；其论点基于民族志研究，著作未录入 sources.json。"},
            {"holder": "T. G. H. Strehlow", "school": "中部澳大利亚民族志", "view": "Strehlow 通过中部原住民的祖先叙事与仪式记录，指出神话、歌谣与特定地域的密切联系；其材料与解读在学界有讨论，著作未录入 sources.json。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 认为神话时间可经仪式重演而被更新，为理解“梦创时代”提供现象学参照，不直接等同于对该传统的专门结论。"}
        ],
        "comparisons": [
            {"tradition": "波利尼西亚神话", "basis_source": "enc-wiki-list-myth", "note": "以权威百科条目作大洋洲背景的一般参照（该来源未在线核验，见待核实）；属弱参照，不推断同源。"},
            {"tradition": "非洲传统", "basis_source": "ins-world-history", "note": "以机构资料作跨区域母题的一般参照（该来源未在线核验），属弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>澳大利亚原住民神话示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>澳大利亚原住民神话（示意）</text><rect x='280' y='92' width='200' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>梦创时代</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>祖先叙事</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>地域关联</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>口传·仪式</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>社群传承</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>岩画传统</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>物质载体</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>殖民记录语境与文化敏感性需考虑</text></svg>",
        "pending_notes": "1) 外部记录的完整性与准确性有限，正文已标注；2) Stanner、Strehlow 著作未录入 sources.json，已标注；3) 材料涉及文化敏感性，本站仅作学术描述；4) 跨区域比较为弱参照，待补专门文献；“梦创时代（Dreaming）”采用中文为主、英文括注。",
        "needs_verification": True
    },
    "myth-inca": {
        "level": "L2",
        "source_text": "印加神话的材料主要经西班牙征服时期的编年史、口传记录与考古材料保存，核心母题包括太阳神崇拜与王室起源传说。记录者的立场与材料的中介性为学界讨论议题，本站如实标注。",
        "versions": [
            "印加王室起源叙事把统治者与太阳神关联，服务于王权合法性的表达，不同编年史记载有差异。",
            "太阳神（因蒂）与月亮、星辰崇拜在安第斯地区有本土传统，与官方王室神话并存。",
            "殖民时期记录与更早的口传、考古材料之间存在语境差异，直接对应需谨慎。"
        ],
        "interpretations": [
            {"holder": "Rebecca Stone-Miller", "school": "安第斯艺术史与考古", "view": "Stone-Miller 通过安第斯物质文化与艺术分析印加宇宙观，认为王权神话与物质象征相互支撑；其著作未录入 sources.json。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 以太阳的周期性运行与宇宙中心的象征为参照框架，提示印加太阳神与王权仪式的宇宙论关联；此为现象学层面的参照，不直接等同于对印加材料的专门结论。"},
            {"holder": "Tom D. Dillehay", "school": "安第斯考古学", "view": "Dillehay 以考古材料研究安第斯社会的形成，强调本土传统与外部影响的区分；其著作未录入 sources.json。"}
        ],
        "comparisons": [
            {"tradition": "阿兹特克神话", "basis_source": "ins-world-history", "note": "以机构资料作中美洲—安第斯背景的一般参照（该来源未在线核验，见待核实）；属弱参照，不推断同源。"},
            {"tradition": "波利尼西亚神话", "basis_source": "ins-british-museum", "note": "以机构藏品背景作太阳神母题的一般参照（该机构页未在线核验），属弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>印加神话材料示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>印加神话材料与王室叙事（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>印加神话</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>太阳神</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>因蒂崇拜</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>王室起源</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>合法性叙事</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>殖民记录</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>中介性</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>记录立场与考古材料需互证</text></svg>",
        "pending_notes": "1) 殖民记录立场与材料语境已标注；2) Stone-Miller、Dillehay 著作未录入 sources.json，已声明；3) 两张比较均为机构弱参照，待补专门文献。",
        "needs_verification": True
    },
    "myth-olmec": {
        "level": "L2",
        "source_text": "奥尔梅克是中美洲早期文明，其神话信息主要来自考古材料（如巨石头像与兽人图像）与后世传说的间接推断。由于缺乏可释读的神话文本，任何神话解读都属推测，本站如实标注待核实。",
        "versions": [
            "奥尔梅克文明的宗教形象多由考古遗物推断，缺乏同时期可释读的神话文本。",
            "兽人图像与后来中美洲神祇母题的相似性为学界讨论议题，但具体对应关系无定论。",
            "关于奥尔梅克与其他中美洲文明的关系，考古学界有多种模型，本站不作单一化结论。"
        ],
        "interpretations": [
            {"holder": "Peter David Joralemon", "school": "中美洲考古与图像学", "view": "Joralemon 通过奥尔梅克图像分析其宗教符号，提出神祇谱系的推断；此类解读依赖图像证据，学界有讨论，著作未录入 sources.json。"},
            {"holder": "Karl A. Taube", "school": "中美洲考古与图像学", "view": "Taube 强调考古与图像材料对重建中美洲神祇的重要性，主张跨区域比较需以材料为基础，其著作未录入 sources.json。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 可从巨蛇、丰产等母题作现象学参照，但对奥尔梅克材料不构成专门结论。"}
        ],
        "comparisons": [
            {"tradition": "玛雅神话", "basis_source": "ins-world-history", "note": "以机构资料作中美洲文化背景的一般参照（该来源未在线核验）；属弱参照，不推断具体母题同源。"},
            {"tradition": "阿兹特克神话", "basis_source": "ins-british-museum", "note": "以机构藏品背景作区域一般参照（该机构页未在线核验），属弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>奥尔梅克神话材料示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>奥尔梅克神话材料（考古推断）</text><rect x='280' y='92' width='200' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>考古遗物</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>巨石头像</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>统治象征</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>兽人图像</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>宗教符号</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>后世推断</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>无定论</text><text x='380' y='322' text-anchor='middle' fill='var(--svg-text)' font-size='13'>无可释读文本，神话解读均属推测</text></svg>",
        "pending_notes": "1) 无可释读神话文本，一切解读为考古推断，正文已标注；2) Joralemon、Taube 著作未录入 sources.json，已声明；3) 跨文明比较为弱参照，不推断同源。",
        "needs_verification": True
    },
    "myth-canaanite": {
        "level": "L2",
        "source_text": "迦南神话主要依据乌加里特楔形文字文献与考古材料重建，核心神祇包括巴力与阿娜特，丰产与风暴母题突出。学界对其与希伯来圣经的关系有长期研究，本站只记录有文献依据的对照。",
        "versions": [
            "乌加里特文献保存了巴力循环等神话文本，是重建迦南宗教的一手材料。",
            "不同城邦与时期的地方传统存在差异，乌加里特材料不能代表全部迦南地区。",
            "迦南神话与旧约材料的关系为学界研究议题，具体影响路径有争论，本站不下定论。"
        ],
        "interpretations": [
            {"holder": "Theodor H. Gaster", "school": "圣经民俗与比较宗教学", "view": "Gaster 以民俗与神话学方法比较乌加里特与旧约材料，指出近东背景的关联，属学术研究，不替信仰表态。"},
            {"holder": "Henri Frankfort", "school": "古代近东思想研究", "view": "Frankfort 以神话意象分析近东宇宙观，为理解迦南神话提供比较框架。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 以丰产与风暴母题的比较框架提示乌加里特材料与近东宇宙观的关系；此为现象学参照，属框架性对照。"}
        ],
        "comparisons": [
            {"tradition": "希伯来经典传统", "basis_source": "aca-myth-legend-custom", "note": "Gaster 的旧约民俗研究记录了乌加里特材料与希伯来经典的比较，属有文献依据的对照，不主张信仰同源。"},
            {"tradition": "美索不达米亚神话", "basis_source": "aca-before-philosophy", "note": "Frankfort 的近东思想研究作一般框架参照，具体影响路径有争论。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>迦南神话材料示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>迦南神话材料（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>乌加里特文献</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>巴力</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>风暴·丰产</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>阿娜特</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>战争·丰产</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>旧约比较</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>学界有争论</text><text x='380' y='322' text-anchor='middle' fill='var(--svg-text)' font-size='13'>乌加里特材料不代表全部迦南地区</text></svg>",
        "pending_notes": "1) 与旧约材料的影响路径学界有争论，正文未下定论；2) 三位学者论点为概括，细节待核对；3) 不主张信仰同源。",
        "needs_verification": True
    },
    "rel-sikhism": {
        "level": "L2",
        "source_text": "锡克教是起源于南亚的宗教传统，以《古鲁·格兰特·萨希卜》为核心经典，强调一神、师承与平等。本站采用学术描述性立场，不评判信仰真伪。",
        "versions": [
            "锡克教传统以十位古鲁的传承为历史叙事核心，第十位古鲁后经典成为社群权威的中心。",
            "不同教派与社群在实践与组织上各有侧重，是历史发展的结果。",
            "锡克教与印度教、伊斯兰教在历史语境中互动，但教义上保持自身传统。"
        ],
        "interpretations": [
            {"holder": "Stephen Prothero", "school": "比较宗教学", "view": "Prothero 认为锡克教在亚伯拉罕诸教与印度宗教的比较框架中具有独特目标，不宜化约为其他传统的分支，属通俗学术著作观点。"},
            {"holder": "Wendy Doniger", "school": "芝加哥学派（印度宗教与文本研究）", "view": "Doniger 从文本史与诠释多样性的角度指出，锡克教经典与古鲁传统是在特定历史中形成的独立文本系统，其意义须回到其自身语言与编纂脉络中考量。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 以神圣文本与师承在宗教史中的角色为参照，提示锡克教经典权威的现象学意义；属框架性对照。"}
        ],
        "comparisons": [
            {"tradition": "印度教", "basis_source": "enc-brit-hinduism", "note": "以权威百科条目作南亚宗教背景的一般参照（该来源未在线核验）；属弱参照，具体教义差异待专门文献核对。"},
            {"tradition": "伊斯兰教", "basis_source": "enc-wiki-world-religion", "note": "以百科条目作一神教背景的一般参照（该来源未在线核验），属弱参照，不主张同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>锡克教结构示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>锡克教结构（描述性示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>锡克教</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>核心经典</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>古鲁·格兰特</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>师承</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>十位古鲁</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>平等</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>社群实践</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>描述性立场，不评判信仰真伪</text></svg>",
        "pending_notes": "1) 教派与实践差异待专门文献核对；2) 三位学者观点为概括，百科来源未在线核验已标弱参照；3) 不替信仰表态。",
        "needs_verification": True
    },
    "rel-zoroastrianism": {
        "level": "L2",
        "source_text": "琐罗亚斯德教源于古伊朗，以查拉图斯特拉的教导为基础，《阿维斯陀》为其核心经典，善恶二元论与火崇拜为其显著主题。本站采用学术描述性立场，不评判信仰真伪。",
        "versions": [
            "《阿维斯陀》的各部分成书年代不一，伽萨被认为较早，后续部分在神学上有所发展。",
            "不同时期与地区（如伊朗与印度帕西人社群）的传统在实践与教义理解上存在差异。",
            "琐罗亚斯德教与前琐罗亚斯德伊朗传统的关系为学界议题，具体改革内容有讨论。"
        ],
        "interpretations": [
            {"holder": "Georges Dumézil", "school": "印欧比较神话学", "view": "Dumézil 以三功能假说把伊朗神话与印欧其他传统比较，属学派框架，学界对适用性有讨论。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 认为善恶二元与宇宙斗争母题在宗教史上有广泛对应，为理解琐罗亚斯德教提供现象学参照，不替信仰表态。"},
            {"holder": "Richard Foltz", "school": "伊朗宗教与跨文化研究", "view": "Foltz 强调琐罗亚斯德教在丝绸之路上的跨文化传播与互动，其著作未录入 sources.json。"}
        ],
        "comparisons": [
            {"tradition": "波斯神话", "basis_source": "aca-gods-indo-europeans", "note": "Dumézil 的印欧比较把前伊斯兰伊朗材料并置，属学派框架，不主张信仰同源。"},
            {"tradition": "摩尼教", "basis_source": "enc-wiki-world-religion", "note": "以百科条目作二元论宗教背景的一般参照（该来源未在线核验），属弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>琐罗亚斯德教主题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>琐罗亚斯德教主题（描述性示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>阿维斯陀</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>善恶二元</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>宇宙斗争</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>火崇拜</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>仪式核心</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>伽萨</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>较早部分</text><text x='380' y='322' text-anchor='middle' fill='var(--svg-text)' font-size='13'>描述性立场，不评判信仰真伪</text></svg>",
        "pending_notes": "1) 各部分组成年代不一，正文未列具体年数；2) Foltz 著作未录入 sources.json，已声明；3) 与前伊斯兰传统的关系为学界议题，不替信仰表态。",
        "needs_verification": True
    },
    "rel-shamanism": {
        "level": "L2",
        "source_text": "萨满教跨多个文化传统，以萨满的仪式、出神与精灵交往为特征。Eliade 的《萨满教》是其研究的经典著作，Hultkrantz 的北美原住民宗教研究提供区域材料。本站采用学术描述性立场，不评判信仰真伪。",
        "versions": [
            "不同地区与民族的萨满实践差异显著，不宜预设统一的萨满教模式。",
            "Eliade 提出的萨满经典模式影响深远，但学界对其普遍适用性有批评与修订。",
            "Hultkrantz 强调北美原住民宗教的多样性，反对把复杂实践简化为单一样板。"
        ],
        "interpretations": [
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 认为萨满的出神与宇宙旅行是宗教现象学的重要母题，提出经典模式，但其普遍性在学界有争论。"},
            {"holder": "Åke Hultkrantz", "school": "宗教民族学（北美研究）", "view": "Hultkrantz 认为北美原住民的萨满实践需在其具体生态与文化语境中理解，反对过度泛化；其著作已录入 sources.json。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "Lévi-Strauss 为分析萨满仪式中的象征与治疗功能提供方法论参照，属学派立场。"}
        ],
        "comparisons": [
            {"tradition": "西伯利亚神话", "basis_source": "aca-shamanism", "note": "Eliade 的萨满教研究以西伯利亚材料为重要案例，属有文献依据的对照。"},
            {"tradition": "北美原住民宗教", "basis_source": "aca-religions-american-indians", "note": "Hultkrantz 的区域研究记录了北美萨满实践的多样性，属有文献依据的对照，不主张同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>萨满教实践主题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>萨满教实践主题（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>萨满教</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>出神旅行</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>仪式状态</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>精灵交往</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>中介角色</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>治疗功能</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>社群实践</text><text x='380' y='322' text-anchor='middle' fill='var(--svg-text)' font-size='13'>地区差异显著，不预设统一模式</text></svg>",
        "pending_notes": "1) Eliade 经典模式的普遍适用性有学界争论，正文已标注；2) 地区实践差异待专门文献核对；3) Lévi-Strauss 的萨满研究著作未录入 sources.json，其象征与治疗论点为概括；4) 不替信仰表态。",
        "needs_verification": True
    },
    "rel-manichaeism": {
        "level": "L2",
        "source_text": "摩尼教源于3世纪波斯，由摩尼创立，融合多种宗教元素，以二元论宇宙观著称，历史上曾广泛传播后渐衰微。本站采用学术描述性立场，不评判信仰真伪。",
        "versions": [
            "摩尼教的教义以光明与黑暗的二元对立为核心，具体神话叙事见其经典残篇。",
            "摩尼教在传播中与各地文化互动，形成不同地区的表达形态。",
            "其与诺斯替、基督教、琐罗亚斯德教等传统的关系为学界研究议题，具体影响路径有讨论。"
        ],
        "interpretations": [
            {"holder": "Elaine Pagels", "school": "早期基督教与诺斯替研究", "view": "Pagels 对诺斯替文献的研究揭示了早期基督教内部二元论倾向的多样形态，为理解摩尼教所处的宗教史语境提供旁证，但摩尼教自身的教义需据其经典残篇专门考察，本文未据此对摩尼教下结论。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 可从二元论与宇宙救赎母题作现象学参照，属框架性对照。"},
            {"holder": "Richard Foltz", "school": "伊朗宗教与跨文化研究", "view": "Foltz 研究丝路上的宗教互动，为理解摩尼教传播提供跨文化参照，其著作未录入 sources.json。"}
        ],
        "comparisons": [
            {"tradition": "诺斯替传统", "basis_source": "aca-gnostic-gospels", "note": "Pagels 的诺斯替研究作历史语境的一般参照，不主张直接同源。"},
            {"tradition": "琐罗亚斯德教", "basis_source": "enc-wiki-world-religion", "note": "以百科条目作波斯宗教背景的一般参照（该来源未在线核验），属弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>摩尼教主题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>摩尼教主题（描述性示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>二元论</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>光明</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>善的原则</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>黑暗</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>恶的原则</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>救赎</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>解脱叙事</text><text x='380' y='322' text-anchor='middle' fill='var(--svg-text)' font-size='13'>与其他传统的关系为学界议题</text></svg>",
        "pending_notes": "1) 与其他宗教的影响路径学界有争论；2) Foltz 著作未录入 sources.json，已声明；3) 琐罗亚斯德教比较为弱参照，待补专门文献。",
        "needs_verification": True
    },
    "rel-bahai": {
        "level": "L2",
        "source_text": "巴哈伊信仰源于19世纪波斯，主张上帝唯一、宗教同源与人类一体，其经典包括巴哈欧拉的著作。本站采用学术描述性立场，不评判信仰真伪。",
        "versions": [
            "巴哈伊信仰自巴比教背景中发展而来，其形成与19世纪波斯的社会语境相关。",
            "该传统强调宗教演进与人类团结的教义，在不同文化中形成多元的实践形态。",
            "其早期历史与组织发展为学界研究对象，本站仅作描述性记录。"
        ],
        "interpretations": [
            {"holder": "Stephen Prothero", "school": "比较宗教学", "view": "Prothero 的宗教比较框架可用于理解巴哈伊信仰在诸宗教中的位置，属通俗学术著作观点，不替信仰表态。"},
            {"holder": "Peter Smith", "school": "巴哈伊信仰研究", "view": "Smith 系统梳理巴哈伊信仰的历史与教义，其著作为专门研究，未录入 sources.json。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 可从宗教同源与救赎母题作现象学参照，属框架性对照。"}
        ],
        "comparisons": [
            {"tradition": "伊斯兰教", "basis_source": "enc-wiki-world-religion", "note": "以百科条目作亚伯拉罕诸教背景的一般参照（该来源未在线核验），属弱参照，不主张同源。"},
            {"tradition": "琐罗亚斯德教", "basis_source": "enc-wiki-world-religion", "note": "以百科条目作波斯宗教背景的一般参照（该来源未在线核验，见待核实）；仅作背景线索，非巴哈伊—琐罗亚斯德教比较的实证依据，属弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>巴哈伊信仰主题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>巴哈伊信仰主题（描述性示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>核心教义</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>上帝唯一</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>一神论</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>宗教同源</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>渐进启示</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>人类一体</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>团结教义</text><text x='380' y='322' text-anchor='middle' fill='var(--svg-text)' font-size='13'>描述性立场，不评判信仰真伪</text></svg>",
        "pending_notes": "1) 早期历史与组织发展待专门文献核对；2) Peter Smith 著作未录入 sources.json，已声明；3) 两张比较均为弱参照，待补专门文献。",
        "needs_verification": True
    },
    "rel-mormonism": {
        "level": "L2",
        "source_text": "耶稣基督后期圣徒教会（摩门教）源于19世纪美国的基督教复原运动，以《摩门经》等经典与约瑟·斯密的教导为基础。本站采用学术描述性立场，不评判信仰真伪。",
        "versions": [
            "该传统的形成与19世纪美国第二次大觉醒的社会语境相关，强调复原早期基督教。",
            "其经典体系包括《摩门经》及后续启示文献，不同宗派对经典的采信有差异。",
            "该传统内部在经典采信、先知继承与教义侧重上形成多个分支，主要宗派对《摩门经》与后续启示的权威有不同理解。",
        ],
        "interpretations": [
            {"holder": "Stephen Prothero", "school": "比较宗教学", "view": "Prothero 把摩门教作为美国新兴宗教的案例讨论，强调其独特性，属通俗学术著作观点，不替信仰表态。"},
            {"holder": "Jan Shipps", "school": "摩门教历史研究", "view": "Shipps 以历史学方法研究摩门教的形成与发展，强调需从其自身语境理解，其著作未录入 sources.json。"},
            {"holder": "Max Weber", "school": "宗教社会学", "view": "Weber 的宗教社会学为理解新兴宗教与社会结构的关系提供框架，具体到摩门教的结论待核对。"}
        ],
        "comparisons": [
            {"tradition": "基督教", "basis_source": "enc-wiki-world-religion", "note": "以百科条目作基督教背景的一般参照（该来源未在线核验），属弱参照，不主张教义同源。"},
            {"tradition": "伊斯兰教", "basis_source": "enc-brit-islam", "note": "以权威百科的伊斯兰教条目作一般参照（该来源未在线核验，见待核实）；仅作亚伯拉罕诸教背景线索，非摩门教—伊斯兰教比较的实证依据，属弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>摩门教主题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>后期圣徒运动主题（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>后期圣徒</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>复原运动</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>19世纪美国</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>经典体系</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>摩门经等</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>宗派差异</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>经典采信</text><text x='380' y='322' text-anchor='middle' fill='var(--svg-text)' font-size='13'>描述性立场，不评判信仰真伪</text></svg>",
        "pending_notes": "1) 历史发展与组织演变待专门文献核对；2) Jan Shipps、Max Weber 的代表著作未录入 sources.json，其论点为概括；3) 两张比较均为弱参照，待补专门文献。",
        "needs_verification": True
    },
    "rel-tibetan-buddhism": {
        "level": "L2",
        "source_text": "藏传佛教是佛教传入青藏高原后形成的金刚乘传统，以显密结合、师承与寺院制度为特征。本站采用学术描述性立场，不评判信仰真伪。",
        "versions": [
            "藏传佛教在历史发展中形成多个教派，各派在教义侧重与修持方法上各有传统。",
            "显宗与密宗的修持体系在寺院教育中并行，密续与坛城等主题为研究重点。",
            "其与印度佛教、汉传佛教的关系为学界研究议题，具体传播路径有讨论。"
        ],
        "interpretations": [
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 可从宇宙轴、坛城与修行实践作现象学参照，属框架性对照，不构成对藏传佛教的专门结论。"},
            {"holder": "Richard Gombrich", "school": "早期佛教研究（语文学与历史方法）", "view": "Gombrich 主张早期佛教教义须放在巴利文经典的具体语境中理解，其语文学方法可用于辨明藏传佛教对印度佛教的承继与转化，但藏传材料本身需另据藏文文献专门考察。"},
            {"holder": "Stephen Prothero", "school": "比较宗教学", "view": "Prothero 强调各宗教传统的独特目标，为宗教比较提供框架，属通俗学术著作观点。"}
        ],
        "comparisons": [
            {"tradition": "佛教（汉传）", "basis_source": "enc-brit-buddhism", "note": "以权威百科条目作佛教传统背景的一般参照（该来源未在线核验），属弱参照，具体差异待专门文献核对。"},
            {"tradition": "印度教密教", "basis_source": "enc-brit-tantrism", "note": "以权威百科条目作密教背景的一般参照（该来源未在线核验），属弱参照，不主张同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>藏传佛教主题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>藏传佛教主题（描述性示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>金刚乘</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>显密结合</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>寺院教育</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>师承</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>灌顶传统</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>坛城</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>密续主题</text><text x='380' y='322' text-anchor='middle' fill='var(--svg-text)' font-size='13'>描述性立场，不评判信仰真伪</text></svg>",
        "pending_notes": "1) 教派差异与传播路径待专门文献核对；2) 三位学者观点为概括，百科来源未在线核验已标弱参照；3) 不替信仰表态。",
        "needs_verification": True
    },
    "rel-zen": {
        "level": "L2",
        "source_text": "禅宗是汉传佛教的重要宗派，以坐禅与公案等修持方式著称，在东亚形成多个分支。本站采用学术描述性立场，不评判信仰真伪。",
        "versions": [
            "禅宗传统以师徒相承与公案参究为特色，不同宗派在修持方法与教义表述上各有侧重。",
            "汉传禅宗与日本禅宗在制度与美学表达上各有发展，是历史与地域条件的结果。",
            "禅宗与经典佛教的关系为学界研究议题，其“不立文字”的表述需放在具体语境中理解。"
        ],
        "interpretations": [
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《神圣与世俗》中讨论通过修行实践进入神圣时间的方式，为理解禅修的时间观提供现象学参照。"},
            {"holder": "Stephen Prothero", "school": "比较宗教学", "view": "Prothero 把禅宗作为佛教传统独特修行目标的案例，强调不宜化约，属通俗学术著作观点。"},
            {"holder": "D. T. Suzuki", "school": "禅学研究", "view": "Suzuki 以英文著述向西方介绍禅宗，强调其体验性；其表述影响深远但在学界有讨论，著作未录入 sources.json。"}
        ],
        "comparisons": [
            {"tradition": "佛教（藏传）", "basis_source": "enc-brit-buddhism", "note": "以权威百科条目作佛教传统背景的一般参照（该来源未在线核验）；属弱参照，具体修持差异待专门文献核对。"},
            {"tradition": "道教", "basis_source": "enc-wiki-world-religion", "note": "以百科条目作中国宗教背景的一般参照（该来源未在线核验），属弱参照，不主张同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>禅宗修持主题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>禅宗修持主题（描述性示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>禅宗</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>坐禅</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>修持核心</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>公案</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>参究话头</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>师承</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>法脉相传</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>描述性立场，不评判信仰真伪</text></svg>",
        "pending_notes": "1) 宗派修持差异待专门文献核对；2) Suzuki 著作未录入 sources.json，已声明；百科来源未在线核验已标弱参照；3) 不替信仰表态。",
        "needs_verification": True
    },
    "rel-pureland": {
        "level": "L2",
        "source_text": "净土宗是汉传佛教的重要宗派，以称名念佛与往生净土为核心实践，在东亚广泛流传。本站采用学术描述性立场，不评判信仰真伪。",
        "versions": [
            "净土宗以净土经典为依据，强调信愿行与称名念佛，不同祖师对教义的阐释各有侧重。",
            "汉传净土与日本净土宗在修行重点与制度上各有发展，是地域与历史条件的结果。",
            "净土观念与佛教宇宙论的关系为学界研究议题，本站仅作描述性记录。"
        ],
        "interpretations": [
            {"holder": "Stephen Prothero", "school": "比较宗教学", "view": "Prothero 把净土宗作为佛教追求往生目标的案例，强调各传统目标不同，属通俗学术著作观点。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 关于神圣空间与中心的论述指出，宗教传统常以某一理想世界为宇宙秩序的原型，净土作为理想佛国的象征可置于这一框架下理解，但此仅为一般理论参照，不构成对净土信仰的专门结论。"},
            {"holder": "Peter Harvey", "school": "佛教伦理与哲学研究", "view": "Harvey 系统梳理佛教伦理与实践，为理解净土宗提供背景参照，其具体结论待核对。"}
        ],
        "comparisons": [
            {"tradition": "佛教（禅宗）", "basis_source": "enc-brit-buddhism", "note": "以权威百科条目作汉传佛教背景的一般参照（该来源未在线核验）；属弱参照，修持差异待专门文献核对。"},
            {"tradition": "基督教", "basis_source": "enc-wiki-world-religion", "note": "以百科条目作救赎主题的一般参照（该来源未在线核验），属弱参照，不主张同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>净土宗主题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>净土宗主题（描述性示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>净土宗</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>称名念佛</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>核心实践</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>信愿行</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>三要素</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>往生净土</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>目标</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>描述性立场，不评判信仰真伪</text></svg>",
        "pending_notes": "1) 净土观念与宇宙论的关系待专门文献核对；2) Harvey 著作未录入 sources.json，百科来源未在线核验，已标；3) 不替信仰表态。",
        "needs_verification": True
    },
    "motif-twin": {
        "level": "L2",
        "sources_extra": ["aca-eternal-return"],
        "source_text": "孪生母题以双生子的对立与互补为核心，见于多传统的神话叙事。Frazer《金枝》与比较神话学对相关母题有研究，本站只记录有文献依据的对照。",
        "versions": [
            "一些传统中孪生兄弟分别代表对立原则（如光明与黑暗、农耕与狩猎），其关系构成叙事张力。",
            "孪生子中的一人常具凡人性、另一人具神性，或二者轮流存在，形态因传统而异。",
            "把不同文化的孪生叙事并置属母题层面比较，不主张同源。"
        ],
        "interpretations": [
            {"holder": "James George Frazer", "school": "早期比较宗教学", "view": "Frazer 在《金枝》中讨论成对神祇与季节循环的关系，为孪生母题提供早期学派参照，其泛化结论已被现代学界修订。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "Lévi-Strauss 在《结构人类学》中以孪生说明神话如何以对立与中介调和范畴，属方法论层面的参照。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《永恒回归的神话》中把成对神祇的对立解读为宇宙秩序周期性重演的神话表达，属其永恒回归框架的具体案例。"}
        ],
        "comparisons": [
            {"tradition": "希腊神话", "basis_source": "aca-comparative-myth", "note": "比较神话学在印欧框架内讨论孪生母题，属学术参照，不主张同源。"},
            {"tradition": "印度神话", "basis_source": "aca-comparative-myth", "note": "Puhvel 的比较神话学通论为跨传统孪生母题提供框架性参照，属弱参照，具体文本对应待专门文献核对。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>孪生母题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>孪生母题（仅示意，不表示同源）</text><rect x='290' y='96' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='126' text-anchor='middle' fill='var(--svg-text)' font-size='14'>孪生</text><line x1='380' y1='142' x2='380' y2='176' stroke='currentColor' opacity='0.5'/><line x1='220' y1='176' x2='540' y2='176' stroke='currentColor' opacity='0.5'/><line x1='220' y1='176' x2='220' y2='214' stroke='currentColor' opacity='0.5'/><line x1='540' y1='176' x2='540' y2='214' stroke='currentColor' opacity='0.5'/><rect x='130' y='214' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='220' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>一方</text><text x='220' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>对立原则A</text><rect x='450' y='214' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='540' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>另一方</text><text x='540' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>对立原则B</text><rect x='230' y='312' width='300' height='44' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='340' text-anchor='middle' fill='var(--svg-text)' font-size='13'>对立与互补并存，不主张同源</text></svg>",
        "pending_notes": "1) 不同传统差异大，不主张同源；2) Frazer 泛化结论已标为早期学派观点；3) 比较为框架性参照，细节待核。",
        "needs_verification": True
    },
    "motif-sacrifice": {
        "level": "L2",
        "source_text": "献祭母题以牺牲建立秩序或换取恩典为核心，见于多传统的仪式与神话。Frazer《金枝》与 Harrison 的希腊宗教研究对献祭有专门讨论，本站只记录有文献依据的对照。",
        "versions": [
            "一些传统把献祭理解为与神祇交换或沟通的仪式，强调其维系宇宙秩序的功能。",
            "献祭的含义在不同传统中差异显著，从感恩、赎罪到代赎各有侧重，不宜单一化。",
            "学界对献祭起源有多种理论，无一定论，本站并列呈现有文献依据的观点。"
        ],
        "interpretations": [
            {"holder": "James George Frazer", "school": "早期比较宗教学", "view": "Frazer 把献祭与季节、丰产仪式联系起来，属早期学派观点，其泛化结论在现代学界受到修订。"},
            {"holder": "Jane Ellen Harrison", "school": "剑桥学派（神话—仪式理论）", "view": "Harrison 以仪式先行论分析希腊宗教中的献祭，强调仪式实践的核心地位，属学派研究。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《永恒回归的神话》中把献祭视为宇宙创生的重演，以此解释献祭的时间意义。"}
        ],
        
        "comparisons": [
            {"tradition": "希腊神话", "basis_source": "aca-myth-ritual-religion", "note": "Harrison 的神话—仪式理论为希腊献祭研究提供有文献依据的参照。"},
            {"tradition": "希伯来经典传统", "basis_source": "aca-golden-bough", "note": "Frazer 的《金枝》为早期学派参照，其结论已被修订，此处并列呈现，不主张同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>献祭母题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>献祭母题（仅示意，不表示同源）</text><rect x='290' y='96' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='126' text-anchor='middle' fill='var(--svg-text)' font-size='14'>献祭</text><line x1='380' y1='142' x2='380' y2='176' stroke='currentColor' opacity='0.5'/><line x1='160' y1='176' x2='600' y2='176' stroke='currentColor' opacity='0.5'/><line x1='160' y1='176' x2='160' y2='214' stroke='currentColor' opacity='0.5'/><line x1='380' y1='176' x2='380' y2='214' stroke='currentColor' opacity='0.5'/><line x1='600' y1='176' x2='600' y2='214' stroke='currentColor' opacity='0.5'/><rect x='70' y='214' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='160' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>秩序维系</text><text x='160' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>宇宙论功能</text><rect x='290' y='214' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>交换沟通</text><text x='380' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>人神关系</text><rect x='510' y='214' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='600' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>赎罪代赎</text><text x='600' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>含义之一</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>含义因传统而异，不宜单一化</text></svg>",
        "pending_notes": "1) 献祭起源理论无定论，正文并列呈现；2) Frazer 早期结论已标修订；3) 比较为学派参照，不主张同源。",
        "needs_verification": True
    },
    "motif-scapegoat": {
        "level": "L2",
        "source_text": "替罪羊母题以代罪者承担群体罪责为核心，见于多传统的仪式与经典文本。Frazer《金枝》与 Gaster 的旧约民俗研究对其有讨论，本站只记录有文献依据的对照。",
        "versions": [
            "一些传统中有把群体罪责转移至代罪者并予以放逐或牺牲的仪式，具体形态因文化而异。",
            "旧约文献中的相关仪式为学界研究对象，其历史背景与象征意义有不同解读。",
            "把不同传统的代罪仪式并置属母题层面比较，不主张同源。"
        ],
        "interpretations": [
            {"holder": "James George Frazer", "school": "早期比较宗教学", "view": "Frazer 在《金枝》中讨论代罪与季节仪式的关联，属早期学派观点，其结论在现代学界受到修订。"},
            {"holder": "Theodor H. Gaster", "school": "圣经民俗与比较宗教学", "view": "Gaster 以民俗学方法分析旧约中的相关仪式，属专门研究，不替信仰表态。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在讨论罪与净化的宗教现象时，把代罪仪式视为群体通过转移罪责以恢复宇宙秩序的一种机制，替罪羊母题即其赎罪—净化结构的一个案例。"}
        ],
        "comparisons": [
            {"tradition": "希伯来经典传统", "basis_source": "aca-myth-legend-custom", "note": "Gaster 的旧约民俗研究记录了相关仪式的分析，属有文献依据的对照，不主张信仰同源。"},
            {"tradition": "希腊神话", "basis_source": "aca-golden-bough", "note": "Frazer 的《金枝》为早期学派参照，其结论已被修订，此处并列呈现。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>替罪羊母题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>替罪羊母题（仅示意，不表示同源）</text><rect x='70' y='150' width='170' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='155' y='174' text-anchor='middle' fill='var(--svg-text)' font-size='13'>群体</text><text x='155' y='194' text-anchor='middle' fill='var(--svg-text)' font-size='12'>罪责累积</text><line x1='240' y1='180' x2='320' y2='180' stroke='currentColor' opacity='0.5'/><rect x='320' y='150' width='170' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='405' y='174' text-anchor='middle' fill='var(--svg-text)' font-size='13'>代罪者</text><text x='405' y='194' text-anchor='middle' fill='var(--svg-text)' font-size='12'>承担转移</text><line x1='490' y1='180' x2='570' y2='180' stroke='currentColor' opacity='0.5'/><rect x='570' y='150' width='140' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='640' y='174' text-anchor='middle' fill='var(--svg-text)' font-size='13'>放逐/牺牲</text><text x='640' y='194' text-anchor='middle' fill='var(--svg-text)' font-size='12'>净化</text><rect x='230' y='282' width='300' height='48' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='304' text-anchor='middle' fill='var(--svg-text)' font-size='13'>形态因文化而异，不主张同源</text><text x='380' y='356' text-anchor='middle' fill='var(--svg-text)' font-size='12'>学术描述，不替信仰表态</text></svg>",
        "pending_notes": "1) 旧约仪式的历史背景有不同解读，本站不下定论；2) Frazer 早期结论已标修订；3) 比较为母题层面参照，不主张同源。",
        "needs_verification": True
    },
    "motif-culturehero": {
        "level": "L2",
        "source_text": "文化英雄母题以为人类带来火、农耕或技艺的英雄为核心，见于多传统的神话与口传。Campbell《千面英雄》与 Harrison 的神话—仪式理论对相关主题有讨论，本站只记录有文献依据的对照。",
        "versions": [
            "一些文化英雄以盗火、驯化作物或传授技艺为核心事迹，反映人类对文明起源的解释。",
            "文化英雄常兼具神性与人性，或为半神，形态因传统而异。",
            "把不同传统的文化英雄并置属母题层面比较，不主张同源。"
        ],
        "interpretations": [
            {"holder": "Joseph Campbell", "school": "比较神话学（单一神话模型）", "view": "Campbell 在《千面英雄》中把盗火者归入英雄旅程的馈赠带回阶段，属分析模型，学界对其概括性有批评。"},
            {"holder": "Jane Ellen Harrison", "school": "剑桥学派（神话—仪式理论）", "view": "Harrison 在《希腊宗教研究导论》中把普罗米修斯等文化英雄与仪式实践相联系，属其仪式先行论的具体案例。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 认为文化英雄的技艺传授常伴随宇宙创生的重演，为文明起源神话提供现象学参照。"}
        ],
        "comparisons": [
            {"tradition": "希腊神话", "basis_source": "aca-hero-faces", "note": "Campbell 的著作把希腊英雄纳入文化英雄讨论，属有文献依据的参照，并标注模型的概括性。"},
            {"tradition": "北美原住民神话", "basis_source": "aca-religions-american-indians", "note": "Hultkrantz 的美洲原住民宗教研究为区域参照（非文化英雄母题的专门来源），属弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>文化英雄母题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>文化英雄母题（仅示意，不表示同源）</text><rect x='290' y='96' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='126' text-anchor='middle' fill='var(--svg-text)' font-size='14'>文化英雄</text><line x1='380' y1='142' x2='380' y2='176' stroke='currentColor' opacity='0.5'/><line x1='170' y1='176' x2='590' y2='176' stroke='currentColor' opacity='0.5'/><line x1='170' y1='176' x2='170' y2='214' stroke='currentColor' opacity='0.5'/><line x1='380' y1='176' x2='380' y2='214' stroke='currentColor' opacity='0.5'/><line x1='590' y1='176' x2='590' y2='214' stroke='currentColor' opacity='0.5'/><rect x='80' y='214' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>盗火</text><text x='170' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>技艺起源</text><rect x='290' y='214' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>农耕</text><text x='380' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>作物驯化</text><rect x='500' y='214' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>半神性</text><text x='590' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>神人之间</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>Campbell 模型被批评为过度概括</text></svg>",
        "pending_notes": "1) Campbell 模型的概括性争议已标注；2) 三种解读均为学派立场，细节待核；3) 比较为母题层面参照，不主张同源。",
        "needs_verification": True
    },
    "motif-moon": {
        "level": "L2",
        "source_text": "月亮母题以月亮运行与神格化为核心，见于多传统的神话与仪式。Eliade 的宗教现象学对月亮与时间、周期主题有讨论，本站只记录有文献依据的对照。",
        "versions": [
            "一些传统把月亮神格化，赋予其时间、生育或狩猎等职能，形态因文化而异。",
            "月相周期常与时间计算、节期安排相关，月亮在宇宙论中占有一席之地。",
            "把不同传统的月神并置属母题层面比较，不主张同源。"
        ],
        "interpretations": [
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《永恒回归的神话》中把月相的周期变化与仪式时间的重复相联系，为月亮母题提供现象学参照。"},
            {"holder": "James George Frazer", "school": "早期比较宗教学", "view": "Frazer 在《金枝》中讨论月亮与季节、女性仪式的关联，属早期学派观点，其结论已被现代学界修订。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "Lévi-Strauss 曾以月相论证自然范畴的二元分类如何被神话思维运用，属其结构方法的具体案例。"}
        ],
        "comparisons": [
            {"tradition": "埃及神话", "basis_source": "aca-eternal-return", "note": "Eliade 的宇宙周期框架作母题层面的参照，不主张具体神祇同源。"},
            {"tradition": "希腊神话", "basis_source": "enc-wiki-mythology", "note": "以百科条目作一般参照（该来源未在线核验，见待核实），属弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>月亮母题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>月亮母题（仅示意，不表示同源）</text><circle cx='380' cy='130' r='44' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='136' text-anchor='middle' fill='var(--svg-text)' font-size='14'>月亮</text><line x1='380' y1='174' x2='380' y2='210' stroke='currentColor' opacity='0.5'/><line x1='170' y1='210' x2='590' y2='210' stroke='currentColor' opacity='0.5'/><line x1='170' y1='210' x2='170' y2='248' stroke='currentColor' opacity='0.5'/><line x1='380' y1='210' x2='380' y2='248' stroke='currentColor' opacity='0.5'/><line x1='590' y1='210' x2='590' y2='248' stroke='currentColor' opacity='0.5'/><rect x='80' y='248' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='272' text-anchor='middle' fill='var(--svg-text)' font-size='13'>月相周期</text><text x='170' y='290' text-anchor='middle' fill='var(--svg-text)' font-size='12'>时间计算</text><rect x='290' y='248' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='272' text-anchor='middle' fill='var(--svg-text)' font-size='13'>神格化</text><text x='380' y='290' text-anchor='middle' fill='var(--svg-text)' font-size='12'>职能多样</text><rect x='500' y='248' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='272' text-anchor='middle' fill='var(--svg-text)' font-size='13'>宇宙论</text><text x='590' y='290' text-anchor='middle' fill='var(--svg-text)' font-size='12'>周期象征</text><text x='380' y='348' text-anchor='middle' fill='var(--svg-text)' font-size='13'>不同传统差异大，不主张同源</text></svg>",
        "pending_notes": "1) Frazer 早期结论已标修订；2) 希腊比较为百科弱参照，待补专门文献；3) 比较为母题层面参照，不主张同源。",
        "needs_verification": True
    },
    "motif-quest": {
        "level": "L2",
        "source_text": "探寻母题以为求得宝物、真理或救赎而远行为核心，见于多传统的叙事。Campbell《千面英雄》与《奥德赛》等史诗为研究提供材料，本站只记录有文献依据的对照。",
        "versions": [
            "探寻常以远行、试炼与归返为结构，目标可以是实物、知识或救赎。",
            "《奥德赛》常作为探寻母题的经典案例，其叙事细节与模型阶段并不逐一对应。",
            "把不同传统的探寻叙事并置属母题层面比较，不主张同源。"
        ],
        "interpretations": [
            {"holder": "Joseph Campbell", "school": "比较神话学（单一神话模型）", "view": "Campbell 以追寻与归返为英雄旅程的核心阶段，属分析模型，学界对其概括性有批评。"},
            {"holder": "Northrop Frye", "school": "文学原型批评", "view": "Frye 在文学类型与原型框架中分析追寻叙事的结构，属文学批评路径，其著作未录入 sources.json。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 把英雄抵达神圣中心的追寻解读为回归宇宙原初秩序的象征，为探寻母题提供现象学参照。"}
        ],
        "comparisons": [
            {"tradition": "希腊神话", "basis_source": "aca-hero-faces", "note": "Campbell 的著作以《奥德赛》为英雄旅程案例，属有文献依据的参照，并标注模型概括性。"},
            {"tradition": "美索不达米亚神话", "basis_source": "pri-odyssey", "note": "以《奥德赛》原典为探寻母题的文本依据，属文本层面的对照，不主张同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>探寻母题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>探寻母题（示意）</text><rect x='60' y='180' width='150' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='135' y='204' text-anchor='middle' fill='var(--svg-text)' font-size='13'>出发</text><text x='135' y='222' text-anchor='middle' fill='var(--svg-text)' font-size='12'>动机·召唤</text><line x1='210' y1='207' x2='245' y2='207' stroke='currentColor' opacity='0.5'/><rect x='245' y='180' width='150' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='320' y='204' text-anchor='middle' fill='var(--svg-text)' font-size='13'>试炼</text><text x='320' y='222' text-anchor='middle' fill='var(--svg-text)' font-size='12'>远行·考验</text><line x1='395' y1='207' x2='430' y2='207' stroke='currentColor' opacity='0.5'/><rect x='430' y='180' width='150' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='505' y='204' text-anchor='middle' fill='var(--svg-text)' font-size='13'>获得</text><text x='505' y='222' text-anchor='middle' fill='var(--svg-text)' font-size='12'>宝物·真理</text><line x1='580' y1='207' x2='615' y2='207' stroke='currentColor' opacity='0.5'/><rect x='615' y='180' width='100' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='665' y='204' text-anchor='middle' fill='var(--svg-text)' font-size='13'>归返</text><text x='665' y='222' text-anchor='middle' fill='var(--svg-text)' font-size='12'>回馈</text><rect x='230' y='292' width='300' height='46' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>模型为分析框架，非逐一对应</text></svg>",
        "pending_notes": "1) Campbell 模型概括性争议已标注；2) Frye 著作未录入 sources.json，已声明；3) 比较为母题参照，不主张同源。",
        "needs_verification": True
    },
    "fig-hera": {
        "level": "L2",
        "sources_extra": ["pri-odyssey"],
        "source_text": "赫拉是希腊神话的婚姻女神，宙斯之妻，在《神谱》《伊利亚特》与《奥德赛》中均有出现，其形象与奥林匹斯神系和婚姻制度相关。不同文献与地方崇拜中的形象并不完全一致。",
        "versions": [
            "《神谱》把赫拉列入宙斯的配偶与奥林匹斯神系，侧重谱系位置。",
            "荷马史诗中赫拉积极参与神界与人间事务，其权威与宙斯及其他神祇的关系呈现复杂互动。",
            "地方崇拜中的赫拉有不同称号与职能，与泛希腊版本并存。"
        ],
        "interpretations": [
            {"holder": "Jean-Pierre Vernant", "school": "巴黎学派（古希腊神话与思想）", "view": "Vernant 在《希腊神话与思想》中把赫拉作为婚姻与合法配偶秩序的神格来讨论，强调其与城邦家庭结构的关联。"},
            {"holder": "Walter Burkert", "school": "宗教史/古典学", "view": "Burkert 在《希腊宗教》中考察赫拉在阿尔戈斯、萨摩斯等地的祭祀，指出其形象与各地仪式传统密切相关。"},
            {"holder": "Jane Ellen Harrison", "school": "剑桥学派（神话—仪式理论）", "view": "在《希腊宗教研究导论》中，Harrison 以赫拉的婚姻神话为案例，论证仪式实践在神话形成中的优先地位。"}
        ],
        "comparisons": [
            {"tradition": "罗马神话", "basis_source": "pri-virgil-aeneid", "note": "以罗马文学为依据记录赫拉与朱诺的传统对应，属文本层面参照，不主张简单复制。"},
            {"tradition": "迈锡尼宗教", "basis_source": "aca-greek-religion", "note": "Burkert 的希腊宗教研究涉及青铜时代至古典时期的连续性，作背景参照；具体对应关系待专门文献核对。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>赫拉形象来源示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>赫拉形象的主要文献来源</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>赫拉</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>神谱</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>谱系位置</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>荷马史诗</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>神界互动</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>地方崇拜</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>不同称号</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>不同文献中的形象并不完全一致</text></svg>",
        "pending_notes": "1) 地方崇拜材料零散，具体差异待核；2) 三位学者论点为概括，细节待逐条核对；3) 比较为文献层面参照，不主张同源。",
        "needs_verification": True
    },
    "fig-athena": {
        "level": "L2",
        "source_text": "雅典娜是希腊神话的智慧与战争女神，在《伊利亚特》《奥德赛》中频繁出现，与雅典的城邦崇拜密切相关。不同文献与地方传统中的形象有差异。",
        "versions": [
            "荷马史诗中雅典娜以智谋与战争辅助者的形象出现，多次介入英雄事务。",
            "雅典的城邦崇拜把雅典娜作为守护神，其神话与城邦身份建构相关。",
            "地方传说中关于雅典娜的出身与职能有不同版本，与泛希腊叙述并存。"
        ],
        "interpretations": [
            {"holder": "Jean-Pierre Vernant", "school": "巴黎学派（古希腊神话与思想）", "view": "Vernant 分析雅典娜兼具战争与工艺智慧的形象，指出其在城邦政治与工匠技艺之间的中介地位。"},
            {"holder": "Walter Burkert", "school": "宗教史/古典学", "view": "Burkert 在《希腊宗教》中考察雅典娜在雅典卫城与泛希腊祭祀中的地位，强调其崇拜的地域特征。"},
            {"holder": "Jane Ellen Harrison", "school": "剑桥学派（神话—仪式理论）", "view": "Harrison 把雅典娜的出身神话与仪式实践相联系，作为其神话—仪式理论的案例之一。"}
        ],
        "comparisons": [
            {"tradition": "罗马神话", "basis_source": "pri-virgil-aeneid", "note": "以罗马文学为依据记录雅典娜与密涅瓦的传统对应，属文本层面参照，不主张简单复制。"},
            {"tradition": "埃及神话", "basis_source": "aca-greek-religion", "note": "Burkert 的希腊宗教研究为近东影响的一般参照，不主张具体神祇同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>雅典娜形象来源示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>雅典娜形象的主要文献来源</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>雅典娜</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>伊利亚特</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>战争辅助</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>奥德赛</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>智谋引导</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>城邦崇拜</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>雅典守护</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>地方版本与泛希腊叙述并存</text></svg>",
        "pending_notes": "1) 地方传说版本差异待核；2) 三位学者论点为概括，细节待逐条核对；3) 比较为文献层面参照，不主张同源。",
        "needs_verification": True
    },
    "fig-apollo": {
        "level": "L2",
        "source_text": "阿波罗是希腊神话的太阳、音乐、预言与医药之神，在《荷马颂歌》与《伊利亚特》中均有重要篇幅，德尔斐神谕与其崇拜密切相关。不同文献与地方传说中的职能侧重有差异。",
        "versions": [
            "《伊利亚特》中阿波罗以射神与瘟疫、治愈的双重形象出现，参与特洛伊战争的诸神纷争。",
            "《荷马颂歌》中的阿波罗颂歌叙述其出生、建立德尔斐神谕所的事迹，侧重其预言与音乐职能。",
            "古典时期阿波罗与太阳神赫利俄斯的职能逐渐融合，地方崇拜中的形象并不统一。"
        ],
        "interpretations": [
            {"holder": "Walter Burkert", "school": "宗教史/古典学", "view": "Burkert 在《希腊宗教》中考察阿波罗的近东渊源与德尔斐神谕的仪式实践，指出其形象融合了多种文化元素。"},
            {"holder": "Jean-Pierre Vernant", "school": "巴黎学派（古希腊神话与思想）", "view": "Vernant 在《希腊神话与思想》中分析阿波罗的神谕与城邦公共生活的关系，把预言置于理性化决策的历史语境中考察。"},
            {"holder": "Jane Ellen Harrison", "school": "剑桥学派（神话—仪式理论）", "view": "Harrison 在《希腊宗教研究导论》中把德尔斐的崇拜仪式与阿波罗神话的形成相联系。"}
        ],
        "comparisons": [
            {"tradition": "埃及神话", "basis_source": "aca-greek-religion", "note": "Burkert 的希腊宗教研究涉及阿波罗形象的近东背景，作一般参照；具体传播路径待专门文献核对。"},
            {"tradition": "罗马神话", "basis_source": "pri-virgil-aeneid", "note": "以罗马文学为依据记录阿波罗与同名罗马神祇的对应，属文本层面参照，不主张简单复制。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>阿波罗职能示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>阿波罗的主要职能（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>阿波罗</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='150' y1='174' x2='610' y2='174' stroke='currentColor' opacity='0.5'/><line x1='150' y1='174' x2='150' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='610' y1='174' x2='610' y2='212' stroke='currentColor' opacity='0.5'/><rect x='70' y='212' width='160' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='150' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>预言</text><text x='150' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>德尔斐神谕</text><rect x='300' y='212' width='160' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>音乐</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>里拉琴</text><rect x='530' y='212' width='160' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='610' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>射神</text><text x='610' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>瘟疫·治愈</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>职能在古典时期逐渐融合</text></svg>",
        "pending_notes": "1) 近东渊源与职能融合的具体年代待考；2) 三位学者论点以其代表著作为概括，细节待核对；3) 比较为文献层面参照，不主张同源。",
        "needs_verification": True
    },
    "fig-hades": {
        "level": "L2",
        "source_text": "哈迪斯是希腊神话的冥界之神，在《神谱》与荷马史诗中出现，其名亦指冥界本身。关于冥界的观念在不同时期与地点有差异，本站只记录有文献依据的对照。",
        "versions": [
            "《神谱》把哈迪斯列为克洛诺斯之子，与宙斯、波塞冬分掌冥界、天空与海洋。",
            "荷马史诗中的冥界是亡者居所，英雄的冥界旅行（如《奥德赛》中的叙事）构成重要母题。",
            "厄琉息斯秘仪与冥界神话的关系为学界研究议题，具体教义因秘仪性质而材料有限。"
        ],
        "interpretations": [
            {"holder": "Jean-Pierre Vernant", "school": "巴黎学派（古希腊神话与思想）", "view": "Vernant 在《希腊神话与思想》中把哈迪斯与献祭、城邦秩序的图像体系联系起来，分析冥界的象征位置。"},
            {"holder": "Walter Burkert", "school": "宗教史/古典学", "view": "Burkert 在《希腊宗教》中考察冥界崇拜与厄琉息斯秘仪的仪式证据，强调材料的局限性。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《永恒回归的神话》中把冥界旅行解读为通过仪式的象征，亡者穿越冥界即对应从生到死、再至重生的过渡结构，哈迪斯所辖的冥界正是这一过渡的空间。"}
        ],
        "comparisons": [
            {"tradition": "埃及神话", "basis_source": "pri-book-dead", "note": "以《亡灵书》原典为冥界观念的文本依据，与希腊冥界作母题层面的对照，不主张同源。"},
            {"tradition": "美索不达米亚神话", "basis_source": "aca-before-philosophy", "note": "Frankfort 的近东思想研究作一般框架参照，具体对应待专门文献核对。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>哈迪斯与三界分掌示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>克洛诺斯之子分掌三界（示意）</text><rect x='290' y='88' width='180' height='44' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='116' text-anchor='middle' fill='var(--svg-text)' font-size='14'>克洛诺斯</text><line x1='380' y1='132' x2='380' y2='164' stroke='currentColor' opacity='0.5'/><line x1='160' y1='164' x2='600' y2='164' stroke='currentColor' opacity='0.5'/><line x1='160' y1='164' x2='160' y2='202' stroke='currentColor' opacity='0.5'/><line x1='380' y1='164' x2='380' y2='202' stroke='currentColor' opacity='0.5'/><line x1='600' y1='164' x2='600' y2='202' stroke='currentColor' opacity='0.5'/><rect x='80' y='202' width='160' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='160' y='226' text-anchor='middle' fill='var(--svg-text)' font-size='13'>哈迪斯</text><text x='160' y='244' text-anchor='middle' fill='var(--svg-text)' font-size='12'>冥界</text><rect x='300' y='202' width='160' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='226' text-anchor='middle' fill='var(--svg-text)' font-size='13'>宙斯</text><text x='380' y='244' text-anchor='middle' fill='var(--svg-text)' font-size='12'>天空</text><rect x='520' y='202' width='160' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='600' y='226' text-anchor='middle' fill='var(--svg-text)' font-size='13'>波塞冬</text><text x='600' y='244' text-anchor='middle' fill='var(--svg-text)' font-size='12'>海洋</text><rect x='230' y='304' width='300' height='46' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='332' text-anchor='middle' fill='var(--svg-text)' font-size='13'>冥界观念因时期地点而异</text></svg>",
        "pending_notes": "1) 厄琉息斯秘仪材料有限，具体教义不下定论；2) 三位学者论点以其著作为概括，细节待核对；3) 比较为母题层面参照，不主张同源。",
        "needs_verification": True
    },
    "fig-thor": {
        "level": "L2",
        "source_text": "托尔是北欧神话的雷神，以力量与守护著称，主要见于《诗体埃达》与《散文埃达》，其锤子与巨蛇的战斗是核心母题。现存文本多经中世纪记录。",
        "versions": [
            "《诗体埃达》的诗歌中托尔以降服巨人的雷神形象出现，力量与守护职能突出。",
            "《散文埃达》把托尔系统化地置于神谱中，并加入历史化解释框架。",
            "地方传说中托尔的名称与职能留下痕迹，与正典材料形成对照。"
        ],
        "interpretations": [
            {"holder": "Georges Dumézil", "school": "印欧比较神话学", "view": "Dumézil 在《印欧人的神》中把托尔归为三功能中的战争功能，与奥丁、弗雷构成结构对应。"},
            {"holder": "John Lindow", "school": "北欧神话与民俗研究", "view": "Lindow 在《北欧神话》中强调托尔材料的中世纪文本语境，区分诗歌证据与斯诺里的系统化叙述，该著作未录入 sources.json。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《永恒回归的神话》中把托尔制服巨蛇的战斗解读为秩序制服混沌的宇宙母题，属其宇宙斗争论的具体案例。"},
        ],
        "comparisons": [
            {"tradition": "印度神话", "basis_source": "aca-gods-indo-europeans", "note": "Dumézil 的三功能模型把托尔与因陀罗作战争功能对照，属学派框架，不主张同源。"},
            {"tradition": "希腊神话", "basis_source": "aca-comparative-myth", "note": "比较神话学在印欧框架内作功能层面的一般参照，具体对应有讨论。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>托尔核心母题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>托尔核心母题（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>托尔</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>雷与力量</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>战争功能</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>妙尔尼尔</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>雷神之锤</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>巨蛇之战</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>混沌制服</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>现存材料多经中世纪记录</text></svg>",
        "pending_notes": "1) Lindow 著作未录入 sources.json，已声明；2) 雷神之锤等细节待逐条核对原典；3) 三功能模型为学派框架，不替读者下结论。",
        "needs_verification": True
    },
    "fig-loki": {
        "level": "L2",
        "source_text": "洛基是北欧神话中的诡计与变形之神，在《诗体埃达》与《散文埃达》中扮演复杂角色，既协助诸神又制造祸端，并与诸神黄昏相关。其形象在诗歌与散文材料中有差异。",
        "versions": [
            "《诗体埃达》中洛基以机智与变形能力介入诸神事务，形象兼具助益与破坏两面。",
            "《散文埃达》把洛基系统地纳入神谱叙事，并记载其与诸神黄昏的关联。",
            "关于洛基与女性神祇关系及变身为雌性的叙事，学界对其成文年代与解读有讨论。"
        ],
        "interpretations": [
            {"holder": "John Lindow", "school": "北欧神话与民俗研究", "view": "Lindow 在《北欧神话》中指出洛基的复杂性来自诗歌材料的多元传统，反对将其简化为单一反派，著作未录入 sources.json。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "Lévi-Strauss 在《结构人类学》中把诡计者视为神话思维的中介性角色，为分析洛基的越界行为提供具体案例。"},
            {"holder": "Georges Dumézil", "school": "印欧比较神话学", "view": "Dumézil 在《印欧人的神》的印欧框架内讨论洛基与相关诡计者形象，属学派比较，具体对应有讨论。"}
        ],
        "comparisons": [
            {"tradition": "希腊神话", "basis_source": "aca-comparative-myth", "note": "比较神话学在印欧框架内讨论诡计者形象，属一般参照，不主张同源。"},
            {"tradition": "北美原住民神话", "basis_source": "aca-religions-american-indians", "note": "Hultkrantz 的区域研究为诡计者母题提供跨区域参照，属弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>洛基形象面向示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>洛基形象的主要面向（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>洛基</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>诡计</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>机智·欺骗</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>变形</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>形态转换</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>末日关联</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>诸神黄昏</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>诗歌与散文材料中的形象有差异</text></svg>",
        "pending_notes": "1) Lindow 著作未录入 sources.json，已声明；2) 洛基性别变形叙事的年代与解读有争论，不下定论；3) 诡计者比较为学派框架，不主张同源。",
        "needs_verification": True
    },
    "fig-osiris": {
        "level": "L2",
        "source_text": "奥西里斯是埃及神话的冥界与复活之神，其核心叙事见于《亡灵书》与相关铭文，与伊西斯、塞特的神话及王权、死后审判观念相关。不同时期的传统并不统一。",
        "versions": [
            "奥西里斯被塞特杀害、由伊西斯复原的叙事，是古埃及死后重生观念的重要文本。",
            "赫利奥波利斯的神谱把奥西里斯置于九柱神体系，与王权继承的观念相连。",
            "奥西里斯与阿皮斯牛等崇拜形态在不同时期演变，具体对应关系为学界议题。"
        ],
        "interpretations": [
            {"holder": "James George Frazer", "school": "早期比较宗教学", "view": "Frazer 在《金枝》中把奥西里斯与地中海死而复生神祇并置，属早期学派观点，其结论在现代学界受到修订。"},
            {"holder": "Henri Frankfort", "school": "古代近东思想研究", "view": "Frankfort 在《哲学之前》中以神话意象分析埃及的王权与死后世界观，强调不以现代抽象标准误读。"},
            {"holder": "James P. Allen", "school": "埃及学（宗教文本研究）", "view": "Allen 在《埃及宗教思想》中强调创世与冥界传统的多元并存，反对把各地表述简化为单一体系；该著作未录入 sources.json。"}
        ],
        "comparisons": [
            {"tradition": "希腊神话", "basis_source": "aca-golden-bough", "note": "Frazer 的《金枝》为早期学派参照，其结论已被现代学界修订，此处并列呈现，不主张同源。"},
            {"tradition": "美索不达米亚神话", "basis_source": "aca-before-philosophy", "note": "Frankfort 的近东思想研究作一般框架参照，具体对应待专门文献核对。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>奥西里斯神话母题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>奥西里斯神话母题（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>奥西里斯</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>死亡与复原</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>伊西斯寻夫</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>冥界审判</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>亡灵书</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>王权</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>九柱神体系</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>不同时期传统并不统一</text></svg>",
        "pending_notes": "1) Allen 著作未录入 sources.json，已声明；2) Frazer 早期结论已标修订；3) 与阿皮斯牛崇拜的对应为学界议题，不下定论。",
        "needs_verification": True
    },
    "fig-anubis": {
        "level": "L2",
        "source_text": "阿努比斯是埃及神话中胡狼头的冥界引路神，与木乃伊制作、亡灵引导和《亡灵书》中的审判仪式相关。其形象与职能在不同时期有演变，本站只记录有文献依据的对照。",
        "versions": [
            "古王国金字塔文中阿努比斯与丧葬仪式相关，负责引导亡者并参与木乃伊化的象征。",
            "《亡灵书》中的心脏称量仪式里阿努比斯担任天平看守，与奥西里斯的审判职能配合。",
            "希腊罗马时期阿努比斯形象与赫尔墨斯结合为赫尔墨斯—阿努比斯，反映文化接触。"
        ],
        "interpretations": [
            {"holder": "James P. Allen", "school": "埃及学（宗教文本研究）", "view": "Allen 在《埃及宗教思想》中分析阿努比斯在丧葬仪式中的引导角色，指出其职能与亡者转化的观念相连，该著作未录入 sources.json。"},
            {"holder": "Henri Frankfort", "school": "古代近东思想研究", "view": "Frankfort 在《哲学之前》中以神话意象解释埃及的冥界观，把阿努比斯视为亡者过渡仪式的神格化。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《永恒回归的神话》中把冥界引导解读为通过仪式的象征，阿努比斯的引路职能即对应亡者从生到死的过渡阶段。"}
        ],
        "comparisons": [
            {"tradition": "希腊神话", "basis_source": "aca-before-philosophy", "note": "Frankfort 的近东—希腊思想比较为一般框架参照，不主张具体神祇同源。"},
            {"tradition": "苏美尔神话", "basis_source": "ins-british-museum", "note": "以机构藏品资料作近东冥界观的一般参照（该机构页未在线核验），属弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>阿努比斯职能示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>阿努比斯职能（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>阿努比斯</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>亡灵引导</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>冥界引路</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>木乃伊化</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>丧葬仪式</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>审判天平</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>亡灵书</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>形象与职能随时期演变</text></svg>",
        "pending_notes": "1) Allen 著作未录入 sources.json，已声明；2) 希腊罗马时期融合形象的具体年代待考；3) 比较为框架/弱参照，不主张同源。",
        "needs_verification": True
    },
    "fig-gilgamesh": {
        "level": "L2",
        "source_text": "吉尔伽美什是美索不达米亚史诗中的乌鲁克王，其故事见于苏美尔早期诗篇与巴比伦标准版《吉尔伽美什史诗》，包含友谊、洪水和生死探寻等母题。多个版本并存且文本有残缺。",
        "versions": [
            "苏美尔早期诗篇与巴比伦十二泥板标准版在情节与主题上有差异，后者经系统编纂。",
            "洪水叙事在史诗中与《阿特拉哈西斯》有情节对应，二者关系为学界研究议题。",
            "寻求永生而不得的结局在不同版本中细节有别，文本部分残缺。"
        ],
        "interpretations": [
            {"holder": "Thorkild Jacobsen", "school": "美索不达米亚宗教史", "view": "Jacobsen 在《黑暗中的珍宝》中把吉尔伽美什的探寻解读为对王权与死亡界限的反思，强调史诗与城邦秩序的关联。"},
            {"holder": "Samuel Noah Kramer", "school": "苏美尔学", "view": "Kramer 在《苏美尔神话》中通过泥板整理指出苏美尔吉尔伽美什诗篇与巴比伦版本的承继关系。"},
            {"holder": "Joseph Campbell", "school": "比较神话学（单一神话模型）", "view": "Campbell 在《千面英雄》中把吉尔伽美什纳入英雄旅程的讨论，属分析模型，其概括性在学界有批评。"}
        ],
        "comparisons": [
            {"tradition": "希腊神话", "basis_source": "aca-hero-faces", "note": "Campbell 的著作为英雄旅程框架参照，标注模型的概括性，不主张同源。"},
            {"tradition": "希伯来经典传统", "basis_source": "aca-myth-legend-custom", "note": "Gaster 的旧约民俗研究为洪水母题比较提供文献依据，不主张信仰同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>吉尔伽美什史诗母题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>吉尔伽美什史诗母题（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>吉尔伽美什</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='150' y1='174' x2='610' y2='174' stroke='currentColor' opacity='0.5'/><line x1='150' y1='174' x2='150' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='610' y1='174' x2='610' y2='212' stroke='currentColor' opacity='0.5'/><rect x='70' y='212' width='160' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='150' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>乌鲁克王</text><text x='150' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>城邦秩序</text><rect x='300' y='212' width='160' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>洪水叙事</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>与阿特拉哈西斯</text><rect x='530' y='212' width='160' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='610' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>永生探寻</text><text x='610' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>而不得</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>多版本并存，文本部分残缺</text></svg>",
        "pending_notes": "1) 洪水两版本关系与先后学界有讨论；2) 文本残缺，具体年代未列；3) Campbell 模型概括性已标注，不主张同源。",
        "needs_verification": True
    },
    "fig-inanna": {
        "level": "L2",
        "source_text": "伊南娜是苏美尔神话的爱与战争女神，其崇拜与乌鲁克城密切关联，神话材料包括神庙颂歌与《伊南娜下冥界》等文本。其形象与权力、丰产主题相连，解读依赖泥板整理。",
        "versions": [
            "苏美尔神庙颂歌把伊南娜与乌鲁克王权、丰产仪式相联系，突出其城邦守护职能。",
            "《伊南娜下冥界》叙述女神的冥界之旅与复返，是理解其神格的重要文本。",
            "后来阿卡德传统中的伊什塔尔与苏美尔伊南娜存在承继关系，但具体演变有讨论。"
        ],
        "interpretations": [
            {"holder": "Samuel Noah Kramer", "school": "苏美尔学", "view": "Kramer 在《苏美尔神话》中通过泥板翻译重建伊南娜的神话谱系，指出其形象与乌鲁克城邦的关联。"},
            {"holder": "Thorkild Jacobsen", "school": "美索不达米亚宗教史", "view": "Jacobsen 在《黑暗中的珍宝》中分析伊南娜兼具爱与战争职能的张力，把其神话与城邦权力结构相联系。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《永恒回归的神话》中把伊南娜的下冥界与复返解读为死而复生母题的典型案例，女神往返冥界对应宇宙周期的象征重演。"}
        ],
        "comparisons": [
            {"tradition": "埃及神话", "basis_source": "aca-before-philosophy", "note": "Frankfort 的近东思想比较为一般框架参照，不主张具体女神同源。"},
            {"tradition": "希腊神话", "basis_source": "aca-golden-bough", "note": "Frazer 的《金枝》为早期学派参照，其结论已被现代学界修订，此处并列呈现。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>伊南娜神格面向示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>伊南娜神格面向（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>伊南娜</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>爱与丰产</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>神庙颂歌</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>战争</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>权力张力</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>下冥界</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>死而复返</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>与阿卡德伊什塔尔的关系有讨论</text></svg>",
        "pending_notes": "1) 与伊什塔尔的承继关系学界有讨论；2) Kramer/Jacobsen 论点以其著作为概括，细节待核对；3) Frazer 早期结论已标修订，不主张同源。",
        "needs_verification": True
    },
    "fig-fuxi": {
        "level": "L2",
        "source_text": "伏羲是中国神话中的人文始祖，与画八卦、教民渔猎等传说相关，其形象见于《易经》相关传统与后世文献，并与女娲并称。相关传说的早期形态与文献年代为学界讨论议题。",
        "versions": [
            "《易经》的符号体系在传统文化中被归因于伏羲画卦，此为文化起源叙事的一部分。",
            "后世文献把伏羲与女娲并称，赋予其教民渔猎、制嫁娶等文明开创职能。",
            "画像石与文献中的伏羲—女娲交尾形象反映后世信仰，其确切年代与含义待核实。"
        ],
        "interpretations": [
            {"holder": "袁珂", "school": "中国神话学（神话整理与研究）", "view": "袁珂在《中国古代神话》中辑录散见文献，把伏羲列为中国创世与人文始祖神话的核心人物；该著作未录入 sources.json。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "Lévi-Strauss 在《结构人类学》中的神话分析方法，可为解读伏羲神话中的分类与对立提供方法论参照。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《永恒回归的神话》中把文化英雄开创文明的功业视为宇宙创生原型的地上重演，伏羲画卦、教民诸事即属此类原型重演的叙事。"}
        ],
        "comparisons": [
            {"tradition": "希腊神话", "basis_source": "aca-short-history-myth", "note": "Armstrong 的神话通论为文化英雄母题的一般参照，属弱参照，具体文本关联待专门文献核对。"},
            {"tradition": "印度神话", "basis_source": "aca-comparative-myth", "note": "比较神话学通论为跨文化母题参照，不主张同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>伏羲传说母题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>伏羲传说母题（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>伏羲</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>画八卦</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>符号体系</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>渔猎嫁娶</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>文明开创</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>女娲并称</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>始祖神话</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>早期形态与文献年代待核实</text></svg>",
        "pending_notes": "1) 伏羲传说早期形态与文献年代待核实；2) 袁珂著作未录入 sources.json，已声明；3) 比较为框架/弱参照，不主张同源。",
        "needs_verification": True
    },
    "fig-sun-wukong": {
        "level": "L2",
        "source_text": "孙悟空是明代神魔小说《西游记》中的神猴形象，由小说塑造而成，兼具神通与修行主题。其形象与民间传说、佛教与道教元素相关，本站以文学与宗教文化角度描述。",
        "versions": [
            "《西游记》中的孙悟空由石而生，学艺、大闹天宫后护送唐僧取经，是小说塑造的文学形象。",
            "孙悟空的形象融合了民间猴神传说与宗教修行主题，具体源流为学界研究议题。",
            "后世戏曲、民间信仰中的孙悟空形象与小说文本有差异，反映形象的流传演变。"
        ],
        "interpretations": [
            {"holder": "鲁迅", "school": "中国小说史研究", "view": "鲁迅在《中国小说史略》中提出孙悟空的形象可能源于唐人传奇中的淮河水神无支祁，属中国本土源流说；该著作未录入 sources.json。"},
            {"holder": "胡适", "school": "中国章回小说考证", "view": "胡适在《中国章回小说考证》中主张孙悟空形象可能受印度史诗《罗摩衍那》中神猴哈奴曼的影响，属外来说；该著作未录入 sources.json。"},
            {"holder": "Joseph Campbell", "school": "比较神话学（单一神话模型）", "view": "Campbell 在《千面英雄》中提出的英雄旅程模型可用于分析取经叙事的结构，属分析框架，其概括性在学界有批评。"}
        ],
        "comparisons": [
            {"tradition": "印度神话", "basis_source": "aca-short-history-myth", "note": "Armstrong 的神话通论仅为神话演变的背景线索（该书为通俗概述）；孙悟空是否受印度哈奴曼影响属鲁迅、胡适以来未决的学界争论，此处并列两说不下结论，非实证依据。"},
            {"tradition": "希腊神话", "basis_source": "aca-hero-faces", "note": "Campbell 的英雄旅程框架为叙事结构参照，标注模型概括性，不主张同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>孙悟空形象结构示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>孙悟空形象结构（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>孙悟空</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='150' y1='174' x2='610' y2='174' stroke='currentColor' opacity='0.5'/><line x1='150' y1='174' x2='150' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='610' y1='174' x2='610' y2='212' stroke='currentColor' opacity='0.5'/><rect x='70' y='212' width='160' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='150' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>石生神猴</text><text x='150' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>文学形象</text><rect x='300' y='212' width='160' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>大闹天宫</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>神通</text><rect x='530' y='212' width='160' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='610' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>取经修行</text><text x='610' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>转化主题</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>形象源流为学界研究议题</text></svg>",
        "pending_notes": "1) 孙悟空形象源流（无支祁说/哈奴曼说）为鲁迅、胡适以来未决的学界争论，正文并列不下定论；2) 鲁迅、胡适、Campbell 的著作未录入 sources.json，其论点作为学界代表列举；3) 比较不主张同源。",
        "needs_verification": True
    },
    "myth-armenian": {
        "level": "L2",
        "source_text": "亚美尼亚神话的材料主要经前基督教时期的口传、古典作者记载及后世文献保存，核心涉及太阳神、雷神与英雄传说。由于基督教化较早，本土神话多经间接记录，重建依赖比较与考据，本站如实标注。",
        "versions": [
            "亚美尼亚前基督教神祇（如太阳神与雷神）的职能见于古典记载与后世整理，原貌多经基督教化改写。",
            "英雄史诗与民族起源传说与历史记忆交织，具体年代与史实性为学界讨论议题。",
            "亚美尼亚神话与邻近伊朗、高加索传统有可比母题，具体关系为比较研究议题。"
        ],
        "interpretations": [
            {"holder": "Jaan Puhvel", "school": "印欧比较神话学", "view": "Puhvel 在《比较神话学》中把亚美尼亚语材料纳入印欧比较框架，指出其雷神与太阳神母题与伊朗、斯拉夫材料的可比性，属学派比较。"},
            {"holder": "Georges Dumézil", "school": "印欧比较神话学", "view": "Dumézil 在《印欧人的神》中以三功能假说讨论亚美尼亚材料在印欧神系中的位置，具体对应关系学界有讨论。"},
            {"holder": "James R. Russell", "school": "亚美尼亚研究", "view": "Russell 在《Zoroastrianism in Armenia》中主张亚美尼亚神话须置于伊朗—高加索的文化接触语境中理解，该著作未录入 sources.json。"}
        ],
        "comparisons": [
            {"tradition": "波斯神话", "basis_source": "aca-comparative-myth", "note": "Puhvel 的印欧比较把亚美尼亚与伊朗材料并置，属学派框架，不主张直接同源。"},
            {"tradition": "希腊神话", "basis_source": "aca-gods-indo-europeans", "note": "Dumézil 的印欧框架作一般参照，具体对应有讨论，不主张同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>亚美尼亚神话材料示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>亚美尼亚神话材料（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>亚美尼亚神话</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>太阳神</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>古典记载</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>雷神</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>与伊朗可比</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>英雄传说</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>民族起源</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>基督教化较早，多经间接记录</text></svg>",
        "pending_notes": "1) 前基督教神话多经间接记录，原貌难以完整重建；2) Russell 著作未录入 sources.json，已声明；3) 印欧比较为学派框架，不主张直接同源。",
        "needs_verification": True
    },
    "motif-skyfather": {
        "level": "L2",
        "source_text": "天父母题以天空的人格化为至高父神为核心，在印欧比较神话学中被系统讨论。Dumézil 与 Puhvel 的著作对该母题在印欧诸传统中的位置有专门分析，本站只记录有文献依据的对照。",
        "versions": [
            "印欧诸传统中常见以天空或雷霆之神为至高者的形象，其名称与职能同源关系为比较研究议题。",
            "天父的职能在主权、战争与丰产维度上的分配因传统而异，不宜单一化。",
            "把不同传统的至高天空神并置属母题层面比较，不主张具体文本同源。"
        ],
        "interpretations": [
            {"holder": "Georges Dumézil", "school": "印欧比较神话学", "view": "Dumézil 在《印欧人的神》中把天父型神祇归入主权功能，论证其在印欧神系结构中的位置，属三功能模型的主权功能代表案例。"},
            {"holder": "Jaan Puhvel", "school": "印欧比较神话学", "view": "Puhvel 在《比较神话学》中通过词源与功能比较，论证印欧天父神（如 *Dyēus）在各传统的对应关系，属语文学比较。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《比较宗教的模式》中把天空神与神圣超越性相联系，指出天父形象常退居而让位于更贴近人间的神祇。"}
        ],
        "comparisons": [
            {"tradition": "希腊神话", "basis_source": "aca-gods-indo-europeans", "note": "Dumézil 的印欧比较把宙斯型天父神纳入主权功能框架，属学派比较，不主张直接同源。"},
            {"tradition": "北欧神话", "basis_source": "aca-comparative-myth", "note": "Puhvel 的印欧框架作天父母题的一般参照，具体对应有讨论。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>天父母题跨印欧传统示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>天父母题（仅示意，不表示同源）</text><rect x='290' y='96' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='126' text-anchor='middle' fill='var(--svg-text)' font-size='14'>天父</text><line x1='380' y1='142' x2='380' y2='176' stroke='currentColor' opacity='0.5'/><line x1='170' y1='176' x2='590' y2='176' stroke='currentColor' opacity='0.5'/><line x1='170' y1='176' x2='170' y2='214' stroke='currentColor' opacity='0.5'/><line x1='380' y1='176' x2='380' y2='214' stroke='currentColor' opacity='0.5'/><line x1='590' y1='176' x2='590' y2='214' stroke='currentColor' opacity='0.5'/><rect x='80' y='214' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>主权功能</text><text x='170' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>三功能之一</text><rect x='290' y='214' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>天空/雷霆</text><text x='380' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>超越性</text><rect x='500' y='214' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='238' text-anchor='middle' fill='var(--svg-text)' font-size='13'>退居现象</text><text x='590' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>让位人间神</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>三功能模型为学派框架，不主张同源</text></svg>",
        "pending_notes": "1) 印欧天父神的词源对应为语文学研究议题，具体结论有争论；2) Dumézil 三功能模型学界有批评；3) 比较为学派框架，不主张直接同源。",
        "needs_verification": True
    },
    "myth-dravidian": {
        "level": "L2",
        "source_text": "达罗毗荼神话指南印度泰米尔语地区的本土神祇与史诗传统，主要见于泰米尔桑加姆文学、史诗与地方往世书，与北印度的吠陀—往世书传统既有交融又有自身特色。材料以泰米尔语文本为核心，本文只记录有文献依据的对照。",
        "versions": [
            "泰米尔桑加姆诗歌中的穆鲁甘等神祇带有本土山地与战争色彩，与后来的往世书系统化叙述侧重不同。",
            "南印度神庙传统把地方神祇与梵语往世书的神谱相调和，形成兼具地方性与普世性的形态。",
            "达罗毗荼诸神与北印度吠陀神系的关系为学界研究议题，二者长期并存交融。"
        ],
        "interpretations": [
            {"holder": "George L. Hart", "school": "泰米尔文学与南亚宗教研究", "view": "Hart 在《The Poems of Ancient Tamil》中论证古代泰米尔诗歌有其独立的宗教与审美传统，穆鲁甘等神祇带有本土根源，不能简单视作吠陀神系的派生；该著作未录入 sources.json。"},
            {"holder": "Wendy Doniger", "school": "芝加哥学派（印度宗教与文本研究）", "view": "Doniger 在《The Implied Spider》中主张印度宗教的多样性，认为南印度本土神祇与北印度传统的关系应在具体的地区史与文本史中理解，而非套用单一框架。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《比较宗教的模式》中关于神圣空间与节期的论述，可说明泰米尔神庙如何把地方性空间转化为神圣中心，此为理论参照而非专门结论。"}
        ],
        "comparisons": [
            {"tradition": "印度教（吠陀传统）", "basis_source": "pri-rigveda", "note": "以《梨俱吠陀》原典为北印度传统的文本依据，与达罗毗荼诸神作母题层面的对照，不主张同源或派生。"},
            {"tradition": "印度教（往世书）", "basis_source": "enc-brit-hinduism", "note": "以权威百科条目作往世书传统的背景参照（该来源未在线核验），弱参照，具体关系待专门文献核对。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>达罗毗荼神话与吠陀传统关系示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>南印度本土传统与北印度传统（示意）</text><rect x='80' y='110' width='250' height='70' fill='var(--svg-node)' stroke='currentColor'/><text x='205' y='138' text-anchor='middle' fill='var(--svg-text)' font-size='14'>泰米尔本土传统</text><text x='205' y='162' text-anchor='middle' fill='var(--svg-text)' font-size='12'>穆鲁甘·桑加姆诗歌</text><rect x='430' y='110' width='250' height='70' fill='var(--svg-node)' stroke='currentColor'/><text x='555' y='138' text-anchor='middle' fill='var(--svg-text)' font-size='14'>吠陀—往世书传统</text><text x='555' y='162' text-anchor='middle' fill='var(--svg-text)' font-size='12'>梵语神谱</text><line x1='330' y1='145' x2='430' y2='145' stroke='currentColor' opacity='0.5' stroke-dasharray='6 4'/><rect x='230' y='250' width='300' height='64' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='276' text-anchor='middle' fill='var(--svg-text)' font-size='13'>长期并存交融</text><text x='380' y='298' text-anchor='middle' fill='var(--svg-text)' font-size='12'>非简单派生关系</text></svg>",
        "pending_notes": "1) 达罗毗荼与吠陀传统的关系为学界议题，本文不下定论；2) Hart 著作未录入 sources.json，已声明；3) 往世书比较为百科弱参照，待补专门文献。",
        "needs_verification": True
    },
    "myth-georgian": {
        "level": "L2",
        "source_text": "格鲁吉亚神话指高加索地区格鲁吉亚人的前基督教神祇与英雄传说，涉及太阳神、丰产神与民族英雄史诗。材料经古典记载与后世整理保存，基督教化后多经改写，本文如实标注。",
        "versions": [
            "格鲁吉亚前基督教神祇（如太阳神与丰产神）的职能见于古典与后世记载，原貌多经基督教化改写。",
            "民族英雄史诗（如阿米兰尼传说）与历史记忆交织，其史实性与年代为学界讨论议题。",
            "格鲁吉亚神话与高加索、伊朗邻近传统有可比母题，具体关系为比较研究议题。"
        ],
        "interpretations": [
            {"holder": "Georges Dumézil", "school": "印欧比较神话学", "view": "Dumézil 在《印欧人的神》中考察高加索民族（含格鲁吉亚）的传说与印欧三功能结构的可能关联，但指出格鲁吉亚语非印欧语，比较须谨慎；其结论学界有讨论。"},
            {"holder": "Jaan Puhvel", "school": "印欧比较神话学", "view": "Puhvel 在《比较神话学》中把高加索材料纳入印欧比较的边疆地带讨论，强调文化接触而非语言同源。"},
            {"holder": "Kevin Tuite", "school": "高加索民族学与语言人类学", "view": "Tuite 主张格鲁吉亚神话须在高加索与近东的文化接触语境中理解，反对直接套用印欧模型；该著作未录入 sources.json。"}
        ],
        "comparisons": [
            {"tradition": "波斯神话", "basis_source": "aca-comparative-myth", "note": "Puhvel 的印欧比较为高加索—伊朗接触提供框架性参照，属弱参照，不主张同源。"},
            {"tradition": "希腊神话", "basis_source": "aca-gods-indo-europeans", "note": "Dumézil 的印欧框架作一般参照，格鲁吉亚非印欧语，比较须谨慎，不主张同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>格鲁吉亚神话位置示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>格鲁吉亚神话：高加索的接触地带（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>格鲁吉亚神话</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='150' y1='174' x2='610' y2='174' stroke='currentColor' opacity='0.5'/><line x1='150' y1='174' x2='150' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='610' y1='174' x2='610' y2='212' stroke='currentColor' opacity='0.5'/><rect x='70' y='212' width='160' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='150' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>太阳神</text><text x='150' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>丰产职能</text><rect x='300' y='212' width='160' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>英雄史诗</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>阿米兰尼</text><rect x='530' y='212' width='160' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='610' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>文化接触</text><text x='610' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>高加索·伊朗</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>格鲁吉亚语非印欧语，印欧比较须谨慎</text></svg>",
        "pending_notes": "1) 前基督教神话多经间接记录，原貌难完整重建；2) Tuite 著作未录入 sources.json，已声明；3) 印欧/伊朗比较为框架弱参照，不主张同源。",
        "needs_verification": True
    },
    "rel-ancient-egyptian": {
        "level": "L2",
        "source_text": "古埃及宗教是古埃及的多神崇拜体系，核心包括太阳神崇拜、奥西里斯冥界观与法老的神权，主要文献为金字塔文、棺椁文、《亡灵书》与神庙铭文。不同时期与中心的传统并不统一，本文只记录有文献依据的对照。",
        "versions": [
            "古王国金字塔文以王权与太阳神拉为核心，中王国棺椁文把死后重生观念扩展到更广人群。",
            "赫利奥波利斯、孟菲斯、底比斯等中心各有创世传统，彼此并存而非单线演进。",
            "新王国阿肯那顿短暂推行阿顿崇拜，改革后恢复旧神系，反映宗教与政治的互动。"
        ],
        "interpretations": [
            {"holder": "Henri Frankfort", "school": "古代近东思想研究", "view": "Frankfort 在《哲学之前》中以神话意象分析埃及的王权与宇宙观，主张不以现代抽象标准误读古埃及宗教思维。"},
            {"holder": "James P. Allen", "school": "埃及学（宗教文本研究）", "view": "Allen 在《埃及宗教思想》中强调埃及创世与冥界传统的多元并存，各中心是并行表述而非单线演进；该著作未录入 sources.json。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《永恒回归的神话》中把埃及王权仪式与宇宙创生的周期性重演相联系，说明法老加冕如何被赋予宇宙论意义。"}
        ],
        "comparisons": [
            {"tradition": "美索不达米亚神话", "basis_source": "aca-before-philosophy", "note": "Frankfort 的近东思想研究把埃及与美索不达米亚宇宙观并置，属有文献依据的比较，不主张同源。"},
            {"tradition": "希腊宗教", "basis_source": "pri-book-dead", "note": "以《亡灵书》原典为埃及冥界观的文本依据，与希腊宗教作母题层面参照，不主张同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>古埃及宗教三大中心示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>古埃及宗教：多中心并存（示意）</text><rect x='60' y='110' width='190' height='64' fill='var(--svg-node)' stroke='currentColor'/><text x='155' y='136' text-anchor='middle' fill='var(--svg-text)' font-size='13'>赫利奥波利斯</text><text x='155' y='158' text-anchor='middle' fill='var(--svg-text)' font-size='12'>九柱神·拉</text><rect x='285' y='110' width='190' height='64' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='136' text-anchor='middle' fill='var(--svg-text)' font-size='13'>孟菲斯</text><text x='380' y='158' text-anchor='middle' fill='var(--svg-text)' font-size='12'>普塔·言语创世</text><rect x='510' y='110' width='190' height='64' fill='var(--svg-node)' stroke='currentColor'/><text x='605' y='136' text-anchor='middle' fill='var(--svg-text)' font-size='13'>底比斯</text><text x='605' y='158' text-anchor='middle' fill='var(--svg-text)' font-size='12'>阿蒙—拉</text><line x1='155' y1='174' x2='605' y2='174' stroke='currentColor' opacity='0.4'/><rect x='130' y='230' width='500' height='60' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='13'>文献：金字塔文—棺椁文—亡灵书—神庙铭文</text><text x='380' y='278' text-anchor='middle' fill='var(--svg-text)' font-size='12'>多中心传统并存，非单线演进</text><text x='380' y='336' text-anchor='middle' fill='var(--svg-text)' font-size='12'>法老神权与死后重生为核心主题</text></svg>",
        "pending_notes": "1) 各中心传统与年代学界有讨论，正文未列具体年数；2) Allen 著作未录入 sources.json，已声明；3) 比较为文献/框架参照，不主张同源。",
        "needs_verification": True
    },
    "myth-turkic": {
        "level": "L2",
        "source_text": "突厥神话指突厥语民族的腾格里（苍天）信仰、狼祖传说与萨满传统，主要经碑铭、民族志与口传保存。腾格里为至高天神，狼祖为民族起源母题。本文只记录有文献依据的对照。",
        "versions": [
            "古代突厥碑铭把腾格里与可汗的统治合法性相联系，君权被赋予天命色彩。",
            "狼祖传说在不同突厥语民族中母题相近而细节有别，反映共同的民族起源叙事。",
            "突厥神话与蒙古、通古斯等北亚传统在萨满信仰层面有可比之处，具体关系为研究议题。"
        ],
        "interpretations": [
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《萨满教》中把突厥—蒙古萨满的升天与神灵交往纳入宗教现象学分析，指出腾格里信仰的至高天特征，属跨区域比较研究。"},
            {"holder": "Denis Sinor", "school": "内亚史与阿尔泰学研究", "view": "Sinor 强调突厥—蒙古的腾格里信仰与天命观是内亚游牧政治文化的一部分，须在草原社会语境中理解；该著作未录入 sources.json。"},
            {"holder": "Jean-Paul Roux", "school": "突厥—蒙古宗教史", "view": "Roux 在《突厥与蒙古的宗教》中系统梳理腾格里信仰与狼祖母题的历史演变；该著作未录入 sources.json。"}
        ],
        "comparisons": [
            {"tradition": "蒙古萨满传统", "basis_source": "aca-shamanism", "note": "Eliade 的萨满教研究把突厥与蒙古萨满并置讨论，属有文献依据的对照。"},
            {"tradition": "印欧神话", "basis_source": "aca-gods-indo-europeans", "note": "Dumézil 的印欧框架仅作天父/至高神母题的一般参照；突厥语非印欧语，比较须谨慎，不主张同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>突厥腾格里信仰结构示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>突厥腾格里信仰结构（示意）</text><rect x='290' y='82' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='112' text-anchor='middle' fill='var(--svg-text)' font-size='14'>腾格里（苍天）</text><line x1='380' y1='128' x2='380' y2='164' stroke='currentColor' opacity='0.5'/><line x1='160' y1='164' x2='600' y2='164' stroke='currentColor' opacity='0.5'/><line x1='160' y1='164' x2='160' y2='202' stroke='currentColor' opacity='0.5'/><line x1='380' y1='164' x2='380' y2='202' stroke='currentColor' opacity='0.5'/><line x1='600' y1='164' x2='600' y2='202' stroke='currentColor' opacity='0.5'/><rect x='70' y='202' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='160' y='226' text-anchor='middle' fill='var(--svg-text)' font-size='13'>天命</text><text x='160' y='244' text-anchor='middle' fill='var(--svg-text)' font-size='12'>可汗合法性</text><rect x='290' y='202' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='226' text-anchor='middle' fill='var(--svg-text)' font-size='13'>狼祖</text><text x='380' y='244' text-anchor='middle' fill='var(--svg-text)' font-size='12'>民族起源</text><rect x='510' y='202' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='600' y='226' text-anchor='middle' fill='var(--svg-text)' font-size='13'>萨满</text><text x='600' y='244' text-anchor='middle' fill='var(--svg-text)' font-size='12'>升天·交往神灵</text><text x='380' y='308' text-anchor='middle' fill='var(--svg-text)' font-size='13'>突厥语非印欧语，印欧比较须谨慎</text></svg>",
        "pending_notes": "1) 腾格里信仰的历史演变复杂，具体年代待核；2) Sinor、Roux 著作未录入 sources.json，已声明；3) 印欧比较须谨慎、不主张同源。",
        "needs_verification": True
    },
    "myth-ugric": {
        "level": "L2",
        "source_text": "乌戈尔神话指匈牙利与西伯利亚乌戈尔语民族（汉特、曼西）的传统，涉及萨满宇宙观、天父与森林精灵等母题。材料主要经民族志与口传保存，本文如实标注。",
        "versions": [
            "西伯利亚乌戈尔民族的萨满宇宙观以多层天界与精灵信仰为特征，材料多经近代民族志记录。",
            "匈牙利民间传统保留若干乌拉尔语系母题，但经基督教化与欧洲化改写。",
            "乌戈尔神话与芬兰等乌拉尔语系传统有可比之处，具体关系为比较研究议题。"
        ],
        "interpretations": [
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《萨满教》中把西伯利亚乌戈尔萨满的宇宙层界与出神经验纳入现象学分析，指出其与北亚萨满传统的连续性。"},
            {"holder": "Jaan Puhvel", "school": "印欧比较神话学", "view": "Puhvel 在《比较神话学》中把乌拉尔语系（含乌戈尔与芬兰）材料作为印欧比较的邻近参照，指出二者母题的可比性，同时强调乌拉尔语非印欧语、比较须谨慎。"},
            {"holder": "Mihály Hoppál", "school": "民族学与萨满研究", "view": "Hoppál 在《Shamans and Symbols》中研究西伯利亚与喀尔巴阡地区的萨满符号传统，主张以民族志细节重建宇宙观；该著作未录入 sources.json。"}
        ],
        "comparisons": [
            {"tradition": "芬兰神话", "basis_source": "aca-comparative-myth", "note": "Puhvel 的比较神话学为乌拉尔语系内部母题比较提供框架参照；该语系非印欧语，比较须谨慎，不主张同源。"},
            {"tradition": "西伯利亚萨满传统", "basis_source": "aca-shamanism", "note": "Eliade 的萨满教研究把乌戈尔与更广的西伯利亚萨满并置，属有文献依据的对照。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>乌戈尔萨满宇宙观示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>乌戈尔萨满宇宙观：多层天界（示意）</text><rect x='230' y='80' width='300' height='44' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='108' text-anchor='middle' fill='var(--svg-text)' font-size='13'>上层天界</text><rect x='230' y='150' width='300' height='44' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='178' text-anchor='middle' fill='var(--svg-text)' font-size='13'>中层：人间</text><rect x='230' y='220' width='300' height='44' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='248' text-anchor='middle' fill='var(--svg-text)' font-size='13'>下层：精灵与亡者</text><line x1='380' y1='264' x2='380' y2='300' stroke='currentColor' opacity='0.5'/><rect x='280' y='300' width='200' height='40' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='326' text-anchor='middle' fill='var(--svg-text)' font-size='12'>萨满出神穿越层界</text></svg>",
        "pending_notes": "1) 乌戈尔材料多经近代民族志记录，原貌难完整重建；2) Hoppál 著作未录入 sources.json，已声明；3) 芬兰比较为框架弱参照，不主张同源。",
        "needs_verification": True
    },
    "myth-lithuanian": {
        "level": "L2",
        "source_text": "立陶宛神话指波罗的海地区立陶宛人的多神教传统，涉及雷神、太阳神与命运神等，材料经中世纪文献与民俗保存，基督教化后多经改写。立陶宛是欧洲较晚基督教化的地区，遗存相对丰富。",
        "versions": [
            "立陶宛中世纪文献记录雷神佩尔库纳斯与太阳神等崇拜，是波罗的海多神教的较晚见证。",
            "民间传说中的神祇经基督教化改写，其原貌需经考据重建。",
            "波罗的海神话与斯拉夫、北欧传统在印欧框架内有可比母题，具体关系为研究议题。"
        ],
        "interpretations": [
            {"holder": "Jaan Puhvel", "school": "印欧比较神话学", "view": "Puhvel 在《比较神话学》中把波罗的海材料纳入印欧比较，指出立陶宛雷神佩尔库纳斯与斯拉夫、北欧雷神的词源与功能对应，属语文学比较。"},
            {"holder": "Georges Dumézil", "school": "印欧比较神话学", "view": "Dumézil 在《印欧人的神》中讨论波罗的海神祇在印欧三功能结构中的位置，其结论学界有讨论。"},
            {"holder": "Marija Gimbutas", "school": "波罗的海考古与民俗研究", "view": "Gimbutas 结合考古与民俗研究波罗的海宗教，强调其史前根源；其部分理论在学界有争议。"}
        ],
        "comparisons": [
            {"tradition": "斯拉夫神话", "basis_source": "aca-comparative-myth", "note": "Puhvel 的印欧比较把波罗的海与斯拉夫材料并置，属学派框架，不主张直接同源。"},
            {"tradition": "北欧神话", "basis_source": "aca-gods-indo-europeans", "note": "Dumézil 的印欧框架作雷神母题的一般参照，具体对应有讨论。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>立陶宛神话神祇示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>立陶宛多神教神祇（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>波罗的海神系</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>佩尔库纳斯</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>雷神</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>太阳神</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>光与丰产</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>命运神</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>Laima</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>欧洲较晚基督教化，遗存相对丰富</text></svg>",
        "pending_notes": "1) 原貌多经基督教化改写，需考据重建；2) Gimbutas 部分理论有争议，正文已标；3) 印欧比较为学派框架，不主张同源。",
        "needs_verification": True
    },
    "rel-vaishnavism": {
        "level": "L2",
        "source_text": "毗湿奴派是以毗湿奴及其化身（如罗摩、黑天）为最高神格的印度教传统，经典包括《毗湿奴往世书》与史诗，强调虔信（bhakti）。本文采用学术描述性立场，不评判信仰真伪。",
        "versions": [
            "毗湿奴派以《毗湿奴往世书》等为基础，把毗湿奴视为维护宇宙的至高神，化身叙事是其核心。",
            "不同地区与流派（如罗摩派、黑天派）在化身侧重与修行实践上各有发展。",
            "毗湿奴派与湿婆派在最高神格的理解上不同，是印度教内部并存的传统。"
        ],
        "interpretations": [
            {"holder": "Wendy Doniger", "school": "芝加哥学派（印度宗教与文本研究）", "view": "Doniger 在《印度教研究》相关论述中强调毗湿奴化身叙事的多义性与阐释史，主张在文本脉络中理解其神学意涵，避免化约为单一体系。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《比较宗教的模式》中把化身与神圣显现的结构相联系，说明毗湿奴化身如何被理解为宇宙秩序在不同时代的再显现。"},
            {"holder": "Friedhelm Hardy", "school": "南印度宗教与虔信研究", "view": "Hardy 在《Viraha-Bhakti》中研究南印度虔信传统的形成，强调情感性虔信在黑天崇拜中的核心地位；该著作未录入 sources.json。"}
        ],
        "comparisons": [
            {"tradition": "印度教（湿婆派）", "basis_source": "enc-brit-hinduism", "note": "以权威百科条目作湿婆派背景的一般参照（该来源未在线核验）；两派并存，具体神学差异待专门文献核对。"},
            {"tradition": "佛教", "basis_source": "aca-patterns-religion", "note": "Eliade 的比较宗教框架作神圣显现母题的一般参照，不主张教义同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>毗湿奴派结构示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>毗湿奴派（描述性示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>毗湿奴</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>罗摩</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>化身之一</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>黑天</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>化身之一</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>虔信</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>虔信实践</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>与湿婆派并存，描述性立场</text></svg>",
        "pending_notes": "1) 化身谱系与流派差异待专门文献核对；2) Hardy 著作未录入 sources.json，已声明；3) 百科来源未在线核验，标弱参照；不替信仰表态。",
        "needs_verification": True
    },
    "rel-shaivism": {
        "level": "L2",
        "source_text": "湿婆派是以湿婆为最高神格的印度教传统，强调苦行、瑜伽与林伽崇拜，经典包括湿婆阿含与相关往世书。本文采用学术描述性立场，不评判信仰真伪。",
        "versions": [
            "湿婆派把湿婆视为兼具毁灭与再生的至高神，苦行与瑜伽是其修行的核心面向。",
            "克什米尔湿婆派等流派在哲学上发展出独特的意识—显现理论，与其他流派侧重不同。",
            "湿婆派与毗湿奴派在最高神格理解上不同，是印度教内部并存的传统。"
        ],
        "interpretations": [
            {"holder": "Wendy Doniger", "school": "芝加哥学派（印度宗教与文本研究）", "view": "Doniger 在《Śiva: The Erotic Ascetic》中分析湿婆兼具苦行与情欲的张力，指出这一对立是理解其神格的关键；该著作未录入 sources.json。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《瑜伽：不朽与自由》中把湿婆作为苦行与瑜伽传统的原型神格，说明其形象与修行实践的内在联系。"},
            {"holder": "Karel Werner", "school": "印度哲学与宗教研究", "view": "Werner 主张湿婆形象的多面性须结合印度宗教史的不同层次理解，反对单一化解读；该著作未录入 sources.json。"}
        ],
        "comparisons": [
            {"tradition": "印度教（毗湿奴派）", "basis_source": "enc-brit-hinduism", "note": "以权威百科条目作毗湿奴派背景的一般参照（该来源未在线核验）；两派并存，具体神学差异待专门文献核对。"},
            {"tradition": "印度教（密教）", "basis_source": "aca-patterns-religion", "note": "Eliade 的比较宗教框架作苦行—瑜伽母题的一般参照，不主张教义同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>湿婆派面向示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>湿婆派（描述性示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>湿婆</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>苦行</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>瑜伽</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>林伽崇拜</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>仪式核心</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>毁灭再生</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>宇宙循环</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>苦行与情欲的张力是理解其神格的关键</text></svg>",
        "pending_notes": "1) 各流派哲学差异待专门文献核对；2) Doniger、Werner 著作未录入 sources.json，已声明；3) 百科来源未在线核验，标弱参照；不替信仰表态。",
        "needs_verification": True
    },
    "motif-labyrinth": {
        "level": "L2",
        "source_text": "迷宫母题以迷径、考验与中心为核心，最著名的案例是希腊的克里特迷宫与弥诺陶洛斯叙事。学界对迷宫母题的象征意义有专门研究，本文只记录有文献依据的对照。",
        "versions": [
            "希腊神话中的克里特迷宫关押弥诺陶洛斯，忒修斯以线团指引走出，是迷宫母题的经典叙事。",
            "不同传统与艺术中的迷宫／迷径意象在宗教仪式与朝圣中有不同功能，形态各异。",
            "把不同文化的迷宫意象并置属母题层面比较，不主张同源。"
        ],
        "interpretations": [
            {"holder": "Joseph Campbell", "school": "比较神话学（单一神话模型）", "view": "Campbell 在《千面英雄》中把迷宫与弥诺陶洛斯之战纳入英雄旅程的试炼阶段，属分析模型，学界对其概括性有批评。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "Lévi-Strauss 在《结构人类学》中以迷径说明神话如何以曲折路径表达对立与中介，属方法论参照。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《永恒回归的神话》中把迷宫的入口与中心解读为通往神圣中心的仪式性路径，为理解迷宫母题提供现象学维度。"}
        ],
        "comparisons": [
            {"tradition": "希腊神话", "basis_source": "aca-hero-faces", "note": "Campbell 的著作以忒修斯—弥诺陶洛斯为英雄试炼案例，属有文献依据的参照，并标注模型概括性。"},
            {"tradition": "宗教朝圣传统", "basis_source": "aca-eternal-return", "note": "Eliade 的宇宙中心框架作迷径—朝圣母题的一般参照，不主张同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>迷宫母题结构示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>迷宫母题：迷径与中心（示意）</text><rect x='60' y='120' width='150' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='135' y='144' text-anchor='middle' fill='var(--svg-text)' font-size='13'>入口</text><text x='135' y='162' text-anchor='middle' fill='var(--svg-text)' font-size='12'>启程</text><path d='M210 147 H320 V210 H450 V147 H560' fill='none' stroke='currentColor' opacity='0.5'/><rect x='560' y='120' width='140' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='630' y='144' text-anchor='middle' fill='var(--svg-text)' font-size='13'>中心</text><text x='630' y='162' text-anchor='middle' fill='var(--svg-text)' font-size='12'>试炼·弥诺陶洛斯</text><rect x='230' y='270' width='300' height='58' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='294' text-anchor='middle' fill='var(--svg-text)' font-size='13'>线团指引·归返</text><text x='380' y='314' text-anchor='middle' fill='var(--svg-text)' font-size='12'>英雄旅程的试炼阶段</text></svg>",
        "pending_notes": "1) 迷宫意象在不同传统中功能各异，不主张同源；2) Campbell 模型概括性已标注；3) 比较为学派/框架参照，待补专门文献。",
        "needs_verification": True
    },
    "motif-phoenix": {
        "level": "L2",
        "source_text": "不死鸟母题以死而复生的神鸟为核心，经典形态为希腊—罗马的火凤凰（phoenix）自焚后重生，其他传统亦有类似的重生鸟意象。本文只记录有文献依据的对照。",
        "versions": [
            "希腊—罗马传统中的凤凰周期性自焚并从灰烬重生，象征更新与永恒，记载见于古典作家。",
            "其他传统中的重生鸟意象在形态与象征上各异，母题相近但文化语境不同。",
            "把不同传统的重生鸟并置属母题层面比较，不主张同源。"
        ],
        "interpretations": [
            {"holder": "James George Frazer", "school": "早期比较宗教学", "view": "Frazer 在《金枝》中把凤凰重生与季节循环、死亡—复活母题相联系，属早期学派观点，其泛化结论在现代学界受到修订。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《永恒回归的神话》中把凤凰自焚重生解读为宇宙周期性更新的象征，属其永恒回归框架的典型意象。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "Lévi-Strauss 在《结构人类学》中的结构方法可分析不死鸟如何以生/死对立的中介角色出现，属方法论参照。"}
        ],
        "comparisons": [
            {"tradition": "埃及神话", "basis_source": "aca-golden-bough", "note": "Frazer 的《金枝》为早期学派参照，把凤凰与近东—埃及的太阳鸟意象并置，其结论已被修订，此处并列呈现。"},
            {"tradition": "希腊神话", "basis_source": "aca-eternal-return", "note": "Eliade 的宇宙更新框架作不死鸟母题的一般参照，不主张具体文本同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>不死鸟母题循环示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>不死鸟：自焚与重生（示意）</text><rect x='80' y='150' width='150' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='155' y='174' text-anchor='middle' fill='var(--svg-text)' font-size='13'>生</text><text x='155' y='192' text-anchor='middle' fill='var(--svg-text)' font-size='12'>凤凰</text><line x1='230' y1='177' x2='290' y2='177' stroke='currentColor' opacity='0.5'/><rect x='290' y='150' width='150' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='365' y='174' text-anchor='middle' fill='var(--svg-text)' font-size='13'>自焚</text><text x='365' y='192' text-anchor='middle' fill='var(--svg-text)' font-size='12'>死亡</text><line x1='440' y1='177' x2='500' y2='177' stroke='currentColor' opacity='0.5'/><rect x='500' y='150' width='150' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='575' y='174' text-anchor='middle' fill='var(--svg-text)' font-size='13'>重生</text><text x='575' y='192' text-anchor='middle' fill='var(--svg-text)' font-size='12'>灰烬中</text><path d='M575 216 Q575 270 155 270 Q155 270 155 210' fill='none' stroke='currentColor' opacity='0.4'/><text x='380' y='308' text-anchor='middle' fill='var(--svg-text)' font-size='13'>循环象征：更新与永恒</text></svg>",
        "pending_notes": "1) 不同传统重生鸟意象差异大，不主张同源；2) Frazer 早期结论已标修订；3) 比较为母题层面参照，待补专门文献。",
        "needs_verification": True
    },
    "rel-tantrism": {
        "level": "L2",
        "source_text": "密教（怛特罗）指以密续、坛城、咒法与观想为特征的印度教—佛教修行传统，经典为各类怛特罗文献。它在印度教与佛教中均有发展，形成复杂的仪轨与神学体系。本文采用学术描述性立场，不评判信仰真伪。",
        "versions": [
            "印度教密教以湿婆—性力崇拜为核心，发展出身体修炼与仪轨体系，经典为湿婆阿含与怛特罗。",
            "佛教密宗（金刚乘）以密续、灌顶与坛城观想为特征，与显宗修法形成对照。",
            "密教在印度、西藏与东亚各有本土化形态，实践与理论侧重不同。"
        ],
        "interpretations": [
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《瑜伽：不朽与自由》中把密教的观想与身印纳入瑜伽传统的谱系，指出其与古典瑜伽在技术上的连续性。"},
            {"holder": "Wendy Doniger", "school": "芝加哥学派（印度宗教与文本研究）", "view": "Doniger 在《Śiva: The Erotic Ascetic》中分析密教湿婆—性力形象的苦行与情欲张力，强调其象征须在文本脉络中理解。"},
            {"holder": "David Gordon White", "school": "南亚宗教与密教研究", "view": "White 在《Kiss of the Yogini》中主张密教须据其怛特罗文献与地方实践研究，反对以现代视角简化；该著作未录入 sources.json。"}
        ],
        "comparisons": [
            {"tradition": "印度教（湿婆派）", "basis_source": "aca-patterns-religion", "note": "Eliade 的比较宗教框架作密教与湿婆派关系的一般参照，不主张教义同源。"},
            {"tradition": "佛教（藏传）", "basis_source": "enc-brit-tantrism", "note": "以权威百科密教条目作背景参照（该来源未在线核验），弱参照，具体差异待专门文献核对。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>密教要素示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>密教（怛特罗）要素（示意）</text><circle cx='380' cy='180' r='60' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='176' text-anchor='middle' fill='var(--svg-text)' font-size='14'>坛城</text><text x='380' y='196' text-anchor='middle' fill='var(--svg-text)' font-size='12'>曼荼罗</text><text x='380' y='96' text-anchor='middle' fill='var(--svg-text)' font-size='13'>灌顶传承</text><text x='200' y='300' text-anchor='middle' fill='var(--svg-text)' font-size='13'>密续经典</text><text x='560' y='300' text-anchor='middle' fill='var(--svg-text)' font-size='13'>身印·观想</text><line x1='380' y1='120' x2='240' y2='290' stroke='currentColor' opacity='0.4'/><line x1='380' y1='120' x2='520' y2='290' stroke='currentColor' opacity='0.4'/><text x='380' y='352' text-anchor='middle' fill='var(--svg-text)' font-size='13'>印度教与佛教皆有发展，描述性立场</text></svg>",
        "pending_notes": "1) 密教文献庞杂、年代跨度大，具体年代未列；2) White 著作未录入 sources.json，已声明；3) 百科来源未在线核验，标弱参照；不替信仰表态。",
        "needs_verification": True
    },
    "rel-ancient-greek": {
        "level": "L2",
        "source_text": "古希腊宗教指古希腊城邦的祭祀、神谕与神秘崇拜体系，主要材料包括保萨尼亚斯《希腊志》等古典文献与考古遗存。它以公共祭祀与地方崇拜为核心，缺乏统一教义，本文只记录有文献依据的对照。",
        "versions": [
            "城邦公共祭祀以神庙、祭坛与节庆为中心，各城邦守护神与仪式传统各异。",
            "德尔斐、多多纳等神谕在公共决策与私人事务中扮演角色，其运作方式随时代演变。",
            "厄琉息斯秘仪等神秘崇拜以入教仪式与来世许诺为特征，具体教义因秘仪性质而材料有限。"
        ],
        "interpretations": [
            {"holder": "Walter Burkert", "school": "宗教史/古典学", "view": "Burkert 在《希腊宗教》中主张古希腊宗教的核心在祭祀实践而非教义体系，并把其形成置于近东文化影响的历史语境中。"},
            {"holder": "Jean-Pierre Vernant", "school": "巴黎学派（古希腊神话与思想）", "view": "Vernant 在《希腊神话与思想》中把希腊宗教实践与城邦公共空间、政治秩序相联系，分析祭祀与城邦认同的关系。"},
            {"holder": "Jane Ellen Harrison", "school": "剑桥学派（神话—仪式理论）", "view": "Harrison 在《希腊宗教研究导论》中强调仪式先于神话，把希腊诸神的起源追溯至古代仪式实践。"}
        ],
        "comparisons": [
            {"tradition": "古埃及宗教", "basis_source": "aca-before-philosophy", "note": "Frankfort 的近东—埃及思想比较为古代宗教的一般框架参照，不主张具体崇拜同源。"},
            {"tradition": "罗马宗教", "basis_source": "pri-pausanias", "note": "以《希腊志》等古典文献为依据记录希腊崇拜，与罗马宗教作历史关联的文本对照，不主张简单复制。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>古希腊宗教结构示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>古希腊宗教：实践为核心（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>城邦祭祀</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>神庙·节庆</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>公共崇拜</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>神谕</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>德尔斐</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>秘仪</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>厄琉息斯</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>以实践为核心，缺乏统一教义</text></svg>",
        "pending_notes": "1) 秘仪材料有限，具体教义不下定论；2) 三位学者论点以其代表著作为概括，细节待核对；3) 比较为框架/文本层面参照，不主张同源。",
        "needs_verification": True
    },
    "motif-cosmicegg": {
        "level": "L2",
        "source_text": "宇宙卵母题以原初之卵化生天地为核心，见于印度《梨俱吠陀》的金胎（Hiranyagarbha）与希腊俄耳甫斯教等传统。学界对其结构有专门讨论，本文只记录有文献依据的对照。",
        "versions": [
            "印度《梨俱吠陀》以金胎（Hiranyagarbha）为宇宙本源，原初之卵孵化出天地，是宇宙卵母题的经典形态。",
            "希腊俄耳甫斯教神话亦以宇宙卵为创世起点，与印度形态结构相近而文化语境不同。",
            "把不同传统的宇宙卵并置属母题层面比较，不主张同源。"
        ],
        "interpretations": [
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《永恒回归的神话》中把宇宙卵视为创世原型的一种表达，强调其象征宇宙从潜能到显现的结构。"},
            {"holder": "James George Frazer", "school": "早期比较宗教学", "view": "Frazer 在《金枝》中把宇宙卵母题与丰产、创世观念相联系，属早期学派观点，其泛化结论在现代学界受到修订。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "Lévi-Strauss 在《结构人类学》中以卵的封闭/开启对立说明创世神话如何组织宇宙论范畴，属方法论参照。"}
        ],
        "comparisons": [
            {"tradition": "印度神话", "basis_source": "pri-rigveda", "note": "以《梨俱吠陀》金胎颂为宇宙卵母题的文本依据，属原典层面的对照。"},
            {"tradition": "希腊神话", "basis_source": "aca-eternal-return", "note": "Eliade 的创世原型框架作俄耳甫斯教宇宙卵母题的一般参照，不主张具体文本同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>宇宙卵母题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>宇宙卵：原初之卵化生天地（示意）</text><ellipse cx='380' cy='150' rx='60' ry='78' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='156' text-anchor='middle' fill='var(--svg-text)' font-size='14'>原初之卵</text><line x1='380' y1='228' x2='380' y2='264' stroke='currentColor' opacity='0.5'/><line x1='200' y1='264' x2='560' y2='264' stroke='currentColor' opacity='0.5'/><line x1='200' y1='264' x2='200' y2='300' stroke='currentColor' opacity='0.5'/><line x1='560' y1='264' x2='560' y2='300' stroke='currentColor' opacity='0.5'/><rect x='120' y='300' width='160' height='48' fill='var(--svg-node)' stroke='currentColor'/><text x='200' y='330' text-anchor='middle' fill='var(--svg-text)' font-size='13'>天</text><rect x='480' y='300' width='160' height='48' fill='var(--svg-node)' stroke='currentColor'/><text x='560' y='330' text-anchor='middle' fill='var(--svg-text)' font-size='13'>地</text><text x='380' y='372' text-anchor='middle' fill='var(--svg-text)' font-size='12'>金胎（Hiranyagarbha）·俄耳甫斯教</text></svg>",
        "pending_notes": "1) 不同传统的宇宙卵母题差异大，不主张同源；2) Frazer 早期结论已标修订；3) 比较为原典/框架参照，待补专门文献。",
        "needs_verification": True
    },
    "fig-amaterasu": {
        "level": "L2",
        "source_text": "天照大神是日本神话的太阳女神，在《古事记》《日本书纪》中居于皇祖神的核心地位，其隐入岩户与复出的叙事是重要母题。材料经奈良时代编纂，带有政治语境。",
        "versions": [
            "《古事记》叙述天照大神隐入天岩户、众神以歌舞引其复出的故事，是天皇世系神话的关键环节。",
            "《日本书纪》的对应记载附有异文，反映编纂时对多种材料的取舍。",
            "天照大神与皇祖神、伊势神宫崇拜的结合，是历史与政治条件的结果。"
        ],
        "interpretations": [
            {"holder": "本居宣长", "school": "国学（日本古典研究）", "view": "本居宣长在《古事记传》中主张以日本古典语言的固有精神理解天照大神神话，反对用中国式道德化框架解读；该著作未录入 sources.json。"},
            {"holder": "Donald L. Philippi", "school": "日本神话译介与研究", "view": "Philippi 在《古事记》英译本导论中强调天照大神叙事作为文学与神话文本的独特性，指出其编纂意图的复杂性；该著作未录入 sources.json。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《永恒回归的神话》中把太阳神与王权、宇宙秩序相联系，为理解天照大神的皇祖神地位提供现象学参照。"}
        ],
        "comparisons": [
            {"tradition": "日本神话（须佐之男）", "basis_source": "pri-kojiki", "note": "以《古事记》原典为依据记录天照大神与须佐之男的姐弟关系及相关叙事，属同文本内的对照。"},
            {"tradition": "希腊神话", "basis_source": "aca-eternal-return", "note": "Eliade 的太阳—王权框架作母题层面的一般参照，不主张同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>天照大神岩户叙事示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>天照大神：岩户隐没与复出（示意）</text><rect x='90' y='140' width='160' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='164' text-anchor='middle' fill='var(--svg-text)' font-size='13'>天照大神</text><text x='170' y='184' text-anchor='middle' fill='var(--svg-text)' font-size='12'>太阳女神</text><line x1='250' y1='170' x2='330' y2='170' stroke='currentColor' opacity='0.5'/><rect x='330' y='140' width='160' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='410' y='164' text-anchor='middle' fill='var(--svg-text)' font-size='13'>隐入岩户</text><text x='410' y='184' text-anchor='middle' fill='var(--svg-text)' font-size='12'>世界失光</text><line x1='490' y1='170' x2='570' y2='170' stroke='currentColor' opacity='0.5'/><rect x='570' y='140' width='140' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='640' y='164' text-anchor='middle' fill='var(--svg-text)' font-size='13'>复出</text><text x='640' y='184' text-anchor='middle' fill='var(--svg-text)' font-size='12'>光复</text><rect x='230' y='270' width='300' height='52' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='294' text-anchor='middle' fill='var(--svg-text)' font-size='13'>众神歌舞引其复出</text><text x='380' y='314' text-anchor='middle' fill='var(--svg-text)' font-size='12'>皇祖神与天皇世系的关键环节</text></svg>",
        "pending_notes": "1) 两部正史编纂语境与材料来源学界有讨论；2) 本居宣长、Philippi 著作未录入 sources.json，已声明；3) 太阳—王权比较为框架参照，不主张同源。",
        "needs_verification": True
    },
    "fig-susanoo": {
        "level": "L2",
        "source_text": "须佐之男是日本神话中的风暴与英雄神，在《古事记》《日本书纪》中以其暴烈行为与被逐出高天原、斩杀八岐大蛇等叙事著称。其形象兼具破坏与英雄两面。",
        "versions": [
            "《古事记》叙述须佐之男在高天原扰害、被逐后于出云斩杀八岐大蛇、获草薙剑的经过。",
            "《日本书纪》的对应记载附有异文，对须佐之男的评价与叙事侧重略有不同。",
            "须佐之男与出云地方神话、大国主神谱系的关系是理解其形象的重要线索。"
        ],
        "interpretations": [
            {"holder": "本居宣长", "school": "国学（日本古典研究）", "view": "本居宣长在《古事记传》中注重以古典语言本身理解须佐之男的暴烈与英雄两面，反对道德化的简化解读；该著作未录入 sources.json。"},
            {"holder": "Donald L. Philippi", "school": "日本神话译介与研究", "view": "Philippi 在《古事记》英译本中把须佐之男的八岐大蛇退治视为出云神话循环的核心叙事，强调其文学结构；该著作未录入 sources.json。"},
            {"holder": "Joseph Campbell", "school": "比较神话学（单一神话模型）", "view": "Campbell 在《千面英雄》中把屠蛇英雄纳入英雄旅程的试炼主题，属分析模型，学界对其概括性有批评。"}
        ],
        "comparisons": [
            {"tradition": "日本神话（天照大神）", "basis_source": "pri-kojiki", "note": "以《古事记》原典为依据记录须佐之男与天照大神的姐弟关系及高天原叙事，属同文本内对照。"},
            {"tradition": "希腊神话", "basis_source": "aca-hero-faces", "note": "Campbell 的屠蛇英雄框架作母题层面参照，标注模型概括性，不主张同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>须佐之男英雄叙事示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>须佐之男：暴烈与英雄两面（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>须佐之男</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='200' y1='174' x2='560' y2='174' stroke='currentColor' opacity='0.5'/><line x1='200' y1='174' x2='200' y2='212' stroke='currentColor' opacity='0.5'/><line x1='560' y1='174' x2='560' y2='212' stroke='currentColor' opacity='0.5'/><rect x='110' y='212' width='180' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='200' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>高天原扰害</text><text x='200' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>被逐出</text><rect x='470' y='212' width='180' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='560' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>斩八岐大蛇</text><text x='560' y='256' text-anchor='middle' fill='var(--svg-text)' font-size='12'>获草薙剑</text><rect x='230' y='310' width='300' height='46' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='338' text-anchor='middle' fill='var(--svg-text)' font-size='13'>出云神话循环的核心英雄</text></svg>",
        "pending_notes": "1) 两部正史异文与评价差异待核；2) 本居宣长、Philippi 著作未录入 sources.json，已声明；3) Campbell 模型概括性已标注，不主张同源。",
        "needs_verification": True
    },
    "fig-dagda": {
        "level": "L2",
        "source_text": "达格达是爱尔兰神话中达努神族（Tuatha Dé Danann）的至善之神，以其棒槌、大锅与竖琴等法器著称，材料见于《侵略之书》等中世纪爱尔兰文献。其形象经基督教时代抄写者记录。",
        "versions": [
            "《侵略之书》等文献把达格达列为达努神族的首领之一，其法器象征力量、丰产与音乐。",
            "爱尔兰神话循环中达格达的形象与王权、丰产仪式相关，具体细节因文本而异。",
            "中世纪抄本的基督教化改写影响了对达格达原貌的重建，需谨慎考据。"
        ],
        "interpretations": [
            {"holder": "Proinsias Mac Cana", "school": "凯尔特文学与神话研究", "view": "Mac Cana 在《Celtic Mythology》中把达格达置于爱尔兰神族的社会与王权结构中理解，强调其法器母题的功能意义；该著作未录入 sources.json。"},
            {"holder": "Georges Dumézil", "school": "印欧比较神话学", "view": "Dumézil 在《印欧人的神》中把达格达与印欧神系的主权或丰产功能相联系，属学派比较，具体对应学界有讨论。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《永恒回归的神话》中关于丰产与王权仪式的论述，可用于理解达格达法器母题的宇宙论意涵，属理论参照。"}
        ],
        "comparisons": [
            {"tradition": "威尔士神话", "basis_source": "pri-mabinogion", "note": "以《马比诺吉昂》原典为依据记录威尔士—爱尔兰神话的对应人物，属文本层面参照，不主张简单等同。"},
            {"tradition": "北欧神话", "basis_source": "aca-gods-indo-europeans", "note": "Dumézil 的印欧比较作丰产—主权功能的一般参照，不主张直接同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>达格达法器与职能示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>达格达：法器与职能（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>达格达</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>棒槌</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>生死之力</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>大锅</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>丰产·供养</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>竖琴</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>音乐·秩序</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>达努神族的首领之一，经中世纪抄本保存</text></svg>",
        "pending_notes": "1) 中世纪抄本的基督教化改写影响原貌重建；2) Mac Cana 著作未录入 sources.json，已声明；3) 印欧比较为学派框架，不主张同源。",
        "needs_verification": True
    },
    "fig-cu-chulainn": {
        "level": "L2",
        "source_text": "库丘林是爱尔兰神话阿尔斯特循环（Ulster Cycle）的核心英雄，其事迹见于《夺牛长征记》等中世纪爱尔兰史诗，以其超凡武艺与悲剧命运著称。材料经基督教时代抄本保存。",
        "versions": [
            "《夺牛长征记》叙述库丘林独自抵御康诺特大军的事迹，是阿尔斯特循环的核心文本。",
            "库丘林的出身、师承与死亡叙事在不同文本中有差异，需综合考据。",
            "中世纪抄本的编纂立场影响了对库丘林形象的呈现，具体细节需谨慎。"
        ],
        "interpretations": [
            {"holder": "Proinsias Mac Cana", "school": "凯尔特文学与神话研究", "view": "Mac Cana 在《Celtic Mythology》中把库丘林置于阿尔斯特的社会与英雄伦理中理解，强调其形象的口传底色与文本中介；该著作未录入 sources.json。"},
            {"holder": "Georges Dumézil", "school": "印欧比较神话学", "view": "Dumézil 在《印欧人的神》的印欧框架内讨论库丘林与印欧英雄传统的可比性，属学派比较，具体对应学界有讨论。"},
            {"holder": "Joseph Campbell", "school": "比较神话学（单一神话模型）", "view": "Campbell 在《千面英雄》中把英雄的试炼与悲剧命运纳入英雄旅程讨论，属分析模型，学界对其概括性有批评。"}
        ],
        "comparisons": [
            {"tradition": "威尔士神话", "basis_source": "pri-mabinogion", "note": "以《马比诺吉昂》原典为依据记录威尔士英雄传统，与爱尔兰阿尔斯特循环作文本层面参照，不主张简单等同。"},
            {"tradition": "希腊神话", "basis_source": "aca-hero-faces", "note": "Campbell 的英雄旅程框架作叙事结构参照，标注模型概括性，不主张同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>库丘林英雄叙事示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>库丘林：阿尔斯特循环核心英雄（示意）</text><rect x='60' y='150' width='150' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='135' y='174' text-anchor='middle' fill='var(--svg-text)' font-size='13'>出身·师承</text><text x='135' y='194' text-anchor='middle' fill='var(--svg-text)' font-size='12'>超凡武艺</text><line x1='210' y1='180' x2='280' y2='180' stroke='currentColor' opacity='0.5'/><rect x='280' y='150' width='200' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='174' text-anchor='middle' fill='var(--svg-text)' font-size='13'>夺牛长征记</text><text x='380' y='194' text-anchor='middle' fill='var(--svg-text)' font-size='12'>独御大军</text><line x1='480' y1='180' x2='550' y2='180' stroke='currentColor' opacity='0.5'/><rect x='550' y='150' width='160' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='630' y='174' text-anchor='middle' fill='var(--svg-text)' font-size='13'>悲剧命运</text><text x='630' y='194' text-anchor='middle' fill='var(--svg-text)' font-size='12'>英雄之死</text><rect x='230' y='270' width='300' height='50' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='294' text-anchor='middle' fill='var(--svg-text)' font-size='13'>中世纪爱尔兰史诗保存</text><text x='380' y='312' text-anchor='middle' fill='var(--svg-text)' font-size='12'>口传底色与文本中介</text></svg>",
        "pending_notes": "1) 不同文本的出身/死亡叙事有差异，需综合考据；2) Mac Cana 著作未录入 sources.json，已声明；3) 印欧/Campbell 比较为框架，不主张同源。",
        "needs_verification": True
    },
    "myth-maori": {
        "level": "L2",
        "source_text": "毛利神话指新西兰毛利人的创世、祖先与航海传说，核心涉及天父地母（Ranginui 与 Papatūānuku）的分离与森林之神 Tāne 等。材料经口传与19世纪以来的记录保存，本文如实标注。",
        "versions": [
            "毛利创世叙事以天父地母的分离为核心，Tāne 推开父母使光进入世界，是宇宙起源的关键母题。",
            "不同部落（iwi）的谱系与神名各有差异，口传版本随社群而变。",
            "19世纪以来的记录与当代毛利社群叙述之间存在语境差异，解读需谨慎。"
        ],
        "interpretations": [
            {"holder": "Anne Salmond", "school": "毛利与太平洋历史研究", "view": "Salmond 在《Two Worlds》中主张毛利宇宙观须在毛利自身的社会与土地脉络中理解，强调天父地母谱系与社群认同的关联；该著作未录入 sources.json。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《永恒回归的神话》中把天地分离视为创世原型的一种表达，说明其象征世界从混沌到秩序的开启。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "Lévi-Strauss 在《结构人类学》中的结构方法可分析天父地母分离中的亲缘与自然—文化对立，属方法论参照。"}
        ],
        "comparisons": [
            {"tradition": "波利尼西亚神话", "basis_source": "enc-wiki-list-myth", "note": "以权威百科条目作波利尼西亚背景的一般参照（该来源未在线核验），弱参照，不推断同源。"},
            {"tradition": "澳大利亚原住民神话", "basis_source": "ins-world-history", "note": "以机构资料作大洋洲区域背景的一般参照（该来源未在线核验），弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>毛利创世母题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>毛利创世：天父地母的分离（示意）</text><rect x='150' y='90' width='460' height='40' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='116' text-anchor='middle' fill='var(--svg-text)' font-size='13'>天父 Ranginui</text><rect x='150' y='250' width='460' height='40' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='276' text-anchor='middle' fill='var(--svg-text)' font-size='13'>地母 Papatūānuku</text><line x1='380' y1='130' x2='380' y2='250' stroke='currentColor' opacity='0.5'/><rect x='310' y='168' width='140' height='44' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='196' text-anchor='middle' fill='var(--svg-text)' font-size='12'>Tāne 推开父母</text><text x='380' y='330' text-anchor='middle' fill='var(--svg-text)' font-size='13'>光进入世界·秩序开启</text><text x='380' y='360' text-anchor='middle' fill='var(--svg-text)' font-size='12'>各部族谱系与神名有别</text></svg>",
        "pending_notes": "1) 不同部落谱系差异大，口传版本随社群而变；2) Salmond 著作未录入 sources.json，已声明；3) 百科/机构来源未在线核验，标弱参照。",
        "needs_verification": True
    },
    "myth-vietnamese": {
        "level": "L2",
        "source_text": "越南神话指越南的龙子仙孙（Lạc Long Quân 与 Âu Cơ）建国传说、四神信仰与地方神祇传统，材料见于《岭南摭怪》等汉文与喃字文献。本文只记录有文献依据的对照。",
        "versions": [
            "龙子仙孙传说叙述雒龙君与妪姬结合、生百卵、分治山海的建国叙事，是越南民族起源的核心神话。",
            "四神（伞圆山神、扶董天王等）信仰与抗外患、护佑家国的主题相关，见于民间与官方记载。",
            "越南神话与邻近的中国、占婆传统有交融，具体关系为研究议题。"
        ],
        "interpretations": [
            {"holder": "Keith Taylor", "school": "越南史与东南亚研究", "view": "Taylor 在《The Birth of Vietnam》中主张越南的起源传说须置于其自身的历史与政治脉络中理解，龙子仙孙叙事与越南国家认同的建构相关；该著作未录入 sources.json。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《永恒回归的神话》中关于民族起源与宇宙创生重演的论述，可说明龙子仙孙传说如何为共同体提供神圣起源，此为理论参照。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "Lévi-Strauss 在《结构人类学》中的结构方法可分析龙（水）与仙（山）的对立与结合如何在建国神话中组织亲缘与地域范畴，属方法论参照。"}
        ],
        "comparisons": [
            {"tradition": "中国神话", "basis_source": "enc-wiki-list-myth", "note": "以权威百科条目作东亚背景的一般参照（该来源未在线核验），弱参照，不推断同源。"},
            {"tradition": "东南亚传统", "basis_source": "ins-world-history", "note": "以机构资料作区域背景的一般参照（该来源未在线核验），弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>越南龙子仙孙母题示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>龙子仙孙：建国神话（示意）</text><rect x='70' y='120' width='200' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='144' text-anchor='middle' fill='var(--svg-text)' font-size='13'>雒龙君</text><text x='170' y='164' text-anchor='middle' fill='var(--svg-text)' font-size='12'>龙·水</text><rect x='490' y='120' width='200' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='144' text-anchor='middle' fill='var(--svg-text)' font-size='13'>妪姬</text><text x='590' y='164' text-anchor='middle' fill='var(--svg-text)' font-size='12'>仙·山</text><line x1='270' y1='150' x2='490' y2='150' stroke='currentColor' opacity='0.5'/><rect x='280' y='230' width='200' height='54' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='13'>生百卵·分治山海</text><text x='380' y='272' text-anchor='middle' fill='var(--svg-text)' font-size='12'>民族起源</text><text x='380' y='336' text-anchor='middle' fill='var(--svg-text)' font-size='13'>见于《岭南摭怪》等文献</text></svg>",
        "pending_notes": "1) 建国传说的文献年代与史实性待核；2) Taylor 著作未录入 sources.json，已声明；3) 百科/机构来源未在线核验，标弱参照。",
        "needs_verification": True
    },
    "myth-siberian": {
        "level": "L2",
        "source_text": "西伯利亚神话指西伯利亚诸民族（如通古斯、萨莫耶德、雅库特等）的萨满宇宙观与动物祖灵传说，核心涉及多层天界、精灵信仰与萨满出神。材料经民族志记录保存，本文如实标注。",
        "versions": [
            "西伯利亚诸民族的萨满宇宙观以多层天界与精灵信仰为特征，具体层数与神名因民族而异。",
            "动物祖灵与图腾母题在狩猎民族传统中占有核心地位，与生计方式相关。",
            "近代民族志记录与当代社群叙述之间存在语境差异，重建原貌需谨慎。"
        ],
        "interpretations": [
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《萨满教》中把西伯利亚萨满的升天、宇宙层界与出神经验系统化，视为理解萨满教的经典范例，其普遍性在学界有讨论。"},
            {"holder": "Åke Hultkrantz", "school": "宗教民族学", "view": "Hultkrantz 强调西伯利亚萨满实践须结合各民族的生态与生计方式理解，反对把复杂传统简化为统一样板，其方法论见其区域研究。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "Lévi-Strauss 在《结构人类学》中以萨满的象征治疗说明神话思维如何组织自然—文化范畴，属方法论参照。"}
        ],
        "comparisons": [
            {"tradition": "北美原住民萨满", "basis_source": "aca-shamanism", "note": "Eliade 的萨满教研究把西伯利亚与北美萨满并置讨论，属有文献依据的对照，不主张直接同源。"},
            {"tradition": "乌戈尔神话", "basis_source": "aca-religions-american-indians", "note": "Hultkrantz 的区域宗教研究作萨满比较的一般参照（该书以美洲为主，此处仅作方法参照），弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>西伯利亚萨满宇宙观示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>西伯利亚萨满宇宙观（示意）</text><rect x='250' y='80' width='260' height='40' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='106' text-anchor='middle' fill='var(--svg-text)' font-size='13'>上层天界</text><rect x='250' y='150' width='260' height='40' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='176' text-anchor='middle' fill='var(--svg-text)' font-size='13'>中层：人间</text><rect x='250' y='220' width='260' height='40' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='246' text-anchor='middle' fill='var(--svg-text)' font-size='13'>下层：精灵与亡者</text><line x1='380' y1='260' x2='380' y2='298' stroke='currentColor' opacity='0.5'/><rect x='280' y='298' width='200' height='40' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='324' text-anchor='middle' fill='var(--svg-text)' font-size='12'>萨满出神穿越层界</text></svg>",
        "pending_notes": "1) 各民族宇宙观差异大，层数神名待核；2) 近代民族志记录语境需考虑；3) 北美/美洲来源参照为方法弱参照，不主张同源。",
        "needs_verification": True
    },
    "myth-etruscan": {
        "level": "L2",
        "source_text": "伊特鲁里亚神话指意大利伊特鲁里亚文明的神祇与占卜传统，材料零散，主要经罗马文献转述与考古遗物（如铜镜、壁画）间接重建。由于缺乏本土神话文本，任何解读都属推测，本文如实标注。",
        "versions": [
            "伊特鲁里亚神祇多经罗马文献与考古图像推断，缺乏同时期可释读的神话文本。",
            "占卜术（肠卜、雷电占）是伊特鲁里亚宗教的显著特征，后为罗马所吸收。",
            "伊特鲁里亚神祇与希腊、罗马神祇的对应为学界讨论议题，具体关系无定论。"
        ],
        "interpretations": [
            {"holder": "Massimo Pallottino", "school": "伊特鲁里亚学", "view": "Pallottino 在《The Etruscans》中主张伊特鲁里亚宗教须据考古与图像材料重建，强调其本土特征与对罗马的影响，反对简单视作希腊的翻版；该著作未录入 sources.json。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《永恒回归的神话》中关于占卜与宇宙秩序的论述，可用于理解伊特鲁里亚占卜术如何被视为解读神意的技术，属理论参照。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "Lévi-Strauss 在《结构人类学》中的结构方法可分析伊特鲁里亚神祇对应关系中的分类逻辑，属方法论参照。"}
        ],
        "comparisons": [
            {"tradition": "希腊神话", "basis_source": "enc-wiki-list-myth", "note": "以权威百科条目作地中海背景的一般参照（该来源未在线核验），弱参照，不推断同源。"},
            {"tradition": "罗马神话", "basis_source": "ins-met", "note": "以大都会博物馆藏品资料作考古背景参照（该机构页未在线核验），弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>伊特鲁里亚神话材料示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>伊特鲁里亚：考古重建（示意）</text><rect x='80' y='120' width='180' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='144' text-anchor='middle' fill='var(--svg-text)' font-size='13'>铜镜·壁画</text><text x='170' y='164' text-anchor='middle' fill='var(--svg-text)' font-size='12'>图像材料</text><rect x='300' y='120' width='180' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='390' y='144' text-anchor='middle' fill='var(--svg-text)' font-size='13'>罗马文献</text><text x='390' y='164' text-anchor='middle' fill='var(--svg-text)' font-size='12'>转述</text><rect x='520' y='120' width='180' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='610' y='144' text-anchor='middle' fill='var(--svg-text)' font-size='13'>占卜术</text><text x='610' y='164' text-anchor='middle' fill='var(--svg-text)' font-size='12'>肠卜·雷电</text><text x='380' y='250' text-anchor='middle' fill='var(--svg-text)' font-size='13'>缺乏本土神话文本，解读属推测</text><text x='380' y='300' text-anchor='middle' fill='var(--svg-text)' font-size='12'>后为罗马宗教所吸收</text></svg>",
        "pending_notes": "1) 缺乏本土神话文本，一切解读为考古推断；2) Pallottino 著作未录入 sources.json，已声明；3) 百科/机构来源未在线核验，标弱参照。",
        "needs_verification": True
    },
    "myth-phoenician": {
        "level": "L2",
        "source_text": "腓尼基神话指古代腓尼基城邦（如推罗、西顿）的神祇崇拜，核心神祇包括埃尔、巴力与梅尔卡特，材料经古典作者记载、乌加里特文献与考古铭文间接保存。本文只记录有文献依据的对照。",
        "versions": [
            "腓尼基城邦的巴力与梅尔卡特崇拜与航海、殖民活动相关，各城邦主神略有不同。",
            "乌加里特文献（属邻近迦南传统）为理解腓尼基神祇提供了重要参照，但二者不完全等同。",
            "希腊罗马作者对腓尼基神祇的记述带有其自身立场，需谨慎使用。"
        ],
        "interpretations": [
            {"holder": "Frank Moore Cross", "school": "迦南与希伯来宗教研究", "view": "Cross 在《Canaanite Myth and Hebrew Epic》中通过乌加里特材料研究迦南—腓尼基神祇，指出巴力等神祇与希伯来传统的关联与差异；该著作未录入 sources.json。"},
            {"holder": "Theodor H. Gaster", "school": "圣经民俗与比较宗教学", "view": "Gaster 在《旧约中的神话、传说与习俗》中以民俗学方法比较腓尼基—迦南材料与旧约，属专门研究，不替信仰表态。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《比较宗教的模式》中关于丰产与风暴神祇的论述，可为理解巴力母题提供现象学参照。"}
        ],
        "comparisons": [
            {"tradition": "迦南神话", "basis_source": "aca-myth-legend-custom", "note": "Gaster 的旧约民俗研究记录了乌加里特—迦南材料，与腓尼基作有文献依据的关联，不主张完全等同。"},
            {"tradition": "希腊神话", "basis_source": "enc-brit-mythology", "note": "以权威百科条目作地中海背景的一般参照（该来源未在线核验），弱参照，不推断同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>腓尼基神话神祇示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>腓尼基城邦神祇（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>腓尼基神系</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>埃尔</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>至高神</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>巴力</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>风暴·丰产</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>梅尔卡特</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>推罗主神·航海</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>经古典记载与乌加里特文献间接保存</text></svg>",
        "pending_notes": "1) 腓尼基与迦南传统不完全等同，正文已区分；2) Cross 著作未录入 sources.json，已声明；3) 百科来源未在线核验，标弱参照。",
        "needs_verification": True
    },
    "myth-thracian": {
        "level": "L2",
        "source_text": "色雷斯神话指古代色雷斯人的神祇信仰，以扎尔莫克西斯（Zalmoxis）等神祇著称，材料零散，主要经希腊作者记载与考古间接保存。本文如实标注材料局限。",
        "versions": [
            "希腊作者（如希罗多德）记载色雷斯的扎尔莫克西斯信仰与不死观念，带有其自身立场。",
            "色雷斯神祇与印欧、色雷斯—达契亚传统的关系为学界讨论议题。",
            "缺乏本土神话文本，色雷斯宗教的重建依赖间接材料，需谨慎。"
        ],
        "interpretations": [
            {"holder": "Georges Dumézil", "school": "印欧比较神话学", "view": "Dumézil 在《印欧人的神》的印欧框架内讨论色雷斯—达契亚神祇的可能位置，属学派比较，具体对应有争论。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《萨满教》与《永恒回归的神话》中讨论扎尔莫克西斯与不死、秘传的关联，指出其可能的萨满式特征，属理论参照。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "Lévi-Strauss 在《结构人类学》中的结构方法可用于分析色雷斯不死观念中的生死对立，属方法论参照。"}
        ],
        "comparisons": [
            {"tradition": "希腊神话", "basis_source": "enc-brit-mythology", "note": "以权威百科条目作希腊—色雷斯背景的一般参照（该来源未在线核验），弱参照，不推断同源。"},
            {"tradition": "印欧传统", "basis_source": "aca-gods-indo-europeans", "note": "Dumézil 的印欧框架作一般参照，具体对应有争论，不主张同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>色雷斯神话材料示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>色雷斯：扎尔莫克西斯与不死（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>扎尔莫克西斯</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>不死观念</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>秘传</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>希腊记载</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>希罗多德</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>印欧关联</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>比较研究</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>缺乏本土文本，依赖间接材料重建</text></svg>",
        "pending_notes": "1) 材料零散、缺乏本土文本，重建须谨慎；2) 印欧对应为学派框架，有争论；3) 百科来源未在线核验，标弱参照。",
        "needs_verification": True
    },
    "myth-korean": {
        "level": "L2",
        "source_text": "朝鲜神话指朝鲜半岛的建国神话（檀君、朱蒙）与巫俗传统，材料见于《三国遗事》《三国史记》等汉文文献与口传。建国叙事带有政治与宗教语境，本文只记录有文献依据的对照。",
        "versions": [
            "《三国遗事》记载檀君神话（桓雄、熊女、檀君建国），是朝鲜建国叙事的核心文本。",
            "《三国史记》记载朱蒙（东明王）传说，与高句丽建国叙事相关。",
            "檀君、朱蒙叙事经后世整理，其史实性与编纂意图为学界讨论议题。"
        ],
        "interpretations": [
            {"holder": "James Huntley Grayson", "school": "朝鲜宗教史研究", "view": "Grayson 在《Korea: A Religious History》中主张朝鲜建国神话须置于其政治与巫俗宗教脉络中理解，强调檀君叙事与王权合法性的关联；该著作未录入 sources.json。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《永恒回归的神话》中关于建国与宇宙创生重演的论述，可说明檀君神话如何为王朝提供神圣起源，属理论参照。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "Lévi-Strauss 在《结构人类学》中的结构方法可分析檀君神话中天—地、人—兽的对立与中介，属方法论参照。"}
        ],
        "comparisons": [
            {"tradition": "中国神话", "basis_source": "enc-wiki-list-myth", "note": "以权威百科条目作东亚背景的一般参照（该来源未在线核验），弱参照，不推断同源。"},
            {"tradition": "日本神话", "basis_source": "ins-world-history", "note": "以机构资料作东亚建国神话背景的一般参照（该来源未在线核验），弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>朝鲜建国神话示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>朝鲜建国神话：檀君与朱蒙（示意）</text><rect x='80' y='130' width='240' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='200' y='154' text-anchor='middle' fill='var(--svg-text)' font-size='13'>檀君神话</text><text x='200' y='174' text-anchor='middle' fill='var(--svg-text)' font-size='12'>桓雄·熊女·建国</text><rect x='440' y='130' width='240' height='60' fill='var(--svg-node)' stroke='currentColor'/><text x='560' y='154' text-anchor='middle' fill='var(--svg-text)' font-size='13'>朱蒙传说</text><text x='560' y='174' text-anchor='middle' fill='var(--svg-text)' font-size='12'>高句丽建国</text><rect x='230' y='250' width='300' height='54' fill='var(--svg-node)' stroke='currentColor' opacity='0.7'/><text x='380' y='274' text-anchor='middle' fill='var(--svg-text)' font-size='13'>《三国遗事》《三国史记》</text><text x='380' y='294' text-anchor='middle' fill='var(--svg-text)' font-size='12'>汉文文献与口传保存</text></svg>",
        "pending_notes": "1) 建国叙事的史实性与编纂意图待核；2) Grayson 著作未录入 sources.json，已声明；3) 百科/机构来源未在线核验，标弱参照。",
        "needs_verification": True
    },
    "myth-basque": {
        "level": "L2",
        "source_text": "巴斯克神话指巴斯克地区的传统信仰，以大地女神安博托（Mari）与化身为蛇的 Mali 等传说著称，材料主要经口传与近代民族志记录保存。巴斯克语非印欧语，其神话渊源为研究议题。",
        "versions": [
            "巴斯克民间传统以安博托（Mari）为大地与气象的主宰，其居所与巴斯克各地的山洞相关。",
            "化身为蛇的传说与巴斯克家屋、亲缘观念相连，反映其独特的社会结构。",
            "口传材料经近代民族志记录，与基督教化后的民间信仰交融，原貌需谨慎重建。"
        ],
        "interpretations": [
            {"holder": "José Miguel de Barandiarán", "school": "巴斯克民族学", "view": "Barandiarán 在《Mitología vasca》中作为巴斯克民族学奠基者，主张以田野调查与口传记录重建巴斯克传统信仰，强调其史前根源；该著作未录入 sources.json。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《永恒回归的神话》中关于大地母神与宇宙中心的论述，可用于理解安博托作为大地主宰的象征，属理论参照。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "Lévi-Strauss 在《结构人类学》中的结构方法可分析安博托—蛇传说中自然与家屋的对立，属方法论参照。"}
        ],
        "comparisons": [
            {"tradition": "伊比利亚传统", "basis_source": "enc-wiki-list-myth", "note": "以权威百科条目作区域背景的一般参照（该来源未在线核验），弱参照，不推断同源。"},
            {"tradition": "印欧神话", "basis_source": "enc-brit-mythology", "note": "以权威百科条目作印欧背景的一般参照（该来源未在线核验）；巴斯克语非印欧语，比较须谨慎，弱参照。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>巴斯克神话示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>巴斯克：大地女神安博托（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>安博托（Mari）</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>大地</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>气象主宰</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>山洞居所</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>地方圣所</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>蛇化身</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>家屋·亲缘</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>巴斯克语非印欧语，渊源为研究议题</text></svg>",
        "pending_notes": "1) 口传材料经民族志记录，原貌需谨慎重建；2) Barandiarán 著作未录入 sources.json，已声明；3) 百科来源未在线核验，弱参照；巴斯克语非印欧语，印欧比较须谨慎。",
        "needs_verification": True
    },
    "myth-micronesian": {
        "level": "L2",
        "source_text": "密克罗尼西亚神话指密克罗尼西亚群岛的岛屿创世、航海与祖灵传说，材料主要经口传与20世纪以来的民族志记录保存。各岛群传统有联系也有差异，本文如实标注材料局限。",
        "versions": [
            "密克罗尼西亚各岛群的创世叙事以岛屿从海中升起、祖灵化生等母题为特征，细节因岛群而异。",
            "航海传说反映密克罗尼西亚人的海洋文化与导航知识，口传版本随移民演变。",
            "殖民时期记录与当代社群叙述之间存在语境差异，解读需谨慎。"
        ],
        "interpretations": [
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《永恒回归的神话》中关于宇宙创生与中心的论述，可说明岛屿创世叙事如何把岛屿确立为神圣空间，属理论参照。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "Lévi-Strauss 在《结构人类学》中的结构方法可分析海洋—陆地、祖灵—后裔的分类逻辑，属方法论参照。"},
            {"holder": "Åke Hultkrantz", "school": "宗教民族学", "view": "Hultkrantz 在《The Religions of the American Indians》等方法论著作中强调，海洋/区域民族的口传传统须结合其生计方式理解，这一宗教民族学方法主张回到具体语境、避免脱离生计方式的抽象比较。"}
        ],
        "comparisons": [
            {"tradition": "波利尼西亚神话", "basis_source": "enc-wiki-list-myth", "note": "以权威百科条目作太平洋背景的一般参照（该来源未在线核验），弱参照，不推断同源。"},
            {"tradition": "美拉尼西亚传统", "basis_source": "ins-world-history", "note": "以机构资料作大洋洲区域背景的一般参照（该来源未在线核验），弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>密克罗尼西亚神话示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>密克罗尼西亚：岛屿与航海（示意）</text><ellipse cx='380' cy='200' rx='120' ry='60' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='205' text-anchor='middle' fill='var(--svg-text)' font-size='14'>岛屿</text><text x='160' y='140' text-anchor='middle' fill='var(--svg-text)' font-size='13'>岛屿升起</text><text x='600' y='140' text-anchor='middle' fill='var(--svg-text)' font-size='13'>航海传说</text><text x='160' y='280' text-anchor='middle' fill='var(--svg-text)' font-size='13'>祖灵化生</text><text x='600' y='280' text-anchor='middle' fill='var(--svg-text)' font-size='13'>导航知识</text><line x1='260' y1='170' x2='170' y2='150' stroke='currentColor' opacity='0.4'/><line x1='500' y1='170' x2='590' y2='150' stroke='currentColor' opacity='0.4'/><text x='380' y='330' text-anchor='middle' fill='var(--svg-text)' font-size='13'>各岛群传统有联系也有差异</text></svg>",
        "pending_notes": "1) 各岛群传统差异大，口传经民族志记录；2) 殖民记录语境已标注；3) 百科/机构来源未在线核验，弱参照。",
        "needs_verification": True
    },
    "myth-plains-native": {
        "level": "L2",
        "source_text": "北美平原原住民神话指大平原诸部落的创世、太阳舞与野牛传说，材料主要经口传与民族志记录保存。各部落传统差异显著，本文只记录有文献依据的对照。",
        "versions": [
            "平原诸部落的太阳舞仪式与创世、更新主题相关，具体形态因部落而异。",
            "野牛（bison）在平原生计与神话中占有核心地位，相关传说与狩猎文化相连。",
            "口传材料经19世纪以来民族志记录，与当代部落叙述之间存在语境差异。"
        ],
        "interpretations": [
            {"holder": "Åke Hultkrantz", "school": "宗教民族学（北美研究）", "view": "Hultkrantz 在《The Religions of the American Indians》中系统研究北美原住民宗教，强调平原部落的太阳舞与宇宙更新观念须结合其生计与社群理解。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《永恒回归的神话》中关于仪式更新与宇宙周期的论述，可说明太阳舞如何重演宇宙秩序，属理论参照。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "Lévi-Strauss 在《结构人类学》中的结构方法可分析野牛—猎人、神圣—世俗的对立分类，属方法论参照。"}
        ],
        "comparisons": [
            {"tradition": "北美西北海岸传统", "basis_source": "aca-religions-american-indians", "note": "Hultkrantz 的区域研究把北美诸区域宗教并置讨论，属有文献依据的对照，不主张完全等同。"},
            {"tradition": "西伯利亚萨满传统", "basis_source": "enc-wiki-list-myth", "note": "以权威百科条目作跨区域母题的一般参照（该来源未在线核验），弱参照，不推断同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>北美平原原住民神话示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>北美平原：太阳舞与野牛（示意）</text><circle cx='380' cy='160' r='50' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='166' text-anchor='middle' fill='var(--svg-text)' font-size='13'>太阳</text><rect x='110' y='250' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='200' y='274' text-anchor='middle' fill='var(--svg-text)' font-size='13'>太阳舞</text><text x='200' y='292' text-anchor='middle' fill='var(--svg-text)' font-size='12'>宇宙更新</text><rect x='470' y='250' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='560' y='274' text-anchor='middle' fill='var(--svg-text)' font-size='13'>野牛传说</text><text x='560' y='292' text-anchor='middle' fill='var(--svg-text)' font-size='12'>狩猎文化</text><line x1='380' y1='210' x2='290' y2='250' stroke='currentColor' opacity='0.4'/><line x1='380' y1='210' x2='470' y2='250' stroke='currentColor' opacity='0.4'/><text x='380' y='348' text-anchor='middle' fill='var(--svg-text)' font-size='12'>各部落传统差异显著</text></svg>",
        "pending_notes": "1) 各部落传统差异显著，口传经民族志记录；2) 与西北海岸/西伯利亚的比较为区域/弱参照，不主张同源。",
        "needs_verification": True
    },
    "myth-northwest-native": {
        "level": "L2",
        "source_text": "北美西北海岸原住民神话指该地区诸部落（如海达、特林吉特）的乌鸦、逆戟鲸与氏族起源传说，材料经口传与民族志记录保存，与图腾柱、夸富宴等制度相连。",
        "versions": [
            "乌鸦在西北海岸神话中兼具创世者与诡计者两面，相关传说解释光、潮汐等自然现象。",
            "氏族起源传说与图腾、家屋和夸富宴制度相连，构成社会结构的叙事基础。",
            "口传材料经19世纪以来民族志记录，与当代部落叙述之间存在语境差异。"
        ],
        "interpretations": [
            {"holder": "Åke Hultkrantz", "school": "宗教民族学（北美研究）", "view": "Hultkrantz 在《The Religions of the American Indians》中讨论西北海岸的图腾与氏族宗教，强调其与社会制度、海洋生计的关联。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "Lévi-Strauss 在《结构人类学》中以西北海岸的图腾与面具艺术说明神话思维的分类逻辑，属方法论参照。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《神圣与世俗》中关于神圣与世俗空间的论述，可说明家屋与图腾如何把社会秩序神圣化，属理论参照。"}
        ],
        "comparisons": [
            {"tradition": "北美平原传统", "basis_source": "aca-religions-american-indians", "note": "Hultkrantz 的区域研究把北美诸区域宗教并置讨论，属有文献依据的对照，不主张完全等同。"},
            {"tradition": "西伯利亚萨满传统", "basis_source": "ins-british-museum", "note": "以大英博物馆藏品资料作跨区域母题的一般参照（该机构页未在线核验），弱参照，不推断同源。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>西北海岸神话示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>西北海岸：乌鸦与氏族（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>乌鸦</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>创世</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>光·潮汐</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>诡计者</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>机智狡黠</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>氏族起源</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>图腾·夸富宴</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>口传经民族志记录保存</text></svg>",
        "pending_notes": "1) 口传经民族志记录，语境差异需考虑；2) 与平原/西伯利亚的比较为区域/弱参照，不主张同源。",
        "needs_verification": True
    },
    "myth-berber": {
        "level": "L2",
        "source_text": "柏柏尔神话指北非柏柏尔人的传统信仰，涉及自然神、精灵与地方圣所，材料零散，主要经古典记载、考古与近代民族志间接保存。柏柏尔语非阿拉伯语，传统有其自身渊源。",
        "versions": [
            "柏柏尔传统中的自然神与精灵信仰见于古典记载与近代民族志，原貌多经伊斯兰化改写。",
            "地方圣所与圣地崇拜在柏柏尔社群中长期延续，与伊斯兰圣徒崇拜交融。",
            "柏柏尔神话与古埃及、迦太基等邻近传统的关系为研究议题，材料有限。"
        ],
        "interpretations": [
            {"holder": "Gabriel Camps", "school": "柏柏尔学与北非研究", "view": "Camps 主编《Encyclopédie berbère》，主张柏柏尔传统须综合语言学、考古与民族志研究，强调其本土延续性；该著作未录入 sources.json。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《永恒回归的神话》中关于圣地与中心的神圣化论述，可说明柏柏尔地方圣所的宗教意涵，属理论参照。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "Lévi-Strauss 在《结构人类学》中的结构方法可分析柏柏尔自然神与精灵信仰中的分类逻辑，属方法论参照。"}
        ],
        "comparisons": [
            {"tradition": "古埃及宗教", "basis_source": "enc-wiki-list-myth", "note": "以权威百科条目作北非背景的一般参照（该来源未在线核验），弱参照，不推断同源。"},
            {"tradition": "迦太基传统", "basis_source": "ins-world-history", "note": "以机构资料作地中海—北非背景的一般参照（该来源未在线核验），弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>柏柏尔神话示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>柏柏尔：自然神与地方圣所（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>柏柏尔传统</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>自然神</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>古典记载</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>精灵信仰</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>民族志记录</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>地方圣所</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>圣地崇拜</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>材料零散，多经伊斯兰化改写</text></svg>",
        "pending_notes": "1) 材料零散、多经伊斯兰化改写，重建须谨慎；2) Camps 著作未录入 sources.json，已声明；3) 百科/机构来源未在线核验，弱参照。",
        "needs_verification": True
    },
    "rel-caodai": {
        "level": "L2",
        "source_text": "高台教是20世纪在越南兴起的融合型宗教，1926年正式创立，糅合佛教、道教、儒教与天主教等元素，以“三期普度”与 Cao Đài 至高神为核心。本文采用学术描述性立场，不评判信仰真伪。",
        "versions": [
            "高台教创立于1926年的越南，其教义融合多种宗教传统，反映近代越南的宗教与社会语境。",
            "高台教的组织与仪轨吸收天主教、佛教等形式，形成独特的混合形态。",
            "高台教在越南近现代史中与民族主义、社会运动有交集，其发展经历政治变迁。"
        ],
        "interpretations": [
            {"holder": "Stephen Prothero", "school": "比较宗教学", "view": "Prothero 在《God Is Not One》中把高台教等新兴融合宗教作为宗教多样性的案例，强调其独特目标而非简单归并，属通俗学术著作观点。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《神圣与世俗》中关于宗教融合与神圣显现的论述，可说明高台教如何整合多种传统的神圣符号，属理论参照。"},
            {"holder": "Émile Durkheim", "school": "宗教社会学", "view": "Durkheim 在《宗教生活的基本形式》中关于宗教作为社会集体表征的理论，可分析高台教在越南社会整合中的功能，属社会学框架。"}
        ],
        "comparisons": [
            {"tradition": "越南民间宗教", "basis_source": "enc-wiki-world-religion", "note": "以百科条目作越南宗教背景的一般参照（该来源未在线核验），弱参照，不主张同源。"},
            {"tradition": "其他新兴宗教", "basis_source": "ins-pluralism", "note": "以哈佛 Pluralism 项目资料作新兴宗教背景的一般参照（该机构页未在线核验），弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>高台教融合结构示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>高台教：融合型宗教（描述性示意）</text><rect x='300' y='88' width='160' height='44' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='116' text-anchor='middle' fill='var(--svg-text)' font-size='13'>高台（Cao Đài）</text><line x1='380' y1='132' x2='380' y2='166' stroke='currentColor' opacity='0.5'/><line x1='130' y1='166' x2='630' y2='166' stroke='currentColor' opacity='0.5'/><line x1='130' y1='166' x2='130' y2='204' stroke='currentColor' opacity='0.5'/><line x1='290' y1='166' x2='290' y2='204' stroke='currentColor' opacity='0.5'/><line x1='450' y1='166' x2='450' y2='204' stroke='currentColor' opacity='0.5'/><line x1='630' y1='166' x2='630' y2='204' stroke='currentColor' opacity='0.5'/><rect x='50' y='204' width='160' height='50' fill='var(--svg-node)' stroke='currentColor'/><text x='130' y='234' text-anchor='middle' fill='var(--svg-text)' font-size='13'>佛教</text><rect x='210' y='204' width='160' height='50' fill='var(--svg-node)' stroke='currentColor'/><text x='290' y='234' text-anchor='middle' fill='var(--svg-text)' font-size='13'>道教</text><rect x='370' y='204' width='160' height='50' fill='var(--svg-node)' stroke='currentColor'/><text x='450' y='234' text-anchor='middle' fill='var(--svg-text)' font-size='13'>儒教</text><rect x='550' y='204' width='160' height='50' fill='var(--svg-node)' stroke='currentColor'/><text x='630' y='234' text-anchor='middle' fill='var(--svg-text)' font-size='13'>天主教</text><text x='380' y='310' text-anchor='middle' fill='var(--svg-text)' font-size='13'>1926年创立，近代越南融合型宗教</text><text x='380' y='340' text-anchor='middle' fill='var(--svg-text)' font-size='12'>描述性立场，不评判信仰真伪</text></svg>",
        "pending_notes": "1) 高台教教义与组织细节待专门文献核对；2) 百科/机构来源未在线核验，标弱参照；3) 描述性立场，不替信仰表态。",
        "needs_verification": True
    },
    "rel-tenrikyo": {
        "level": "L2",
        "source_text": "天理教是19世纪在日本兴起的新宗教，由中山美伎于1838年创立，以“天理王命”为至高神、强调“阳気づとめ”（喜勤）与救济实践。本文采用学术描述性立场，不评判信仰真伪。",
        "versions": [
            "天理教由中山美伎创立，其教义围绕天理王命与人类本来平等、互助救济的理念展开。",
            "天理教在近代日本经历制度化与海外传播，组织形态随时代演变。",
            "天理教与神道、佛教等传统有交融，也保有自身独特的仪礼与教义。"
        ],
        "interpretations": [
            {"holder": "Stephen Prothero", "school": "比较宗教学", "view": "Prothero 在《God Is Not One》中把天理教等新兴宗教作为宗教多样性的案例，强调其独特目标而非简单归并，属通俗学术著作观点。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《神圣与世俗》中关于神圣显现与救赎的论述，可说明天理教的救济实践如何被赋予神圣意义，属理论参照。"},
            {"holder": "Émile Durkheim", "school": "宗教社会学", "view": "Durkheim 在《宗教生活的基本形式》中关于宗教作为社会集体表征的理论，可分析天理教在近代日本社会整合与救济中的功能。"}
        ],
        "comparisons": [
            {"tradition": "日本新兴宗教", "basis_source": "enc-wiki-world-religion", "note": "以百科条目作日本宗教背景的一般参照（该来源未在线核验），弱参照，不主张同源。"},
            {"tradition": "神道教", "basis_source": "ins-pluralism", "note": "以哈佛 Pluralism 项目资料作日本宗教多元背景的一般参照（该机构页未在线核验），弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>天理教结构示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>天理教（描述性示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>天理王命</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>救济实践</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>喜勤</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>平等互助</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>本来平等</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>海外传播</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>制度化</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>1838年创立，描述性立场</text></svg>",
        "pending_notes": "1) 天理教教义与组织细节待专门文献核对；2) 百科/机构来源未在线核验，标弱参照；3) 描述性立场，不替信仰表态。",
        "needs_verification": True
    },
    "rel-yiguandao": {
        "level": "L2",
        "source_text": "一贯道是源于中国、盛行于近现代的民间宗教结社，融合儒、释、道与民间信仰，以“明明上帝”为至高神、强调三宝与普度。本文采用学术描述性立场，不评判信仰真伪。",
        "versions": [
            "一贯道融合儒释道与民间信仰，其教义以明明上帝、三宝心法与普度为核心。",
            "一贯道在20世纪的传播经历社会与政治变迁，组织形态与活动随之演变。",
            "一贯道与其他民间宗教结社在教义与仪轨上既有交融也有差异。"
        ],
        "interpretations": [
            {"holder": "Stephen Prothero", "school": "比较宗教学", "view": "Prothero 在《God Is Not One》中把一贯道等融合型民间宗教作为宗教多样性案例，强调其独特目标而非简单归并，属通俗学术著作观点。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《神圣与世俗》中关于神圣显现与救度的论述，可说明一贯道三宝心法的宗教意涵，属理论参照。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "Lévi-Strauss 在《结构人类学》中的结构方法可分析一贯道三教融合中的分类与调和逻辑，属方法论参照。"}
        ],
        "comparisons": [
            {"tradition": "中国民间宗教", "basis_source": "enc-wiki-world-religion", "note": "以百科条目作中国民间宗教背景的一般参照（该来源未在线核验），弱参照，不主张同源。"},
            {"tradition": "其他新兴宗教", "basis_source": "ins-pluralism", "note": "以哈佛 Pluralism 项目资料作新兴宗教背景的一般参照（该机构页未在线核验），弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>一贯道融合结构示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>一贯道：三教融合（描述性示意）</text><rect x='300' y='88' width='160' height='44' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='116' text-anchor='middle' fill='var(--svg-text)' font-size='13'>明明上帝</text><line x1='380' y1='132' x2='380' y2='166' stroke='currentColor' opacity='0.5'/><line x1='160' y1='166' x2='600' y2='166' stroke='currentColor' opacity='0.5'/><line x1='160' y1='166' x2='160' y2='204' stroke='currentColor' opacity='0.5'/><line x1='380' y1='166' x2='380' y2='204' stroke='currentColor' opacity='0.5'/><line x1='600' y1='166' x2='600' y2='204' stroke='currentColor' opacity='0.5'/><rect x='80' y='204' width='160' height='50' fill='var(--svg-node)' stroke='currentColor'/><text x='160' y='234' text-anchor='middle' fill='var(--svg-text)' font-size='13'>儒</text><rect x='300' y='204' width='160' height='50' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='234' text-anchor='middle' fill='var(--svg-text)' font-size='13'>释</text><rect x='520' y='204' width='160' height='50' fill='var(--svg-node)' stroke='currentColor'/><text x='600' y='234' text-anchor='middle' fill='var(--svg-text)' font-size='13'>道</text><text x='380' y='300' text-anchor='middle' fill='var(--svg-text)' font-size='13'>三宝心法·普度</text><text x='380' y='336' text-anchor='middle' fill='var(--svg-text)' font-size='12'>描述性立场，不评判信仰真伪</text></svg>",
        "pending_notes": "1) 一贯道教义与传播史待专门文献核对；2) 百科/机构来源未在线核验，标弱参照；3) 描述性立场，不替信仰表态。",
        "needs_verification": True
    },
    "fig-quetzalcoatl": {
        "level": "L2",
        "source_text": "羽蛇神（魁札尔科亚特尔，Quetzalcoatl）是中部美洲神话中的重要神祇，兼具风、智慧、王权与创造等职能，见于托尔特克与阿兹特克传统及考古图像。其身份兼有神祇与历史祭司—统治者叙事层次。",
        "versions": [
            "羽蛇神在中部美洲传统中兼具丰产、风与智慧职能，不同时期与地区的形象侧重有差异。",
            "关于羽蛇神与托尔特克统治者（如 Topiltzin Quetzalcoatl）的关联，文献记载与学术解读存在争议。",
            "西班牙征服时期的记录与本土编年史对羽蛇神的描述立场不同，需互证。"
        ],
        "interpretations": [
            {"holder": "Joseph Campbell", "school": "比较神话学（单一神话模型）", "view": "Campbell 在《千面英雄》中把羽蛇神式的文化英雄纳入英雄旅程讨论，属分析模型，学界对其概括性有批评。"},
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《永恒回归的神话》中关于宇宙秩序与神圣显现的论述，可说明羽蛇神作为文明赐予者的象征，属理论参照。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "Lévi-Strauss 在《结构人类学》中的结构方法可分析羽蛇（天/地、鸟/蛇）的中介象征，属方法论参照。"}
        ],
        "comparisons": [
            {"tradition": "玛雅神话", "basis_source": "ins-world-history", "note": "以机构资料作中部美洲背景的一般参照（该来源未在线核验），弱参照，不推断同源。"},
            {"tradition": "阿兹特克神话", "basis_source": "enc-wiki-list-myth", "note": "以权威百科条目作阿兹特克背景的一般参照（该来源未在线核验），弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>羽蛇神职能示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>羽蛇神：神祇与文明赐予者（示意）</text><rect x='290' y='92' width='180' height='46' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='122' text-anchor='middle' fill='var(--svg-text)' font-size='14'>羽蛇神</text><line x1='380' y1='138' x2='380' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='590' y2='174' stroke='currentColor' opacity='0.5'/><line x1='170' y1='174' x2='170' y2='212' stroke='currentColor' opacity='0.5'/><line x1='380' y1='174' x2='380' y2='212' stroke='currentColor' opacity='0.5'/><line x1='590' y1='174' x2='590' y2='212' stroke='currentColor' opacity='0.5'/><rect x='80' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='170' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>风与智慧</text><text x='170' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>文明赐予</text><rect x='290' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>王权</text><text x='380' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>祭司—统治者</text><rect x='500' y='212' width='180' height='54' fill='var(--svg-node)' stroke='currentColor'/><text x='590' y='236' text-anchor='middle' fill='var(--svg-text)' font-size='13'>创世</text><text x='590' y='254' text-anchor='middle' fill='var(--svg-text)' font-size='12'>秩序建立</text><text x='380' y='320' text-anchor='middle' fill='var(--svg-text)' font-size='13'>神祇与历史叙事层次并存，解读有争议</text></svg>",
        "pending_notes": "1) 羽蛇神与托尔特克统治者的关联有争议，正文不下定论；2) 三种解读为框架/方法论参照，具体论点待专门文献核对；3) 百科/机构来源未在线核验，标弱参照。",
        "needs_verification": True
    },
    "fig-mictlantecuhtli": {
        "level": "L2",
        "source_text": "米克特兰特库特利（Mictlantecuhtli）是阿兹特克神话的冥界（Mictlan）之神，与冥界九层、亡者旅程及骷髅形象相关，材料见于殖民时期记录与前殖民抄本。本文只记录有文献依据的对照。",
        "versions": [
            "米克特兰特库特利作为冥界之主，与亡者穿越九层冥界的旅程叙事相关，形象多与骷髅、猫头鹰相联系。",
            "殖民时期记录与前殖民抄本对冥界观念的描述存在立场差异，需互证。",
            "阿兹特克冥界观与玛雅等中美洲传统的冥界母题有可比之处，具体关系为研究议题。"
        ],
        "interpretations": [
            {"holder": "Mircea Eliade", "school": "宗教现象学", "view": "Eliade 在《永恒回归的神话》中把冥界旅行解读为通过仪式的象征，亡者穿越九层冥界即对应从生到死的过渡结构，属理论参照。"},
            {"holder": "Claude Lévi-Strauss", "school": "结构主义人类学", "view": "Lévi-Strauss 在《结构人类学》中的结构方法可分析冥界层级与生死对立的神话分类，属方法论参照。"},
            {"holder": "Joseph Campbell", "school": "比较神话学（单一神话模型）", "view": "Campbell 在《千面英雄》中把冥界之旅纳入英雄旅程的试炼阶段，属分析模型，学界对其概括性有批评。"}
        ],
        "comparisons": [
            {"tradition": "玛雅神话", "basis_source": "enc-wiki-list-myth", "note": "以权威百科条目作中美洲冥界母题的一般参照（该来源未在线核验），弱参照，不推断同源。"},
            {"tradition": "阿兹特克神话", "basis_source": "ins-world-history", "note": "以机构资料作阿兹特克背景的一般参照（该来源未在线核验），弱参照，待补专门文献。"}
        ],
        "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><title>阿兹特克冥界结构示意</title><rect x='10' y='10' width='740' height='380' fill='none' stroke='currentColor' opacity='0.25'/><text x='380' y='42' text-anchor='middle' fill='var(--svg-text)' font-size='20'>米克特兰特库特利与九层冥界（示意）</text><rect x='250' y='82' width='260' height='40' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='108' text-anchor='middle' fill='var(--svg-text)' font-size='13'>冥界之主</text><rect x='250' y='140' width='260' height='40' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='166' text-anchor='middle' fill='var(--svg-text)' font-size='13'>九层冥界旅程</text><rect x='250' y='198' width='260' height='40' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='224' text-anchor='middle' fill='var(--svg-text)' font-size='13'>骷髅·猫头鹰</text><rect x='250' y='256' width='260' height='40' fill='var(--svg-node)' stroke='currentColor'/><text x='380' y='282' text-anchor='middle' fill='var(--svg-text)' font-size='13'>亡者归宿</text><text x='380' y='340' text-anchor='middle' fill='var(--svg-text)' font-size='13'>殖民记录与前殖民抄本需互证</text></svg>",
        "pending_notes": "1) 冥界观念细节与殖民记录立场待核；2) 三种解读为框架/方法论参照；3) 百科/机构来源未在线核验，标弱参照。",
        "needs_verification": True
    }
}
