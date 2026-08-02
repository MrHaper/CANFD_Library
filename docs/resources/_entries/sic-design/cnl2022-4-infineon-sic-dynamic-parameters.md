---
title: CNL 2022-4:Infineon CAN SIC 动态参数详解
description: Infineon 工程师详解 CAN SIC 收发器新增动态参数,阐明动态参数定义、测量方法及其与 EMC 测试结果的关系。
type: SIC设计专题
organization: CAN Newsletter
year: 2022
access: free
status: verified
download: local
priority: 3
audience: [模拟IC]
tags: [SIC, 动态参数, EMC]
source: https://www.can-cia.org
local_file: files/sic-design/CNL2022-4_Infineon_CAN_SIC_dynamic_parameters.pdf
---

## 是什么
CAN Newsletter 2022-4 期刊载的 Infineon 工程师撰文,详解 CAN SIC 收发器新增的动态参数。文章说明了这些动态参数的定义与测量方法,并阐明 SIC 动态参数与 EMC 测试结果之间的关系,属于 CiA 官方杂志的一手权威材料。

## 为什么值得读
- **模拟IC 工程师**:SIC 收发器数据手册里的动态参数直接约束发射器/接收器电路的指标设定,这篇权威文章帮你准确理解每个参数的含义与测量口径,避免按旧 HS-CAN 经验误读新参数。
- 理解动态参数与 EMC 表现的关联,可以在设计阶段预判一致性测试(如 IEC 62228-3)的通过裕度,是"设计—测试"闭环的关键输入。

## 核心内容要点
- SIC 收发器新增动态参数的背景:高速数据相位下的信号质量与 EMC 要求。
- 关键动态参数的定义与测量方法(与数据手册参数表逐项对应)。
- 动态参数表现与 EMC 测试结果之间的关系分析。
- 对收发器电路设计指标设定的指导意义。

## 怎么读
建议配合知识库 [原理篇](../../../knowledge/sic-design/principle.md) 理解动态参数背后的物理机理,再对照 [设计篇](../../../knowledge/sic-design/design.md) 的参数章节逐项对标,最后用 NXP TJA1463 / TI TCAN1463 等 SIC 数据手册交叉验证参数口径。可安排在阅读 iCC 2020 Kvaser 振铃机理论文之后。

[📄 下载本地 PDF](../../../files/sic-design/CNL2022-4_Infineon_CAN_SIC_dynamic_parameters.pdf)

## 参见
- [CAN SIC 词条](../../../glossary/can-sic.md)
- [SIC 设计专题知识库](../../../knowledge/sic-design/index.md)
- [NXP TJA1463 CAN SIC 收发器数据手册](../vendors/nxp-tja1463.md)
