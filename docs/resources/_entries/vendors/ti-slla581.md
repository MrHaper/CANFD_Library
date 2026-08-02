---
title: SLLA581 白皮书:CAN FD 收发器中 SIC 如何释放真正潜力
description: TI 白皮书,系统讲解 SIC 原理——通过主动驱动/振铃抑制改善 dominant→recessive 边缘,在复杂拓扑中解锁 2/5 Mbps 及以上 CAN FD。
type: 厂商资料
organization: TI
year: 2025
access: free
status: verified
download: local
priority: 3
audience: [模拟IC]
tags: [TI, 白皮书]
source: https://www.ti.com/lit/pdf/SLLA581
local_file: files/vendors/TI_SLLA581_SIC_whitepaper.pdf
---

## 是什么
TI SLLA581 白皮书《How Signal Improvement Capability Unlocks the Real Potential of CAN FD Transceivers》(Rev A, 2025-10-06)系统讲解 SIC 原理:通过主动驱动 / 振铃抑制改善 dominant→recessive 边缘,从而在复杂拓扑(多短桩、星型)中解锁 2/5 Mbps 及以上 CAN FD。

## 为什么值得读
- **模拟IC 工程师**:从系统层面理解"为什么要做 SIC、振铃/回波的根源",是把芯片级指标(输出级阻尼、位对称)与网络层收益联系起来的桥梁文档。
- **嵌入式开发工程师**:理解 SIC 收发器与传统 CAN FD 收发器在拓扑、位时序、采样点上的差异,用于网络设计与选型论证。
- **学生**:一篇读懂"信号改善能力"来龙去脉的入门读物,是进入 SIC 收发器设计的绝佳起点。

## 核心内容要点
### 内部框图要点
- 白皮书聚焦系统与网络层面的原理阐述,不提供芯片内部框图;相关 SIC 输出级结构请参见 TCAN1463-Q1 等数据手册原文。
- 文档中给出的 SIC 与传统收发器对比图是理解"为何需要主动振铃抑制"的关键图示。

### 关键电气参数
- 围绕"振铃抑制 / 位时序"展开论述:主动驱动改善 dominant→recessive 边缘,支撑复杂拓扑(多短桩、星型)下的 2/5 Mbps 及以上 CAN FD。
- 对比传统 CAN FD 收发器在拓扑、位时序、采样点上的差异;具体数值指标以数据手册为准,白皮书不替代规格书。

### 对收发器设计的意义
- 把芯片级指标(输出级阻尼、位对称)与网络层收益联系起来,指导 SIC 输出级设计的取舍方向。
- 可作为向非模拟背景同事 / 客户解释"SIC 为什么值得做"的沟通文档。

## 怎么读
建议通读一遍建立整体认知,再带着"振铃/回波从哪来、输出级如何抑制"的问题回到 TCAN1463-Q1 / TJA1463 数据手册精读电气特性;与 SDAA190(CAN/CAN FD/CAN XL 对比)配合阅读可衔接 CAN XL 演进路线。

[📄 下载本地 PDF](../../../files/vendors/TI_SLLA581_SIC_whitepaper.pdf)

## 参见
- [TCAN1463-Q1 CAN SIC 收发器(Sleep/INH/WAKE)数据手册](ti-tcan1463-q1.md)
- [TJA1463 CAN SIC 收发器(Sleep)数据手册](nxp-tja1463.md)
- [SDAA190 应用笔记:CAN / CAN FD / CAN XL 对比](ti-sdaa190.md)
- [资源库 — 厂商资料](../../vendors.md)
