---
title: 勘误与贡献
description: 本站资源收集过程中的勘误记录,以及提交新资料、提交勘误的贡献指南(收录标准、校验流程)。
search: { boost: 1 }
---
# 勘误与贡献

## 🔧 勘误记录

资料库在收集与核对过程中,发现并更正了若干常见误区与遗漏。这里如实记录,避免读者在外部资料中踩同样的坑。每条均给出涉及的本站页面链接。

### 1. CiA 613 系列实为 CAN XL,不是 CAN FD SIC 测试规范

- **误传**:610~613 系列被部分资料当作 CAN FD SIC 的测试规范。
- **实情**:经 CiA 官网核实,**610~613 系列全部是 CAN XL 文档**。SIC 收发器的规范本体是 **ISO 11898-2:2024**(SIC 章节),其前身 **CiA 601-4 已于 2023 年撤回并入 ISO**。
- **涉及页面**:[CiA 610–613 系列(CAN XL)](resources/_entries/standards/cia-610-613-can-xl-series.md) · [CiA 601-4(SIC,已并入 ISO)](resources/_entries/standards/cia-601-4-sic.md) · [ISO 11898-2:2024](resources/_entries/standards/iso-11898-2-2024.md)

### 2. 补充收录遗漏标准 — IEC 62228-3

- **情况**:建库初期未单独收录 **IEC 62228-3**(Integrated circuits — EMC evaluation of transceivers — Part 3: CAN transceivers)。它是 CAN 收发器 **EMC 评估的关键标准**,在后续补充时已收录。
- **获取渠道**:IEC Webstore(webstore.iec.ch)付费购买,本站仅提供索引与官方链接。
- **涉及页面**:[IEC 62228-3:2019](resources/_entries/standards/iec-62228-3-2019.md) · 相关术语:[EMI/EMC](glossary/emi-emc.md) · [CISPR 25](glossary/cispr25.md)

### 3. 《Controller Area Network Prototyping with Arduino》作者更正

- **误传**:部分渠道将作者标为 K. Tindell。
- **实情**:该书真实作者是 **Wilfried Voss**,本站已按真实作者收录(出版年份 2014)。
- **涉及页面**:[2014 Voss — CAN Arduino Prototyping](resources/_entries/books/2014-voss-can-arduino-prototyping.md) · 教材书目总览见 [资源库·教材书籍](resources/books.md)

### 4. Infineon CAN SIC 产品是 TLE9371(非 TLE9255)

- **误传**:部分渠道将 TLE9255 当作 Infineon 的 SIC 收发器。
- **实情**:Infineon 的 **CAN SIC 产品是 TLE9371**;TLE9255 只是**普通 CAN FD** 收发器。收录时已纠正并分别建档。
- **涉及页面**:[Infineon TLE9371(SIC)](resources/_entries/vendors/infineon-tle9371v.md) · [Infineon TLE9255(普通 CAN FD)](resources/_entries/vendors/infineon-tle9255w.md)

!!! info "勘误遵循的核对原则"
    以上勘误均以**官方源头**为准:标准类以 CiA / ISO 官网为准,产品类以厂商官网产品页为准,书籍类以出版方 / 作者信息为准。欢迎读者复核后继续补充,见下方贡献指南。

---

## ✅ 收录标准

本站的收录遵循以下原则,以保证可访问性与可审计性:

1. **版权策略**:仅托管**可免费公开获取**的 PDF(如 Bosch 公开规范、Google Patents 专利原文、CiA iCC 开放获取论文、MDPI / IEICE / EURASIP 等开放期刊论文、厂商公开数据手册与应用笔记)。
2. **付费资料只放链接**:ISO / IEC / SAE 等付费标准、IEEE 付费期刊论文、商业教材,**不托管全文**,仅提供官方获取渠道(如 webstore.iec.ch、IEEE Xplore、出版社)与索引信息。
3. **条目可溯源**:每条资源记录来源(官方链接 / DOI / 专利号),并标注是否已验证可访问。
4. **类型归位**:标准 / 专利 / 论文 / 期刊 / 教材 / 厂商 / 工具社区分目录收录,新条目需放入对应分类的 `_data/*.json`。

---

## 🤝 贡献指南

### 提交勘误

- 发现条目信息有误(编号、作者、版本、链接失效、归属分类错误等),请在仓库 **GitHub Issues** 提交,标题建议以 `勘误:` 开头,说明错误内容与正确来源。
- 我们核对后会更新 `docs/_data/*.json` 与对应条目页,并在本页"勘误记录"中追加。

### 提交新资料

1. **Fork 本仓库**,按 [收录标准](#-收录标准) 判断资料是否符合收录条件;
2. 将条目信息补充到对应分类的 `docs/_data/*.json`(字段格式参见同目录其他条目);
3. 本地校验:在仓库根目录运行
   ```bash
   python scripts/validate_resources.py docs/
   ```
   校验通过(无报错)后再提交;
4. 发起 **Pull Request**,说明资料名称、来源链接与推荐理由,并勾选"符合版权策略"。

### 其他贡献

- 术语词条、教程、学习路线内容建议:同样通过 Issues / PR 提交;
- 版权存疑的资料:优先在 Issue 中讨论,不要直接添加 PDF。

!!! tip "仓库地址"
    仓库地址见 `mkdocs.yml` 中的 `repo_url`(上线前由施工方替换为真实地址)。Issues 入口为 `repo_url/issues`。
