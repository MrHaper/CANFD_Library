---
title: 模拟IC 工程师学习路线
description: 面向 CAN FD / CAN SIC 收发器模拟设计工程师的分阶段路线,从建立概念到协议、物理层 SIC 规范、芯片电路、测试认证与量产。
tags: [模拟IC, 专家]
search: { boost: 1 }
---
# 模拟IC 工程师学习路线

> 本路线以"已流片一颗 CAN FD(SIC)收发器芯片"为背景设计:帮助你把"协议 → 物理层 → 收发器设计 → 测试认证"的全流程知识系统补齐,最终能对标 ISO 11898-2:2024 与主流竞品(TJA1463 / TCAN1463 / TLE9371)独立开展设计工作。

## 这条路线适合谁

- 正在或即将从事 **CAN FD / CAN SIC 收发器模拟设计**(输出级、接收比较器、振铃抑制电路、ESD 保护)的芯片工程师;
- 需要把协议级知识(为什么需要 BRS、TDC、传播延迟对称性)落到电路指标上的人;
- 有模拟电路基础(运放、比较器、输出级、EMC 概念),但不要求精通嵌入式开发;
- 特别适合:芯片设计新人、从模拟通用芯片转向车载总线芯片的工程师。

> 想先评估自己的知识结构,可先读 [CAN FD](../glossary/can-fd.md) 与 [CAN SIC](../glossary/can-sic.md) 词条,确认基本概念无盲区后再开始。

## 路线总览

| 阶段 | 主题 | 预计周期 | 关键输出 |
|---|---|---|---|
| 0 | 建立概念 | 1 周 | 全局图景:CAN FD 在车载网络中的位置 |
| 1 | 协议与位定时 | 2~4 周 | BRS 时序约束 → 收发器传播延迟对称性需求 |
| 2 | 物理层与 SIC 规范(核心) | 4~8 周 | SIC 收发器设计指标(振铃抑制/回波损耗/沿整形/EMC) |
| 3 | 芯片架构与电路实现 | 长期 | 输出级、接收比较器、振铃抑制电路方案 |
| 4 | 测试与认证 | 2~4 周 | 一致性测试计划、表征项清单 |
| 5 | 系统集成与量产 | 按需 | 应用电路、车规认证路径 |

> 阶段 2 是本路线核心,投入时间应占全路线一半以上;**阶段 3 没有固定终点**,与日常工作融合,持续迭代。

---

## 阶段 0:建立概念(约 1 周)

### 目标
建立 CAN FD 的全局图景:它是什么、为什么出现、在车载网络中处于什么位置,为后续所有阶段提供上下文锚点。

### 必读资料
- [Bosch CAN FD Specification v1.0(2012)](../resources/_entries/standards/bosch-2012-canfd-spec.md) — 协议源头,免费 PDF,理解 CAN FD 的原始设计动机;
- [Wikipedia: CAN bus](../resources/_entries/tools-community/community-wikipedia-can.md) — 一天内建立 CAN 总线全貌的最低成本入口;
- [CiA CAN Knowledge 知识库](../resources/_entries/tools-community/community-cia-can-knowledge.md) — CiA 官方科普,权威且免费,术语口径统一;
- [CAN FD 词条](../glossary/can-fd.md) — 本网站术语表,先锚定核心定义;
- [CAN SIC 词条](../glossary/can-sic.md) — 知道 SIC 是"信号改善能力",为阶段 2 埋伏笔。

### 动手任务
- [ ] 用 SocketCAN 或 USB-CAN 卡做一次 CAN FD 回环收发(收发 ≥ 100 帧),亲眼看到 CAN FD 帧([SocketCAN 工具](../resources/_entries/tools-community/socketcan.md)、[USB-CAN 卡](../resources/_entries/tools-community/can-interface-card.md));
- [ ] 手绘一张 A4 的 CAN FD 数据帧结构图,标出 EDL/BRS/ESI 三个新增位的位置与作用;
- [ ] 用一句话向同事解释"CAN FD 相比 Classical CAN 多了什么"(检验是否真的理解)。

