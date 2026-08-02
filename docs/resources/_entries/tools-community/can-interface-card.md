---
title: CAN 接口卡(USB / PCIe)
description: 上位机收发报文、回环测试
type: 工具
organization: PEAK / Vector / Kvaser / 周立功 ZLG
access: paid
status: verified
download: link
priority: 1
audience: [模拟IC]
tags: [硬件设备]
source: https://www.peak-system.com
---

## 是什么
CAN / CAN FD **接口卡**(USB / PCIe 等形态),厂商包括 PEAK、Vector、Kvaser、周立功 ZLG 等,把 PC 与 CAN 总线连接起来,配合上位机软件(SocketCAN、BusMaster、python-can、厂商自带工具等)实现报文收发与回环测试。

## 为什么值得读
- **模拟IC 工程师**:回环测试自研收发器、把 PC 接入被测总线,是验证基本收发功能的最短路。
- **嵌入式开发工程师**:开发与调试时的标准硬件通道。
- **学生**:一块入门级 USB-CAN 接口卡 + 免费软件即可搭建完整实验环境。

## 核心内容要点
- **用途**:上位机收发报文、回环测试;配合 SocketCAN / BusMaster / python-can 等软件使用。
- **免费/付费**:付费(硬件设备)。
- **适用场景**:开发/测试——PC 与 CAN 总线之间的数据通道。
- 注意:不同厂商接口卡与软件工具链配套(如 PEAK 配 PCAN-View、Kvaser 配 canKing、ZLG 配 USBCAN 工具),购买前确认驱动与生态支持。

## 怎么读
先确定自己的软件工具链(SocketCAN / BusMaster / python-can 等),再按兼容性选接口卡;按 07 工具与社区 README 第五节建议,配一块卡即可开始回环收发、观察位流。

## 获取渠道
PEAK-System 官网(接口卡产品页):<https://www.peak-system.com>

## 参见
- [SocketCAN](socketcan.md)
- [BusMaster](busmaster.md)
- [python-can](python-can.md)
- [周立功 ZLG(致远电子)](community-zlg.md)
- [资源库 — 工具与社区](../../tools-community.md)
