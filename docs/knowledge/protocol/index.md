---
title: 协议基础
description: CAN 与 CAN FD 协议基础知识点:帧格式、仲裁与错误处理、CRC 与位填充,是进入其他分域的起点。
tags: [协议]
---

# 协议基础

本子域整理 CAN / CAN FD **数据链路层**的权威知识点:从四种帧类型与帧格式,到仲裁与错误处理机制,再到 CRC 与位填充的检错编码。这里的每个知识点是[教程](../../tutorials/index.md)与[术语表](../../glossary/index.md)的"锚点",也构成理解[位定时与同步](../bit-timing/index.md)与[物理层与SIC](../physical-layer/index.md)的上游基础。

## 知识点

| 知识点 | 难度 | 定位 |
|---|---|---|
| [帧格式总览:四种帧类型与经典 vs FD](frame-format.md) | 入门 | 数据/远程/错误/过载四种帧,以及经典 CAN 与 CAN FD 在控制场、DLC、CRC、填充上的格式差异 |
| [仲裁与错误处理](arbitration-and-error.md) | 进阶 | 位仲裁机制、五类错误检测、错误帧结构与 Error Active/Passive/Bus-off 状态机 |
| [CRC(17/21 位)与位填充](crc-and-bit-stuffing.md) | 进阶 | CRC 选择规则与覆盖范围、仲裁相位 5 位规则与数据相位固定填充 |

## 相关入口

- 教程:[图解 CAN FD 帧结构](../../tutorials/01-can-fd-frame-structure.md)、[CAN 2.0 与 CAN FD 的 5 个关键差异](../../tutorials/02-can2-vs-canfd.md)
- 术语:[协议类词条](../../glossary/index.md)
- 标准规范:[ISO 11898-1 (2024)](../../resources/_entries/standards/iso-11898-1-2024.md)、[Bosch CAN FD Specification v1.0](../../resources/_entries/standards/bosch-2012-canfd-spec.md)
- 相邻子域:[位定时与同步](../bit-timing/index.md)
