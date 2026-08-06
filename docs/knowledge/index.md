---
title: 知识库总览
description: 系统整理协议基础、位定时、物理层与SIC、收发器设计、控制器、工具测试、项目实践笔记与 SIC 设计专题八大知识子域,是教程与术语表的"锚点"参考树。
tags: [知识库]
---

# 知识库总览

知识库按**协议对象分域**整理 CAN FD 的权威知识点,是[教程](../tutorials/index.md)与[术语表](../glossary/index.md)的"锚点":每个知识点页回答"是什么/为什么",并链到教程("怎么用")与资源(标准/专利/厂商资料,"去哪找")。八大子域覆盖从协议到芯片电路再到测试认证的完整链条,其中**项目实践笔记**沉淀实际项目问题的技术分析,**SIC 设计专题**为 SIC 收发器从原理到设计再到测试的专项深度知识。

## 子域

| 子域 | 定位 |
|---|---|
| [协议基础](protocol/index.md) | 帧格式、仲裁与错误处理、CRC 与位填充——数据链路层的基础知识,全人群起点 |
| [位定时与同步](bit-timing/index.md) | 时间量子与采样点、相位裕度、TDC——一帧两速(BRS)的时序账,全人群 |
| [物理层与SIC](physical-layer/index.md) | ISO 11898-2 结构、振铃抑制、回波损耗与 EMC——SIC 信号改善技术,模拟IC 为主 |
| [收发器设计](transceiver-design/index.md) | 输出级、接收比较器、ESD 与共模抑制——收发器模拟电路设计,模拟IC |
| [控制器与驱动](controller/index.md) | SocketCAN、寄存器与 TDC 配置、DBC——嵌入式工程师的操作层 |
| [工具与测试](tools/index.md) | 分析工具对比、示波器抓帧、一致性测试——从调试到认证,嵌入式 + 模拟IC |
| [项目实践笔记](project-notes/index.md) | 实际项目问题的技术分析与知识点沉淀——问题背景/根因/分析/结论,持续更新,全人群 |
| [SIC设计专题](sic-design/index.md) | CAN SIC 收发器专项深度知识——原理(振铃机理/信号改善)→ 设计(芯片架构/振铃抑制电路)→ 测试(参数测量/一致性/EMC),模拟IC 主线 |

## 使用建议

- **按人分流**:嵌入式工程师从[控制器与驱动](controller/index.md)、[位定时与同步](bit-timing/index.md)入手;模拟 IC 工程师从[收发器设计](transceiver-design/index.md)、[物理层与SIC](physical-layer/index.md)深入;新手从[协议基础](protocol/index.md)打底;[项目实践笔记](project-notes/index.md)按需查阅,不限人群。
- **按任务分流**:排查误码 → 位定时 + 物理层;调试驱动 → 控制器 + 工具;流片认证 → 收发器设计 + 工具(一致性测试)。

## 相关入口

- **设计参考**:收发器各模块的参数设计要点见[设计参考总览](../design/index.md)(规格基线 → 时序预算 → 模块设计 → 自查总表)
- 教程:[全部 12 篇教程](../tutorials/index.md)
- 术语表:[全部词条](../glossary/index.md)
- 学习路线:[学习路线总览](../learn/index.md)
