---
title: TDC(Transmitter Delay Compensation)
description: CAN FD 控制器在数据相位补偿收发器与总线环路延迟的机制,使采样不再依赖物理层延迟。
tags: [进阶, 位定时]
---
- **定义**:TDC(Transmitter Delay Compensation,收发器延迟补偿)是 CAN FD 协议控制器在数据相位采用的采样补偿机制:发送节点测量"TxD 发出 → 收发器 → 总线 → 回环到 RxD"的环路延迟,在数据相位不再按固定采样点采样,而是延迟到期望的"第二采样点"(SSP,Secondary Sample Point)采样。
- **位置/背景**:TDC 机制由 ISO 11898-1 定义,最早出现在 Bosch 2012 年 CAN FD 规范第 8 章(Bit Timing Requirements / Transceiver Delay Compensation);仅用于数据相位,仲裁相位仍用经典采样点采样。
- **作用与影响**:TDC 消除了收发器与总线环路延迟对数据相位采样点位置的占用,使数据相位比特率可突破经典 1 Mbit/s 上限(实践中常用 2/5 Mbit/s)。TDC 精度取决于收发器传播延迟的稳定性与对称性,因此对收发器延迟对称性、环路延迟一致性提出要求;现代 CAN FD 控制器均有 TDC 相关配置寄存器。
- **参见**:
  - [brs.md](brs.md)、[propagation-delay-symmetry.md](propagation-delay-symmetry.md)、[loop-delay.md](loop-delay.md)、[sample-point.md](sample-point.md)
  - [Bosch CAN FD Specification v1.0](../resources/_entries/standards/bosch-2012-canfd-spec.md)
  - [CiA 601-3(位定时配置与评估工具)](../resources/_entries/standards/cia-601-3-bit-timing.md)
  - [Hartwich 2012: CAN with Flexible Data-Rate](../resources/_entries/papers/2012-hartwich-can-fd.md)