---

## 阶段 1:协议与位定时(2~4 周)

### 目标
吃透帧格式与位定时机制,尤其是 **BRS(位速率切换)带来的时序约束**,并把该约束转化为对收发器"传播延迟对称性"的明确要求——这是协议通往电路的第一座桥。

### 必读资料
- [ISO 11898-1:2024](../resources/_entries/standards/iso-11898-1-2024.md) — 帧格式、EDL/BRS/ESI、CRC、位填充、位定时与同步的权威定义;
- [ISO 11898-1:2015](../resources/_entries/standards/iso-11898-1-2015.md) — 与 2024 版对照,观察协议演进(2024 版撤销了 2015 版中已被 CAN FD 替代的内容);
- [Hartwich 2012:CAN FD 原始论文](../resources/_entries/papers/2012-hartwich-can-fd.md) — CAN FD 设计者本人写的第一篇协议论文,理解设计动机;
- [CiA 601-3 位定时配置与评估](../resources/_entries/standards/cia-601-3-bit-timing.md) — 位定时配置实操指南;
- [饶运涛《CAN 原理与应用》](../resources/_entries/books/2007-raoyuntao-can-principles.md) 或 [Lawrenz《CAN System Engineering》](../resources/_entries/books/2013-lawrenz-can-system-engineering.md) — 中文/英文各选一本,补充系统级理解。

### 动手任务
- [ ] 用位定时公式手工计算一组 CAN FD 配置(仲裁段 500 kbit/s + 数据段 2 Mbit/s),算出采样点、相位裕度,并说明 TDC 何时必须开启;
- [ ] 写出"BRS 切换瞬间位时序约束"的推导,结论落在一句话:**为什么数据段速率越高,对收发器环路延迟对称性的要求越苛刻**;
- [ ] 对照 [采样点](../glossary/sample-point.md)、[相位裕度](../glossary/phase-margin.md)、[TDC](../glossary/tdc.md)、[传播延迟对称性](../glossary/propagation-delay-symmetry.md) 词条,把 4 个概念串成一段连贯表述。

---

## 阶段 2:物理层与 SIC 规范(核心,4~8 周)

### 目标
逐条精读 **ISO 11898-2:2024 的 SIC 章节**,把振铃抑制、回波损耗、上升/下降沿整形、EMC 要求转化为可落到电路的 SIC 收发器设计指标。这是本路线投入最大、也最核心的一站。

### 必读资料
- [ISO 11898-2:2024](../resources/_entries/standards/iso-11898-2-2024.md) — SIC 收发器的"金标准",逐条精读,重点:振铃抑制、回波损耗、沿整形、EMC;
- [ISO 11898-2:2016](../resources/_entries/standards/iso-11898-2-2016.md) — 与 2024 版对比阅读,看清 SIC 比普通 CAN FD 新增了什么;
- [CiA 140 勘误(CiA Corrigendum Proposal)](../resources/_entries/standards/cia-140-corrigendum.md) — 免费勘误,配合 2024 版使用;
- [CiA 601-1 物理接口实现](../resources/_entries/standards/cia-601-1-physical-interface.md) — 延迟对称性数值直接进设计预算;
- [TI SLLA581 白皮书:SIC 如何释放 CAN FD 潜力](../resources/_entries/vendors/ti-slla581.md) — 厂商视角的 SIC 设计动机与系统收益;
- [Adamson 2020:设计 5 Mbps 网络](../resources/_entries/papers/2020-adamson-5mbps-networks.md) — 业界首篇系统论述 SIC 收益的论文,理解"为什么需要 SIC"。

