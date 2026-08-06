---
title: TJA1464 CAN SIC(ASIL B)产品页+Fact Sheet
description: NXP 下一代 CAN SIC(ASIL B)收发器产品页与 Fact Sheet,较 TJA1462 成本优化,扩展总线负载兼容 CAN XL fast mode。
type: 厂商资料
organization: NXP
year: 2026
access: free
status: verified
download: local
priority: 1
audience: [模拟IC]
tags: [NXP, 数据手册/产品页]
source: "https://www.nxp.com/products/TJA1464"

local_file: files/vendors/NXP_TJA1464_CAN_SIC_ASILB_factsheet.pdf
---

## 是什么
NXP TJA1464 是面向 ISO 11898-2:2024 / SAE J2284-1~5 的下一代 CAN SIC 收发器(数据手册为 Preproduction 状态,产品介绍 2026-03-16),较 TJA1462 更成本优化,新增 ASIL B(ISO 26262)功能安全,并扩展总线负载以兼容 CAN XL fast mode。

## 为什么值得读
- **模拟IC 工程师**:Fact Sheet(CANPNFSA4)与产品规格给出 SIC→CAN XL 演进路线(总线负载范围扩大),是规划下一代收发器(支持 CAN XL)的参考;ASIL B 文档清单可作功能安全设计模板。
- **嵌入式开发工程师**:了解 ASIL B 功能安全在收发器上的落地要求(safety manual / FMEDA),用于安全相关 ECU 选型。

## 核心内容要点
### 内部框图要点
- ISO 11898-2:2024 / SAE J2284-1~5 的 CAN SIC 收发器,较 TJA1462 成本优化,新增 ASIL B(ISO 26262)功能安全(含 safety manual / FMEDA)。
- 详细模块结构以数据手册与 Fact Sheet 原文为准。

### 关键电气参数
- 扩展总线负载 45–65 Ω,兼容 CAN XL fast mode;唤醒模式时间缩短至 1.45 µs。
- 其余参数详见产品页 / Fact Sheet 原文,不在此逐项转录。

### 对收发器设计的意义
- SIC→CAN XL 演进路线(总线负载范围扩大)可作为自研下一代收发器的方向参考。
- ASIL B 文档清单(safety manual / FMEDA)可复制为功能安全设计模板。

## 怎么读
先读 Fact Sheet 了解定位与演进路线,再按需查看产品页的规格表与文档清单;与 SDAA190(CAN/CAN FD/CAN XL 对比)互相印证。

[📄 下载本地 PDF](../../../files/vendors/NXP_TJA1464_CAN_SIC_ASILB_factsheet.pdf)

## 参见
- [TJA1462 CAN SIC 收发器(Standby)数据手册](nxp-tja1462.md)
- [SDAA190 应用笔记:CAN / CAN FD / CAN XL 对比](ti-sdaa190.md)
- [TJA1463 CAN SIC 收发器(Sleep)数据手册](nxp-tja1463.md)
- [资源库 — 厂商资料](../../vendors.md)
