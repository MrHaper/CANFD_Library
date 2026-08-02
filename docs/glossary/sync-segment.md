---
title: 同步段(Sync Segment)
description: 位时间的第一段,固定为 1 个时间量子,是节点进行硬同步与重同步的基准位置。
tags: [进阶, 位定时]
---
- **定义**:同步段(Synchronization Segment, Sync Seg)是位时间的第一段,长度固定为 1 TQ。节点在检测到总线电平边沿(隐性→显性或显性→隐性)时,以该段为基准进行硬同步(帧起始时)或重同步(帧内),调整相位缓冲段以对齐采样点。
- **位置/背景**:位于位时间最前:Sync Seg → Prop Seg → PS1 → PS2。同步段不参与传播延迟补偿,其存在是为了给"边沿应出现的时刻"一个统一的参考点。
- **作用与影响**:同步段配合 [RJW](re-sync-jump-width.md) 决定节点容忍时钟偏差与总线相位漂移的能力;同步能力不足时,长帧高速率下会出现采样点偏移与位错误,是 CAN FD 数据相位调试的关注点之一。
- **参见**:
  - [bit-time.md](bit-time.md)、[re-sync-jump-width.md](re-sync-jump-width.md)、[sample-point.md](sample-point.md)
  - [ISO 11898-1 (2015)](../resources/_entries/standards/iso-11898-1-2015.md)
  - [Bosch CAN FD Specification v1.0](../resources/_entries/standards/bosch-2012-canfd-spec.md)
