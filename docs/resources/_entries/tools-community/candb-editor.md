---
title: CANdb++(DBC 编辑器)
description: 报文矩阵(DBC)编辑,理解车载信号定义
type: 工具
organization: Vector
access: paid
status: verified
download: link
priority: 1
audience: [模拟IC, 嵌入式]
tags: [软件工具, 商业]
source: https://www.vector.com
---

## 是什么
CANdb++ 是 Vector 出品的 **DBC(报文矩阵)编辑器**,用于创建与维护 CAN / CAN FD 网络的信号定义(DBC 文件):报文、信号、多路复用、信号布局与属性等,是理解车载信号定义的关键工具。

## 为什么值得读
- **模拟IC 工程师**:理解"信号如何映射进报文",便于阅读协议栈与测试向量。
- **嵌入式开发工程师**:DBC 是车载软件开发的事实格式,掌握其编辑与理解能力是基本功。

## 核心内容要点
- **免费/付费**:商业付费(可随 Vector 工具链申请试用)。
- **适用场景**:开发——DBC 报文矩阵编辑与维护。
- **OS 支持**:Windows。
- 与 CANoe / CANalyzer 配套,导出的 DBC 可直接用于仿真与测试。

## 怎么读
用 CANdb++ 打开一份现成 DBC 文件,观察报文/信号/多路复用三个层级,再对照 CAN FD 帧结构理解数据场位段划分;进阶可自己建一个最小网络。

## 获取渠道
Vector 官网(DBC 编辑工具页):<https://www.vector.com>

## 参见
- [CANoe / CANalyzer](canoe-canalyzer.md)
- [SocketCAN](socketcan.md)
- [资源库 — 工具与社区](../../tools-community.md)
