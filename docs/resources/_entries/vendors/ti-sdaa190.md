---
title: SDAA190 应用笔记:CAN / CAN FD / CAN XL 对比
description: TI 应用笔记,对比经典 CAN、CAN FD 与 CAN XL 的协议、物理层、数据速率与收发器要求,给出选型与迁移路径。
type: 厂商资料
organization: TI
year: 2026
access: free
status: verified
download: local
priority: 1
audience: [模拟IC]
tags: [TI, 应用笔记]
source: https://www.ti.com/lit/pdf/SDAA190
local_file: files/vendors/TI_SDAA190_CAN_CANFD_CANXL_compare.pdf
---

## 是什么
TI SDAA190 应用笔记(2026-06-18)对比经典 CAN、CAN FD 与 CAN XL 的协议、物理层、数据速率(最高 20 Mbit/s)与收发器要求,并给出选型与迁移路径。

## 为什么值得读
- **模拟IC 工程师**:快速补齐"从 CAN FD 到 CAN XL 物理层差异(如总线负载范围、信号改善等级)"的知识框架,与 NXP TJA1464(CAN XL ready)互相印证。
- **嵌入式开发工程师**:面向新项目协议选型与迁移的决策参考。

## 核心内容要点
### 内部框图要点
- 应用笔记为对比综述型文档,不含芯片内部框图;重点在协议与物理层的横向对比。
- 覆盖经典 CAN、CAN FD 与 CAN XL 的协议、物理层、数据速率与收发器要求。

### 关键电气参数
- 数据速率对比最高 20 Mbit/s(CAN XL);CAN FD 与 CAN XL 的物理层差异(总线负载范围、信号改善等级)是核心看点。
- 具体数值详见原文对比表,不在此逐项转录。

### 对收发器设计的意义
- 建立三代协议对物理层要求的纵向认知,为规划下一代(CAN XL)收发器提供框架。
- 与 TJA1464 的 CAN XL 兼容能力互相印证,指导演进方向。

## 怎么读
通读对比表建立全貌即可;若面向 CAN XL 设计,再结合 ISO 11898-2:2024(SIC XL 部分)深入。

[📄 下载本地 PDF](../../../files/vendors/TI_SDAA190_CAN_CANFD_CANXL_compare.pdf)

## 参见
- [TJA1464 CAN SIC(ASIL B)产品页 + Fact Sheet](nxp-tja1464.md)
- [SLLA581 白皮书:SIC 如何释放 CAN FD 真正潜力](ti-slla581.md)
- [资源库 — 厂商资料](../../vendors.md)
