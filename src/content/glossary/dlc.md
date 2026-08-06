---
title: DLC(Data Length Code)
description: 4 位数据长度码,指示帧中数据字段的字节数,经典 CAN 与 CAN FD 编码规则不同。
tags: [入门, 协议]
---
- **定义**:DLC(Data Length Code)是控制场中的 4 位字段,指示数据字段长度。经典 CAN 中 DLC 0~8 直接对应 0~8 字节,9~15 保留;CAN FD 中 DLC 0~8 对应 0~8 字节,9~15 分别映射为 12、16、20、24、32、48、64 字节。
- **位置/背景**:位于控制场末尾:… → BRS → ESI → **DLC(4 位)** → 数据字段。帧起始处(SOF 后的前 9 位之前)与数据相位交界处是速率切换的边界。
- **作用与影响**:CAN FD 通过非连续 DLC 映射把最大有效载荷提升到 64 字节;CRC 长度(17/21 位)由 DLC 决定(≤16 字节用 17 位 CRC,否则 21 位);CRC 覆盖场中包含 DLC,确保长度信息不被篡改。
- **参见**:
  - [can-fd.md](can-fd.md)、[crc.md](crc.md)、[error-frame.md](error-frame.md)
  - [Hartwich 2012: CAN with Flexible Data-Rate](../resources/_entries/papers/2012-hartwich-can-fd.md)
  - [Bosch CAN FD Specification v1.0](../resources/_entries/standards/bosch-2012-canfd-spec.md)
