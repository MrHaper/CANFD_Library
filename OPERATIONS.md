# CAN FD 知识库 — 运营交接文档

> 本文档供后续维护者 / AI Agent 接手本仓库运营时阅读。**接手前请完整阅读本文档**,再开始任何修改。
> 文档版本:v1.0 · 交接日期:2026-08-02 · 上线日期:2026-08-02 · 交接基线 commit:`0e46e83`

---

## 1. 项目概览

| 项 | 值 |
|---|---|
| 站点 | https://MrHaper.github.io/CANFD_Library/ |
| 源码仓库 | https://github.com/MrHaper/CANFD_Library(main 分支 + gh-pages 部署分支) |
| 技术栈 | MkDocs Material ≥ 9.6(Python 3.9+,本机 3.14)、mkdocs-minify-plugin、jieba、GitHub Actions |
| 站点性质 | 中文 CAN FD 学习资料库:105 条资源(标准/专利/论文/期刊/教材/厂商/工具社区)+ 51 术语词条 + 12 原创教程 + 2 学习路线 + 7 知识子域 18 知识点页 |
| 目标读者 | 模拟 IC 设计工程师(主线)与嵌入式工程师(辅助) |
| 建站背景 | 团队已流片一颗 CAN FD (SIC) 收发器芯片,网站沉淀"协议→物理层→收发器设计→测试认证"全流程知识 |

**一次构建即发布:** 推送 `main` → GitHub Actions 自动 `mkdocs build` → `gh-deploy --force` 推送到 `gh-pages` 分支 → GitHub Pages 发布。

---

## 2. 快速开始(本地)

```bash
# 环境:Python 3.9+(开发机 3.14 已实测)
python -m venv .venv && source .venv/Scripts/activate   # Windows bash
pip install -r requirements.txt

# 本地预览(改 docs/ 后自动重建)
mkdocs serve

# 严格构建(上线门禁:零警告零报错)
mkdocs build --strict

# 资源数据校验(内容运营必跑;ERROR=0 才算通过)
python scripts/validate_resources.py docs/

# 校验脚本单元测试(27 个用例)
python -m pytest scripts/test_validate_resources.py -v
```

> 注意:PyYAML 的 `safe_load` 无法解析 `mkdocs.yml` 中 `!!python/object/apply:pymdownx.slugs.slugify`(PyYAML 限制,非配置错误),验证 YAML 请用 `mkdocs build` 而非 yaml.safe_load。

---

## 3. 仓库结构

```
docs/
├── index.md                 # 首页(人群入口卡/TOP10/最新收录)
├── learn/                   # 学习路线:总览 + analog-ic(6 阶段)/embedded(5)
├── knowledge/               # 知识库:7 子域(protocol/bit-timing/physical-layer/
│                            #   transceiver-design/controller/tools/project-notes)
│                            #   × 3 知识点页 + project-notes index/模板
├── tutorials/               # 12 篇原创教程(01~12 编号)+ index
├── resources/
│   ├── index.md             # 资源库总览
│   ├── standards.md …       # 7 个分类汇总页(按 priority 3/2/1 三表)
│   ├── _data/*.json         # ★ 资源元数据唯一数据源(7 个文件,105 条)
│   ├── _entries/<分类>/*.md # ★ 每条资源一个条目页(导读五节 + frontmatter)
│   └── …
├── files/<分类>/*.pdf       # 35 个公开 PDF(仅可免费获取的,版权红线见 §7.2)
├── glossary/                # 51 词条 + A-Z 索引
├── javascripts/mermaid.js   # mermaid 初始化
└── contribute.md / about.md
scripts/
├── extract_metadata.py      # 从资料库 README 提取元数据 → _data/*.json(建库用,一般不再跑)
├── validate_resources.py    # 内容运营门禁:校验 _data/*.json 与本地文件
└── test_validate_resources.py  # pytest 27 用例
mkdocs.yml                   # 站点配置(8 板块 nav/jieba 搜索/mermaid/深浅色)
user_dict.txt                # jieba 自定义词典(中文搜索分词)
.github/workflows/ci.yml     # 自动部署 workflow
```

**数据流:** `_data/*.json`(元数据)→ `_entries/<分类>/<slug>.md`(条目页,frontmatter 与 JSON 一致)→ 汇总页表格引用。**改资料先改 JSON 再同步条目页,顺序不可颠倒。**

---

## 4. 内容运营流程

### 4.1 新增/收录一份资料(标准流程)

