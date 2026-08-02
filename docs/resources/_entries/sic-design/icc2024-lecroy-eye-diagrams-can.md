---
title: iCC 2024:LeCroy CAN 眼图分析
description: LeCroy 论文介绍用眼图评估 CAN/CAN FD 信号质量的方法,是收发器输出验证的测试方法参考。
type: SIC设计专题
organization: LeCroy
year: 2024
access: free
status: verified
download: local
priority: 1
audience: [模拟IC]
tags: [SIC, 眼图, 测试方法]
source: https://www.can-cia.org
local_file: files/sic-design/iCC2024_LeCroy_eye_diagrams_CAN.pdf
---

## 是什么
LeCroy(示波器厂商)在 iCC 2024(国际 CAN 会议)发表的论文,介绍用眼图评估 CAN / CAN FD 信号质量的方法,涵盖眼图测量原理、测量设置与信号质量判读思路,是收发器输出验证的测试方法参考。

## 为什么值得读
- **模拟IC 工程师**:眼图是验证收发器输出信号质量与 SIC 改善效果的核心测量手段,论文给出系统性的测量与判读方法,可纳入自己的验证计划。
- 来自示波器厂商的一手测量经验,能帮你规避测量设置(探头、触发、采集)带来的误判。

## 核心内容要点
- 眼图测量原理与关键设置。
- CAN / CAN FD 信号质量的评估维度与判读方法。
- 测试环境(探针、线缆、触发)对测量结果的影响。
- 眼图方法在 SIC 效果验证中的应用。

## 怎么读
配合知识库 [测试篇](../../../knowledge/sic-design/testing.md) 的芯片级参数测量与网络级验证章节:先用知识库建立测试框架,再精读本文补充眼图测量细节;可与 CNL 2025-1 esd 实测文章互为对照。

[📄 下载本地 PDF](../../../files/sic-design/iCC2024_LeCroy_eye_diagrams_CAN.pdf)

## 参见
- [CAN SIC 词条](../../../glossary/can-sic.md)
- [示波器 CAN 解码工具条目](../../../resources/_entries/tools-community/oscilloscope-can-decoding.md)
- [SIC 设计专题知识库 — 测试篇](../../../knowledge/sic-design/testing.md)
