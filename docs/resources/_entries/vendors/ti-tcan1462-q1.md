---
title: TCAN1462-Q1 CAN SIC 收发器(Standby)数据手册
description: TI 8 引脚 CAN SIC 收发器数据手册,ISO 11898-2:2016 + CiA 601-4,VIO 1.7–5.5 V,Standby 远程唤醒与 ±58 V 总线容错。
type: 厂商资料
organization: TI
year: 2024
access: free
status: verified
download: local
priority: 1
audience: [模拟IC]
tags: [TI, 数据手册]
source: https://www.ti.com/lit/gpn/TCAN1462-Q1
local_file: files/vendors/TI_TCAN1462-Q1_CAN_SIC_datasheet.pdf
---

## 是什么
TI TCAN1462-Q1 是 8 引脚(SOIC / VSON / SOT-23)CAN SIC 收发器数据手册(Rev B, 2024-10-08),符合 ISO 11898-2:2016 + CiA 601-4,VIO 支持 1.7–5.5 V,Standby 远程唤醒、热插拔与 ±58 V 总线容错。

## 为什么值得读
- **模拟IC 工程师**:与 TCAN1463-Q1 对照可理解"SIC 核 + 不同电源管理外设(standby vs sleep/INH)"的产品家族化设计思路,以及 8 Mbps 下位时序对称性的 Spec 写法。
- **嵌入式开发工程师**:与 TCAN1044A / TCAN1042 引脚兼容,是 8 引脚 SIC 替换升级的选型参考。
- **学生**:两份 TI SIC 手册对照学习家族化产品规划。

## 核心内容要点
### 内部框图要点
- 8 引脚(SOIC / VSON / SOT-23)CAN SIC 收发器,符合 ISO 11898-2:2016 + CiA 601-4。
- Standby 远程唤醒、热插拔;与 TCAN1044A / TCAN1042 引脚兼容;具体模块划分与引脚功能详见数据手册原文。

### 关键电气参数
- VIO 支持 1.7–5.5 V;±58 V 总线容错。
- 8 Mbps 下位时序对称性指标见数据手册"电气特性"章节。

### 对收发器设计的意义
- 展示"SIC 核 + Standby 外设"的 8 引脚产品形态,用于理解收发器家族化的功能取舍。
- 位时序对称性 Spec 写法可作自研芯片指标定义参考。

## 怎么读
与 TCAN1463-Q1 数据手册对照,重点比较 Standby vs Sleep/INH 的电源管理差异;再与 TCAN1044A 对比理解 SIC 带来的改进。

[📄 下载本地 PDF](../../../files/vendors/TI_TCAN1462-Q1_CAN_SIC_datasheet.pdf)

## 参见
- [TCAN1463-Q1 CAN SIC 收发器(Sleep/INH/WAKE)数据手册](ti-tcan1463-q1.md)
- [TJA1462 CAN SIC 收发器(Standby)数据手册](nxp-tja1462.md)
- [TCAN1044-Q1 CAN FD 收发器数据手册](ti-tcan1044-q1.md)
- [资源库 — 厂商资料](../../vendors.md)
