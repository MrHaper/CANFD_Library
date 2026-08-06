---
title: Bus-off(离线状态)
description: 节点错误计数超限后完全退出总线通信的状态,需检测到恢复序列才能重新上线。
tags: [进阶, 协议]
---
- **定义**:Bus-off 是 CAN 错误处理状态机的最终状态:节点的发送错误计数(TEC)超过 255 时进入 Bus-off,节点完全停止总线通信(既不发帧也不影响总线),以隔离持续故障的节点。恢复条件是检测到 128 次连续的 11 个隐性位(总线空闲序列)。
- **位置/背景**:属于 ISO 11898-1 定义的错误处理状态机:Error Active(主动错误)→ Error Passive(被动错误)→ Bus-off。错误计数由节点自身的成功/失败收发动态增减。
- **作用与影响**:Bus-off 机制防止故障节点"淹没"总线,是 CAN 可靠性的关键设计;但进入/恢复的延时(取决于重试策略)会造成节点暂时离线,影响实时性。对嵌入式工程师而言,理解 Bus-off 与 ESI 位、错误帧的联动是排查"节点莫名失联"问题的基础。
- **参见**:
  - [esi.md](esi.md)、[error-frame.md](error-frame.md)、[arbitration.md](arbitration.md)
  - [ISO 11898-1 (2015)](../resources/_entries/standards/iso-11898-1-2015.md)
  - [ISO 11898-1 (2024)](../resources/_entries/standards/iso-11898-1-2024.md)
