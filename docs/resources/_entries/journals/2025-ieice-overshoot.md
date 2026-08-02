---
title: Design and analysis of a low voltage overshoot CAN transceiver interface circuit
description: 西安电子科技大学在 IEICE Electronics Express 发表的 CAN 收发器接口过冲(overshoot)设计与分析论文,面向高速/低电压工作下的振铃抑制与 EMC 发射控制,开放获取并已提供本地 PDF。
type: 期刊
organization: 西安电子科技大学微电子学院
year: 2025
access: free
status: verified
download: local
priority: 3
audience: [模拟IC]
tags: [期刊论文, 收发器, 信号完整性]
source: https://doi.org/10.1587/elex.22.20240720
local_file: files/journals/J2025_IEICE_low_voltage_overshoot_CAN_interface.pdf
---

## 是什么
Weifeng Liu、Jinhui Zhou、Li Zhang(西安电子科技大学微电子学院)、Lei Bai(宝鸡文理学院物理与光电技术学院)发表在 IEICE Electronics Express 2025 年 Vol.22, No.11(文章号 22.20240720)的 CAN 收发器接口电路论文。围绕 CAN 收发器接口在高速/低电压工作下的输出过冲(overshoot)问题展开设计与分析。官方摘要未获取,以下要点依据题目与全文元数据(引用文献)整理:参考文献覆盖 ISO 11898 总线标准、IEC/TS 62228(CAN 收发器 EMC 评估)、TI TCAN1042 CAN FD 收发器、过冲抑制二极管对(IRPS 2017),可见其关注点包括振铃抑制与 EMC 发射控制。

## 为什么值得读
- **模拟IC 工程师**:输出过冲/振铃直接决定 CAN 总线电磁发射与位错误率,是收发器物理层最核心的指标之一。西安电子科技大学团队的本土设计工作对国产 CAN FD 收发器(含 SIC)设计有参考价值,且开放获取。按资料库阅读优先级建议,这是收发器设计工程师应**最先读**的一篇。
- **嵌入式开发工程师**:理解总线波形过冲/振铃对位错误率与 EMC 的影响。

## 核心内容要点
- 围绕 CAN 收发器接口在高速/低电压工作下的输出过冲(overshoot)问题展开设计与分析。
- 参考文献覆盖 ISO 11898 总线标准、IEC/TS 62228(CAN 收发器 EMC 评估)、TI TCAN1042 CAN FD 收发器、过冲抑制二极管对(IRPS 2017)等。
- 关注点包括振铃抑制与 EMC 发射控制;IEICE Electronics Express 为开放获取期刊,可免费全文阅读。

## 怎么读
开放获取,已提供本地 PDF。建议先看接口电路设计与过冲抑制方案,再对照 ISO 11898 总线标准与 IEC/TS 62228 理解其 EMC 评估背景;可作为收发器物理层阅读的起点,再衔接 CAN FD 眼图与 EMC 抗扰类文献。

[📄 下载本地 PDF](../../../files/journals/J2025_IEICE_low_voltage_overshoot_CAN_interface.pdf)

## 参见
- [ISO 11898-2 (2024)](../standards/iso-11898-2-2024.md)
- [IEC/TS 62228-3 (2019)](../standards/iec-62228-3-2019.md)
- [Novel ringing suppression circuit to achieve higher data rates in a linear passive star CAN FD](../papers/2014-mori-ringing-suppression.md)
- [资源库 — 期刊](../../journals.md)