### 动手任务
- [ ] 把 ISO 11898-2:2024 中 SIC 相关电气参数整理成一张表格(参数/条款号/典型值/含义),对照 [TJA1463 数据手册](../resources/_entries/vendors/nxp-tja1463.md) 逐项核对,标注哪些参数自己芯片能满足、哪些有差距;
- [ ] 推导回波损耗与输出阻抗、终端阻抗的关系式,并说明 5 Mbit/s 下回波损耗预算为何收紧;
- [ ] 用示波器对比普通收发器与 SIC 收发器的总线波形,拍下"振铃被抑制"的对比图(可借助 [示波器 CAN 解码](../resources/_entries/tools-community/oscilloscope-can-decoding.md);测试方法参考 [NXP AH1308](../resources/_entries/vendors/nxp-ah1308.md));
- [ ] 写一份"我理解的 SIC 设计指标清单",覆盖:输出级、接收比较器、振铃抑制电路三处的关键指标与来源条款。

---

## 阶段 3:芯片架构与电路实现(长期,结合工作)

### 目标
从规范走向电路:搞清各家厂商怎么做 SIC——通过关键专利读电路思路,通过竞品数据手册读内部框图与电气参数,形成自己的芯片架构与电路实现方案。

### 必读资料
- [TI US9606948B2(recessive nulling 隐性抵消,边沿加速)](../resources/_entries/patents/us9606948b2.md) — 显性→隐性边沿加速的核心思路;
- [TI US11310072B2(瞬态触发振铃抑制电路)](../resources/_entries/patents/us11310072b2.md) — 振铃抑制的 TI 实现;
- [Microchip US11539548B2(阻抗匹配 + 斜率控制)](../resources/_entries/patents/us11539548b2.md) — 明确标注 CAN SIC 的专利;
- [Bosch US11068429B2(振荡抑制单元)](../resources/_entries/patents/us11068429b2.md) — 振铃抑制的另一流派;
- [NXP TJA1463 数据手册](../resources/_entries/vendors/nxp-tja1463.md) — 竞品内部框图与电气参数的第一对标对象;
- [Deloge 2015:0.14µm HV SOI 收发器](../resources/_entries/papers/2015-deloge-soi-cmos-transceiver.md) — 芯片级实现论文,工艺与电路结合的范例。

### 动手任务
- [ ] 对照 [TJA1463 数据手册](../resources/_entries/vendors/nxp-tja1463.md) **画出接收比较器框图**(差分输入 → 比较器 → 迟滞 → 输出整形),标注每一级的带宽/迟滞/共模范围要求;
- [ ] 对照 [TJA1463](../resources/_entries/vendors/nxp-tja1463.md)、[TCAN1463-Q1](../resources/_entries/vendors/ti-tcan1463-q1.md)、[TLE9371](../resources/_entries/vendors/infineon-tle9371v.md) 三家数据手册,比较"同一 SIC 核心 + 不同外设"的家族化设计思路,并画出自研芯片的输出级框图,标出 SIC 振铃抑制电路应挂在哪一级、由什么触发;
- [ ] 把 [US9606948B2](../resources/_entries/patents/us9606948b2.md)、[US11310072B2](../resources/_entries/patents/us11310072b2.md)、[US11539548B2](../resources/_entries/patents/us11539548b2.md)、[US11068429B2](../resources/_entries/patents/us11068429b2.md)、[US10020841B2](../resources/_entries/patents/us10020841b2.md) 五篇振铃抑制专利的电路方案做成对比表(方案/触发方式/优劣势/适用场景),形成自己的方案选型文档;
- [ ] 结合 [传播延迟对称性](../glossary/propagation-delay-symmetry.md) 词条,核算自研芯片的环路延迟预算,找出最紧的约束点。

---

## 阶段 4:测试与认证(2~4 周)

### 目标
把"设计"推向"可信":掌握一致性测试计划、物理层 EMC 评估方法与数据手册表征项的完整清单,为流片后表征与认证做准备。

