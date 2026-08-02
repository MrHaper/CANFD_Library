---
title: 显性/隐性电平(Dominant/Recessive Levels)
description: CAN 总线差分信号的两级状态:显性(0)对应约 2 V 差分,隐性(1)对应约 0 V 差分。
tags: [入门, 收发器]
---
- **定义**:CAN 总线采用差分显性/隐性两级电平:显性(Dominant,逻辑 0)时 CANH 与 CANL 差分电压约为 2 V(标称 CANH≈3.5 V、CANL≈1.5 V,视供电与负载);隐性(Recessive,逻辑 1)时两线均约为 2.5 V,差分电压约为 0 V。具体电平由 ISO 11898-2 与器件数据手册给出。
- **位置/背景**:显性/隐性电平存在于总线物理介质连接层;接收器通过差分电压阈值(常见约 0.5 V~0.9 V,视器件)判别两种状态。显性优先于隐性,这是仲裁与错误帧的物理基础。
- **作用与影响**:电平幅度与阈值决定抗噪与共模能力;隐性期间总线处于高阻弱驱动状态,易受干扰与振铃,这正是 CAN SIC 振铃抑制要解决的问题之一。电平幅度也影响发射(E M C)与功耗。
- **参见**:
  - [arbitration.md](arbitration.md)、[common-mode-range.md](common-mode-range.md)、[transceiver.md](transceiver.md)
  - [ISO 11898-2 (2016)](../resources/_entries/standards/iso-11898-2-2016.md)
  - [TI SDAA190: CAN/CAN FD/CAN XL 对比](../resources/_entries/vendors/ti-sdaa190.md)
