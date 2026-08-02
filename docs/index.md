---
title: 首页
description: 面向模拟IC设计工程师、嵌入式工程师与学生的 CAN FD / CAN SIC 学习资料库:学习路线、知识库、教程、资源库、术语表一站直达。
search: { boost: 2 }
---
# CAN FD 知识库

> **一个站点,补齐 CAN FD / CAN SIC 从协议到芯片的全流程知识。**
>
> 本知识库面向 **模拟 IC 设计工程师、嵌入式工程师与学生** 三类读者,围绕"协议 → 物理层 → 收发器设计 → 测试认证"的全流程,聚合了权威标准、专利、论文、教材与厂商资料,并配以可执行的分角色学习路线与原创教程。建站动机是团队已流片一颗 CAN FD (SIC) 收发器芯片——这里沉淀的就是这条路上需要的一切。

## 👥 按你的身份进入

三条学习路线均由阶段目标、必读资料与动手任务组成,按顺序走即可,关键节点互相交叉互链。

!!! tip "模拟IC 设计工程师"
    - **适合谁**:正在或打算做 CAN FD / CAN SIC 收发器模拟设计(输出级、接收比较器、振铃抑制电路)的芯片工程师
    - **路线周期**:约 10~20 周集中学习,阶段 3(芯片架构与电路实现)结合工作长期投入
    - **终点能力**:独立推导 SIC 收发器设计指标(振铃抑制 / 回波损耗 / 传播延迟对称性 / EMC),读懂竞品手册与关键专利,制定一致性测试计划
    - **[:material-chip: 进入模拟IC 路线](learn/analog-ic.md)**

!!! abstract "嵌入式工程师"
    - **适合谁**:要用 MCU 给产品加上 CAN FD(控制器初始化、驱动、协议栈、调试)的嵌入式开发工程师
    - **路线周期**:约 8~17 周
    - **终点能力**:在实际硬件上跑通 CAN FD 收发,正确配置采样点与 TDC,用示波器解码抓帧、排查错误帧,完成 DBC 与多节点系统搭建
    - **[:material-memory: 进入嵌入式路线](learn/embedded.md)**

!!! info "学生 / 转行者"
    - **适合谁**:从零开始、预算有限的高校学生或转行者,没有硬件基础也想低成本入门
    - **路线周期**:约 7~13 周
    - **终点能力**:理解 CAN FD 帧结构与工作机制,用低成本硬件跑通双节点收发,并根据兴趣明确下一步方向(IC 或嵌入式)
    - **[:material-account-school: 进入学生路线](learn/student.md)**

## 🗺️ 全站内容导览

| 板块 | 是什么 | 入口 |
|------|--------|------|
| 学习路线 | 按读者身份规划的分阶段路径:学什么、怎么学、学到什么程度算过 | [学习路线总览](learn/index.md) |
| 知识库 | 按协议对象分域的权威知识点:协议基础、位定时、物理层与 SIC、收发器设计、控制器与工具 | [知识库总览](knowledge/index.md) |
| 教程 | 原创动手教程:帧结构、SocketCAN 回环、位定时配置、示波器抓帧、plugfest 等 | [教程列表](tutorials/index.md) |
| 资源库 | 标准、专利、论文、期刊、教材、厂商资料、工具与社区的分类索引,附收录与版权说明 | [资源库总览](resources/index.md) |
| 术语表 | A-Z 词条即时查漏:遇到陌生词点进来先看定义 | [术语表索引](glossary/index.md) |
| 勘误与贡献 | 收集过程中发现的资料勘误记录,以及提交新资料 / 勘误的渠道 | [勘误与贡献](contribute.md) |

## ⭐ 必读 TOP 10

以下是全站资料中最值得优先精读的 10 组条目,按优先级排列(★ 越多越优先)。全部链接指向本站资源条目页。