### 必读资料
- [ISO 16845-1 一致性测试计划](../resources/_entries/standards/iso-16845-1-2016.md) — 协议一致性测试的权威依据;
- [ISO 16845-2 CAN FD 一致性测试](../resources/_entries/standards/iso-16845-2-2018.md) — CAN FD 专用一致性测试计划;
- [IEC 62228-3 CAN 收发器 EMC 评估](../resources/_entries/standards/iec-62228-3-2019.md) — 收发器 EMC 测试方法(与 [IEC 62228-3 词条](../glossary/iec-62228-3.md) 对照);
- [CiA plugfest 互操作测试](../resources/_entries/tools-community/certification-cia-plugfest.md) — 与主流收发器互联验证的行业惯例;
- [一致性测试与认证渠道总览](../resources/_entries/tools-community/certification-conformance-standards.md) — 认证路径全景;
- [Nishida 2022:EMC 评估方法](../resources/_entries/papers/2022-nishida-emc-evaluation.md) — 学界对收发器 EMC 评估的最新方法。

### 动手任务
- [ ] 把 TJA1463 数据手册的表征项逐条与 [ISO 16845](../glossary/iso-16845.md)、IEC 62228-3 条款对照,生成"表征项 ↔ 标准条款"映射表;
- [ ] 为自研芯片写一份《一致性测试计划》草稿,包含:测试项、设备、pass/fail 判据、所需测试环境([一致性测试工具](../resources/_entries/tools-community/canfd-conformance-tester.md)、[EMC 测试系统](../resources/_entries/tools-community/emc-test-system.md));
- [ ] 列出参加 CiA plugfest 的清单(被测项、对比对象、期望数据),评估自研芯片与主流收发器的互联风险点。

---

## 阶段 5:系统集成与量产(按需)

### 目标
让芯片"上车":掌握应用电路、PCB/EMC 设计规则、车规认证路径,完成从芯片到系统的最后一公里。

### 必读资料
- [SAE J2284-4(500 kbit/s + 2 Mbit/s 车载应用)](../resources/_entries/standards/sae-j2284-4-2016.md) — 车载 CAN FD 应用的整车层面标准;
- [TI SLVAFC1 应用笔记(PCB/EMC 设计)](../resources/_entries/vendors/ti-slvafc1.md) — 布局布线实战规则;
- [TI SDAA190 应用笔记](../resources/_entries/vendors/ti-sdaa190.md) — 电路设计补充;
- [NXP AH1308(振铃抑制与网络设计)](../resources/_entries/vendors/nxp-ah1308.md) — 网络级设计要点;
- [NXP UCANS32K1SIC 评估板](../resources/_entries/vendors/nxp-ucans32k1sic.md) — 现成 SIC 评估硬件,可借来复测自己的芯片。

### 动手任务
- [ ] 参照 TJA1463 数据手册典型应用电路,画出自己芯片的最小系统应用电路(含电源、VIO、总线终端);
- [ ] 对照 [AEC-Q100](../glossary/aec-q100.md)、[EMI/EMC](../glossary/emi-emc.md) 词条,写一份"车规认证路径"清单(器件级 → 板级 → 系统级各要过什么测试);
- [ ] 用 UCANS32K1SIC 评估板与自研芯片做一次互联测试,记录眼图与错误帧。

---

## 完成标志

当你满足以下全部条件时,可认为本路线已完成:

- [ ] 能不看资料复述 CAN FD 帧结构,并解释 BRS 时序约束如何转化为收发器传播延迟对称性需求;
- [ ] 能对照 ISO 11898-2:2024 列出 SIC 收发器全部关键设计指标(振铃抑制/回波损耗/沿整形/EMC),并说明每个指标影响哪个电路模块;
- [ ] 画得出自研芯片的输出级与接收比较器框图,并标注出振铃抑制电路的挂载位置与触发机制;
- [ ] 手里有一份完整的《一致性测试计划》,且表征项已与 ISO 16845 / IEC 62228-3 条款建立映射;
- [ ] 能用一句话向非专业人士讲清"你的芯片比 TJA1463 好/差在哪里",并有数据支撑。

## 参见

- [嵌入式工程师学习路线](embedded.md) — 如果想了解芯片另一端(MCU 侧)怎么用,可交叉参考;
- [学习路线总览](index.md) — 两条路线如何选;
- [物理层与 SIC 知识域](../knowledge/physical-layer/index.md) — 相关知识点参考树;
- [收发器设计知识域](../knowledge/transceiver-design/index.md) — 电路实现相关知识点。
