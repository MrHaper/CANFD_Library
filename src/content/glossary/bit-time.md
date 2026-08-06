---
title: 位时间(Bit Time)
description: 一个位的标称持续时间,由同步段、传播段与相位缓冲段组成,是采样与同步的基本单位。
tags: [进阶, 位定时]
---
- **定义**:位时间(Bit Time)是总线上一个位的标称持续时间,等于 1/比特率。它被划分为整数个时间量子(TQ):同步段(Sync Seg)+ 传播段(Prop Seg)+ 相位缓冲段 1(PS1)+ 相位缓冲段 2(PS2)。位时间内的 TQ 总数常见为 8~25(视控制器与配置)。
- **位置/背景**:位时间划分在协议控制器内部完成,由波特率预分频器与段寄存器决定;采样点位于 PS1 与 PS2 交界。CAN FD 对仲裁相位与数据相位分别配置位时间。
- **作用与影响**:位时间的段结构决定采样点百分比、同步能力与可容忍的相位误差;配置不当(如传播段过短、PS2 为 0)会导致采样错误与重同步失败,是 CAN FD 调试中最常见的问题来源之一。
- **参见**:
  - [time-quantum.md](time-quantum.md)、[sync-segment.md](sync-segment.md)、[propagation-segment.md](propagation-segment.md)、[sample-point.md](sample-point.md)
  - [CiA 601-3(位定时配置与评估工具)](../resources/_entries/standards/cia-601-3-bit-timing.md)
  - [ISO 11898-1 (2015)](../resources/_entries/standards/iso-11898-1-2015.md)
