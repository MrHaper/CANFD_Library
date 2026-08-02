---
title: 帧格式总览:四种帧类型与经典 vs FD
description: CAN 的四种帧类型(数据/远程/错误/过载)与 CAN FD 数据帧的完整位序,以及经典 CAN 与 CAN FD 在控制场、DLC、CRC、填充上的格式差异。
tags: [入门, 协议]
---

## 定义

CAN 总线上只存在四种帧类型:**数据帧**(Data Frame,携带有效载荷)、**远程帧**(Remote Frame,请求对方发送数据)、**错误帧**(Error Frame,节点报告检测到的协议错误)与**过载帧**(Overload Frame,延迟后续帧或报告接收器过载)。其中数据帧是通信主体,其余三种是辅助机制。

**CAN FD 数据帧**是数据帧在 CAN FD 协议下的扩展形态:帧骨架与经典 CAN 相同(SOF → 仲裁场 → 控制场 → 数据场 → CRC 场 → ACK 场 → EOF),差异集中在控制场的三个标志位(**EDL、BRS、ESI**)以及 DLC 映射、CRC 长度与填充规则上。帧格式与位序由 **ISO 11898-1** 定义,源头是 Bosch 2012 年 CAN FD 规范。

## 要点

### 四种帧类型

| 帧类型 | 结构 | 作用 |
|---|---|---|
| 数据帧 | 仲裁场 + 控制场 + 数据场 + CRC + ACK + EOF | 传输数据,通信主体 |
| 远程帧 | 同数据帧但**无数据场**(DLC 表示请求长度) | 请求对方发送指定标识符的数据;经典 CAN 由 RTR 位区分,FD 中 RTR 位被 RRS 位取代,实际工程已不推荐使用 |
| 错误帧 | 错误标志(6 位)+ 错误分隔符(8 位隐性) | 节点检测到协议错误时向全网广播,见[仲裁与错误处理](arbitration-and-error.md) |
| 过载帧 | 过载标志(6 位显性)+ 过载分隔符(8 位隐性) | 仅在帧间空间发送,延迟后续帧或报告过载 |

### CAN FD 数据帧位序(标准 11 位标识符)

```
SOF → 仲裁场(11 位 ID + RTR/RRS) → 控制场(IDE → EDL → res → BRS → ESI → DLC)
     → 数据场(0~64 字节) → CRC 场(17/21 位 CRC + 固定填充位 + CRC delimiter)
     → ACK 场(ACK slot + ACK delimiter) → EOF(7 位隐性)
```

扩展帧(29 位标识符)的控制场为 `SRR → IDE → EDL → res → BRS → ESI → DLC`。三个标志位一句话记忆:**EDL 决定"这是什么帧",BRS 决定"数据段跑多快",ESI 报告"发送方状态如何"**。

### 经典 CAN vs CAN FD 数据帧

| 维度 | 经典 CAN(Classical) | CAN FD |
|---|---|---|
| 数据场 | 最多 8 字节 | 最多 **64 字节** |
| 比特率 | 整帧单速率,≤ 1 Mbit/s | 一帧两速:仲裁相位 + 数据相位(BRS 切换),数据相位实践常用 2/5 Mbit/s |
| 控制场 | `IDE + r0 + DLC`(标准帧) | `IDE + EDL + res + BRS + ESI + DLC` |
| CRC | 15 位,不覆盖填充位 | **17 位(数据 ≤ 16 字节)或 21 位(> 16 字节)**,覆盖填充位 |
| 位填充 | 连续 5 个同电平后插 1 个反相 | 仲裁相位同左;数据相位**固定填充**(每 4 位插 1 个反相) |
| 速率切换边界 | 无 | BRS 位之后进入数据相位,**CRC delimiter 处切回**仲裁速率 |

### DLC 非连续映射

DLC 是 4 位字段:0~8 对应 0~8 字节;9~15 分别映射 12/16/20/24/32/48/64 字节。CRC 长度也由数据长度决定(≤16 字节用 17 位,>16 字节用 21 位)。

### 兼容性边界

FD 帧前部(SOF、仲裁场)与经典帧完全一致,两类节点可公平仲裁;但经典节点把 EDL 位解读为保留位 r0/r1,读到隐性即判格式错误并触发错误帧。**"仲裁兼容"不等于"全网络兼容"**:同一网络要么全支持 CAN FD,要么分网/分时部署。

## 与收发器/控制器设计的关联

- **对控制器(嵌入式)**:解码器必须按 EDL/BRS/ESI 解析帧类型与速率切换边界;DLC 非连续映射决定 CRC 引擎选 17 位还是 21 位多项式;发送器在 BRS 之后、CRC delimiter 之前以数据相位速率工作,需要两套位定时与 TDC 支持。
- **对收发器(模拟 IC)**:帧格式本身不由收发器解释,但 BRS 造成的"仲裁速率 ↔ 数据速率"切换要求收发器传播延迟对称性与环回延迟稳定(否则高速数据相位无法可靠采样);错误帧由收发器以显性电平驱动,被动错误状态下以隐性发送。帧结构是推导[位定时与同步](../bit-timing/index.md)和[物理层](../physical-layer/index.md)需求的上游输入。

## 参见

- 教程:[图解 CAN FD 帧结构:EDL/BRS/ESI 一图看懂](../../tutorials/01-can-fd-frame-structure.md)、[CAN 2.0 与 CAN FD 的 5 个关键差异](../../tutorials/02-can2-vs-canfd.md)
- 词条:[EDL](../../glossary/edl.md)、[BRS](../../glossary/brs.md)、[ESI](../../glossary/esi.md)、[DLC](../../glossary/dlc.md)、[远程帧](../../glossary/remote-frame.md)、[过载帧](../../glossary/overload-frame.md)
- 标准规范:[ISO 11898-1 (2024)](../../resources/_entries/standards/iso-11898-1-2024.md)、[Bosch CAN FD Specification v1.0](../../resources/_entries/standards/bosch-2012-canfd-spec.md)
- 论文:[Hartwich 2012: CAN with Flexible Data-Rate](../../resources/_entries/papers/2012-hartwich-can-fd.md)
