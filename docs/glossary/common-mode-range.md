---
title: 共模范围(Common-mode Range)
description: 接收器在 CANH/CANL 相对地电位偏移时仍能正确判别显性/隐性的共模电压范围。
tags: [进阶, 收发器]
---
- **定义**:共模范围(Common-mode Range)是 CAN 收发器接收比较器可正常工作的共模输入电压范围:总线两线相对地的平均电位(V_CANH 与 V_CANL 的平均)发生偏移时,接收器仍须正确判别差分电平的显性/隐性。经典高速 CAN 收发器的共模范围典型覆盖 -12 V ~ +12 V(具体以标准与器件手册为准)。
- **位置/背景**:共模偏移来自地电位差、线束耦合干扰与故障注入;ISO 11898-2 对差分接收器提出共模范围要求,器件数据手册会标注该指标。
- **作用与影响**:共模范围不足会导致接收器误判(如把噪声当成显性位),引发错误帧与通信中断;对车载多节点、长线束与故障(对电源/对地短路)防护设计尤为重要,是收发器选型的必查项。
- **参见**:
  - [dominant-recessive-levels.md](dominant-recessive-levels.md)、[transceiver.md](transceiver.md)、[emi-emc.md](emi-emc.md)
  - [NXP TJA1044 CAN FD 数据手册](../resources/_entries/vendors/nxp-tja1044.md)
  - [TI TCAN1044-Q1 CAN FD 数据手册](../resources/_entries/vendors/ti-tcan1044-q1.md)
