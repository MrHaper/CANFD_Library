---
title: CAN FD(CAN with Flexible Data-rate)
description: 在经典 CAN 基础上扩展的可变数据速率协议,数据字段最多 64 字节,数据相位速率高于仲裁相位。
tags: [入门, 协议]
---
- **定义**:CAN FD(Controller Area Network with Flexible Data-rate)是 Bosch 于 2012 年提出的 CAN 扩展协议,后经 ISO 11898-1:2015 标准化。它复用经典 CAN 的仲裁机制与物理层,但将数据字段从最多 8 字节扩展到 64 字节,并允许在数据相位以更高比特率(最高 8 Mbit/s)传输。
- **位置/背景**:属于数据链路层(DLL)与物理编码子层(PCS)规范(ISO 11898-1)。通过 EDL 位与经典帧区分,帧内新增 BRS、ESI 位;物理层沿用差分总线,由 ISO 11898-2 定义高速收发器。
- **作用与影响**:显著提升单帧有效载荷与数据吞吐;因数据相位速率提高,收发器必须满足更严格的环路延迟与传播延迟对称性要求,由此引入 TDC(收发器延迟补偿)与新一代 CAN SIC 收发器。
- **参见**:
  - [classical-can.md](classical-can.md)、[edl.md](edl.md)、[brs.md](brs.md)
  - [Bosch CAN FD Specification v1.0](../resources/_entries/standards/bosch-2012-canfd-spec.md)
  - [Hartwich 2012: CAN with Flexible Data-Rate](../resources/_entries/papers/2012-hartwich-can-fd.md)
  - [ISO 11898-1 (2015)](../resources/_entries/standards/iso-11898-1-2015.md)
