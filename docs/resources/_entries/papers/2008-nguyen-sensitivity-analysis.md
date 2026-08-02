---
title: Sensitivity analysis of passive CAN bus components to investigate signal integrity of CAN network physical layer
description: KAI/Fraunhofer IIS/Infineon 在 BMAS 2008 对 CAN 物理层无源器件参数偏差做敏感性分析,输出各参数对信号质量指标的敏感度排序。
type: 论文
organization: KAI / Fraunhofer IIS / Infineon
year: 2008
access: paid
status: verified
download: link
priority: 1
audience: [模拟IC]
tags: [学术论文, 物理层, 信号完整性, 网络]
source: https://doi.org/10.1109/bmas.2008.4751240
---

## 是什么
Thang Nguyen (KAI)、Joachim Haase (Fraunhofer IIS/EAS)、Georg Pelz (Infineon Technologies) 在 2008 IEEE BMAS 发表的论文:对 CAN 网络物理层中的无源器件(线缆、连接器、端接、共模扼流圈等)参数偏差进行敏感性分析,研究这些偏差如何影响差分信号完整性与位时序,采用行为建模/仿真方法输出各参数对信号质量指标的敏感度排序。

## 为什么值得读
- **模拟IC 工程师**:从网络物理层信号完整性反向给出收发器驱动能力、输出阻抗与斜率控制的裕量要求,是收发器驱动设计做系统级仿真(协同仿真)时的依据。
- **嵌入式开发工程师**:理解端接、线缆等无源器件参数偏差如何影响总线信号质量。
- **学生**:了解敏感性分析与行为建模在信号完整性研究中的应用。

## 核心内容要点
- 对 CAN 网络物理层中的无源器件(线缆、连接器、端接、共模扼流圈等)参数偏差进行敏感性分析。
- 研究偏差如何影响差分信号完整性与位时序。
- 采用行为建模/仿真方法,输出各参数对信号质量指标的敏感度排序。

## 怎么读
关注敏感度排序结论,理解哪些无源器件参数最影响信号完整性,再反推收发器驱动能力与输出阻抗的裕量要求。

## 获取渠道
付费论文(IEEE):通过 IEEEXplore 按 DOI 访问,需机构订阅或单篇购买。
DOI: [10.1109/bmas.2008.4751240](https://doi.org/10.1109/bmas.2008.4751240)

## 参见
- [Characterizing the physical layer of CAN FD](2020-hancock-physical-layer.md)
- [ISO 11898-2 (2024)](../standards/iso-11898-2-2024.md)
- [资源库 — 论文](../../papers.md)
