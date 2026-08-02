---
title: CAN with Flexible Data-Rate
description: CAN FD 数据链路层奠基论文,Bosch 在 2012 年首次提出"帧内比特率切换 + 64 字节数据场"的 CAN FD 帧格式。
type: 论文
organization: Robert Bosch
year: 2012
access: free
status: verified
download: local
priority: 2
audience: [模拟IC]
tags: [学术论文]
source: https://www.can-cia.org/fileadmin/cia/documents/proceedings/2012_hartwich.pdf
local_file: files/papers/2012_Hartwich_CAN_with_Flexible_Data-Rate.pdf
---

## 是什么
CAN FD 数据链路层的奠基文献。Florian Hartwich (Robert Bosch GmbH) 在第 13 届国际 CAN 会议 (13th iCC) 首次提出 CAN FD 新帧格式:帧内比特率切换 (BRS 位) + 最大 64 字节数据场,并设计了可保持与原 CAN 相同汉明距离的新 CRC 序列(17/21 位),同时给出两种比特率的配置方法。

## 为什么值得读
- **模拟IC 工程师**:明确 CAN FD 帧结构与两段比特率(仲裁段/数据段)对收发器时序、环路延迟和边沿对称性的要求,是理解 CAN FD 收发器需要比经典 CAN 更低传播延迟的根本原因。
- **嵌入式开发工程师**:理解帧内比特率切换 (BRS) 的原理与控制器端位速率配置方法。

## 核心内容要点
- 背景:车载网络带宽需求使 CAN 的 1 Mbit/s 比特率和 8 字节载荷成为瓶颈。
- 提出"帧内比特率切换"(BRS 位)+ 最大 64 字节数据场的 CAN FD 新帧格式。
- 设计保持与原 CAN 相同汉明距离的新 CRC 序列(17/21 位)。
- 用首款 CAN FD 协议控制器搭配标准 CAN 收发器实测比特率上限,并给出两种比特率的配置方法。

## 怎么读
先通读帧格式与 CRC 设计部分,再重点理解 BRS 位切换对收发器环路延迟的要求;最后对照 ISO 11898-1:2024 看标准化后的差异。PDF 免费公开,可直接下载本地阅读。

[📄 下载本地 PDF](../../../files/papers/2012_Hartwich_CAN_with_Flexible_Data-Rate.pdf)

## 参见
- [ISO 11898-1 (2024)](../standards/iso-11898-1-2024.md)
- [ISO 11898-2 (2024)](../standards/iso-11898-2-2024.md)
- [CiA 601 系列 Part 3](../standards/cia-601-3-bit-timing.md)
- [资源库 — 论文](../../papers.md)
