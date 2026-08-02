---
title: can-utils(CAN 调试工具集)
description: Linux 下开源的 CAN/CAN FD 命令行工具集,含抓帧、发送、负载生成与错误注入。
tags: [入门, 工具]
---
- **定义**:can-utils 是 Linux 下基于 SocketCAN 的 CAN 工具集,常用命令包括 `candump`(抓帧)、`cansend`(发送)、`cangen`(随机负载生成)、`candump`/`cangen` 组合做压力测试、`canfdtest`(CAN FD 回环测试)与 `cansniffer` 等。
- **位置/背景**:can-utils 依赖 SocketCAN 内核模块,通常在嵌入式 Linux 与车载开发板上预装或交叉编译;它支持 CAN FD 帧的收发与 DLC 扩展长度。
- **作用与影响**:can-utils 是"零成本上手 CAN FD"的核心工具,可用于验证位定时配置、观察错误帧、做总线负载与回环测试;其存在使 Linux 平台成为 CAN 调试最便捷的环境之一。
- **参见**:
  - [socketcan.md](socketcan.md)、[python-can.md](python-can.md)、[busmaster.md](busmaster.md)
  - [can-utils(资源条目)](../resources/_entries/tools-community/can-utils.md)
  - [SocketCAN(资源条目)](../resources/_entries/tools-community/socketcan.md)
