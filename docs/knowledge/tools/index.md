---
title: 工具与测试
description: 总线分析工具对比、示波器抓帧、一致性测试——从抓包分析、物理层波形验证到芯片认证的工具知识域。
tags: [工具, 测试]
---

# 工具与测试

本子域整理 CAN FD **工具与测试**的权威知识点:从总线分析工具的选型对比(CANoe/BusMaster/SocketCAN/PCAN),到示波器抓帧与眼图分析的物理层验证方法,再到 ISO 16845 / IEC 62228-3 / plugfest 的一致性测试与认证路径。这里同时服务[控制器与驱动](../controller/index.md)的调试与[收发器设计](../transceiver-design/index.md)的表征与认证。

## 知识点

| 知识点 | 难度 | 定位 |
|---|---|---|
| [总线分析工具对比:CANoe / BusMaster / SocketCAN / PCAN](tool-comparison.md) | 入门 | 主流工具定位、成本与适用场景对比,按任务选型的思路 |
| [示波器抓 CAN FD 帧:触发、解码与眼图](scope-capture.md) | 进阶 | 差分探头、触发与协议解码设置、数据相位眼图与振铃观察 |
| [一致性测试:ISO 16845 / IEC 62228-3 / plugfest](conformance-testing.md) | 专家 | 协议一致性、收发器 EMC 评估、CiA plugfest 互操作与第三方实验室认证路径 |

## 相关入口

- 教程:[示波器抓 CAN FD 帧](../../tutorials/10-scope-capture.md)、[一致性测试与 plugfest](../../tutorials/11-conformance-plugfest.md)、[用 SocketCAN 5 分钟跑通 CAN FD 回环](../../tutorials/05-socketcan-loopback.md)
- 术语:[SocketCAN](../../glossary/socketcan.md)、[DBC](../../glossary/dbc.md)、[ISO 16845](../../glossary/iso-16845.md)、[plugfest](../../glossary/plugfest.md)
- 工具条目:[CANoe/CANalyzer](../../resources/_entries/tools-community/canoe-canalyzer.md)、[示波器 + CAN/CAN FD 解码](../../resources/_entries/tools-community/oscilloscope-can-decoding.md)、[CAN FD 一致性测试系统](../../resources/_entries/tools-community/canfd-conformance-tester.md)
- 相邻子域:[控制器与驱动](../controller/index.md)、[物理层与SIC](../physical-layer/index.md)
