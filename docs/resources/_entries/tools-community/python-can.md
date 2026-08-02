---
title: python-can
description: Python 操作 CAN 接口的标准库,适合写脚本做数据分析
type: 工具
organization: python-can 社区
access: free
status: verified
download: link
priority: 1
audience: [模拟IC, 嵌入式]
tags: [软件工具, 开源免费]
source: https://github.com/hardbyte/python-can
---

## 是什么
python-can 是 Python 生态中操作 CAN / CAN FD 接口的**开源标准库**,提供统一的收发报文 API,并支持多种硬件后端(如 SocketCAN、PEAK、Vector 等接口),适合写脚本做数据分析与自动化测试。

## 为什么值得读
- **模拟IC 工程师**:用几行脚本批量收发报文、统计总线数据,辅助验证收发器行为。
- **嵌入式开发工程师**:把 CAN 报文采集/回放并入 Python 自动化测试与数据分析流程。

## 核心内容要点
- **免费/付费**:开源免费(MIT 许可)。
- **适用场景**:开发/测试/数据分析——脚本化收发、记录与解析。
- **OS 支持**:跨平台;实际可用性取决于所选硬件后端(如 Linux 走 SocketCAN)。
- 需要配合具体的 CAN 硬件接口使用。

## 怎么读
按官方文档安装后,先从"连接总线路 → 收发单帧"的最小示例开始;再结合自己手里的接口卡(或 Linux SocketCAN)做数据分析脚本。

## 获取渠道
GitHub 项目主页(文档/代码):<https://github.com/hardbyte/python-can>

## 参见
- [SocketCAN](socketcan.md)
- [can-utils](can-utils.md)
- [CAN 接口卡(USB / PCIe)](can-interface-card.md)
- [资源库 — 工具与社区](../../tools-community.md)
