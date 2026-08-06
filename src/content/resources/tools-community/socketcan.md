---
title: SocketCAN
description: Linux 原生 CAN/CAN FD 协议栈与工具(candump、cansend、cangen),实验首选
type: 工具
organization: Linux 内核
access: free
status: verified
download: link
priority: 1
audience: [模拟IC, 嵌入式]
tags: [软件工具, 开源(内核自带)]
source: "https://www.kernel.org/doc/html/latest/networking/can.html"

---

## 是什么
SocketCAN 是 **Linux 内核原生**的 CAN / CAN FD 协议栈,把 CAN 总线抽象为网络接口(socket),配合内核自带/配套的命令行工具(candump、cansend、cangen 等)即可收发与生成报文,是 Linux 下做 CAN 实验的**首选**方案,免费且零安装成本。

## 为什么值得读
- **模拟IC 工程师**:在 Linux 环境用 SocketCAN 快速搭收发实验,验证自研收发器基本功能。
- **嵌入式开发工程师**:理解 Linux 下 CAN 的抽象模型(网络接口而非串口),是车载 Linux 开发的基础技能。

## 核心内容要点
- **免费/付费**:免费(Linux 内核自带)。
- **适用场景**:学习/开发/测试——报文收发、报文生成、抓包。
- **OS 支持**:Linux。
- 典型配套工具:candump(抓取报文)、cansend(发送报文)、cangen(按规则生成报文)。
- 需一块被 Linux 内核支持的 CAN 接口卡(如 SocketCAN 驱动支持的 USB-CAN)。

## 怎么读
先读内核文档了解接口模型与配置方法,再按 07 工具与社区 README 第五节建议:配一块 USB-CAN 接口卡,用 candump / cansend / cangen 做回环收发、观察位流,是最快的入门方式。

## 获取渠道
Linux 内核文档(官方权威说明):<https://www.kernel.org/doc/html/latest/networking/can.html>

## 参见
- [can-utils](can-utils.md)
- [python-can](python-can.md)
- [CAN 接口卡(USB / PCIe)](can-interface-card.md)
- [资源库 — 工具与社区](../../tools-community.md)
