---
title: TCAN1463-Q1 CAN SIC 收发器(Sleep/INH/WAKE)数据手册
description: TI 车规 CAN SIC 收发器数据手册,符合 ISO 11898-2:2016 与 CiA 601-4,带 INH 高边电源控制与 SWE 定时器,主动消除振铃并支持 8 Mbps。
type: 厂商资料
organization: TI
year: 2022
access: free
status: verified
download: local
priority: 3
audience: [模拟IC]
tags: [TI, 数据手册]
source: https://www.ti.com/lit/gpn/TCAN1463-Q1
local_file: files/vendors/TI_TCAN1463-Q1_CAN_SIC_datasheet.pdf
---

## 是什么
TI TCAN1463-Q1 是符合 ISO 11898-2:2016 与 CiA 601-4 SIC 的车规低功耗 CAN SIC 收发器数据手册(Rev C, 2022-12-22),支持 8 Mbps CAN FD,带 INH 高边电源控制、INH_MASK、WAKE 与 SWE 定时器等系统级电源管理功能。

## 为什么值得读
- **模拟IC 工程师**:TI 对 SIC 的实现(TXD DTO、SWE 定时器、INH 电源门控)展示了大拓扑下系统级低功耗与振铃抑制的完整方案;EVM(TCAN1463EVM,用户指南 SLLU343)布局可参考。
- **嵌入式开发工程师**:理解 INH/INH_MASK/WAKE/SWE 定时器在整车电源管理中的用法,是低功耗 CAN 节点设计的参考。
- **学生**:与 NXP TJA1463 对照,可同时看到两家厂商对同一 SIC 标准的差异化实现。

## 核心内容要点
### 内部框图要点
- 符合 ISO 11898-2:2016 与 CiA 601-4 SIC 的车规低功耗收发器核心,主动消除 dominant→recessive 边缘振铃并增强位对称。
- 集成 INH 高边电源控制、INH_MASK、WAKE 与 SWE 定时器等电源管理外设;VSON / SOIC / SOT-23-THN 14 引脚,与 TCAN1043 引脚兼容。
- 具体模块划分与引脚功能详见数据手册原文"内部框图 / 引脚信息"章节。

### 关键电气参数
- 支持 8 Mbps CAN FD;±58 V 总线容错。
- TXD DTO(TXD 显性超时)、欠压与过温保护。
- 系统级低功耗设计(INH 电源门控、SWE 定时器);其余详细参数见数据手册"电气特性"章节。

### 对收发器设计的意义
- 展示"SIC 核心 + 电源管理外设"的系统级方案:SWE 定时器与 INH 电源门控可用于自研芯片的低功耗模式设计。
- EVM(TCAN1463EVM)布局可参考,用于验证大拓扑下的振铃抑制效果。

## 怎么读
先读"特性与说明"了解 INH/WAKE/SWE 定时器的系统设计意图,再对照 ISO 11898-2:2016 精读 SIC 相关电气特性,最后参考 EVM 用户指南(SLLU343)理解布局要点。与 NXP TJA1463、Infineon TLE9371V 三份 SIC 数据手册对照阅读可形成完整对标认知。

[📄 下载本地 PDF](../../../files/vendors/TI_TCAN1463-Q1_CAN_SIC_datasheet.pdf)

## 参见
- [TJA1463 CAN SIC 收发器(Sleep)数据手册](nxp-tja1463.md)
- [TCAN1462-Q1 CAN SIC 收发器(Standby)数据手册](ti-tcan1462-q1.md)
- [TLE9371V CAN SIC 收发器数据手册](infineon-tle9371v.md)
- [SLLA581 白皮书:SIC 如何释放 CAN FD 真正潜力](ti-slla581.md)
- [资源库 — 厂商资料](../../vendors.md)
