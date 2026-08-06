---
title: Interoperability challenges for CAN FD/PN transceivers
description: C&S group 在 16th iCC 披露高速 CAN 收发器互操作测试的经验教训,CAN FD/选择性唤醒收发器共存场景的互操作要点。
type: 论文
organization: C&S group
year: 2017
access: free
status: verified
download: local
priority: 1
audience: [模拟IC]
tags: [学术论文, CAN FD, 收发器]
source: "https://www.can-cia.org/fileadmin/cia/documents/proceedings/2017_wosnitza.pdf"

local_file: files/papers/2017_Wosnitza_Interoperability_CAN_FD_PN_transceivers.pdf
---

## 是什么
C. Wosnitza (C&S group,基于 Bosch 等厂商参与的一致性测试工作)在第 16 届国际 CAN 会议 (16th iCC) 披露高速 CAN 收发器互操作测试的教训,阐述高速率通信下与 CAN FD / 选择性唤醒 (Partial Networking) 收发器共存场景的互操作要点。

## 为什么值得读
- **模拟IC 工程师**:不同厂商的 SIC/HS-CAN 收发器混用时,边沿对称性、位时序裕量等参数必须收敛,本文是互操作设计约束的直接来源。
- **嵌入式开发工程师**:理解多厂商网络中选择收发器时的互操作考量。

## 核心内容要点
- 背景:ISO 16845-1/-2 新国际标准对 CAN FD 一致性测试提出要求,OEM 与硅片厂商需求被收集对齐,2016 年发布首个高速 CAN 收发器互操作测试规范。
- 披露高速 CAN 互操作测试的教训。
- 阐述高速率通信下与 CAN FD / 选择性唤醒收发器共存场景的互操作要点。

## 怎么读
重点读互操作测试的教训与共存场景要点,理解多厂商混用时边沿对称性与位时序裕量为何必须收敛。PDF 免费公开,可直接下载本地阅读。

[📄 下载本地 PDF](../../../files/papers/2017_Wosnitza_Interoperability_CAN_FD_PN_transceivers.pdf)

## 参见
- [ISO 16845-1](../standards/iso-16845-1-2016.md)
- [ISO 16845-2](../standards/iso-16845-2-2018.md)
- [Characterizing the physical layer of CAN FD](2020-hancock-physical-layer.md)
- [资源库 — 论文](../../papers.md)
