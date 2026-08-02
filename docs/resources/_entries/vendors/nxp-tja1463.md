---
title: TJA1463 CAN SIC 收发器(Sleep)数据手册
description: NXP TJA146x 家族 CAN SIC 收发器数据手册,实现 ISO 11898-2:2024 与 CiA 601-4 SIC,抑制网络振铃并支持 CAN FD 至 8 Mbit/s。
type: 厂商资料
organization: NXP
year: 2025
access: free
status: verified
download: local
priority: 3
audience: [模拟IC]
tags: [NXP, 数据手册]
source: https://www.nxp.com/docs/en/data-sheet/TJA1463.pdf
local_file: files/vendors/NXP_TJA1463_CAN_SIC_datasheet.pdf
---

## 是什么
NXP TJA1463 是 TJA146x 家族 CAN SIC(Signal Improvement Capability)收发器(Sleep 模式版本)的数据手册(Rev 3.0, 2025-02-12),实现 ISO 11898-2:2024 第三版与 CiA 601-4 SIC,通过显著抑制网络振铃支持 CAN FD 至 8 Mbit/s,并集成 VIO 电平接口、欠压检测与失效安全等完整收发器功能。

## 为什么值得读
- **模拟IC 工程师**:数据手册中"位时序对称性/环路延迟"与"振铃抑制"相关电气特性(SIC 输出级指标)可直接作为自己流片芯片的 Spec 对标清单;EME/EMI 测试方法与 IEC 62228-3 的对照也在此文档中。
- **嵌入式开发工程师**:了解主流 SIC 收发器的 Sleep 模式电源管理、VIO 电平接口与失效安全设计,便于选型与车载网络拓扑规划。
- **学生**:一份完整的 SIC 收发器数据手册范本,可与 ISO 11898-2:2024 条款一一对应,是"芯片级规范长什么样"的直观教材。

## 核心内容要点
### 内部框图要点
- TJA146x 家族 CAN SIC 收发器,实现 ISO 11898-2:2024 第三版与 CiA 601-4 SIC,显著抑制网络振铃。
- 含 Sleep 模式电源管理、VIO(3.3–5 V)电平接口、欠压检测与失效安全等模块;采用 SO14 / HVSON14 封装,与前代 TJA1043 / TJA1443 引脚兼容。
- 具体模块划分、引脚定义与典型应用电路详见数据手册原文"内部框图 / 引脚信息"章节。

### 关键电气参数
- 支持 CAN FD 至 8 Mbit/s;低 EME / 高 EMI 特性。
- VIO 电平接口 3.3–5 V;内置欠压检测与失效安全。
- 车规等级 AEC-Q100 Grade 1;其余详细参数见数据手册"电气特性"章节(资料库未逐项转录,以原文为准)。

### 对收发器设计的意义
- SIC 输出级的位时序对称性 / 环路延迟与振铃抑制指标,可直接作为自己流片芯片的 Spec 对标清单。
- EME/EMI 测试方法与 IEC 62228-3 对照,可复用到自研芯片的 EMC 测试与认证流程。

## 怎么读
建议与 ISO 11898-2:2024、CiA 601-4 对照阅读:先看内部框图建立模块认知,再精读位时序对称性与振铃抑制电气特性,最后对照 EMC 测试章节理解测试方法。可与 NXP TJA1462(Standby 版)对比,观察"同一 SIC 核心 + 不同电源管理外设"的家族化设计思路。

[📄 下载本地 PDF](../../../files/vendors/NXP_TJA1463_CAN_SIC_datasheet.pdf)

## 参见
- [TJA1462 CAN SIC 收发器(Standby)数据手册](nxp-tja1462.md)
- [TJA1464 CAN SIC(ASIL B)产品页 + Fact Sheet](nxp-tja1464.md)
- [TCAN1463-Q1 CAN SIC 收发器(Sleep/INH/WAKE)数据手册](ti-tcan1463-q1.md)
- [SLLA581 白皮书:SIC 如何释放 CAN FD 真正潜力](ti-slla581.md)
- [资源库 — 厂商资料](../../vendors.md)
