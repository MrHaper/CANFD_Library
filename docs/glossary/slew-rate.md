---
title: 压摆率(Slew Rate)
description: 收发器输出信号的电压变化速率,决定上升/下降沿陡峭程度,是 EMI 与时序的折衷点。
tags: [进阶, 收发器]
---
- **定义**:压摆率(Slew Rate)是收发器输出(总线电压)随时间变化的速率,即上升/下降沿的陡峭程度。CAN FD 收发器按数据速率档位提供不同的输出沿整形(如经典模式与 FD/SIC 模式),部分器件通过 TXD 引脚斜率控制或寄存配置调节。
- **位置/背景**:压摆率属于物理介质连接层的驱动特性,ISO 11898-2 与器件数据手册规定了输出对称性与边沿特性;SIC 收发器采用受控/整形的输出沿以平衡 EMC 与高速采样需求。
- **作用与影响**:沿越陡,信号在采样点处越"干净"、时序裕度越大,但高频分量增强导致 EMI 增加;沿越缓,EMI 越小但边沿时间占用位时间,高速数据相位下可能来不及稳定。压摆率设计是收发器 EMC 与时序性能的核心折衷点。
- **参见**:
  - [emi-emc.md](emi-emc.md)、[can-sic.md](can-sic.md)、[bit-rate.md](bit-rate.md)
  - [NXP TJA1044 CAN FD 数据手册](../resources/_entries/vendors/nxp-tja1044.md)
  - [TI TCAN1463-Q1 CAN SIC 数据手册](../resources/_entries/vendors/ti-tcan1463-q1.md)
