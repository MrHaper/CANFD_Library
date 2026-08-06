---
title: TJA1462 CAN SIC 收发器(Standby)数据手册
description: "NXP TJA146x 家族 8 引脚版本 CAN SIC 收发器数据手册,实现 ISO 11898-2:2024 与 CiA 601-4 SIC,Standby 带总线唤醒。"

type: 厂商资料
organization: NXP
year: 2025
access: free
status: verified
download: local
priority: 1
audience: [模拟IC]
tags: [NXP, 数据手册]
source: "https://www.nxp.com/docs/en/data-sheet/TJA1462.pdf"

local_file: files/vendors/NXP_TJA1462_CAN_SIC_datasheet.pdf
---

## 是什么
NXP TJA1462 是 TJA146x 家族的 8 引脚(SO8 / HVSON8)版本 CAN SIC 收发器数据手册(Rev 3.0, 2025-02-12),实现 ISO 11898-2:2024 与 CiA 601-4 SIC,更紧的位时序对称性支持大型拓扑下 5 Mbit/s 乃至 8 Mbit/s CAN FD,Standby 模式带总线唤醒。

## 为什么值得读
- **模拟IC 工程师**:与 TJA1463 同源,SIC 输出驱动(回波/振铃抑制)与接收器共模/EMC 指标一致;8 引脚小型封装版本适合对照学习"无 Sleep 功能"的简化收发器架构。
- **嵌入式开发工程师**:与 TJA1042 / TJA1044GT 兼容替换,是 8 引脚 SIC 升级路径的选型参考。

## 核心内容要点
### 内部框图要点
- 8 引脚(SO8 / HVSON8)版本的 CAN SIC 收发器,实现 ISO 11898-2:2024 + CiA 601-4 SIC。
- Standby 模式带总线唤醒;与 TJA1042 / TJA1044GT 兼容替换;具体模块划分与引脚功能详见数据手册原文"内部框图 / 引脚信息"章节。

### 关键电气参数
- 更紧的位时序对称性,支持大型拓扑下 5 Mbit/s 乃至 8 Mbit/s CAN FD。
- SIC 输出驱动(回波/振铃抑制)与接收器共模/EMC 指标与 TJA1463 一致;其余详细参数见数据手册"电气特性"章节。

### 对收发器设计的意义
- 作为"无 Sleep 功能的简化 SIC 架构"样本,帮助理解 8 引脚收发器的模式/引脚取舍。
- 位时序对称性 Spec 写法与 TJA1463 对照,可用于自研芯片指标定义。

## 怎么读
与 TJA1463 数据手册对照阅读:重点比较两者在模式、封装、引脚上的差异,再精读位时序对称性章节;更深入的 SIC 概念可先读 SLLA581 白皮书。

[📄 下载本地 PDF](../../../files/vendors/NXP_TJA1462_CAN_SIC_datasheet.pdf)

## 参见
- [TJA1463 CAN SIC 收发器(Sleep)数据手册](nxp-tja1463.md)
- [TCAN1462-Q1 CAN SIC 收发器(Standby)数据手册](ti-tcan1462-q1.md)
- [TJA1044 CAN FD 收发器数据手册](nxp-tja1044.md)
- [资源库 — 厂商资料](../../vendors.md)