| 优先级 | 资料 | 一句话说明 | 条目页 |
|:------:|------|-----------|--------|
| ★★★ | **ISO 11898-2:2024**(SIC 权威规范)+ CiA 140 勘误 | SIC 收发器的"金标准",逐条精读振铃抑制、回波损耗、沿整形与 EMC | [ISO 11898-2:2024](resources/_entries/standards/iso-11898-2-2024.md) · [CiA 140 勘误](resources/_entries/standards/cia-140-corrigendum.md) |
| ★★★ | **Bosch CAN FD Specification v1.0** | CAN FD 协议源头,免费 PDF,建概念必读 | [Bosch 2012 规范](resources/_entries/standards/bosch-2012-canfd-spec.md) |
| ★★★ | **TJA1463 / TCAN1463 SIC 数据手册** | 两家主流 SIC 收发器竞品手册,内部框图与电气参数直接进设计预算 | [NXP TJA1463](resources/_entries/vendors/nxp-tja1463.md) · [TI TCAN1463](resources/_entries/vendors/ti-tcan1463-q1.md) |
| ★★★ | **Adamson 2020 iCC 论文** | "CAN signal improvement and designing 5-Mbps networks",SIC 设计思路第一手资料 | [Adamson 2020](resources/_entries/papers/2020-adamson-5mbps-networks.md) |
| ★★★ | **TI SLLA581 SIC 白皮书** | SIC 技术原理与设计要点的权威应用文档 | [TI SLLA581](resources/_entries/vendors/ti-slla581.md) |
| ★★☆ | **ISO 11898-1**(2024/2015) | 帧格式、EDL/BRS/ESI、CRC、位定时与采样点的协议本体 | [ISO 11898-1:2024](resources/_entries/standards/iso-11898-1-2024.md) |
| ★★☆ | **TI US9606948B2 + Microchip US11539548B2 专利** | 隐性抵消(边沿加速)与 SIC 阻抗匹配 + 斜率控制,看各家电路怎么做 | [US9606948B2](resources/_entries/patents/us9606948b2.md) · [US11539548B2](resources/_entries/patents/us11539548b2.md) |
| ★★☆ | **CiA 601-1 / 601-3** | 物理接口实现(延迟对称性数值)与位定时配置评估 | [CiA 601-1](resources/_entries/standards/cia-601-1-physical-interface.md) · [CiA 601-3](resources/_entries/standards/cia-601-3-bit-timing.md) |
| ★★☆ | **ISO 16845-1 / -2** | 一致性测试计划,流片后表征与认证的依据 | [ISO 16845-1](resources/_entries/standards/iso-16845-1-2016.md) · [ISO 16845-2](resources/_entries/standards/iso-16845-2-2018.md) |
| ★☆☆ | **Lawrenz《CAN System Engineering》/ 饶运涛教材** | 中英文经典教材,系统学习或中文入门 | [Lawrenz 2013](resources/_entries/books/2013-lawrenz-can-system-engineering.md) · [饶运涛 2007](resources/_entries/books/2007-raoyuntao-can-principles.md) |

!!! warning "关于规范类条目的可获取性"
    带 ★ 的 ISO / CiA 等标准为**付费版权资料**,本站只提供索引页与官方获取渠道,不托管 PDF;可直接免费下载的只有明确标注公开的资料(如 Bosch 规范、专利、开放获取论文)。

## 🔍 站内搜索提示

右上角搜索框支持中文分词(默认开启建议与高亮),可以从不同角度切入:

- **按关键词搜概念**:`SIC`、`振铃抑制`、`回波损耗`、`传播延迟`、`BRS`、`TDC`、`采样点`、`bit stuffing`——命中知识库章节、教程与术语词条;
- **按编号搜资料**:`11898`、`ISO 16845`、`601`、`TJA1463`、`SLLA581`、`US9606948`——直接定位资源条目页;
- **想系统浏览**:从[资源库总览](resources/index.md)按类型(标准/专利/论文/期刊/教材/厂商/工具社区)逐页翻,每条目都标注了来源与是否可免费获取;
- **不确定从哪开始**:回到本文的[必读 TOP 10](#-必读-top-10),或按身份进入对应[学习路线](learn/index.md)。

> 如果发现条目信息有误(作者、编号、链接失效等),请到[勘误与贡献](contribute.md)查看勘误记录,并通过该页的渠道提交反馈。

## 🆕 最新收录

- [ISO 11898-2:2024(SIC 权威规范)](resources/_entries/standards/iso-11898-2-2024.md)、[Bosch CAN FD Specification v1.0](resources/_entries/standards/bosch-2012-canfd-spec.md) — 协议与物理层两大源头文档
- [12 篇 SIC/CAN FD 收发器专利](resources/patents.md)(TI/NXP/Bosch/Infineon/Microchip,全部可下载 PDF)
- [Adamson 2020:5 Mbps 网络设计](resources/_entries/papers/2020-adamson-5mbps-networks.md)、[SLLA581 SIC 白皮书](resources/_entries/vendors/ti-slla581.md) — SIC 设计必读
- [原创教程 12 篇](tutorials/index.md)与[术语表 51 词条](glossary/index.md)同步上线
- 勘误收录:[CiA 613 实为 CAN XL](resources/_entries/standards/cia-610-613-can-xl-series.md)、[TLE9255 非 SIC](resources/_entries/vendors/infineon-tle9255w.md) 等 4 条,见[勘误与贡献](contribute.md)
