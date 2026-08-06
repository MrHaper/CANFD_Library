---
title: 采样点(Sample Point)
description: 节点对总线电平进行采样的时刻,位于相位缓冲段 1 与 2 的交界,通常以位时间百分比表示。
tags: [进阶, 位定时]
---
- **定义**:采样点(Sample Point)是节点对总线电平进行采样的时刻,位于位时间中相位缓冲段 1(PS1)与相位缓冲段 2(PS2)的交界处。其位置常用"占位时间的百分比"表示:采样点 = (Sync Seg + Prop Seg + PS1)/位时间。CAN 要求位时间中至少有一个采样点,采样点的确切百分比由段配置决定。
- **位置/背景**:仲裁相位采样点常见配置在约 70%~87.5% 之间(视配置);CAN FD 数据相位通常推荐采样点尽量靠后(如 80%~90%,视配置),因为采样点越靠后,留出的重同步/相位裕度越大。CAN FD 数据相位采样依赖 TDC 与"第二采样点"机制。
- **作用与影响**:采样点位置决定节点对总线延迟、时钟偏差与振铃的容忍能力;全网络节点的采样点必须一致(或落在容差内),否则同一帧在不同节点可能被判为不同电平。采样点百分比是位定时配置与一致性测试的核心检查项。
- **参见**:
  - [bit-time.md](bit-time.md)、[phase-margin.md](phase-margin.md)、[tdc.md](tdc.md)、[propagation-segment.md](propagation-segment.md)
  - [CiA 601-3(位定时配置与评估工具)](../resources/_entries/standards/cia-601-3-bit-timing.md)
  - [ISO 11898-1 (2015)](../resources/_entries/standards/iso-11898-1-2015.md)
