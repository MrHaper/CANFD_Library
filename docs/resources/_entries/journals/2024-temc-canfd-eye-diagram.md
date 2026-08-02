---
title: Controller Area Network With Flexible Data Rate (CAN FD) Eye Diagram Prediction
description: 密苏里科技大学 EMC 实验室等团队在 T-EMC 提出的 CAN FD 眼图预测方法:以迭代单比特响应法与改进双沿响应法预测眼图,标称 1 Mb/s、可选 2 Mb/s 数据率下与实测几乎一致。
type: 期刊
organization: 密苏里科技大学 EMC 实验室
year: 2024
access: paid
status: verified
download: link
priority: 3
audience: [模拟IC]
tags: [期刊论文, CAN FD, 信号完整性, 网络]
source: https://doi.org/10.1109/TEMC.2024.3350054
---

## 是什么
Junyong Park、DongHyun Kim(密苏里科技大学 EMC 实验室)、Manho Lee(三星电子)、Shinyoung Park(Rambus)、Jonghoon Kim、Joungho Kim(韩国 KAIST)等发表在 IEEE Transactions on Electromagnetic Compatibility 2024 年 Vol.66(pp.949-959)的论文。CAN FD 按状态切换数据速率(数据段最高 5 Mb/s)以突破经典 CAN 的延迟瓶颈,但多 ECU 总线拓扑带来显著信号反射,使信号完整性分析不确定。论文提出 CAN FD 简化模型与眼图预测方法:确定性部分用迭代单比特响应法得到 CAN FD 报文比特概率,统计部分用改进的双沿响应法处理可变速率。预测眼图与实测眼图在标称 1 Mb/s、可选 2 Mb/s 数据率下几乎一致。

## 为什么值得读
- **模拟IC 工程师**:与 SIC 收发器要解决的物理层问题(振铃、反射、眼图闭合)直接对应,提供了收发器+线束+终端网络联合仿真的眼图分析方法,可作为 SIC"信号改善能力"设计验证的参考方法。按资料库阅读优先级建议,属于收发器设计工程师**优先阅读**的第 2 篇。
- **嵌入式开发工程师**:理解多 ECU 拓扑下信号反射如何影响 CAN FD 眼图与数据段速率选择。

## 核心内容要点
- 提出 CAN FD 简化模型与眼图预测方法:确定性部分用迭代单比特响应法得到 CAN FD 报文比特概率。
- 统计部分用改进的双沿响应法处理可变速率。
- 预测眼图与实测眼图在标称 1 Mb/s、可选 2 Mb/s 数据率下几乎一致。

## 怎么读
付费期刊论文。建议先掌握眼图预测方法框架(确定性单比特响应 + 统计双沿响应),再理解收发器+线束+终端联合仿真如何用于 SIC"信号改善能力"设计验证。

## 获取渠道
付费论文(IEEE):通过 IEEEXplore 按 DOI 访问,需机构订阅或单篇购买。
DOI: [10.1109/TEMC.2024.3350054](https://doi.org/10.1109/TEMC.2024.3350054)

## 参见
- [Characterizing the physical layer of CAN FD](../papers/2020-hancock-physical-layer.md)
- [ISO 11898-2 (2024)](../standards/iso-11898-2-2024.md)
- [CiA 601-4 CAN FD node and system design – Part 4: Signal improvement](../standards/cia-601-4-sic.md)
- [资源库 — 期刊](../../journals.md)
