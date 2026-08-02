---
title: 物理层与SIC
description: ISO 11898-2 高速 PMA 结构、振铃抑制、回波损耗与 EMC——聚焦 SIC 信号改善技术的权威知识点。
tags: [物理层, SIC]
---

# 物理层与SIC

本子域整理 CAN **物理层与 SIC 信号改善技术**的权威知识点:从 ISO 11898-2 的高速 PMA 结构,到 SIC 的核心能力振铃抑制,再到回波损耗与 EMC 的收发器表征。这里主要面向模拟 IC 设计工程师,是[收发器设计](../transceiver-design/index.md)子域的上游输入。

## 知识点

| 知识点 | 难度 | 定位 |
|---|---|---|
| [ISO 11898-2 结构:高速 PMA 子层](iso-11898-2-overview.md) | 专家 | HS-PMA 各选项(经典 HS、CAN FD、CAN SIC、CAN SIC XL)、版本演进与电气要求总览 |
| [振铃抑制:SIC 核心能力](ringing-suppression.md) | 专家 | 显性→隐性转换振铃的机理、SIC 主动阻尼方案与测量方法 |
| [回波损耗与 EMC:收发器表征](return-loss-emc.md) | 专家 | 回波损耗定义与频率特性、收发器 EMC 评估标准(IEC 62228-3 / CISPR 25)与表征方法 |

## 相关入口

- 教程:[SIC 是什么](../../tutorials/07-what-is-sic.md)、[振铃抑制原理与测量](../../tutorials/08-ringing-suppression.md)、[一致性测试与 plugfest](../../tutorials/11-conformance-plugfest.md)
- 术语:[物理层与收发器类词条](../../glossary/index.md)
- 标准规范:[ISO 11898-2 (2024)](../../resources/_entries/standards/iso-11898-2-2024.md)、[CiA 601-4(SIC 前身,已撤回)](../../resources/_entries/standards/cia-601-4-sic.md)、[IEC 62228-3](../../resources/_entries/standards/iec-62228-3-2019.md)
- 相邻子域:[位定时与同步](../bit-timing/index.md)、[收发器设计](../transceiver-design/index.md)
