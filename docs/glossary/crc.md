---
title: CRC(循环冗余校验,17/21 位)
description: 帧错误检测字段,CAN FD 按数据长度采用 17 位或 21 位 CRC,并覆盖填充位。
tags: [进阶, 协议]
---
- **定义**:CRC(Cyclic Redundancy Check)是帧尾的检错字段。CAN FD 中数据长度 ≤16 字节时采用 17 位 CRC,>16 字节时采用 21 位 CRC,CRC 覆盖字段包括控制场、数据字段与填充位(仲裁相位按经典规则,数据相位按固定填充规则)。
- **位置/背景**:位于数据字段之后、ACK 场之前:… → 数据字段 → **CRC 场(CRC 序列 + 固定填充位 + CRC delimiter)** → ACK。CRC 多项式与覆盖范围由 ISO 11898-1 规定。
- **作用与影响**:CRC 是 CAN 五类错误检测机制之一(位错误、填充错误、CRC 错误、格式错误、ACK 错误),错误帧由接收到的 CRC 错误触发;21 位 CRC 为长数据帧提供与经典 CAN 15 位 CRC 相当的检错性能。
- **参见**:
  - [bit-stuffing.md](bit-stuffing.md)、[error-frame.md](error-frame.md)、[dlc.md](dlc.md)
  - [ISO 11898-1 (2024)](../resources/_entries/standards/iso-11898-1-2024.md)
  - [Bosch CAN FD Specification v1.0](../resources/_entries/standards/bosch-2012-canfd-spec.md)
