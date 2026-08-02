---
title: can-utils
description: SocketCAN 配套命令行工具
type: 工具
organization: Linux 社区
access: free
status: verified
download: link
priority: 1
audience: [模拟IC, 嵌入式]
tags: [软件工具, 开源免费]
source: https://github.com/linux-can/can-utils
---

## 是什么
can-utils 是 **SocketCAN 配套的命令行工具集**(开源免费),包含 candump(抓取报文)、cansend(发送报文)、cangen(按规则生成报文)等命令,是 Linux 下操作 CAN / CAN FD 最轻量的方式。

## 为什么值得读
- **模拟IC 工程师**:命令行即可完成自研收发器的收发验证,无需图形界面。
- **嵌入式开发工程师**:在脚本与 CI 流程中集成 CAN 报文收发/生成,自动化测试利器。

## 核心内容要点
- **免费/付费**:开源免费。
- **适用场景**:学习/测试——报文抓取、发送、生成。
- **OS 支持**:Linux(基于 SocketCAN)。
- 依赖 Linux 内核 SocketCAN 支持与已配置的 CAN 接口。

## 怎么读
按 07 工具与社区 README 第五节建议,配一块 USB-CAN 接口卡后,用 candump / cansend / cangen 做回环收发、观察位流,是最快的入门方式。

## 获取渠道
GitHub 项目主页(下载/文档):<https://github.com/linux-can/can-utils>

## 参见
- [SocketCAN](socketcan.md)
- [python-can](python-can.md)
- [CAN 接口卡(USB / PCIe)](can-interface-card.md)
- [资源库 — 工具与社区](../../tools-community.md)
