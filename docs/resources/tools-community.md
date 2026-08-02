---
title: 资源库 — 工具与社区
description: CAN FD 软件工具、硬件测试设备、测试与认证渠道、社区与学习平台索引(23 条)
tags: [工具, 社区]
---

# 资源库 — 工具与社区

> 配合前面六类资料使用的**工具、设备、认证渠道与社区平台索引**,来源为资料库 07_工具与社区。全部条目均为外链(download=link)或"获取渠道待补充"(download=none),**本站不托管任何软件**;source 为空的 4 条(阻抗/网络分析仪、知乎/CSDN、EDAboard、厂商社区)在条目页标注了获取渠道待补充,未编造 URL。按优先级排序,★★★ 最优先。

> **使用建议**(摘自资料库 07_工具与社区 第五节):
>
> - **学习协议**:SocketCAN + can-utils 或 BusMaster,配一块 USB-CAN 接口卡,回环收发报文、观察位流是最快的入门方式。
> - **验证物理层**:示波器抓 dominant→recessive 边沿,对比普通 CAN FD 与 SIC 收发器(如 TJA1463 vs TJA1044)的振铃差异,直观理解 SIC 价值。
> - **中文资料提醒**:CAN FD SIC 是 2024 年才标准化的新内容,中文网络资料普遍滞后或错误;涉及 SIC 参数请一律以 ISO 11898-2:2024 和厂商数据手册为准。

## 软件工具

| 名称 | 厂商 | 类型 | 免费 | 适用场景 |
|---|---|---|---|---|
| [CANoe / CANalyzer](_entries/tools-community/canoe-canalyzer.md) | Vector | 商业(付费) | 付费 | 总线仿真、报文分析、一致性测试 |
| [PCAN-View / PCAN-Explorer](_entries/tools-community/pcan-view-explorer.md) | PEAK-System | 商业(基础版免费) | 付费 | 报文查看/记录,入门友好 |
| [Kvaser 软件套件(canKing 等)](_entries/tools-community/kvaser-suite.md) | Kvaser | 商业(部分免费) | 付费 | 总线分析、报文记录 |
| [BusMaster](_entries/tools-community/busmaster.md) | RBEI(开源) | 开源免费 | 免费 | 学习协议帧结构、报文收发 |
| [python-can](_entries/tools-community/python-can.md) | python-can 社区 | 开源免费 | 免费 | 脚本收发、数据分析 |
| [SocketCAN](_entries/tools-community/socketcan.md) | Linux 内核 | 开源(内核自带) | 免费 | Linux 实验、收发报文 |
| [CANdb++(DBC 编辑器)](_entries/tools-community/candb-editor.md) | Vector | 商业 | 付费 | DBC 报文矩阵编辑 |
| [can-utils](_entries/tools-community/can-utils.md) | Linux 社区 | 开源免费 | 免费 | SocketCAN 命令行工具 |

## 硬件测试设备

| 名称 | 厂商 | 类型 | 免费 | 适用场景 |
|---|---|---|---|---|
| [示波器 + CAN/CAN FD 解码](_entries/tools-community/oscilloscope-can-decoding.md) | Keysight / Tektronix / R&S | 硬件设备 | 付费 | 抓总线波形、眼图、振铃、位定时 |
| [CAN 接口卡(USB / PCIe)](_entries/tools-community/can-interface-card.md) | PEAK / Vector / Kvaser / ZLG | 硬件设备 | 付费 | PC 接入总线、回环测试 |
| [CAN FD 一致性测试系统](_entries/tools-community/canfd-conformance-tester.md) | Vector / 第三方实验室 | 硬件设备 | 付费 | 协议一致性测试(ISO 16845) |
| [阻抗/网络分析仪](_entries/tools-community/impedance-network-analyzer.md) ⚠ | 通用仪器 | 硬件设备 | 付费 | 测输出阻抗、回波损耗(SIC 关键指标) |
| [EMC 测试系统(传导发射 / 抗扰度)](_entries/tools-community/emc-test-system.md) | R&S / 第三方实验室 | 硬件设备 | 付费 | CISPR 25 / IEC 62228-3 收发器 EMC 认证 |

## 测试与认证渠道

| 名称 | 厂商 | 类型 | 免费 | 适用场景 |
|---|---|---|---|---|
| [CiA plugfest / interoperability 测试](_entries/tools-community/certification-cia-plugfest.md) | CiA | 认证渠道 | 会员 | CAN FD / SIC 收发器互操作测试 |
| [一致性测试标准](_entries/tools-community/certification-conformance-standards.md) | ISO / IEC | 认证渠道 | 付费 | ISO 16845-1/-2、IEC 62228-3 测试依据 |
| [第三方实验室](_entries/tools-community/certification-third-party-lab.md) | TÜV / SGS / 广电计量 / 赛宝 | 认证渠道 | 付费 | 一致性 / EMC / 车规认证 |

## 社区与学习平台

| 名称 | 厂商 | 类型 | 免费 | 适用场景 |
|---|---|---|---|---|
| [CiA CAN Knowledge](_entries/tools-community/community-cia-can-knowledge.md) | CiA | 官方知识库 | 免费 | 权威成体系的 CAN/CAN FD 原理文章 |
| [Wikipedia: CAN bus / CAN FD](_entries/tools-community/community-wikipedia-can.md) | Wikipedia | 百科 | 免费 | 快速建立全局概念 |
| [Stack Overflow(can 标签)](_entries/tools-community/community-stackoverflow-can.md) | Stack Overflow | 问答社区 | 免费 | 协议与软件实现问题 |
| [知乎 / CSDN(车载网络、CAN FD 话题)](_entries/tools-community/community-zhihu-csdn.md) ⚠ | 知乎 / CSDN | 中文社区 | 免费 | 中文资料检索(**注意甄别错误**) |
| [EDAboard / 电子发烧友论坛](_entries/tools-community/community-edaboard.md) ⚠ | EDAboard / 电子发烧友 | 电子工程论坛 | 免费 | 收发器电路实现讨论 |
| [NXP / TI / Infineon 开发者社区](_entries/tools-community/community-vendor-forums.md) ⚠ | NXP / TI / Infineon | 厂商社区 | 免费 | 竞品调研、应用支持 |
| [周立功 ZLG(致远电子)](_entries/tools-community/community-zlg.md) | 周立功 ZLG | 中文资料库 | 免费 | 中文应用文档、教学视频 |

> ⚠ = 该条目 source 为空,获取渠道待补充(条目页内有 `!!! note` 提示与检索关键词,不编造 URL)。
