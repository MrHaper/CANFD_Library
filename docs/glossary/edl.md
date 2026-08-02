---
title: EDL(Extended Data Length)
description: CAN FD 帧的标志位,隐性表示该帧为 CAN FD 帧,即"扩展数据长度"可用。
tags: [入门, 协议]
---
- **定义**:EDL(Extended Data Length,又称 FDF/FD Format)是控制场中的一位,位于 IDE 之后。EDL 为隐性(1)时表示 CAN FD 帧格式,数据长度可超过 8 字节且数据相位可切换高速率;为显性(0)时为经典 CAN 帧。
- **位置/背景**:位于控制场开头:SOF → 仲裁场 → IDE(显性)→ **EDL** → res → BRS → ESI → DLC。EDL 之前的字段与经典 CAN 完全一致,保证仲裁兼容。
- **作用与影响**:发送节点通过 EDL 宣告帧格式;若网络中混有仅支持经典 CAN 的节点,它们会把 EDL=隐性解读为位错误并触发错误帧,因此 FD 网络必须保证所有节点支持 CAN FD,或将 FD 帧与经典帧分网/分时部署。
- **参见**:
  - [can-fd.md](can-fd.md)、[brs.md](brs.md)、[dlc.md](dlc.md)
  - [Bosch CAN FD Specification v1.0](../resources/_entries/standards/bosch-2012-canfd-spec.md)
  - [ISO 11898-1 (2015)](../resources/_entries/standards/iso-11898-1-2015.md)
