---
title: CAN XL(第三代 CAN)
description: "数据字段最大 2048 字节、数据相位目标 20 Mbit/s 的下一代 CAN,已纳入 ISO 11898-1/-2:2024。"

tags: [进阶, 协议]
---
- **定义**:CAN XL 是继 Classical CAN 与 CAN FD 之后的第三代 CAN,数据字段最大 2048 字节,数据相位目标速率 20 Mbit/s(采用 PWM 编码与 AUI 物理层),由 Bosch 与 CiA 推动,已在 ISO 11898-1:2024(数据链路层+物理编码子层)与 ISO 11898-2:2024(物理介质连接子层)中标准化。
- **位置/背景**:帧格式在 CAN FD 基础上扩展,通过 EDL 之后新增的标志位与 CAN FD 区分;物理层包含 CAN SIC XL(CAN XL 用的 SIC)选项,其信号改善机制与 CAN SIC 同源。
- **作用与影响**:面向"需要高吞吐但无需以太网协议栈"的车载场景,填补 CAN FD 与车载以太网之间的带宽空档;与 CAN FD 帧不直接互操作,需在网关转换。对收发器设计而言,CAN XL 物理层与 SIC 共享振铃抑制、回波损耗等技术底座。
- **参见**:
  - [can-fd.md](can-fd.md)、[edl.md](edl.md)、[can-sic.md](can-sic.md)、[bit-rate.md](bit-rate.md)
  - [CiA 610~613 系列(CAN XL 规范与测试计划)](../resources/_entries/standards/cia-610-613-can-xl-series.md)
  - [ISO 11898-1 (2024)](../resources/_entries/standards/iso-11898-1-2024.md)
  - [ISO 11898-2 (2024)](../resources/_entries/standards/iso-11898-2-2024.md)
