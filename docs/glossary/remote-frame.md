---
title: 远程帧(Remote Frame)
description: 用于请求另一节点发送指定标识符数据的帧,不含数据字段。
tags: [入门, 协议]
---
- **定义**:远程帧(Remote Frame)用于请求总线上的其他节点发送指定标识符的数据帧,其结构省略数据字段,DLC 表示所请求数据的长度。经典 CAN 中由 RTR 位区分数据帧(显性)与远程帧(隐性)。
- **位置/背景**:RTR 位位于仲裁场末尾;在 CAN FD 中 RTR 位被 RRS 位取代,远程帧仍存在但 ISO 11898-1 未规定其具体应用方式。CAN FD 远程帧的仲裁与经典 CAN 不完全一致,实际工程中远程帧已不推荐使用。
- **作用与影响**:经典 CAN 的"请求-响应"模型常用于无数据主动上报的从节点;但远程帧存在仲裁优先级竞态与响应缺失风险,现代设计多改用周期性/事件型数据帧。理解远程帧对排查网络异常(如意外 RTR)仍有帮助。
- **参见**:
  - [arbitration.md](arbitration.md)、[dlc.md](dlc.md)、[classical-can.md](classical-can.md)
  - [ISO 11898-1 (2015)](../resources/_entries/standards/iso-11898-1-2015.md)
  - [Bosch CAN FD Specification v1.0](../resources/_entries/standards/bosch-2012-canfd-spec.md)
