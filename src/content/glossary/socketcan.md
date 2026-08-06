---
title: SocketCAN(Linux CAN 子系统)
description: Linux 内核原生 CAN 协议栈,通过套接字接口访问 CAN/CAN FD 总线。
tags: [入门, 工具]
---
- **定义**:SocketCAN 是 Linux 内核内置的 CAN 协议栈,把 CAN 总线抽象为网络设备(can0、can1 等),通过 PF_CAN 协议族套接字编程访问,并提供 `ip link set can0 up type can bitrate 500000 dbitrate 5000000 fd on` 这类标准配置命令。
- **位置/背景**:SocketCAN 支持经典 CAN 与 CAN FD(含 BRS 数据相位),与 can-utils、python-can 等工具配合,是嵌入式 Linux 与 PC 端 CAN 开发的事实标准。
- **作用与影响**:无需厂商专用驱动即可开发 CAN 应用,天然具备网络栈能力(多接口、过滤、多进程);SocketCAN 的接口抽象与工具生态大幅降低了 CAN FD 调试与测试自动化的门槛,是学习与开发路线的必选项。
- **参见**:
  - [can-utils.md](can-utils.md)、[python-can.md](python-can.md)、[dbc.md](dbc.md)
  - [SocketCAN(资源条目)](../resources/_entries/tools-community/socketcan.md)
  - [can-utils(资源条目)](../resources/_entries/tools-community/can-utils.md)
