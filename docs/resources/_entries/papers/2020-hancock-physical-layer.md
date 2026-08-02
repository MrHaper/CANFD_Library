---
title: Characterizing the physical layer of CAN FD
description: Keysight 在 17th iCC 讲解如何用示波器测量 CAN FD 物理层关键动态脉冲参数(环路延迟、隐性位宽)与眼图模板测试。
type: 论文
organization: Keysight
year: 2020
access: free
status: verified
download: local
priority: 2
audience: [模拟IC]
tags: [学术论文, CAN FD, 物理层]
source: https://www.can-cia.org/fileadmin/cia/documents/proceedings/2020_hancock.pdf
local_file: files/papers/2020_Hancock_Characterizing_the_physical_layer_of_CAN_FD.pdf
---

## 是什么
Keysight Technologies 的 J. Hancock 在第 17 届国际 CAN 会议 (17th iCC,线上) "Physical layer" 分会场的实操论文,面向向 CAN FD 迁移带来的新设计/测试挑战,讲解如何用示波器完成收发器环路延迟 (loop delay) 与隐性位宽 (recessive bit width) 等关键动态脉冲参数的测量,并介绍眼图模板 (eye-diagram mask) 测试。

## 为什么值得读
- **模拟IC 工程师**:给出收发器数据阶段高速率下需满足的动态参数与测量方法,是芯片流片后测试验证与规格对标(如与 SIC 对称边沿要求对标)的直接参考。
- **嵌入式开发工程师**:学会用眼图模板评判物理层模拟信号质量,指导网络排障。
- **学生**:把示波器测量与协议动态参数对应起来,是测试方法论入门。

## 核心内容要点
- 面向 CAN FD 迁移带来的新设计/测试挑战,讲解实操测量方法。
- 关键动态脉冲参数:收发器环路延迟 (loop delay) 与隐性位宽 (recessive bit width)。
- 眼图模板 (eye-diagram mask) 测试:作为一次合成测量完成物理层模拟信号质量测试。

## 怎么读
先掌握 loop delay 与 recessive bit width 两个参数的定义,再看示波器测量设置,最后理解眼图模板如何综合评估信号质量。PDF 免费公开,可直接下载本地阅读。

[📄 下载本地 PDF](../../../files/papers/2020_Hancock_Characterizing_the_physical_layer_of_CAN_FD.pdf)

## 参见
- [CAN signal improvement and designing 5-Mbps networks](2020-adamson-5mbps-networks.md)
- [The physical layer in the CAN XL world](2020-hell-can-xl-physical-layer.md)
- [ISO 11898-2 (2024)](../standards/iso-11898-2-2024.md)
- [资源库 — 论文](../../papers.md)
