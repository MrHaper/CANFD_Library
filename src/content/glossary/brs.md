---
title: BRS(Bit Rate Switch)
description: CAN FD 帧中指示"数据相位切换高速率"的标志位。
tags: [入门, 协议]
---
- **定义**:BRS(Bit Rate Switch)是 CAN FD 控制场中的一位。BRS 为隐性(1)时,该帧的数据相位(数据字段与 CRC 场)以高于仲裁相位的比特率传输;BRS 为显性(0)时整帧保持仲裁速率。
- **位置/背景**:位于 EDL 与 ESI 之间:SOF → 仲裁场 → IDE → EDL → res → **BRS** → ESI → DLC。数据相位在 CRC delimiter 处切回仲裁速率,ACK 与 EOF 仍以仲裁速率发送。
- **作用与影响**:BRS 使同一帧内"慢仲裁 + 快数据"成为可能,是 CAN FD 吞吐提升的关键;但速率切换要求收发器传播延迟对称性、环路延迟与 TDC 必须满足高速数据相位的采样要求,是物理层设计约束的主要来源。
- **参见**:
  - [edl.md](edl.md)、[tdc.md](tdc.md)、[can-fd.md](can-fd.md)
  - [Bosch CAN FD Specification v1.0](../resources/_entries/standards/bosch-2012-canfd-spec.md)
  - [CiA 601-1(物理接口实现)](../resources/_entries/standards/cia-601-1-physical-interface.md)
