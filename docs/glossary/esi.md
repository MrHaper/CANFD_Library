---
title: ESI(Error State Indicator)
description: CAN FD 帧中由发送节点标示自身错误状态的位,隐性表示发送节点处于 Error Passive。
tags: [入门, 协议]
---
- **定义**:ESI(Error State Indicator)是 CAN FD 控制场中的一位,由发送节点在发送时置位:节点处于 Error Active 时 ESI 为显性(0),处于 Error Passive 时 ESI 为隐性(1),接收节点据此可知发送方错误状态。
- **位置/背景**:位于 BRS 之后、DLC 之前:… → res → BRS → **ESI** → DLC。仅在 CAN FD 帧中存在;经典 CAN 帧无此位。
- **作用与影响**:ESI 提供"发送方错误等级"的在线诊断信息,便于系统监测节点健康度与预警;也参与错误处理逻辑,配合错误帧与总线状态机理解节点何时进入 Error Passive / Bus-off。
- **参见**:
  - [can-fd.md](can-fd.md)、[error-frame.md](error-frame.md)、[bus-off.md](bus-off.md)
  - [ISO 11898-1 (2015)](../resources/_entries/standards/iso-11898-1-2015.md)
  - [Bosch CAN FD Specification v1.0](../resources/_entries/standards/bosch-2012-canfd-spec.md)
