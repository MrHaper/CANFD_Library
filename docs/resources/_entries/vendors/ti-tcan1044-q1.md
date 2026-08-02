---
title: TCAN1044-Q1 CAN FD 收发器数据手册
description: TI ISO 11898-2:2016 经典 CAN FD 收发器数据手册,支持 2/5/8 Mbps 优化时序、±58 V 总线容错、接收器共模 ±12 V。
type: 厂商资料
organization: TI
year: 2025
access: free
status: verified
download: local
priority: 1
audience: [模拟IC]
tags: [TI, 数据手册]
source: https://www.ti.com/lit/gpn/TCAN1044-Q1
local_file: files/vendors/TI_TCAN1044-Q1_CAN_FD_datasheet.pdf
---

## 是什么
TI TCAN1044-Q1 是符合 ISO 11898-2:2016 的经典 CAN FD 收发器数据手册(Rev D, 2025-03-05),支持 2/5/8 Mbps 优化时序,1.8–5 V I/O(VIO 变体),Standby + 远程唤醒,±58 V 总线容错,接收器共模 ±12 V。

## 为什么值得读
- **模拟IC 工程师**:TI 的"非 SIC"CAN FD 基线;TCAN-SOIC8-EVM 与 TCAN1042DEVM 通用评估板(用户指南 SLLU385 / SLLU234)提供 8 引脚 CAN 收发器的通用验证平台思路。
- **嵌入式开发工程师**:经济型 CAN FD 节点选型与 VIO 电平适配参考。
- **学生**:与 TCAN1462-Q1 对比理解 SIC 的改进点。

## 核心内容要点
### 内部框图要点
- ISO 11898-2:2016 经典 CAN FD 收发器,含 Standby + 远程唤醒;VIO 变体支持 1.8–5 V I/O。
- 具体模块划分与引脚功能详见数据手册原文"内部框图 / 引脚信息"章节。

### 关键电气参数
- 支持 2/5/8 Mbps 优化时序;±58 V 总线容错;接收器共模 ±12 V。
- 其余详细参数见数据手册"电气特性"章节。

### 对收发器设计的意义
- 作为"非 SIC"基线,用于与 TCAN1462-Q1 / TCAN1463-Q1 的 SIC 指标对比,量化改进幅度。
- 通用评估板(TCAN-SOIC8-EVM)平台思路可复用于自研 8 引脚收发器验证。

## 怎么读
作为基线阅读:先看电气特性与位时序参数,再与 TCAN1462-Q1 对照理解 SIC 的价值;评估板用户指南(SLLU385 / SLLU234)可作为验证平台参考。

[📄 下载本地 PDF](../../../files/vendors/TI_TCAN1044-Q1_CAN_FD_datasheet.pdf)

## 参见
- [TCAN1462-Q1 CAN SIC 收发器(Standby)数据手册](ti-tcan1462-q1.md)
- [TJA1044 CAN FD 收发器数据手册](nxp-tja1044.md)
- [资源库 — 厂商资料](../../vendors.md)
