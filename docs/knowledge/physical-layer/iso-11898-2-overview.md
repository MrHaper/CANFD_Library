---
title: ISO 11898-2 结构:高速 PMA 子层
description: ISO 11898-2 定义的 HS-PMA 各选项(经典 HS、CAN FD、CAN SIC、CAN SIC XL)、版本演进与收发器电气要求总览。
tags: [专家, 物理层]
---

## 定义

**ISO 11898-2**(Road vehicles — CAN — Part 2: High-speed physical medium attachment (PMA) sublayer)规定 CAN **高速物理介质连接(PMA)子层**的电气要求,即高速收发器芯片应满足的驱动能力、接收阈值、共模范围、传播延迟与对称性、回波损耗、EMC 等全部参数。它是收发器芯片设计的**权威参数来源**,与规定数据链路层+物理编码子层的 **ISO 11898-1** 配套构成 CAN 的标准体系。

现行版 **ISO 11898-2:2024** 同时规定全部 CAN HS-PMA 选项:经典 HS、CAN FD(带低功耗/选择性唤醒)、**CAN SIC(signal improvement capability)** 与 **CAN SIC XL**。其前身之一是 **CiA 601-4**(2023 年撤回、内容并入 ISO),建议配合 **CiA 140 勘误**阅读以规避标准中的已知图文错误。

## 要点

### 版本演进

| 版本 | 状态 | 内容 |
|---|---|---|
| ISO 11898-2:2016 | 已撤回 | 首次将 CAN FD 收发器纳入 ISO;合并原 ISO 11898-5(低功耗)与 -6(选择性唤醒);ISO 16845-2:2018 一致性测试针对此版 |
| ISO 11898-2:2024 | 现行 | 新增 **CAN SIC 与 CAN SIC XL**;振铃抑制、动态参数、EMC 条款 |
| ISO 11898-2:2026 | 官网现行显示 | ISO 官网现已显示 2026 版,2024 版为 CiA 文档所引用的参考版 |

### HS-PMA 各选项

| 选项 | 定位 | 关键特征 |
|---|---|---|
| 经典 HS | 经典 CAN 高速收发器 | 支撑 ≤ 1 Mbit/s |
| CAN FD | 带低功耗/选择性唤醒的 FD 收发器 | 更严格的延迟对称性支撑 > 1 Mbit/s 数据相位 |
| **CAN SIC** | FD 收发器信号改善档 | 振铃抑制、回波损耗改善、受控沿整形、EMC 协同,支撑 5 Mbit/s 数据相位与更大拓扑 |
| CAN SIC XL | 与 CAN XL 配套的物理层选项 | 同标准内的新一代物理层底座 |

### 关键电气要求(以标准原文为准)

- **显性/隐性电平**:显性约 2 V 差分、隐性约 0 V 差分;接收阈值视器件。
- **共模范围**:总线两线相对地电位偏移时仍须正确判别,经典高速 CAN 收发器典型覆盖 -12 V ~ +12 V(以器件手册为准)。
- **传播延迟与对称性**:Tx/Rx 延迟对称性决定数据相位可用相位裕度,是 CAN FD 收发器的核心指标。
- **回波损耗**:总线端输入阻抗与 120 Ω 特征阻抗的匹配程度,高速下更严格。
- **振铃抑制**:SIC 条款对显性→隐性转换后的振铃幅度与持续时间(振铃抑制窗口)提出量化要求。
- **EMC**:与 IEC 62228-3(CAN 收发器 IC 级 EMC 评估)配套使用。

### 配套标准

ISO 16845-2(CAN 一致性测试 Part 2:HS-MAU)把 11898-2 的抽象要求翻译成可执行的静态/动态测试(对称性、位时序、环路延迟);ISO/DIS 16845-2 修订版正针对 2024/2026 版制定中。

## 与收发器/控制器设计的关联

- **对收发器(模拟 IC)**:这是 SIC 收发器设计的"金标准"——共模/差分输出、上升/下降沿整形、回波损耗、振铃抑制电路与 EMC 特性全部由此标准定义;流片后的一致性认证也以它为准绳。设计时应按"经典 HS → CAN FD → CAN SIC → SIC XL"顺序理解演进,精读 SIC 条款,并索取 CiA 140 勘误配合使用。
- **对控制器(嵌入式)**:控制器行为由 ISO 11898-1 定义,但 11898-2 的 BRS 时序约束(相位裕度、位不对称)直接决定数据相位能跑多快——理解 11898-2 的物理层要求,才能解释"为什么 5 Mbit/s 需要 SIC 收发器"。

## 参见

- 教程:[SIC 是什么:CAN FD 收发器的信号改善能力](../../tutorials/07-what-is-sic.md)、[收发器传播延迟对称性](../../tutorials/09-delay-symmetry.md)
- 词条:[ISO 11898-2](../../glossary/iso-11898-2.md)、[CAN SIC](../../glossary/can-sic.md)、[收发器](../../glossary/transceiver.md)、[共模范围](../../glossary/common-mode-range.md)
- 标准规范:[ISO 11898-2 (2024)](../../resources/_entries/standards/iso-11898-2-2024.md)、[ISO 11898-2 (2016,历史版)](../../resources/_entries/standards/iso-11898-2-2016.md)、[CiA 140(勘误)](../../resources/_entries/standards/cia-140-corrigendum.md)、[IEC 62228-3](../../resources/_entries/standards/iec-62228-3-2019.md)
