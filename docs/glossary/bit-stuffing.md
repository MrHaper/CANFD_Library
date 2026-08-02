---
title: 位填充(Bit Stuffing)
description: 为防止长串相同位破坏同步而在发送时周期性插入相反位的编码机制。
tags: [入门, 协议]
---
- **定义**:位填充(Bit Stuffing)是 CAN 保证接收节点时钟同步的编码规则:经典 CAN 在连续 5 个相同电平后强制插入 1 个相反填充位;CAN FD 仲裁相位沿用此规则,数据相位改用固定填充(fixed stuffing),每 4 位插入 1 个填充位。
- **位置/背景**:填充位不携带信息,由发送节点在编码时插入、接收节点解码时移除;CRC 计算覆盖填充位,故检错能力包含填充规则。填充位作用于 SOF 之后、CRC delimiter 之前(数据相位固定填充含 CRC 序列本身)。
- **作用与影响**:填充保证信号有足够边沿供节点重同步,支撑长帧与高速数据相位;同时引入带宽开销并成为错误检测的一环(违反填充规则的帧即填充错误,触发错误帧)。
- **参见**:
  - [crc.md](crc.md)、[error-frame.md](error-frame.md)、[arbitration.md](arbitration.md)
  - [ISO 11898-1 (2015)](../resources/_entries/standards/iso-11898-1-2015.md)
  - [Bosch CAN FD Specification v1.0](../resources/_entries/standards/bosch-2012-canfd-spec.md)
