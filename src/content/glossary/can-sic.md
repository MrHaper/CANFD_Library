---
title: CAN SIC(Signal Improvement Capability)
description: 具备振铃抑制等信号改善能力的 CAN FD 收发器,支持更高速率与更大网络拓扑。
tags: [专家, 收发器]
---
- **定义**:CAN SIC(Signal Improvement Capability,信号改善能力)是 CAN FD 收发器的一个类别,通过振铃抑制、受控上升/下降沿与改善的回波损耗,提升高速数据相位的信号质量,使数据相位速率(如 5 Mbit/s)与总线拓扑(更长总线、更多节点)更可靠。
- **位置/背景**:CAN SIC 的规范本体是 ISO 11898-2:2024(其前身为 CiA 601-4,2023 年撤回并并入 ISO 标准)。SIC 收发器满足 ISO 11898-2:2024 对差分与共模振铃抑制、动态参数与 EMC 的要求;CAN SIC XL 是同标准下的 CAN XL 物理层选项。
- **作用与影响**:相比经典 CAN FD 收发器,SIC 在显性→隐性转换后主动抑制振铃,减少位间干扰与采样错误;振铃抑制与回波损耗改善共同支撑更高的数据相位速率。对收发器设计而言,SIC 是当前模拟 IC 设计的主战场,涉及输出级整形、振铃抑制电路与 EMC 协同设计。
- **参见**:
  - [ringing-suppression.md](ringing-suppression.md)、[return-loss.md](return-loss.md)、[transceiver.md](transceiver.md)
  - [ISO 11898-2 (2024)](../resources/_entries/standards/iso-11898-2-2024.md)
  - [CiA 601-4(SIC,已撤回)](../resources/_entries/standards/cia-601-4-sic.md)
  - [NXP TJA1463 CAN SIC 数据手册](../resources/_entries/vendors/nxp-tja1463.md)
