---
title: CAN signal improvement and designing 5-Mbps networks
description: CAN SIC 核心论文:NXP 解释传统 HS-CAN 收发器为何在 5 Mbps 下基本只能点对点工作,并给出构建鲁棒 5 Mbps CAN FD 网络的工程指南。
type: 论文
organization: NXP
year: 2020
access: free
status: verified
download: local
priority: 3
audience: [模拟IC]
tags: [学术论文, 网络]
source: https://www.can-cia.org/fileadmin/cia/documents/proceedings/2020_adamson_engelhard_zhang.pdf
local_file: files/papers/2020_Adamson_CAN_signal_improvement_and_5Mbps_networks.pdf
---

## 是什么
CAN Signal Improvement (SIC) 技术的核心工程文献。T. Adamson、M. Engelhard、C. Zhang (NXP Semiconductors) 在第 17 届国际 CAN 会议 (17th iCC,线上) 的 "CAN FD lower layers" 分会场发表,说明 SIC 技术如何显著简化 2 Mbps CAN FD 网络的创建、支持比标准 HS-CAN 收发器大得多的网络拓扑,并基于工程经验给出构建鲁棒 5 Mbps CAN FD 网络的具体指南。

## 为什么值得读
- **模拟IC 工程师**:这是与 CAN SIC 直接对应的第一手工程文献,直接关联 CiA 601-4 (CAN FD 节点与系统设计 Part 4:信号改善)的技术动机与系统级收益,是 SIC 收发器设计需求分析的必读材料。
- **嵌入式开发工程师**:理解为什么 2 Mbps 以上必须依赖 SIC 收发器,以及如何规划拓扑、端接与 stub 长度。
- **学生**:看到"芯片规格 ← 系统需求"的完整推导链条,是需求分析入门范例。

## 核心内容要点
- 解释传统 HS-CAN 收发器在 5 Mbps 下基本只能点对点工作(多节点反射/振铃限制)的背景。
- 说明 CAN Signal Improvement (SIC) 技术如何显著简化 2 Mbps CAN FD 网络的创建,并支持比标准 HS-CAN 收发器大得多的网络拓扑。
- 基于 NXP 服务客户的工程经验,给出构建鲁棒 5 Mbps CAN FD 网络的指南(拓扑、端接、stub 长度等)。
- 与 CiA 601-4 (SIC 收发器规范) 的技术动机直接对应,是理解 SIC 系统级收益的原始出处。

## 怎么读
建议作为 SIC 设计的"需求来源"精读:先读背景部分(HS-CAN 为何在 5 Mbps 受限于多节点),再读 SIC 改善机制,最后对照 CiA 601-4 看哪些系统级收益被写成规范条款。PDF 免费公开,可直接下载本地阅读。

[📄 下载本地 PDF](../../../files/papers/2020_Adamson_CAN_signal_improvement_and_5Mbps_networks.pdf)

## 参见
- [CiA 601-4 (SIC)](../standards/cia-601-4-sic.md)
- [Characterizing the physical layer of CAN FD](2020-hancock-physical-layer.md)
- [The physical layer in the CAN XL world](2020-hell-can-xl-physical-layer.md)
- [资源库 — 论文](../../papers.md)
