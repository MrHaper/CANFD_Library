---
title: 控制器寄存器与位定时/TDC 配置
description: CAN FD 控制器寄存器的位定时与 TDC 配置——仲裁相位与数据相位两套位定时参数、采样点计算与 SSP 偏移写入流程,以数据手册为准。
tags: [进阶, 控制器]
---

## 定义

CAN FD 控制器通过**寄存器**承载位定时与 TDC 配置:一套**仲裁相位**位定时参数(预分频、TSEG1/TSEG2、SJW)决定采样点位置,一套**数据相位**参数(DBRP、DTSEG1/DTSEG2、TDC 开关与 SSP 偏移)决定 BRS 后的高速位流如何采样。寄存器名与字段布局因控制器型号而异,本页说明**概念与配置逻辑**,具体地址/字段以所使用控制器的数据手册为准。

## 要点

### 仲裁相位位定时(经典配置)

位时间 = 1 × 预分频后的 TQ 数,由四段构成(同步段、传播段、相位缓冲段 1/2),寄存器层面通常合并为:

| 配置项 | 作用 |
|---|---|
| 预分频器(BRP) | 由系统时钟生成时间量子 TQ,决定 TQ 长度与位速率 |
| TSEG1(= 传播段 + 相位缓冲段1) | 决定采样点前的时间,吸收传播延迟 |
| TSEG2(= 相位缓冲段2) | 决定采样点后的时间,留出重同步余量 |
| SJW(重同步跳转宽度) | 限制硬/重同步一次最多调整的 TQ 数 |

采样点 = (1 + TSEG1) / (1 + TSEG1 + TSEG2),常用推荐值(如 75%~87.5%)由 ISO 11898 参考与整车网络约定给出,以网络规范为准。

### 数据相位位定时 + TDC

BRS 切到数据相位后,位时间大幅缩短(5 Mbit/s 时一位约 200 ns),配置要点:

- **DBRP / DTSEG1 / DTSEG2**:数据相位的独立位定时组,原则是**缩短传播段、后置采样点**,把物理层延迟让位给 TDC。
- **TDC 开关**:数据相位 ≥ 2 Mbit/s 基本必须使能(是否必须、开关字段因控制器而异)。
- **SSP 偏移**:TDC 把采样点推迟到 `SSP = t_loop + 偏移`;**偏移值按收发器数据手册的环回延迟设置**(如典型环回延迟量级约 200 ns,具体以所用收发器手册为准),控制器按自身步长取整写入。

TDC 机理与环回延迟三段分解见[收发器延迟补偿(TDC/SSP)](../bit-timing/tdc.md)。

### 配置流程(通用套路)

```
1. 读控制器数据手册:确认仲裁/数据相位寄存器名、位段长度、TDC 支持与 SSP 步长
2. 按目标速率(如 1M/5M)与推荐采样点计算 BRP、TSEG1/TSEG2、SJW
3. 计算数据相位 DBRP/DTSEG1/DTSEG2;查收发器手册的环回延迟 → 设定 SSP 偏移,使能 TDC
4. 使能 FD(含 BRS),启动接口
5. 验证:`ip -details link show can0` 核对时序;抓帧/回环观察错误计数
```

## 与收发器/控制器设计的关联

- **对控制器(嵌入式)**:位定时与 TDC 配置是"把控制器手册、收发器手册、网络速率三者对齐"的过程——采样点与 SSP 的选择直接影响相位裕度与 TDC 补偿精度;配置错误最典型的表现是错误帧计数上升、高速数据相位收发失败。具体寄存器名与字段务必以所使用 MCU 的数据手册为准,不要照搬其他型号。
- **对收发器(模拟 IC)**:控制器配置的 TDC/SSP 值取决于收发器的环回延迟与对称性——收发器把 t_loop 做小、做对称、做稳定,控制器才能把采样点算准;收发器设计者理解控制器侧的配置流程,才能读懂客户为何关心环回延迟与对称性指标。

## 参见

- 教程:[位定时入门](../../tutorials/03-bit-timing-basics.md)、[BRS 与 TDC](../../tutorials/04-brs-tdc.md)、[CAN FD 位定时配置实战](../../tutorials/06-bit-timing-config.md)
- 词条:[TDC](../../glossary/tdc.md)、[采样点](../../glossary/sample-point.md)、[时间量子](../../glossary/time-quantum.md)、[相位裕度](../../glossary/phase-margin.md)、[传播段](../../glossary/propagation-segment.md)、[重同步跳转宽度](../../glossary/re-sync-jump-width.md)
- 标准规范:[Bosch CAN FD Specification v1.0](../../resources/_entries/standards/bosch-2012-canfd-spec.md)
- 相邻子域:[收发器延迟补偿(TDC/SSP)](../bit-timing/tdc.md)、[时间量子与采样点](../bit-timing/time-quantum-sample-point.md)、[SocketCAN](socketcan.md)
