---
title: 振铃抑制(Ringing Suppression)
description: CAN SIC 收发器在显性→隐性转换后主动抑制总线振铃的能力,是 SIC 的核心特性。
tags: [专家, 收发器]
---
- **定义**:振铃抑制(Ringing Suppression)是 CAN SIC 收发器在显性→隐性转换后对总线差分/共模振铃(欠阻尼 LC 振荡)进行主动抑制的能力。ISO 11898-2:2024 对转换后的振铃幅度与持续时间(振铃抑制窗口)提出量化要求。
- **位置/背景**:振铃主要发生在边沿转换后的隐性相位,源于总线分布式电容与线束电感形成的谐振;抑制机制在收发器输出级内实现。规范要求可追溯到 CiA 601-4(SIC 前身规范)与厂商专利。
- **作用与影响**:未抑制的振铃会落入采样点,造成位错误与 TDC 测量抖动,限制数据相位速率与网络规模;振铃抑制使 SIC 网络支持 5 Mbit/s 数据相位、更长总线与非理想终端拓扑,是 SIC 与经典 FD 收发器在波形层面的标志性区别。
- **参见**:
  - [can-sic.md](can-sic.md)、[return-loss.md](return-loss.md)、[bus-termination.md](bus-termination.md)
  - [Mori 2014: CAN 总线振铃抑制](../resources/_entries/papers/2014-mori-ringing-suppression.md)
  - [TI SLLA581: CAN SIC 白皮书](../resources/_entries/vendors/ti-slla581.md)
  - [ISO 11898-2 (2024)](../resources/_entries/standards/iso-11898-2-2024.md)
