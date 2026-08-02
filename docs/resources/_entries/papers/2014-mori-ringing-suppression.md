---
title: Novel ringing suppression circuit to achieve higher data rates in a linear passive star CAN FD
description: DENSO 在 EMC Europe 2014 提出针对线性无源星型 CAN FD 拓扑的振铃抑制电路,是 CAN SIC 对称边沿/振铃抑制思想的关键学术前身。
type: 论文
organization: DENSO
year: 2014
access: paid
status: verified
download: link
priority: 2
audience: [模拟IC]
tags: [学术论文, CAN FD, 振铃抑制]
source: https://doi.org/10.1109/emceurope.2014.6930940
---

## 是什么
Hiroyuki Mori 等人 (DENSO Corporation) 在 2014 IEEE EMC Europe 提出的振铃抑制电路方案,针对无源星型 (linear passive star) CAN FD 拓扑中由阻抗失配引起的差分振铃限制数据率的问题,实测将星型网络的可用数据率提升至更高水平,并分析振铃机理与抑制电路的工作原理和效果。

## 为什么值得读
- **模拟IC 工程师**:差分振铃抑制正是后来 CAN SIC 收发器的核心技术诉求(对称边沿、低回波衰减),本文是 SIC 思想在学术文献中的关键前身,对理解 SIC 收发器为何采用对称驱动与斜率整形有直接帮助。
- **嵌入式开发工程师**:理解星型拓扑下数据率的限制因素与抑制振铃的系统收益。

## 核心内容要点
- 分析无源星型 CAN FD 拓扑中阻抗失配引起的差分振铃及其对数据率的限制。
- 提出振铃抑制电路方案,实测提升星型网络可用数据率。
- 分析振铃机理与抑制电路的工作原理和效果。

## 怎么读
重点读振铃机理分析与抑制电路工作原理,再对照 SIC 规范(对称边沿、低回波衰减)看思想的规范化过程。

## 获取渠道
付费论文(IEEE):通过 IEEEXplore 按 DOI 访问,需机构订阅或单篇购买。
DOI: [10.1109/emceurope.2014.6930940](https://doi.org/10.1109/emceurope.2014.6930940)

## 参见
- [CiA 601-4 (SIC)](../standards/cia-601-4-sic.md)
- [CAN signal improvement and designing 5-Mbps networks](2020-adamson-5mbps-networks.md)
- [资源库 — 论文](../../papers.md)
