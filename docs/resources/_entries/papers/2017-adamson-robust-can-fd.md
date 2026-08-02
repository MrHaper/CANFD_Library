---
title: Managing the transition to robust CAN FD
description: NXP 在 16th iCC 分享与 OEM 合作搭建鲁棒 CAN FD 网络的实战经验,涵盖拓扑、位时序与收发器特性对鲁棒性的影响。
type: 论文
organization: NXP
year: 2017
access: free
status: verified
download: local
priority: 1
audience: [模拟IC]
tags: [学术论文, CAN FD]
source: https://www.can-cia.org/fileadmin/cia/documents/proceedings/2017_adamson.pdf
local_file: files/papers/2017_Adamson_Managing_the_transition_to_robust_CAN_FD.pdf
---

## 是什么
NXP 的 T. Adamson 在第 16 届国际 CAN 会议 (16th iCC) 分享的 CAN FD 落地实战经验:ISO 11898-2:2016 发布后 CAN FD 在车载领域落地,但搭建鲁棒 CAN FD 网络仍充满挑战,论文结合 NXP 与 OEM 合作经验及网络仿真洞察给出应对方法。

## 为什么值得读
- **模拟IC 工程师**:从整车厂系统集成视角反推对收发器性能(环回延迟、边沿斜率、振铃)的要求,适合在收发器设计规格定义阶段参考。
- **嵌入式开发工程师**:了解 CAN FD 落地阶段网络设计的关键权衡(拓扑、位时序、收发器选型)。
- **学生**:短小易读,是快速了解 CAN FD 系统级挑战的入门文章。

## 核心内容要点
- 介绍 NXP 与 OEM 合作过程中的实战经验,以及通过网络仿真得到的洞察。
- 涵盖拓扑、位时序、收发器特性等对网络鲁棒性的影响。
- 从系统集成视角给出对收发器性能(环回延迟、边沿斜率、振铃)的要求。

## 怎么读
作为 CAN FD 系统设计背景阅读,重点看收发器特性如何影响网络鲁棒性,可与 2020 年 Adamson 的 SIC 论文对照以观察需求演进。PDF 免费公开,可直接下载本地阅读。

[📄 下载本地 PDF](../../../files/papers/2017_Adamson_Managing_the_transition_to_robust_CAN_FD.pdf)

## 参见
- [CAN signal improvement and designing 5-Mbps networks](2020-adamson-5mbps-networks.md)
- [ISO 11898-2 (2024)](../standards/iso-11898-2-2024.md)
- [资源库 — 论文](../../papers.md)
