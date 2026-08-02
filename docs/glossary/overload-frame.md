---
title: 过载帧(Overload Frame)
description: 用于延迟后续帧或报告接收器过载状态的帧,结构与错误帧类似。
tags: [进阶, 协议]
---
- **定义**:过载帧(Overload Frame)由过载标志(6 个显性位)与过载分隔符(8 个隐性位)组成。它用于在帧间空间(Interframe Space)内要求延迟后续数据帧的发送,或报告接收器内部过载条件。
- **位置/背景**:过载帧只在帧间空间发送,不插入数据帧内部(与错误帧不同);过载分隔符与错误分隔符结构相同,均为 8 个隐性位。ISO 11898-1 规定了可发送过载帧的触发条件。
- **作用与影响**:过载帧是 CAN 流量控制与错误状态报告机制之一;在经典 CAN 时代用于缓解接收器处理压力。随着控制器处理能力提升,过载帧在实践中已很少使用,但保留在协议中以保证兼容性与一致性测试覆盖。
- **参见**:
  - [error-frame.md](error-frame.md)、[arbitration.md](arbitration.md)、[remote-frame.md](remote-frame.md)
  - [ISO 11898-1 (2015)](../resources/_entries/standards/iso-11898-1-2015.md)
  - [ISO 16845-1(CAN 一致性测试计划)](../resources/_entries/standards/iso-16845-1-2016.md)