1. **版权预检**:仅可免费公开获取的资料可托管 PDF(厂商手册/开放论文/Google Patents/Bosch 公开规范);付费资料(ISO/IEC/SAE/IEEE/教材)只给官方链接,见 §7.2。
2. **更新元数据**:在 `docs/resources/_data/<分类>.json` 增加条目,字段遵循:
   `title/type/organization/year/access(free|paid|member)/status(verified|unverified|withdrawn)/download(local|link|none)/priority(1|2|3)/audience/tags/source/local_file(可选)`。
   **禁止编造字段**:年份未知留空串,链接未知留空(source 空会出 WARNING,可接受)。
3. **生成条目页**:在 `docs/resources/_entries/<分类>/<slug>.md` 按既有模板(是什么/为什么值得读/核心内容要点/怎么读/参见 五节),frontmatter 与 JSON 逐字一致。
4. **复制 PDF**(仅 download=local):放入 `docs/files/<分类>/`,文件名与 `local_file` 值一致(`local_file` 写 `files/<分类>/<文件名>.pdf`,站点路径语义,见 §7.3)。
5. **汇总页**:在对应分类汇总页表格补一行(按 priority 分组;priority=3 置顶)。
6. **门禁**:`python scripts/validate_resources.py docs/` 必须 ERROR=0;`mkdocs build --strict` 零警告;有 pytest 改动时 `python -m pytest scripts/ -v`。
7. 提交推送,等待 Actions 构建成功,抽查线上页面。

### 4.2 勘误与更正

- 收集渠道:GitHub Issues / contribute.md 页内说明。
- 修正位置:条目页正文 + 汇总页 + `contribute.md` 勘误记录(追加一条,含日期与来源)。
- 若涉及元数据字段(作者/年份/链接),同步修正 `_data/*.json` 并重跑校验。
- 重要勘误(如"某标准实为 CAN XL"这类易混点)同时考虑在首页/相关教程加交叉提示。

### 4.3 术语表 / 教程 / 知识库维护

- **词条**(`docs/glossary/<slug>.md`):模板为 定义/位置背景/作用与影响/参见;新增词条后必须在 `glossary/index.md` 索引补一行。
- **教程**(`docs/tutorials/<NN>-*.md`):编号连续;每篇含 mermaid 图、关键结论、动手验证、参见;索引页 `tutorials/index.md` 按难度分组补行。
- **知识点**(`docs/knowledge/<子域>/<topic>.md`):是教程与词条的"锚点",三处口径必须一致(改一处要查另两处)。
- **搜索词典**:新术语加入 `user_dict.txt`(每行"词 词频",如 `振铃抑制 10`)。**禁止含空格的词条**(如 `CAN FD`)——jieba 把空格当硬分隔符,含空格词条永远无法整词切出(实测验证),应写成无空格形式(`CANFD`)。

### 4.4 链接层级铁律(改文件前必读)

页面所在目录深度决定相对链接前缀(以 docs/ 为根):

| 页面位置 | 指向站点根板块(learn/knowledge/tutorials/resources/glossary) | 指向同板块其他目录 |
|---|---|---|
| `docs/xxx.md`(根,如 index/contribute/about) | `resources/_entries/...`(无前缀) | — |
| `docs/knowledge/<子域>/xxx.md`(2 层) | `../../tutorials/...`、`../../glossary/...`、`../../resources/...` | `../<其他子域>/...` |
| `docs/resources/_entries/<分类>/xxx.md`(3 层) | `../../../files/...`、`../../../glossary/...` | `../<同分类其他条目>/...` |
| `docs/resources/xxx.md` 汇总页(1 层) | `_entries/<分类>/...`(无前缀)、`../files/...` | — |

写错层级不会报错,但点击 404——`mkdocs build --strict` 会以 WARNING 提示断链,务必清零。

---

## 5. "项目问题 → 技术分析 → 知识点"工作流(项目实践笔记)

### 5.1 触发

用户或维护者在实际项目开发中提出一个具体问题(现象、波形、测量结果均可),即进入本工作流。

### 5.2 流程

1. **记录问题背景与现象**:发生在什么项目场景、什么环境/拓扑/配置下,复现步骤与实测数据;
2. **根因分析与技术论证**:以 ISO 11898 系列标准与厂商数据手册为准,给出机理分析、图示与定量计算(中文网络资料不作技术依据,口径同 §9 维护纪律);
3. **写成知识点页**:按 `docs/knowledge/project-notes/_template.md` 模板结构(问题背景/现象 → 根因分析 → 技术分析 → 结论与设计建议 → 关联)放入 `docs/knowledge/project-notes/`,frontmatter 含 `tags: [项目实践]`;
4. **同步入口**:首页"最新收录"与 `docs/knowledge/project-notes/index.md` 知识点列表同步更新;
5. **校验门禁后发布**:`mkdocs build --strict` 零警告(涉及资源链接时 `validate_resources.py` ERROR=0),再推送发布。

