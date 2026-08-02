---
title: 收发器延迟补偿(TDC / SSP)
description: CAN FD 数据相位为何必须依赖 TDC,环回延迟的三段分解,第二采样点(SSP)的工作原理,以及对收发器延迟对称性的要求。
tags: [进阶, 位定时]
---

## 定义

**TDC(Transmitter Delay Compensation,收发器延迟补偿)** 是 CAN FD 协议控制器在数据相位采用的采样补偿机制:发送节点测量"TxD 发出 → 收发器驱动 → 总线传播 → 接收比较器 → 回到 RxD"的**环回延迟**,在数据相位不再按固定采样点采样,而是把采样推迟到**第二采样点(SSP,Secondary Sample Point)**,以消除物理层延迟对数据相位采样的占用。

TDC 由 **ISO 11898-1** 定义,概念最早出现在 **Bosch 2012 年 CAN FD 规范第 8 章**(Bit Timing Requirements / Transceiver Delay Compensation)。它**只用于数据相位**;仲裁相位仍用经典采样点。

## 要点

### 为什么必须 TDC:BRS 之后的时序困境

- BRS 把数据相位切到高速率后,一位时间急剧缩短:5 Mbit/s 时一位仅 **200 ns**。
- 而典型 CAN FD 收发器的环回延迟约 **200 ns 量级**(如 NXP TJA1044GT 数据手册给出约 210 ns 典型值)——环回延迟**已经超过一个数据位时间**。
- 发送方在数据相位既要发送又要回读总线确认(仲裁/错误检测依赖回读);若仍按固定采样点采样,采样时刻要么落在自己发出的位还没绕回来时,要么被上一位回波干扰 → 错误帧。

### 环回延迟的三段分解

```
t_loop = tTX + tBUS + tRX

· tTX:发送路径延迟(TxD → 总线差分电平建立),由驱动级与输出沿整形决定
· tBUS:总线传播延迟(双绞线约 5 ns/m 量级,取决于线缆长度)
· tRX:接收路径延迟(总线差分电平 → RxD 建立),由接收比较器与滤波决定
```

仲裁相位靠位时间的**传播段**吸收 t_loop(决定总线长度);数据相位传播段被压缩到 1~2 TQ,t_loop 超过位时间,必须靠 TDC 补偿。

### TDC 工作流程

```
BRS 位为隐性 → 进入数据相位
→ 控制器从 TxD 发出测试边沿并计时
→ 该边沿经收发器与总线环回,在 RxD 收回,测得 t_loop
→ 设定第二采样点 SSP = t_loop + 偏移(偏移按控制器可配置步长取整)
→ 数据相位每个位都在 SSP 采样
→ CRC delimiter 处切回仲裁相位,恢复经典采样点
```

### 关键边界与约束

| 项 | 说明 |
|---|---|
| 适用范围 | 仅数据相位;仲裁相位(仲裁竞争、ACK)用经典采样点 |
| 补偿对象 | 环回延迟的**大小**(tTX + tBUS + tRX) |
| 补偿不了的 | 延迟的**变化**——即收发器传播延迟的不对称性与稳定性 |
| 前提 | 数据相位速率 ≥ 2 Mbit/s 时基本必须使能;开关与 SSP 偏移寄存器以控制器数据手册为准 |

### TDC 精度取决于收发器

TDC 测的是"本节点 tTX + 总线 + 本节点 tRX"的环回;远端节点发来的位经过的是"远端 tTX + 总线 + 本节点 tRX",两者之差中就含对称性误差。因此**对称性是 TDC 精度的天花板**:环回延迟越小越稳、Tx/Rx 越对称,TDC 补偿越准,可支持的数据相位速率越高。

## 与收发器/控制器设计的关联

- **对控制器(嵌入式)**:数据相位 ≥ 2 Mbit/s 时必须使能 TDC,并按收发器数据手册的环回延迟设置 SSP 偏移;TDC 开关、偏移步长与寄存器名因控制器而异。`ip -s -details link show can0` 观察错误计数可验证补偿是否生效。
- **对收发器(模拟 IC)**:TDC 是"为什么 CAN FD 收发器要更低的传播延迟与更好的对称性"的直接原因——收发器把环回延迟做小、做对称、做稳定,控制器才能把采样点算准。这与[相位裕度](phase-margin.md)知识点中的"残余不对称误差消耗裕度"是同一枚硬币的两面。

## 参见

- 教程:[BRS 与 TDC:为什么需要收发器延迟补偿](../../tutorials/04-brs-tdc.md)、[CAN FD 位定时配置实战](../../tutorials/06-bit-timing-config.md)、[收发器传播延迟对称性](../../tutorials/09-delay-symmetry.md)
- 词条:[TDC](../../glossary/tdc.md)、[环路延迟](../../glossary/loop-delay.md)、[采样点](../../glossary/sample-point.md)、[传播延迟对称性](../../glossary/propagation-delay-symmetry.md)、[BRS](../../glossary/brs.md)
- 标准规范:[Bosch CAN FD Specification v1.0(第 8 章 TDC 源头)](../../resources/_entries/standards/bosch-2012-canfd-spec.md)、[ISO 11898-1 (2024)](../../resources/_entries/standards/iso-11898-1-2024.md)
- 论文:[Hartwich 2012: CAN with Flexible Data-Rate](../../resources/_entries/papers/2012-hartwich-can-fd.md)
