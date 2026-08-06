---
title: 控制器与驱动
description: SocketCAN 与 Linux 驱动生态、控制器寄存器与位定时/TDC 配置、DBC 报文矩阵——嵌入式工程师操作 CAN FD 控制器的知识域。
tags: [控制器]
---

# 控制器与驱动

本子域整理 CAN FD **控制器与驱动**的权威知识点:从 SocketCAN 协议栈的架构与使用,到控制器寄存器层面的位定时/TDC 配置,再到 DBC 报文矩阵与信号定义。这里连接[位定时与同步](../bit-timing/index.md)(时序参数的语义来源)与[工具与测试](../tools/index.md)(验证手段),是嵌入式工程师从"能跑"到"跑对"的知识链。

## 知识点

| 知识点 | 难度 | 定位 |
|---|---|---|
| [SocketCAN:Linux 原生 CAN 协议栈](socketcan.md) | 入门 | 设备抽象与 PF_CAN 套接字架构、can-utils 工具链、python-can 桥接 |
| [控制器寄存器与位定时/TDC 配置](register-tdc-config.md) | 进阶 | 仲裁/数据相位两套位定时寄存器、采样点计算与 SSP 偏移写入流程(以数据手册为准) |
| [DBC 报文矩阵与信号定义](dbc.md) | 入门 | 报文/信号/编码/值表的"字典"语义、常用编辑与解析工具、与 CANopen FD 的关系 |

## 相关入口

- 教程:[用 SocketCAN 5 分钟跑通 CAN FD 回环](../../tutorials/05-socketcan-loopback.md)、[CAN FD 位定时配置实战](../../tutorials/06-bit-timing-config.md)
- 术语:[SocketCAN](../../glossary/socketcan.md)、[DBC](../../glossary/dbc.md)、[TDC](../../glossary/tdc.md)、[采样点](../../glossary/sample-point.md)
- 工具条目:[SocketCAN](../../resources/_entries/tools-community/socketcan.md)、[python-can](../../resources/_entries/tools-community/python-can.md)、[CANdb++](../../resources/_entries/tools-community/candb-editor.md)
- 相邻子域:[位定时与同步](../bit-timing/index.md)、[工具与测试](../tools/index.md)
