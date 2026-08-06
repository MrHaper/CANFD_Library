---
title: Classical CAN(经典 CAN / CAN 2.0)
description: CAN 2.0A/B 定义的原始 CAN 协议,数据字段最多 8 字节,比特率上限 1 Mbit/s。
tags: [入门, 协议]
---
- **定义**:Classical CAN(CAN 2.0A/2.0B)是 1990 年代标准化并沿用至今的经典 CAN 协议,帧结构为 SOF、仲裁场(11 或 29 位标识符)、控制场、最多 8 字节数据、CRC 场、ACK 场与 EOF。比特率上限 1 Mbit/s。
- **位置/背景**:由 ISO 11898-1 定义数据链路层,与 ISO 11898-2 高速物理层配套使用,仍是车载网络存量最大的通信形式。CAN FD 帧在仲裁场与其完全兼容,可同网共存。
- **作用与影响**:决定了经典收发器的位定时与采样点设计(仲裁相位采样点常见 75%~87.5%,视配置);经典帧的 8 字节/1 Mbit/s 限制是催生 CAN FD 的直接动因。
- **参见**:
  - [can-fd.md](can-fd.md)、[arbitration.md](arbitration.md)、[bit-stuffing.md](bit-stuffing.md)
  - [ISO 11898-1 (2015)](../resources/_entries/standards/iso-11898-1-2015.md)
  - [Hancock 2020: Characterizing the physical layer of CAN FD](../resources/_entries/papers/2020-hancock-physical-layer.md)
