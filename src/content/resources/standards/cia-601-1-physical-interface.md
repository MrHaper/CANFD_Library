---
title: CiA 601 系列 Part 1
description: CAN FD 节点物理接口实现指南,指定 Tx/Rx 延迟对称性数值与不同速率下 RxD 隐性位时间要求。
type: 标准规范
organization: CiA
year: 2021
version: v2.0.0
access: free
status: verified
download: link
priority: 1
audience: [模拟IC]
tags: [标准规范, CiA 601]
source: "https://www.can-cia.org/can-knowledge/cia-601-series-can-fd-guidelines-and-recommendations"

---

## 是什么
CiA 601-1 是 CAN FD 节点与系统设计系列的技术报告(TR)之一,规定物理接口实现:Tx/Rx 延迟对称性、不同速率(1/2/5 Mbit/s)下 RxD 隐性位时间要求,以及隔离设计的延迟计算规则。

## 为什么值得读
- **模拟IC 工程师**:601-1 的延迟对称性数值直接给出收发器内部电路(驱动、接收比较器、滤波器)的延迟预算。
- **嵌入式开发工程师**:帮助理解节点级物理接口约束,便于板级设计(隔离、走线)。

## 核心内容要点
- Tx/Rx 延迟对称性要求与数值。
- 1/2/5 Mbit/s 速率下 RxD 隐性位时间要求。
- 隔离设计的延迟计算规则。

## 怎么读
与 ISO 11898-2:2024 的对称性条款对照阅读;注册 CiA 账号后可免费下载。

## 参见
- [CiA 601 系列 Part 3](cia-601-3-bit-timing.md)
- [ISO 11898-2 (2024)](iso-11898-2-2024.md)
- [资源库 — 标准规范](../../standards.md)
