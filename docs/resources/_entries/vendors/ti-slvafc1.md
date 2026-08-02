---
title: SLVAFC1 应用笔记:CAN 总线 ESD 过压保护
description: TI 应用笔记,介绍 CAN 总线瞬态与 ESD 耦合路径、IEC 61000-4-2 / ISO 7637 测试方法、TVS 与共模扼流圈选型及 PCB 布局建议。
type: 厂商资料
organization: TI
year: 2022
access: free
status: verified
download: local
priority: 1
audience: [模拟IC]
tags: [TI, 应用笔记]
source: https://www.ti.com/lit/pdf/SLVAFC1
local_file: files/vendors/TI_SLVAFC1_CAN_bus_ESD_protection.pdf
---

## 是什么
TI SLVAFC1 应用笔记(2022-04-27)介绍 CAN 总线瞬态与 ESD 的耦合路径、IEC 61000-4-2 / ISO 7637 测试方法、外部 TVS 与共模扼流圈选型,以及收发器与保护器件协同的 PCB 布局建议。

## 为什么值得读
- **模拟IC 工程师**:收发器片内 ESD(±58 V 容错、8 kV)与片外 TVS 的分工设计,以及测试方法学(ESD/EFT 测试台架)对验证自己流片芯片的 ESD 性能极有价值。
- **嵌入式开发工程师**:面向实车 ESD 故障的防护选型与布局落地指南。
- **学生**:理解"芯片级保护 + 系统级保护"的分层思想。

## 核心内容要点
### 内部框图要点
- 应用笔记为防护设计类文档,不含芯片内部框图;核心是片内/片外保护的分工与协同。
- 内容覆盖:CAN 总线瞬态与 ESD 耦合路径、IEC 61000-4-2 / ISO 7637 测试方法、外部 TVS 与共模扼流圈选型、PCB 布局建议。

### 关键电气参数
- 围绕 ESD/EFT 测试等级与 TVS/共模扼流圈选型参数展开;具体数值见原文,不在此逐项转录。

### 对收发器设计的意义
- 片内 ESD 与片外 TVS 的分工设计思路,可指导自研芯片的 ESD 结构规划。
- ESD/EFT 测试台架方法学可直接复用到自研芯片的验证流程。

## 怎么读
先读 ESD 耦合路径与测试方法建立概念,再重点看 TVS 与共模扼流圈选型、PCB 布局;与 AH1308 的布局章节配合阅读。

[📄 下载本地 PDF](../../../files/vendors/TI_SLVAFC1_CAN_bus_ESD_protection.pdf)

## 参见
- [AH1308 Mantis CAN 收发器应用提示](nxp-ah1308.md)
- [TCAN1044-Q1 CAN FD 收发器数据手册](ti-tcan1044-q1.md)
- [资源库 — 厂商资料](../../vendors.md)
