---
title: 传播延迟对称性(Tx/Rx Delay Symmetry)
description: 收发器发送路径与接收路径延迟之差,决定 CAN FD 数据相位可用的相位裕度。
tags: [专家, 收发器]
---
- **定义**:传播延迟对称性(Tx/Rx delay symmetry)指收发器两条信号路径传播延迟的一致程度,常用"发送方向延迟(TxD→总线)与接收方向延迟(总线→RxD)之差"定义(亦可表述为显性/隐性边沿延迟差)。其绝对值越小,对称性越好。
- **位置/背景**:由 ISO 11898-2 定义,是 CAN FD 数据相位位定时可行性的关键收发器参数;在 >1 Mbit/s 数据相位下,传播延迟不对称会直接消耗数据相位的相位裕度。CiA 601-1 给出了不同数据速率下的延迟对称性参考要求。
- **作用与影响**:不对称延迟使采样点/TDC 判断发生偏差,限制最大数据相位速率与总线长度;对称性越好,可支持的速率越高。该参数是收发器内部驱动级与接收比较器延迟匹配的设计结果,也是一致性测试(如 ISO 16845-2)的测量项。
- **参见**:
  - [tdc.md](tdc.md)、[loop-delay.md](loop-delay.md)、[phase-margin.md](phase-margin.md)、[propagation-segment.md](propagation-segment.md)
  - [CiA 601-1(物理接口实现)](../resources/_entries/standards/cia-601-1-physical-interface.md)
  - [NXP AH1308: CAN 应用提示](../resources/_entries/vendors/nxp-ah1308.md)
  - [ISO 11898-2 (2016)](../resources/_entries/standards/iso-11898-2-2016.md)
