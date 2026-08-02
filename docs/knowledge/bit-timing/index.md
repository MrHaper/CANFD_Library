---
title: 位定时与同步
description: 时间量子与采样点、相位裕度与同步机制、TDC 收发器延迟补偿——CAN/CAN FD 网络时序的权威知识点。
tags: [位定时]
---

# 位定时与同步

本子域整理 CAN / CAN FD **位定时与时序**的权威知识点:从时间量子(TQ)与采样点计算,到相位裕度预算与硬/重同步机制,再到数据相位必须依赖的 TDC(收发器延迟补偿)。CAN FD 的一帧两速(BRS)让这里的每个概念都变成"仲裁相位 vs 数据相位"的两套账,是与[协议基础](../protocol/index.md)和[物理层与SIC](../physical-layer/index.md)交汇最多的子域。

## 知识点

| 知识点 | 难度 | 定位 |
|---|---|---|
| [时间量子与采样点](time-quantum-sample-point.md) | 入门 | TQ 的产生、位时间四段结构与采样点计算(含相位缓冲段的作用) |
| [相位裕度与同步](phase-margin.md) | 进阶 | 相位裕度预算构成、硬同步/重同步机制与 RJW 的权衡 |
| [收发器延迟补偿(TDC / SSP)](tdc.md) | 进阶 | 环回延迟三段分解、第二采样点原理与对收发器对称性的要求 |

## 相关入口

- 教程:[位定时入门](../../tutorials/03-bit-timing-basics.md)、[CAN FD 位定时配置实战](../../tutorials/06-bit-timing-config.md)、[BRS 与 TDC](../../tutorials/04-brs-tdc.md)
- 术语:[位定时类词条](../../glossary/index.md)
- 标准规范:[CiA 601-3(位定时配置与评估工具)](../../resources/_entries/standards/cia-601-3-bit-timing.md)、[CiA 601-1(延迟对称性)](../../resources/_entries/standards/cia-601-1-physical-interface.md)
- 相邻子域:[协议基础](../protocol/index.md)、[物理层与SIC](../physical-layer/index.md)
