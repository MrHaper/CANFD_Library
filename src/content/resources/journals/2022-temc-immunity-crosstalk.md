---
title: Immunity of CAN, CAN FD and Automotive Ethernet 100/1000BASE-T1 to Crosstalk From Power Electronic Systems
description: "德国多特蒙德工业大学 T-EMC 论文:通过仿真与实测对比 CAN、CAN FD 与 Automotive Ethernet 对电力电子系统串扰的鲁棒性,给出 CAN FD 真实车载 EMC 抗扰边界。"

type: 期刊
organization: 德国多特蒙德工业大学,On-board Systems Lab
year: 2022
access: paid
status: verified
download: link
priority: 3
audience: [模拟IC]
tags: [期刊论文, CAN FD]
source: "https://doi.org/10.1109/TEMC.2022.3206334"

---

## 是什么
Carina Austermann、Stephan Frei(德国多特蒙德工业大学,On-board Systems Lab)发表在 IEEE Transactions on Electromagnetic Compatibility 2022 年 Vol.64(pp.2283-2291)的论文。电动化使车内集成了更多电力电子系统,加之线束延长与间距缩小,电力电子系统与通信系统之间的电磁耦合更易发生,可能影响数据传输可靠性。论文通过仿真与实测,对比分析 CAN、CAN FD 与 Automotive Ethernet(100BASE-T1、1000BASE-T1)在来自线缆与 PCB 耦合的共模/差模干扰下的鲁棒性,识别关键耦合配置,并讨论各总线系统的 EMC 性能差异。

## 为什么值得读
- **模拟IC 工程师**:给出 CAN FD 在真实车载 EMC 环境下的抗扰边界,是确定收发器共模抑制能力(CMRR、共模扼流圈配合、差分线路对称性)需求的重要系统级依据。按资料库阅读优先级建议,属于收发器设计工程师**优先阅读**的第 3 篇。
- **嵌入式开发工程师**:理解电力电子系统串扰对 CAN FD 通信可靠性的影响,以及布线/屏蔽层面的对策。

## 核心内容要点
- 通过仿真与实测,对比分析 CAN、CAN FD 与 Automotive Ethernet(100BASE-T1、1000BASE-T1)在共模/差模干扰下的鲁棒性。
- 干扰来源为线缆与 PCB 耦合;研究识别关键耦合配置。
- 讨论各总线系统的 EMC 性能差异。

## 怎么读
付费期刊论文。建议先读结论与关键耦合配置(各总线抗扰差异),再回看仿真/实测方法,最后把 CAN FD 抗扰边界转化为收发器共模抑制能力(CMRR、共模扼流圈配合、差分线路对称性)的需求。

## 获取渠道
付费论文(IEEE):通过 IEEEXplore 按 DOI 访问,需机构订阅或单篇购买。
DOI: [10.1109/TEMC.2022.3206334](https://doi.org/10.1109/TEMC.2022.3206334)

## 参见
- [ISO 11898-2 (2024)](../standards/iso-11898-2-2024.md)
- [CiA 601-4 CAN FD node and system design – Part 4: Signal improvement](../standards/cia-601-4-sic.md)
- [资源库 — 期刊](../../journals.md)
