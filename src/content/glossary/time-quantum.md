---
title: 时间量子(Time Quantum, TQ)
description: 位定时的最小时间单位,由系统时钟分频产生,一个位时间由整数个 TQ 组成。
tags: [进阶, 位定时]
---
- **定义**:时间量子(Time Quantum, TQ)是 CAN 位定时的最小时间单位:控制器将系统时钟(晶振/PLL 输出)按预分频系数分频,得到 TQ = 预分频系数 × 系统时钟周期。位时间中的每个段都以 TQ 的整数倍配置。
- **位置/背景**:TQ 存在于协议控制器的位时序逻辑中,对应 ISO 11898-1 的位时间划分模型;控制器数据手册中的 BRP(Baud Rate Prescaler)即用于生成 TQ。
- **作用与影响**:TQ 越短(预分频越小),段划分越精细,采样点与重同步调整越精确,但要求系统时钟频率更高;TQ 长度与位时间 TQ 数共同决定比特率。CAN FD 高速数据相位通常需要更小的 TQ 以保证采样精度。
- **参见**:
  - [bit-time.md](bit-time.md)、[sample-point.md](sample-point.md)、[re-sync-jump-width.md](re-sync-jump-width.md)
  - [CiA 601-3(位定时配置与评估工具)](../resources/_entries/standards/cia-601-3-bit-timing.md)
  - [ISO 11898-1 (2015)](../resources/_entries/standards/iso-11898-1-2015.md)
