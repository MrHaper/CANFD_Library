---
title: AH1308 Mantis CAN 收发器应用提示
description: NXP Mantis 家族(TJA1044/TJA1057)应用笔记,覆盖应用电路、PCB 布局、EMC/ESD 防护、总线端接与滤波、失效安全设计。
type: 厂商资料
organization: NXP
year: 2020
access: free
status: verified
download: local
priority: 3
audience: [模拟IC]
tags: [NXP, 应用笔记]
source: https://www.nxp.com/docs/en/supporting-information/AH1308_Application_Hints_Mantis.pdf
local_file: files/vendors/NXP_AH1308_Mantis_CAN_app_hints.pdf
---

## 是什么
NXP AH1308 是 Mantis 系列 CAN 收发器(TJA1044 / TJA1057 及其 GT 高速版本)的应用笔记 / 应用提示(Rev 2.2, 2020-01-03),涵盖应用电路、PCB 布局、EMC/ESD 防护、总线端接与滤波、失效安全设计建议。

## 为什么值得读
- **模拟IC 工程师**:应用笔记中最值得精读的一类——含完整原理图、PCB 布局规则和 EMC 测试方法,是学习 CAN 收发器"从芯片到系统"落地细节(共模扼流圈、split termination、总线电容预算)的经典教材。
- **嵌入式开发工程师**:直接可用的布局与端接规则,帮助解决实车 EMC 与信号完整性工程问题。

## 核心内容要点
### 内部框图要点
- 本文件为应用笔记而非芯片数据手册,不含芯片内部框图;Mantis 家族收发器结构参见 TJA1044 数据手册。
- 文档核心是应用层内容:应用电路、PCB 布局、EMC/ESD 防护、总线端接与滤波、失效安全设计建议。

### 关键电气参数
- 围绕"从芯片到系统"的落地参数展开:共模扼流圈选型与位置、split termination、总线电容预算、EMC/ESD 防护结构。
- 具体数值与曲线详见原文相应章节,不在此逐项转录。

### 对收发器设计的意义
- 完整原理图 + PCB 布局规则 + EMC 测试方法,是自研收发器流片后做系统级验证(共模扼流圈配合、端接方案)的对照教材。
- 失效安全设计建议可用于设计自己的总线保护电路。

## 怎么读
建议作为手册精读:先看应用电路与 PCB 布局规则,再对照 EMC 测试方法搭建自己的验证台架;与 TJA1044 数据手册、SLVAFC1(ESD 防护)配合阅读效果更佳。

[📄 下载本地 PDF](../../../files/vendors/NXP_AH1308_Mantis_CAN_app_hints.pdf)

## 参见
- [TJA1044 CAN FD 收发器数据手册](nxp-tja1044.md)
- [SLVAFC1 应用笔记:CAN 总线 ESD 过压保护](ti-slvafc1.md)
- [TCAN1044-Q1 CAN FD 收发器数据手册](ti-tcan1044-q1.md)
- [资源库 — 厂商资料](../../vendors.md)
