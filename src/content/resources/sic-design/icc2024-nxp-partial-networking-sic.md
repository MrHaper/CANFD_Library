---
title: "iCC 2024:NXP 部分网络与 SIC"

description: NXP 论文讨论部分网络(PN)功能与 SIC 收发器的结合及其应用价值,提供功能规划参考。
type: SIC设计专题
organization: NXP
year: 2024
access: free
status: verified
download: local
priority: 2
audience: [模拟IC]
tags: [SIC, 部分网络, 应用价值]
source: "https://www.can-cia.org"

local_file: files/sic-design/iCC2024_NXP_partial_networking_SIC.pdf
---

## 是什么
NXP 在 iCC 2024(国际 CAN 会议)发表的论文,讨论部分网络(Partial Networking,PN)功能与 SIC 收发器的结合及其应用价值,说明如何在高位速率 CAN 网络中叠加部分网络能力,是 SIC 收发器功能规划的应用参考。

## 为什么值得读
- **模拟IC 工程师**:部分网络是收发器的重要功能维度(选择性唤醒/休眠),理解 PN 与 SIC 如何协同,有助于在 SIC 芯片设计中规划功能组合与引脚/寄存器方案。
- 应用价值视角帮助你把信号改善能力与系统能耗需求统一考虑,是架构级规划的背景材料。

## 核心内容要点
- 部分网络功能的基本原理(选择性唤醒、选择性休眠)。
- SIC 与部分网络结合的架构与应用价值。
- 收发器设计中的功能整合考量(信号改善 + PN 逻辑)。
- 面向车用网络的部署建议。

## 怎么读
作为 SIC 应用扩展阅读:先掌握知识库 [原理篇](../../../knowledge/sic-design/principle.md) 与 [设计篇](../../../knowledge/sic-design/design.md) 的 SIC 核心,再读本文理解功能组合;可与 [CAN FD 词条](../../../glossary/can-fd.md) 与部分网络相关词条互参。

[📄 下载本地 PDF](../../../files/sic-design/iCC2024_NXP_partial_networking_SIC.pdf)

## 参见
- [CAN SIC 词条](../../../glossary/can-sic.md)
- [CAN FD 词条](../../../glossary/can-fd.md)
- [SIC 设计专题知识库 — 设计篇](../../../knowledge/sic-design/design.md)