### 5.3 约定

- 每个知识点页必须含:**日期**(YYYY-MM-DD)、**问题来源**(项目/场景描述)、**结论可复现**(给出验证方法或实测数据);
- 同一问题不重复成页;已有知识点覆盖时优先补充原页;
- 链接层级遵循 §4.4(project-notes 位于 knowledge 下 2 层深)。

---

## 6. 部署与发布

- workflow:`.github/workflows/ci.yml`(main 触发,`pip install -r requirements.txt` + `mkdocs gh-deploy --force`);构建产物推 `gh-pages` 分支。
- Pages 设置(已配置,勿动):仓库 Settings → Pages → Source: Deploy from a branch → `gh-pages` / `(root)`。
- **发布后验证清单**:
  1. Actions 页面 run 状态 success;
  2. 首页 200:`https://MrHaper.github.io/CANFD_Library/`;
  3. 本次改动涉及页面 200 + 新链接可点;
  4. 抽查 1 个本地 PDF 链接(如 `/files/standards/Bosch_CAN_FD_Specification_v1.0_2012.pdf`);
  5. 搜索框输入本次新资料关键词可命中。
- 环境备注:本机 push 依赖 Git Credential Manager(已配置 `credential.helper manager`);曾遇到大推送 HTTP 502,已通过 `git config http.postBuffer 524288000` 解决,若复现先检查该配置。

---

## 7. 关键决策与约定(为什么这么设计)

> 改动前先读本节——这些是踩坑后沉淀的约定,违背会引入已修过的 bug。

### 7.1 技术选型(MkDocs Material 而非 VitePress/Hugo/动态站)

静态文档站,内容为王,Markdown 驱动;Material 的搜索(jieba 中文分词 9.2.0+ 内置)、标签、导航开箱即用;维护者只需写 Markdown。否决:VitePress(中文搜索需插件)、Hugo(无 Go 环境)、手写 HTML(70+ 页不可维护)、动态 CMS(超出资料库需求)。

### 7.2 版权红线(不可违反)

**只托管可免费公开获取的 PDF**(厂商数据手册、CiA iCC 开放论文、Google Patents 专利、Bosch 公开规范)。**绝不**上传付费标准(ISO/IEC/SAE)、付费期刊、教材正文;这些资料只提供官方获取链接。收录时无法判断 → 只给链接,不放文件。

### 7.3 local_file 路径语义

`local_file` 值是**站点路径**(构建后 URL),如 `files/standards/xxx.pdf`;PDF 实际存放于 **`docs/files/`** 下(MkDocs 只复制 docs/ 到 site,故必须放 docs/ 内)。校验脚本按"相对 docs/ 目录"解析 local_file(不是仓库根)——改动脚本时不要改回 repo_root 语义。

### 7.4 元数据纪律

- 所有元数据来自资料库索引(Leaning_Library)与厂商/标准官方页面,**禁止编造**任何字段;年份解析不了留空,链接没有留空并加 WARNING。
- priority 推导:以资料库"必读 TOP 10"表为准(★★★=3/★★☆=2/★☆☆=1),不要用宽泛关键词(如"核心")推断——历史上"核心"误命中"核心内容"小标题导致大量条目被错误推为 2。
- status 如实标注 `withdrawn`(已撤销标准)并在条目页加 `!!! warning` 警示;`unverified` 加 note。

### 7.5 页面/锚点细节

- **emoji 前缀标题的锚点带前导连字符**:`## ⭐ 必读 TOP 10` 的 slug 是 `-必读-top-10`(pymdownx 把 emoji 转成连字符),页内链接必须写 `#-必读-top-10`,否则锚点失效(strict 模式会报 no such anchor)。
- mermaid 图通过 `pymdownx.superfences.custom_fences` + unpkg CDN + `docs/javascripts/mermaid.js` 启用;mermaid 是客户端渲染,`web_fetch`/无 JS 环境看不到图(构建时只要 fence 语法合法即可)。
- `_entries/` 与 `glossary/` 下的页面不在 nav 树中(经索引页/汇总页可达,搜索不受影响)——这是有意为之,勿强行加入 nav(会撑爆侧栏)。

### 7.6 中文搜索

`plugins.search` 配置 `lang: zh` + `jieba_dict_user: user_dict.txt`。用户词典不能含空格词条;新增专业术语时同步更新词典,否则分词不理想(如"振铃抑制"可能被拆开)。

---

## 8. 已知限制与遗留事项(交接时点)

