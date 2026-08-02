---
title: Automated analysis for vehicle communication
description: Vector 在 16th iCC 提出将逻辑网络分析与物理层事件严格时间关联的自动化分析概念,用于开发早期定位错误及其物理层根因。
type: 论文
organization: Vector
year: 2017
access: free
status: verified
download: local
priority: 1
audience: [模拟IC]
tags: [学术论文]
source: https://www.can-cia.org/fileadmin/cia/documents/proceedings/2017_donatzer.pdf
local_file: files/papers/2017_Donatzer_Automated_analysis_vehicle_communication.pdf
---

## 是什么
M. Donatzer (Vector Informatik) 在第 16 届国际 CAN 会议 (16th iCC) 提出的车载通信自动化分析方法:将逻辑网络分析与物理层事件建立严格时间关联,使工程师能在开发早期定位错误及其物理层根因。

## 为什么值得读
- **模拟IC 工程师**:从物理层信号质量(振铃、边沿劣化)角度说明收发器驱动能力与网络负载的相互作用,帮助理解系统级验证方法。
- **嵌入式开发工程师**:学习车载网络故障定位的自动化分析思路,缩短排障周期。
- **学生**:见识"逻辑层 × 物理层"跨层关联分析的方法论。

## 核心内容要点
- 背景:CAN FD 数据段更高的带宽使网络对不利拓扑、电磁干扰源、错误端接显著更敏感。
- 提出综合概念,将逻辑网络分析与物理层事件建立严格时间关联。
- 使工程师能在开发早期定位错误及其物理层根因。

## 怎么读
了解自动化分析的整体流程,重点看物理层事件(振铃、边沿劣化)如何与逻辑错误关联定位。PDF 免费公开,可直接下载本地阅读。

[📄 下载本地 PDF](../../../files/papers/2017_Donatzer_Automated_analysis_vehicle_communication.pdf)

## 参见
- [Managing the transition to robust CAN FD](2017-adamson-robust-can-fd.md)
- [Characterizing the physical layer of CAN FD](2020-hancock-physical-layer.md)
- [资源库 — 论文](../../papers.md)
