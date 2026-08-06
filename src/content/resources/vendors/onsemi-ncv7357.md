---
title: NCV7357 CAN FD 收发器数据手册
description: "onsemi CAN FD 高速收发器数据手册,ISO 11898-2:2016,时序保证至 5 Mbps,无需共模扼流圈低 EME,>8 kV 系统 ESD,AEC-Q100 Grade 0。"

type: 厂商资料
organization: onsemi
access: free
status: verified
download: local
priority: 1
audience: [模拟IC]
tags: [onsemi, 数据手册]
source: "https://www.onsemi.com/download/data-sheet/pdf/ncv7357-d.pdf"

local_file: files/vendors/onsemi_NCV7357_CAN_FD_datasheet.pdf
---

## 是什么
onsemi NCV7357 是符合 ISO 11898-2:2016 的 CAN FD 高速收发器数据手册,CAN FD 时序保证至 5 Mbps,无需共模扼流圈即可实现低 EME / 高 EMI。

## 为什么值得读
- **模拟IC 工程师**:低成本 CAN FD 基线 + "无共模扼流圈低 EME"的实现思路;Grade 0(150 °C)车规等级对高温场景设计有参考。
- **嵌入式开发工程师**:SOIC-8 / DFNW-8 封装,经济型 CAN FD 节点选型参考。

## 核心内容要点
### 内部框图要点
- ISO 11898-2:2016 的 CAN FD 高速收发器;具体模块划分与引脚功能详见数据手册原文"内部框图 / 引脚信息"章节。

### 关键电气参数
- CAN FD 时序保证至 5 Mbps;无需共模扼流圈即低 EME / 高 EMI。
- >8 kV 系统 ESD、TXD 超时、热保护、总线短路保护;AEC-Q100 **Grade 0**(150 °C)。
- 封装:SOIC-8 / DFNW-8;其余详细参数见数据手册"电气特性"章节。

### 对收发器设计的意义
- "无共模扼流圈低 EME"的实现思路可作低成本设计的对标对象。
- Grade 0(150 °C)车规等级为高温场景设计提供参考。

## 怎么读
作为低成本基线阅读:先看电气特性,重点对比其"无共模扼流圈"EME 实现与 NXP/TI 方案的差异,再与 TCAN1044-Q1、TJA1044 做性能对标。

[📄 下载本地 PDF](../../../files/vendors/onsemi_NCV7357_CAN_FD_datasheet.pdf)

## 参见
- [TCAN1044-Q1 CAN FD 收发器数据手册](ti-tcan1044-q1.md)
- [TJA1044 CAN FD 收发器数据手册](nxp-tja1044.md)
- [资源库 — 厂商资料](../../vendors.md)
