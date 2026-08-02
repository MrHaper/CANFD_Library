---
title: CANopen FD(CAN FD 高层协议)
description: 基于 CAN FD 传输的高层网络协议,由 CiA 1301 定义应用层与通信规范。
tags: [进阶, 工具]
---
- **定义**:CANopen FD 是基于 CAN FD 帧的高层协议(应用层与通信规范,由 CiA 1301 定义),继承经典 CANopen 的对象字典、PDO/SDO 服务模型,并利用 CAN FD 更大的数据字段与更高数据相位速率提升效率。
- **位置/背景**:CANopen FD 位于 CAN FD 数据链路层之上,面向工业控制、医疗与移动机械等确定性控制网络;CiA 1301 还给出了 CANopen FD 的位定时表(仲裁/数据相位速率组合)。
- **作用与影响**:CANopen FD 让"CAN FD 硬件 + 标准化协议栈"的开发生态落地,提供即插即用式组网与诊断;对收发器设计关系不大,但对系统集成、一致性认证(CiA 测试中心)与协议栈选型有直接意义。
- **参见**:
  - [dbc.md](dbc.md)、[socketcan.md](socketcan.md)、[cia-601.md](cia-601.md)
  - [CiA 1301(CANopen FD 应用层)](../resources/_entries/standards/cia-1301-canopen-fd.md)
  - [CiA 601 系列(CAN FD 节点与系统设计)](../resources/_entries/standards/cia-601-1-physical-interface.md)
