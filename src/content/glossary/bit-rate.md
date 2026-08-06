---
title: 比特率(Bit Rate)
description: 总线上每秒钟传输的位数,CAN FD 允许仲裁相位与数据相位采用不同比特率。
tags: [入门, 位定时]
---
- **定义**:比特率(Bit Rate)是总线上每秒传输的位数(bit/s)。经典 CAN 最高 1 Mbit/s;CAN FD 中仲裁相位一般取 ≤1 Mbit/s(实践常用 500 kbit/s),数据相位最高 8 Mbit/s(实践常用 2/5 Mbit/s);CAN XL 数据相位目标 20 Mbit/s。数据相位速率需各节点配置一致,否则无法同步采样。
- **位置/背景**:比特率由位定时参数决定:比特率 = 1 /(位时间)= 1 /(TQ 数 × TQ 时长),见位时间与时间量子词条。仲裁相位与数据相位的比特率切换由 [BRS](brs.md) 位控制。
- **作用与影响**:提高数据相位比特率直接提升吞吐,但对收发器传播延迟对称性、环路延迟、TDC 与信号质量(振铃、回波损耗)提出更严格要求;这是 CAN FD SIC 收发器与位定时设计的主要驱动力。
- **参见**:
  - [bit-time.md](bit-time.md)、[brs.md](brs.md)、[sample-point.md](sample-point.md)、[tdc.md](tdc.md)
  - [CiA 601-3(位定时配置与评估工具)](../resources/_entries/standards/cia-601-3-bit-timing.md)
  - [Hartwich 2012: CAN with Flexible Data-Rate](../resources/_entries/papers/2012-hartwich-can-fd.md)
