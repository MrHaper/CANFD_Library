---
title: "iCC 2024:Kvaser 高位速率线束布局与 CAN SIC"

description: Kvaser 论文讨论高位速率 CAN 网络的线束布局与 CAN SIC 的关系,给出网络级设计视角。
type: SIC设计专题
organization: Kvaser
year: 2024
access: free
status: verified
download: local
priority: 2
audience: [模拟IC]
tags: [SIC, 线束布局, 网络设计]
source: "https://www.can-cia.org"

local_file: files/sic-design/iCC2024_Kvaser_cable_layout_and_CAN_SIC.pdf
---

## 是什么
Kvaser 在 iCC 2024(国际 CAN 会议)发表的论文,讨论高位速率 CAN 网络的线束布局(拓扑、stub、端接等)与 CAN SIC 的关系,分析线束设计对信号质量的制约,以及 SIC 收发器对网络设计的支撑作用。

## 为什么值得读
- **模拟IC 工程师**:SIC 的效果不是孤立的芯片属性,而与网络级条件(线束、节点数)强耦合;本文帮你理解 SIC 设计的适用边界与系统约束,避免在真实拓扑中误用参数。
- 网络级视角补齐了"芯片设计 — 系统验证"之间的一环,是设计检查清单中系统项的背景材料。

## 核心内容要点
- 高位速率下网络拓扑与线束布局的挑战。
- CAN SIC 对网络设计与信号质量的支撑作用。
- 线束布局/端接/节点配置对 SIC 效果的影响。
- 面向实际网络的布局与验证建议。

## 怎么读
先读知识库 [原理篇](../../../knowledge/sic-design/principle.md) 建立系统级概念(tBit/tREC、Allowable Ringing Time),再精读本文;可与知识库 [物理层与 SIC](../../../knowledge/physical-layer/index.md) 子域互参,理解拓扑约束。

[📄 下载本地 PDF](../../../files/sic-design/iCC2024_Kvaser_cable_layout_and_CAN_SIC.pdf)

## 参见
- [CAN SIC 词条](../../../glossary/can-sic.md)
- [总线端接词条](../../../glossary/bus-termination.md)
- [SIC 设计专题知识库 — 原理篇](../../../knowledge/sic-design/principle.md)
