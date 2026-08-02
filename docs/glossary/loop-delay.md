---
title: 环路延迟(Loop Delay)
description: 信号从 TxD 发出、经收发器驱动、总线传播与接收比较器回到 RxD 的总延迟。
tags: [进阶, 收发器]
---
- **定义**:环路延迟(Loop Delay)指信号从发送侧 TxD 输入开始,经收发器发送路径(TxD→总线)、总线传播、接收路径(总线→RxD)回到本节点或他节点 RxD 的总延迟,可分解为发送延迟 + 总线传播延迟 + 接收延迟。
- **位置/背景**:在仲裁相位,环路延迟必须被传播段(Prop Seg)吸收,决定最大总线长度;在 CAN FD 数据相位,环路延迟由 TDC 测量并补偿,因此其大小不再限制速率,但其一致性(稳定性)影响 TDC 精度。
- **作用与影响**:环路延迟及其随温度/电压/工艺的漂移,是 CAN FD 位定时预算的核心项;延迟抖动越大,数据相位可用相位裕度越小。收发器数据手册通常给出典型环路延迟与延迟对称性指标,供系统做延迟预算。
- **参见**:
  - [propagation-delay-symmetry.md](propagation-delay-symmetry.md)、[tdc.md](tdc.md)、[propagation-segment.md](propagation-segment.md)
  - [CiA 601-1(物理接口实现)](../resources/_entries/standards/cia-601-1-physical-interface.md)
  - [ISO 11898-2 (2016)](../resources/_entries/standards/iso-11898-2-2016.md)
