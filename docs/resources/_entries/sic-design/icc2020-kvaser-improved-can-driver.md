---
title: iCC 2020:Kvaser 改进型 CAN 驱动器与振铃抑制
description: Kvaser 论文从振铃机理出发介绍改进型 CAN 驱动器,是理解 SIC 为什么需要信号改善的原理基础文献。
type: SIC设计专题
organization: Kvaser
year: 2020
access: free
status: verified
download: local
priority: 3
audience: [模拟IC]
tags: [SIC, 振铃抑制]
source: https://www.can-cia.org
local_file: files/sic-design/iCC2020_Kvaser_improved_CAN_driver.pdf
---

## 是什么
Kvaser 在 iCC 2020(国际 CAN 会议)发表的论文,从振铃物理机理出发介绍改进型 CAN 驱动器,解释高速 CAN FD 网络中信号振铃的产生机制与抑制思路,是 SIC 信号改善技术的原理基础文献。

## 为什么值得读
- **模拟IC 工程师**:SIC 设计的全部动机都源于振铃问题,这篇论文从机理层面讲清"为什么会振铃、驱动器可以怎么改",是输出级与振铃抑制电路设计的前提功课。
- 从机理推导到电路改进的完整思路,可直接映射到 recessive nulling / 阻抗匹配等实现路线的取舍依据。

## 核心内容要点
- 振铃的物理机理:传输线反射、阻抗失配与网络拓扑的影响。
- 改进型 CAN 驱动器的设计思路与信号改善机制。
- 改进对更高数据相位速率的支撑作用。
- 与后续 SIC 规范(参数化振铃抑制)的对应关系。

## 怎么读
作为 SIC 原理入门精读:建议放在知识库 [原理篇](../../../knowledge/sic-design/principle.md)(振铃机理小节)之前或同步阅读,先建立机理直觉,再进入参数与电路细节;可衔接 CNL 2022-4 动态参数一文补齐参数视角。

[📄 下载本地 PDF](../../../files/sic-design/iCC2020_Kvaser_improved_CAN_driver.pdf)

## 参见
- [CAN SIC 词条](../../../glossary/can-sic.md)
- [振铃抑制词条](../../../glossary/ringing-suppression.md)
- [SIC 设计专题知识库 — 原理篇](../../../knowledge/sic-design/principle.md)
