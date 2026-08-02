---
title: 重同步跳转宽度(RJW / SJW)
description: 重同步时相位缓冲段可被延长或缩短的最大时间量子数,决定时钟偏差容忍能力。
tags: [进阶, 位定时]
---
- **定义**:重同步跳转宽度(Resynchronization Jump Width, RJW/SJW)是节点重同步时允许对相位缓冲段 1/2 进行延长或缩短的最大 TQ 数。重同步时采样点前后移动不超过 RJW,以校正节点间时钟偏差与相位漂移。
- **位置/背景**:RJW 是位定时的配置参数之一(ISO 11898-1 的位时间模型),其取值受相位缓冲段约束:通常不大于相位缓冲段 1 与相位缓冲段 2 的较小者(具体约束视控制器与标准)。常见配置如 1~4 TQ。
- **作用与影响**:RJW 越大,节点容忍总线各节点晶振偏差与相位跳变的能力越强,有利于长帧与高速率;但 RJW 过大可能使采样点偏移到不稳定区间。CAN FD 数据相位因速率切换与 TDC 引入额外相位不确定性,重同步能力对帧可靠性同样重要。
- **参见**:
  - [sync-segment.md](sync-segment.md)、[bit-time.md](bit-time.md)、[time-quantum.md](time-quantum.md)、[phase-margin.md](phase-margin.md)
  - [ISO 11898-1 (2015)](../resources/_entries/standards/iso-11898-1-2015.md)
  - [CiA 601-3(位定时配置与评估工具)](../resources/_entries/standards/cia-601-3-bit-timing.md)
