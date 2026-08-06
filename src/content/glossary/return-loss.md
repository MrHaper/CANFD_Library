---
title: 回波损耗(Return Loss)
description: 收发器输入阻抗与总线特征阻抗匹配程度的度量,以 dB 表示,数值越大反射越少。
tags: [专家, 收发器]
---
- **定义**:回波损耗(Return Loss)是收发器总线端阻抗与总线特征阻抗(120 Ω 双绞线)匹配程度的度量,定义为入射功率与反射功率之比(以 dB 表示);数值越大,阻抗匹配越好、信号反射越少。CAN FD 高速数据相位尤其关注高数据率频率范围内的回波损耗。
- **位置/背景**:属于 ISO 11898-2(以及 CAN SIC 条款)对收发器输入阻抗的要求;回波损耗随频率变化,高频段更易因寄生电容/电感劣化,是 SIC 收发器设计难点之一。
- **作用与影响**:阻抗失配产生的反射叠加到原始信号上,造成振铃、眼图收窄与采样错误;良好的回波损耗与振铃抑制共同支撑高速数据相位。对设计者而言,封装、引脚与片上输入网络都影响高频回波损耗。
- **参见**:
  - [bus-termination.md](bus-termination.md)、[ringing-suppression.md](ringing-suppression.md)、[can-sic.md](can-sic.md)
  - [ISO 11898-2 (2024)](../resources/_entries/standards/iso-11898-2-2024.md)
  - [Hancock 2020: Characterizing the physical layer of CAN FD](../resources/_entries/papers/2020-hancock-physical-layer.md)
