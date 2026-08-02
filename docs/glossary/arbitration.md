---
title: 仲裁(Arbitration)
description: 多节点同时发送时按标识符逐位竞争总线访问权的机制,显性位优先。
tags: [入门, 协议]
---
- **定义**:仲裁(Arbitration)是 CAN 总线访问机制:多个节点同时发送时,各自在仲裁场逐位发送标识符并回读总线电平;当某节点发送隐性位而总线上读到显性位时,该节点立即退出竞争,继续发送的节点赢得总线。
- **位置/背景**:发生在帧起始(SOF)之后的仲裁场(11 位标准标识符或 29 位扩展标识符)。CAN FD 的仲裁场与经典 CAN 完全一致,因此两类节点可在同一网络共处并公平竞争。
- **作用与影响**:标识符数值越小优先级越高;显性电平(0)优先于隐性电平(1);仲裁不破坏获胜节点正在发送的帧,失败节点在下一帧间空间自动重发。仲裁机制决定网络实时性与优先级分配,是 CAN 无需中央调度即可多主通信的基础。
- **参见**:
  - [classical-can.md](classical-can.md)、[can-fd.md](can-fd.md)、[edl.md](edl.md)、[dominant-recessive-levels.md](dominant-recessive-levels.md)
  - [ISO 11898-1 (2015)](../resources/_entries/standards/iso-11898-1-2015.md)
  - [Bosch CAN FD Specification v1.0](../resources/_entries/standards/bosch-2012-canfd-spec.md)
