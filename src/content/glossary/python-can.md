---
title: python-can(CAN 访问库)
description: 跨平台 Python CAN 库,统一访问 SocketCAN、PCAN、Vector 等后端,便于脚本化测试。
tags: [入门, 工具]
---
- **定义**:python-can 是 Python 生态中的跨平台 CAN 访问库,支持 SocketCAN(PCAN、Vector、Kvaser、IXXAT 等)多种后端接口,提供统一的 `bus.send()` / `bus.recv()` API,并可与 DBC 解析库配合做信号级收发。
- **位置/背景**:python-can 运行在 PC/工控机上,通过 USB-CAN 适配器连接总线,是测试自动化与数据采集的常用层;其社区活跃,文档完善。
- **作用与影响**:让测试脚本、CI 与数据分析直接读写 CAN FD 总线,显著降低 CAN FD 功能验证与故障复现的成本;配合 DBC 可在脚本中按信号名操作,是嵌入式与测试工程师的高频工具。
- **参见**:
  - [socketcan.md](socketcan.md)、[can-utils.md](can-utils.md)、[dbc.md](dbc.md)
  - [python-can(资源条目)](../resources/_entries/tools-community/python-can.md)
  - [BusMaster(资源条目)](../resources/_entries/tools-community/busmaster.md)
