---
title: 相位裕度(Phase Margin)
description: 采样点相对理想位置可容忍的相位偏差,决定网络在延迟与时钟偏差下的可靠余量。
tags: [进阶, 位定时]
---
- **定义**:相位裕度(Phase Margin)指采样点两侧可容忍的相位偏差余量:总相位裕度通常约等于相位缓冲段 1 与相位缓冲段 2 的长度之和(以 TQ 计),它被总线传播延迟、收发器传播延迟不对称、节点时钟偏差等因素共同消耗。
- **位置/背景**:在仲裁相位,相位裕度由传播段与相位缓冲段配置决定;在 CAN FD 数据相位,环路延迟被 TDC 补偿,剩余的不对称误差与量化误差仍会消耗相位裕度,因此数据相位位定时可行性的评估实质是"相位裕度是否为正"。
- **作用与影响**:相位裕度不足会导致采样时刻落在不稳定区间,表现为偶发位错误与帧丢失。对收发器设计而言,传播延迟对称性直接影响数据相位可获得的相位裕度,是高速 CAN FD 网络的关键指标。
- **参见**:
  - [sample-point.md](sample-point.md)、[propagation-delay-symmetry.md](propagation-delay-symmetry.md)、[tdc.md](tdc.md)、[re-sync-jump-width.md](re-sync-jump-width.md)
  - [CiA 601-3(位定时配置与评估工具)](../resources/_entries/standards/cia-601-3-bit-timing.md)
  - [CiA 601-1(物理接口实现)](../resources/_entries/standards/cia-601-1-physical-interface.md)