| # | 事项 | 建议处理时机 |
|---|---|---|
| 1 | tools-community 4 条 source 为空(阻抗/网络分析仪、知乎CSDN、EDAboard、厂商社区),页面已加"获取渠道待补充"提示 | 有可靠 URL 时补上 |
| 2 | mermaid 依赖 unpkg CDN;CDN 故障/内网部署时图表不渲染(文本仍完整) | 有内网需求时自托管 mermaid.min.js |
| 3 | 5 条 tools 条目 description 与 JSON 非逐字一致(语义等价,前端展示优先) | 触发 JSON 同步时顺手统一 |
| 4 | `docs/` 子目录遗留 Task 1 的 8 个 `.gitkeep`(与页面并存,无害) | 清理时统一删除 |
| 5 | 控制台/日志在 Windows GBK 下中文乱码(JSON/文件内容本身 UTF-8 正常);validate_resources.py 已加 `sys.stdout.reconfigure(encoding="utf-8")` 缓解 | 不处理亦可 |
| 6 | 设计文档记载 standards 16 条,实际 17 条(IEC 62228-3 为建库补充);tools-community 20 vs 实际 23 | 以 `_data/*.json` 为准 |
| 7 | ISO 11898-2 条目/知识点提及"ISO 官网现有 2026 更新版" | 随 ISO 版本演进定期复核 |
| 8 | 教程 04 中"2 Mbit/s 以上必须开 TDC"表述偏保守(已注明以控制器手册为准) | 有实测数据时润色 |

---

## 9. 维护纪律(红线,违反即视为事故)

1. **校验门禁**:任何内容改动后 `validate_resources.py` 必须 ERROR=0、`mkdocs build --strict` 零警告;脚本改动后 pytest 27 全过。
2. **不编造**:元数据、参数数值、链接一律以资料库 README / 官方文档为准,拿不准就写"以 XX 为准"或留空。
3. **版权**:见 §7.2,只托管公开可获取 PDF。
4. **技术口径**:涉及 SIC 参数以 ISO 11898-2:2024 与厂商数据手册为准;中文网络资料(知乎/CSDN)错漏多,不可作为技术依据。
5. **链接层级**:见 §4.4 铁律,改文件位置后必须复查相对链接。
6. **单一事实源**:`_data/*.json` 是资源元数据唯一事实源,条目页与汇总页必须与它一致。

---

## 10. 运营节奏建议

| 频率 | 动作 |
|---|---|
| 月度 | 新资料入库(按 §4.1 流程);`user_dict.txt` 补新术语;检查失效外链(可抽查 source URL) |
| 季度 | 勘误合并进 `contribute.md`;清理遗留事项(#1/#3/#4);复核 ISO/CiA 版本演进(#7) |
| 年度 | 内容扩充:知识库知识点 → 教程 → 术语表滚动扩充;统计站点使用情况(如有分析工具) |

**内容扩充优先级**:知识库知识点(锚点)→ 教程 → 术语表;新增主题从学习路线的高频需求出发。

---

## 11. 交接检查清单(接手者确认)

- [ ] 已读本文档 §1~§10,本地 `mkdocs build --strict` 零警告可复现
- [ ] 已跑 `python scripts/validate_resources.py docs/`(ERROR=0)与 pytest(27 passed)
- [ ] 已在浏览器打开线上站点,8 板块导航正常,搜索"振铃抑制"可命中
- [ ] 已知悉版权红线(§7.2)、元数据纪律(§7.4)、链接层级铁律(§4.4)
- [ ] 已知悉遗留事项清单(§8)与维护纪律(§9)

---

## 12. 附录:常用命令速查

```bash
mkdocs serve                          # 本地预览
mkdocs build --strict                 # 严格构建(门禁)
python scripts/validate_resources.py docs/   # 资源数据校验(ERROR=0 通过)
python -m pytest scripts/ -v          # 校验脚本单测(27 passed)
git push origin main                  # 发布(触发 Actions 自动部署)
```

**关联文档(仓库外,项目管理侧)**:`F:\AI Agent\WorkSpace\Project_Manager\CANFD_知识库网站\项目设计文档.md`(设计规格)、`2026-08-02-实施计划.md`(18 任务实施计划)。仓库内权威文档以此 OPERATIONS.md 为准。

---

## 修订记录

| 日期 | 版本 | 内容 |
|---|---|---|
| 2026-08-02 | v1.0 | 初版:上线交接,含概览/快速开始/结构/运营流程/部署/关键决策/遗留事项/纪律/节奏/清单 |
| 2026-08-02 | v1.1 | 方向调整:定位收窄为模拟 IC 设计工程师(主线)+ 嵌入式工程师(辅助);新增 §5"项目问题→技术分析→知识点"工作流;原 §5~§11 顺延为 §6~§12 |
