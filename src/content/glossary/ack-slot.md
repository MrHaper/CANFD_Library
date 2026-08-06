---
title: ACK 场(ACK Slot)
description: 帧尾的确认机制,发送节点发隐性位,正确接收的节点将其驱动为显性。
tags: [入门, 协议]
---
- **定义**:ACK 场由 ACK 槽(1 位)与 ACK 分隔符(1 位,隐性)组成。发送节点在 ACK 槽发送隐性位;凡正确接收并校验(含 CRC 校验)通过的节点,在该位将总线驱动为显性,形成确认;发送节点回读为显性即认为至少有一个节点成功接收。
- **位置/背景**:位于 CRC 分隔符之后、帧结束(EOF)之前:… → CRC delimiter → **ACK slot** → ACK delimiter → EOF。ACK 场始终以仲裁相位速率发送,即使本帧数据相位为高速率。
- **作用与影响**:ACK 是 CAN 错误检测机制之一(ACK 错误):若发送节点在 ACK 槽读到隐性,说明没有节点正确接收,将触发错误帧并重发。ACK 机制保证了"发必达"的确认语义,是 CAN 高可靠性的重要一环。
- **参见**:
  - [crc.md](crc.md)、[error-frame.md](error-frame.md)、[brs.md](brs.md)
  - [ISO 11898-1 (2015)](../resources/_entries/standards/iso-11898-1-2015.md)
  - [Bosch CAN FD Specification v1.0](../resources/_entries/standards/bosch-2012-canfd-spec.md)
