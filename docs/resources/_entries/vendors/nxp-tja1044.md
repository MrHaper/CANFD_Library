---
title: TJA1044 CAN FD 收发器数据手册
description: NXP Mantis 家族经典 CAN FD 收发器数据手册,ISO 11898-2:2016,GT 变体支持 5 Mbit/s 快相位与 210 ns 环路延时。
type: 厂商资料
organization: NXP
year: 2024
access: free
status: verified
download: local
priority: 1
audience: [模拟IC]
tags: [NXP, 数据手册]
source: https://www.nxp.com/docs/en/data-sheet/TJA1044.pdf
local_file: files/vendors/NXP_TJA1044_CAN_FD_datasheet.pdf
---

## 是什么
NXP TJA1044 是 Mantis 家族经典 CAN FD 高速收发器数据手册(Rev 8.0, 2024-11-06),符合 ISO 11898-2:2016;GT 变体支持 5 Mbit/s CAN FD 快相位与 210 ns 环路延时,超低功耗 Standby + 总线唤醒。

## 为什么值得读
- **模拟IC 工程师**:作为"非 SIC"基线收发器,SIC 器件的时序/振铃指标与其对比可量化 SIC 带来的裕量提升(bit timing symmetry、ringing reduction),是性能对标基线。
- **嵌入式开发工程师**:无需共模扼流圈即可获得优秀 EMC、8 kV ESD,是经济型 CAN FD 节点的经典选型。

## 核心内容要点
### 内部框图要点
- Mantis 家族经典 CAN FD 收发器,符合 ISO 11898-2:2016;GT 变体支持 5 Mbit/s CAN FD 快相位。
- 超低功耗 Standby + 总线唤醒;具体模块划分与引脚功能详见数据手册原文"内部框图 / 引脚信息"章节。

### 关键电气参数
- GT 变体:210 ns 环路延时、5 Mbit/s CAN FD 快相位。
- 无需共模扼流圈即获优秀 EMC;8 kV ESD;其余详细参数见数据手册"电气特性"章节。

### 对收发器设计的意义
- 作为"非 SIC"基线,用于与 SIC 器件量化对比位时序对称性与振铃抑制带来的裕量提升。
- 低成本、简化版收发器的架构参考。

## 怎么读
作为对标基线阅读:先看电气特性中位时序相关参数,再与 TJA1462 / TJA1463 的 SIC 指标逐项对比,量化 SIC 的改进幅度。

[📄 下载本地 PDF](../../../files/vendors/NXP_TJA1044_CAN_FD_datasheet.pdf)

## 参见
- [AH1308 Mantis CAN 收发器应用提示](nxp-ah1308.md)
- [TJA1462 CAN SIC 收发器(Standby)数据手册](nxp-tja1462.md)
- [TCAN1044-Q1 CAN FD 收发器数据手册](ti-tcan1044-q1.md)
- [资源库 — 厂商资料](../../vendors.md)
