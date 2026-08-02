---
title: 资源库 — SIC 设计专题
description: CAN SIC 设计专题资料:CAN Newsletter(CiA 官方)文章与 iCC 国际 CAN 会议论文,覆盖动态参数、振铃抑制、演进、测试验证,全部免费公开并提供本地 PDF。
tags: [SIC]
---

# 资源库 — SIC 设计专题

> 本分类收录 **CAN Newsletter(CiA 官方)杂志文章**与 **iCC 国际 CAN 会议论文**,是 CAN SIC(Signal Improvement Capability)收发器设计的专项资料,面向模拟 IC 设计工程师。全部资料**免费公开**,且**已提供本地 PDF**(见各条目页"下载本地 PDF")。内容覆盖:SIC 动态参数与 EMC、振铃抑制原理、设计取舍、SIC → SIC XL 演进、线束布局、眼图与网络验证。全部条目均经 CiA 官网获取并核对,无编造内容。按优先级排序:**必读 ★★★** 为 SIC 核心文献,**推荐 ★★☆** 支撑设计取舍与应用理解,**选读 ★☆☆** 按需查阅。

## 必读(★★★)

| 资料 | 机构 | 年份 | 内容概述 |
|---|---|---|---|
| [CNL 2022-4:Infineon CAN SIC 动态参数详解](_entries/sic-design/cnl2022-4-infineon-sic-dynamic-parameters.md) | CAN Newsletter | 2022 | Infineon 工程师详解 SIC 新增动态参数,阐明参数定义与 EMC 测试的关系(权威) |
| [iCC 2020:Kvaser 改进型 CAN 驱动器与振铃抑制](_entries/sic-design/icc2020-kvaser-improved-can-driver.md) | Kvaser | 2020 | 从振铃机理出发介绍改进型 CAN 驱动器,是 SIC 信号改善的原理基础 |

## 推荐(★★☆)

| 资料 | 机构 | 年份 | 内容概述 |
|---|---|---|---|
| [CNL 2022-3:SIC 收发器多厂商方案访谈](_entries/sic-design/cnl2022-3-sic-transceiver-provider-interviews.md) | CAN Newsletter | 2022 | 多厂商 SIC 收发器方案访谈,对比各家设计取舍 |
| [CNL 2023-1:Infineon SIC 与 SIC XL 选型辨析](_entries/sic-design/cnl2023-1-infineon-sic-vs-sic-xl.md) | CAN Newsletter | 2023 | SIC 与 SIC XL 选型辨析,理解 SIC → SIC XL 演进 |
| [CNL 2025-1:esd CAN SIC 实测信号质量](_entries/sic-design/cnl2025-1-esd-can-sic-signal-quality.md) | CAN Newsletter | 2025 | esd 的 CAN SIC 实测信号质量,应用案例 |
| [iCC 2024:Kvaser 高位速率线束布局与 CAN SIC](_entries/sic-design/icc2024-kvaser-cable-layout-and-can-sic.md) | Kvaser | 2024 | 高位速率线束布局与 SIC 的关系,网络级设计 |
| [iCC 2024:Infineon CAN XL 物理层](_entries/sic-design/icc2024-infineon-can-xl-physical-layer.md) | Infineon | 2024 | CAN XL 物理层设计,SIC 演进全景 |
| [iCC 2024:NXP 部分网络与 SIC](_entries/sic-design/icc2024-nxp-partial-networking-sic.md) | NXP | 2024 | 部分网络功能与 SIC 结合的应用价值 |

## 选读(★☆☆)

| 资料 | 机构 | 年份 | 内容概述 |
|---|---|---|---|
| [iCC 2024:LeCroy CAN 眼图分析](_entries/sic-design/icc2024-lecroy-eye-diagrams-can.md) | LeCroy | 2024 | CAN 眼图分析,信号质量测试方法 |
| [iCC 2024:C&S CAN XL 网络验证](_entries/sic-design/icc2024-cs-can-xl-validation.md) | C&S | 2024 | CAN XL 网络验证,验证方法参考 |

---

## 获取渠道说明

- **CAN Newsletter 文章(CNL 系列)**:由 CiA(CAN in Automation)官方发布,免费公开。本文档收录的 4 篇来自 2022–2025 年各期,均已在本地提供 PDF。
- **iCC 论文(iCC 系列)**:来自 CiA 举办的国际 CAN 会议(International CAN Conference)论文集,免费公开。本文档收录的 6 篇来自 iCC 2020 与 iCC 2024,均已在本地提供 PDF。
- 原始出处统一见 [CiA 官网](https://www.can-cia.org),可按届次浏览全部 CAN Newsletter 文章与 iCC 论文集。
- ⚠️ 相关付费/会员资料(ISO 11898-2:2024、ISO 16845-2、IEC 62228-3、CiA 601-4 历史版、CiA plugfest)不收录于本分类,以链接形式见知识库。

## 与知识库互链

本分类对应知识库的 [SIC 设计专题子域](../knowledge/sic-design/index.md)(原理篇 / 设计篇 / 测试篇)。建议先读知识库建立 SIC 原理到测试的框架,再用本分类资料深化细节:

- [原理篇:振铃机理与信号改善机制](../knowledge/sic-design/principle.md)
- [设计篇:收发器芯片设计要点](../knowledge/sic-design/design.md)
- [测试篇:验证与测试方法](../knowledge/sic-design/testing.md)
- [SIC 学习笔记(HTML 整合版)](../files/sic-design/SIC学习笔记.html)

## 延伸阅读

- 词条:[CAN SIC](../glossary/can-sic.md)、[振铃抑制](../glossary/ringing-suppression.md)、[回波损耗](../glossary/return-loss.md)、[收发器](../glossary/transceiver.md)
- 资源库相关分类:[标准规范](standards.md)(CiA 601 / ISO 11898-2 / ISO 16845 / IEC 62228-3)、[论文](papers.md)(CAN SIC 核心论文、CAN XL 物理层)、[厂商资料](vendors.md)(TJA1463/TCAN1463 等 SIC 收发器数据手册)
