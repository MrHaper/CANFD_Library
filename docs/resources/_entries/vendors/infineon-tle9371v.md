---
title: TLE9371V CAN SIC 收发器数据手册
description: Infineon 真正的 CAN SIC 收发器数据手册(CiA 601-4 Tx-based CAN FD SIC),环路对称性支持 8 Mbit/s,±8 kV ESD。经 alldatasheet 第三方验证。
type: 厂商资料
organization: Infineon
year: 2023
access: free
status: verified
download: link
priority: 1
audience: [模拟IC]
tags: [Infineon, 数据手册]
source: https://www.alldatasheet.com/datasheet-pdf/pdf/1632707/INFINEON/TLE9371VSJ.html
---

## 是什么
Infineon TLE9371VSJ 是 **Infineon 真正的 CAN SIC 产品**(CiA 601-4 Tx-based CAN FD SIC)数据手册(35 页, 2023-02-28):符合 ISO 11898-2:2016、SAE J2284-4/-5,环路对称性支持 8 Mbit/s;注意与 TLE9255(普通 CAN FD)区分,勿混淆。

## 为什么值得读
- **模拟IC 工程师**:欧洲厂商的 SIC 实现与 NXP/TI 对标,可对比三种主流 SIC 收发器的 ESD/EMC/位对称 Spec 差异,完善 SIC 收发器的设计空间认知。
- **嵌入式开发工程师**:区分 Infineon 产品线中"谁才是 SIC"(TLE9371),避免中文网络常见的 TLE9255 误读。

## 核心内容要点
- **这是 Infineon 真正的 CAN SIC 产品**(CiA 601-4 Tx-based CAN FD SIC),与普通 CAN FD 收发器(TLE9255)本质不同。
- 符合 ISO 11898-2:2016、SAE J2284-4/-5;环路对称性支持 8 Mbit/s。
- 关键特性:VIO 3.3/5 V、低静态电流 Standby、宽共模范围(高 EMI)、±8 kV HBM/IEC ESD、CAN 短路保护、TxD 超时、过温保护。
- 数据手册为 35 页版本,详细参数以原文为准。

## 怎么读
将 TLE9371V 与 NXP TJA1463、TI TCAN1463-Q1 三份 SIC 数据手册对照阅读,重点对比 ESD/EMC 与位对称 Spec 的写法差异。

## 获取渠道
alldatasheet 聚合页(免费):<https://www.alldatasheet.com/datasheet-pdf/pdf/1632707/INFINEON/TLE9371VSJ.html>
Infineon 官网产品搜索(浏览器访问,搜 TLE9371):<https://www.infineon.com>。官网抓取受反爬限制,资料库以第三方验证为准。

## 参见
- [TLE9255W CAN FD 收发器(Partial Networking)数据手册](infineon-tle9255w.md)
- [TJA1463 CAN SIC 收发器(Sleep)数据手册](nxp-tja1463.md)
- [TCAN1463-Q1 CAN SIC 收发器(Sleep/INH/WAKE)数据手册](ti-tcan1463-q1.md)
- [资源库 — 厂商资料](../../vendors.md)
