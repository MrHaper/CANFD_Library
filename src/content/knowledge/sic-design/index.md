---
title: SIC 设计专题
description: CAN SIC 收发器从原理到设计再到测试的专项深度知识——面向模拟 IC 设计工程师的完整知识链。
tags: [SIC, 收发器, 专家]
---

# SIC 设计专题

本专题是 **CAN SIC(Signal Improvement Capability)收发器**的专项深度知识子域,面向**模拟 IC 设计工程师**(已流片或正在流片 CAN FD SIC 收发器,系统补齐 SIC 专项知识)。内容覆盖 SIC 的**完整知识链:原理 → 芯片设计 → 验证测试**,所有关键数值均提取自已下载的一手资料(标注出处),避免凭记忆的模糊表述。

- **原理篇**:为什么需要 SIC、振铃物理机理、三方面改进、系统级概念、标准演进;
- **设计篇**:芯片架构、输出级三态阻抗、对称性设计、振铃抑制电路(专利对照)、接收器、SIC 控制逻辑、防护、竞品对照与设计检查清单;
- **测试篇**:芯片级参数测量、一致性测试(ISO 16845/CiA plugfest)、EMC(IEC 62228-3)、网络级验证与测试计划模板。

## 建议学习路径

> 取自专题资料库 README 的建议学习路径。

**第 1 步(原理,1~2 周)**:精读[原理篇](principle.md),配合 TI SLLA581 白皮书与 Adamson 2020 论文。产出:能向别人讲清"为什么隐性位最脆弱、SIC 如何用三态阻抗解决"。

**第 2 步(设计,结合工作长期)**:对照[设计篇](design.md),按**专利 → 数据手册**的顺序研读:

1. 先读 TI US9606948B2(recessive nulling)与 Microchip US11539548B2(SIC 阻抗匹配)——两种最典型路线;
2. 再读 TJA1463/TCAN1463 数据手册的 SIC 参数表,与自己的流片设计逐项对标;
3. 最后对照设计检查清单,找出自己芯片的差距。

**第 3 步(测试,流片后 2~4 周)**:按[测试篇](testing.md)的测试计划模板执行,重点:

- 时序参数与 SIC 窗口测量(示波器);
- Safe Operating Area 仿真 + 台架对照(位模式 1D1R+5D1R+1D1R);
- 多节点星型拓扑实测(0.5 V 判据);
- 争取参加 CiA plugfest 或与主流器件混用互操作测试。

## 三章导航

| 文档 | 内容 | 关键词 |
|------|------|--------|
| [原理篇:振铃机理与信号改善机制](principle.md) | 为什么需要 SIC、振铃机理、三方面改进、关键参数、系统级概念、标准演进 | tBit/tREC、active recessive、RDIFF_act_rec、Allowable Ringing Time |
| [设计篇:收发器芯片设计要点](design.md) | 芯片架构、输出级三态阻抗、对称性设计、振铃抑制电路(专利对照)、接收器、SIC 控制逻辑、防护、竞品对照、设计检查清单 | recessive nulling、阻抗匹配、斜率控制、tact_rec 窗口 |
| [测试篇:验证与测试方法](testing.md) | 芯片级参数测量、一致性测试(ISO 16845/CiA plugfest)、EMC(IEC 62228-3)、网络级验证、测试计划模板 | 眼图、Safe Operating Area、SSP、plugfest |

## SIC 专题站内页

> **推荐入口**:[CAN SIC 专题站内页](../../../sic.md) —— 原理、设计、测试全部内容与 22 张原创技术图已整合为站内单页,直接阅读,不再跳转外部 HTML。

## 相关入口

- **知识库相邻子域**:[物理层与SIC](../physical-layer/index.md)、[收发器设计](../transceiver-design/index.md)、[位定时与同步](../bit-timing/index.md)、[工具与测试](../tools/index.md)
- **教程**:[SIC 是什么](../../tutorials/07-what-is-sic.md)、[振铃抑制原理与测量](../../tutorials/08-ringing-suppression.md)、[收发器传播延迟对称性](../../tutorials/09-delay-symmetry.md)、[一致性测试与 plugfest](../../tutorials/11-conformance-plugfest.md)
- **词条**:[CAN SIC](../../glossary/can-sic.md)、[振铃抑制](../../glossary/ringing-suppression.md)、[回波损耗](../../glossary/return-loss.md)、[收发器](../../glossary/transceiver.md)、[显性/隐性电平](../../glossary/dominant-recessive-levels.md)
- **资源**:[SIC 设计专题资源分类](../../resources/sic-design.md)(CAN Newsletter / iCC 论文、专利、厂商资料集中整理)
