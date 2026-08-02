---
title: 仲裁与错误处理
description: CAN 的位仲裁机制、五类错误检测、错误帧结构与 Error Active / Error Passive / Bus-off 错误状态机。
tags: [进阶, 协议]
---

## 定义

**仲裁(Arbitration)** 是 CAN 多节点共享总线的访问控制机制:多个节点同时发送时,在仲裁场逐位比较标识符,显性位(0)优先于隐性位(1),发送隐性位却读到显性位的节点立即退出竞争,其余节点继续发送——标识符数值越小,优先级越高。

**错误处理**是 CAN 高可靠性的核心:任何节点检测到协议错误时,通过**错误帧**向全网广播"本帧已被破坏",并依据**错误计数**在 Error Active(主动错误)、Error Passive(被动错误)、Bus-off(离线)三态间迁移,以隔离持续故障的节点。机制由 **ISO 11898-1** 定义。

## 要点

### 位仲裁

- 发生在 SOF 之后的仲裁场(11 位标准 / 29 位扩展标识符),逐位进行,不破坏获胜节点的帧。
- 规则:某节点发送隐性位而总线上读到显性位 → 立即退出;继续发送的节点赢得总线。
- CAN FD 仲裁场与经典 CAN 完全一致,两类节点可公平竞争;失败节点在下一帧间空间自动重发。
- 仲裁依赖"发送即回读"——发送方通过位错误检测确认自己是否仍在总线控制中。

### 五类错误检测

| 错误类型 | 触发条件 |
|---|---|
| 位错误(Bit Error) | 发送方在发送位时回读到的电平与自身发送的不同(仲裁/ACK 阶段除外) |
| 填充错误(Stuff Error) | 接收方违反位填充规则(如连续 6 个同电平) |
| CRC 错误(CRC Error) | 接收方计算的 CRC 与接收到的 CRC 序列不一致 |
| 格式错误(Form Error) | 固定格式字段(delimiter、EOF 等)出现非法电平 |
| ACK 错误(Acknowledgment Error) | 发送方在 ACK slot 未收到显性应答 |

### 错误帧

```
错误标志(Error Flag)+ 错误分隔符(Error Delimiter,8 位隐性)
```

- **Error Active** 节点发送 **6 个显性位**的主动错误标志;**Error Passive** 节点发送 **6 个隐性位**的被动错误标志。
- 错误帧可插入任何帧(含正在传输的数据帧)之中,主动错误标志故意违反填充规则,迫使全网同步进入错误处理;错误帧使本帧作废并触发发送节点重发。

### 错误状态机与错误计数

| 状态 | 进入条件(计数判定) | 行为 |
|---|---|---|
| Error Active | TEC ≤ 127 且 REC ≤ 127 | 可发主动错误标志,正常参与仲裁 |
| Error Passive | TEC > 127 或 REC > 127 | 只能发被动错误标志;发送前等待额外 8 位(延迟传输) |
| Bus-off | TEC > 255 | 完全停止总线通信,隔离故障节点;恢复需检测到 128 次连续的 11 个隐性位(总线空闲序列) |

- TEC(发送错误计数)/ REC(接收错误计数)由节点自身收发成败动态增减,成功收发会递减。
- CAN FD 控制场的 **ESI 位**由发送节点报告自身错误状态:Error Active 为显性(0),Error Passive 为隐性(1),为系统提供在线诊断信息。

### 过载帧与错误帧的区别

过载帧结构与错误帧类似(6 位标志 + 8 位隐性分隔符),但**只在帧间空间发送**,用于延迟后续帧或报告接收器过载,不插入数据帧内部;随控制器处理能力提升,实践中已很少使用。

## 与收发器/控制器设计的关联

- **对控制器(嵌入式)**:错误状态机与计数逻辑是控制器硬件的一部分——设计驱动与诊断时,需理解 TEC/REC 的增减规则、Bus-off 恢复序列,以及 ESI 位如何暴露节点状态;排查"节点莫名失联"时,先看是否进入 Bus-off、错误计数从哪类错误累积。
- **对收发器(模拟 IC)**:错误帧要求收发器能把 6 个显性位强驱动到总线(显性驱动能力与错误标志传播的时序);Error Passive 节点发送隐性错误标志,不影响总线。仲裁依赖"发送即回读"的环回路径,这条路径的延迟与对称性正是[位定时与同步](../bit-timing/index.md)分域关注的收发器指标。

## 参见

- 教程:[图解 CAN FD 帧结构:EDL/BRS/ESI 一图看懂](../../tutorials/01-can-fd-frame-structure.md)、[CAN 2.0 与 CAN FD 的 5 个关键差异](../../tutorials/02-can2-vs-canfd.md)
- 词条:[仲裁](../../glossary/arbitration.md)、[错误帧](../../glossary/error-frame.md)、[Bus-off](../../glossary/bus-off.md)、[ESI](../../glossary/esi.md)、[过载帧](../../glossary/overload-frame.md)、[远程帧](../../glossary/remote-frame.md)
- 标准规范:[ISO 11898-1 (2024)](../../resources/_entries/standards/iso-11898-1-2024.md)、[Bosch CAN FD Specification v1.0](../../resources/_entries/standards/bosch-2012-canfd-spec.md)
- 论文:[Hartwich 2012: CAN with Flexible Data-Rate](../../resources/_entries/papers/2012-hartwich-can-fd.md)
