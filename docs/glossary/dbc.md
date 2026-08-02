---
title: DBC(数据库文件)
description: Vector 定义的 CAN 网络描述文件格式,用文本定义报文、信号、编码与值表。
tags: [入门, 工具]
---
- **定义**:DBC(Database CAN)是 Vector 提出的 CAN 网络描述文件格式:以文本方式定义报文(Message)、信号(Signal)、起始位、位长、字节序、缩放/偏移、物理单位与值表,供工具链共享同一套网络"字典",实现信号级解码与仿真。
- **位置/背景**:DBC 文件由网络设计工具(如 CANdb++)或整车网络数据库生成,可描述经典 CAN 与 CAN FD 报文;CANopen 体系另有 EDS 文件,二者机制不同。
- **作用与影响**:DBC 是工具链互操作的黏合剂:抓帧工具按 DBC 把原始字节翻译成"车速=62.5 km/h"这样的信号值,是测试、仿真与数据分析的标准格式;理解 DBC 是嵌入式工程师解析车辆报文的基本功。
- **参见**:
  - [socketcan.md](socketcan.md)、[python-can.md](python-can.md)、[busmaster.md](busmaster.md)
  - [CANdb++(资源条目)](../resources/_entries/tools-community/candb-editor.md)
  - [BusMaster(资源条目)](../resources/_entries/tools-community/busmaster.md)
