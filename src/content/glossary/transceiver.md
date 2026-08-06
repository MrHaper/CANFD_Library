---
title: 收发器(Transceiver)
description: 连接 CAN 控制器与差分总线的接口芯片,负责电平转换与总线驱动/接收。
tags: [入门, 收发器]
---
- **定义**:CAN 收发器(Transceiver)是介于 CAN 协议控制器(TxD/RxD 数字接口)与差分总线(CANH/CANL)之间的模拟接口芯片:发送时把 TxD 电平转换为总线差分显性/隐性电平,接收时把总线差分电平转换为 RxD 逻辑电平,并承担总线故障防护与 ESD 保护。
- **位置/背景**:属于物理介质连接(PMA)子层,由 ISO 11898-2 规定其电气特性(驱动能力、接收阈值、传播延迟、共模范围、EMC 等);连接方式为 CANH/CANL 双线接总线,一端接控制器。
- **作用与影响**:收发器决定了网络的物理层性能:传播延迟及其对称性、压摆率与 EMI、共模范围、回波损耗、振铃行为。CAN FD 高速数据相位对收发器环路延迟与对称性提出新要求,由此催生了 CAN FD 收发器与 CAN SIC 收发器两类产品。
- **参见**:
  - [can-sic.md](can-sic.md)、[propagation-delay-symmetry.md](propagation-delay-symmetry.md)、[common-mode-range.md](common-mode-range.md)
  - [NXP TJA1462 CAN SIC 数据手册](../resources/_entries/vendors/nxp-tja1462.md)
  - [TI TCAN1463-Q1 CAN SIC 数据手册](../resources/_entries/vendors/ti-tcan1463-q1.md)
  - [ISO 11898-2 (2024)](../resources/_entries/standards/iso-11898-2-2024.md)
