---
title: 传播段(Propagation Segment)
description: 位时间中用于补偿总线与收发器传播延迟的段,保证显性回波在采样点前稳定。
tags: [进阶, 位定时]
---
- **定义**:传播段(Propagation Segment, Prop Seg)是位时间中用于吸收信号传播延迟的段:发送节点发出的显性电平经总线传播并被自身回读确认,传播段必须足够长,使这个回波在采样点之前稳定。经验上可取 ≥ 2 ×(总线传播延迟 + 收发器环路延迟)。
- **位置/背景**:位于同步段之后、相位缓冲段 1 之前。在仲裁相位,传播段长度直接影响采样点位置;在 CAN FD 数据相位,环路延迟由 TDC 补偿,传播段通常可缩短至 1~2 TQ。
- **作用与影响**:传播段过长会挤压相位缓冲段、推迟采样点;过短则在高延迟网络上采样到未稳定的电平。其配置与总线长度、收发器延迟预算直接相关,是位定时设计(尤其经典 CAN 网络)的核心参数之一。
- **参见**:
  - [bit-time.md](bit-time.md)、[loop-delay.md](loop-delay.md)、[tdc.md](tdc.md)、[sample-point.md](sample-point.md)
  - [CiA 601-3(位定时配置与评估工具)](../resources/_entries/standards/cia-601-3-bit-timing.md)
  - [ISO 11898-1 (2015)](../resources/_entries/standards/iso-11898-1-2015.md)
