---
title: Design of the Circuits for a CMOS CAN Transceiver Chip with Slew Rate Control
description: 吉林大学 2012 年发表的带斜率控制功能的 CMOS CAN 收发器芯片电路设计论文(Advanced Materials Research),0.5µm 工艺,经典 CAN 收发器架构入门参考。
type: 期刊
organization: 吉林大学
year: 2012
access: free
status: verified
download: link
priority: 1
audience: [模拟IC]
tags: [期刊论文, 收发器]
source: "https://doi.org/10.4028/www.scientific.net/AMR.433-440.1895"

---

## 是什么
Hui Hui Zhan、Shao Xin Zong、Xiu Gang Han、Chuan Nan Li(吉林大学)发表在 Advanced Materials Research(Trans Tech Publications,会议论文集性质的期刊出版物)2012 年 Vol.433-440(pp.1895-1902)的论文。基于 0.5µm n-well CMOS 工艺设计 CAN 收发器,Hspice 仿真表明满足 ISO-11898,可工作在 1 Mbit/s。

## 为什么值得读
- **模拟IC 工程师**:早期国产 CAN 收发器芯片设计的完整架构示例(发射机/接收机划分、斜率控制、滞回接收、保护电路),适合快速建立经典 CAN 收发器架构概念。注意:出版形式为会议论文集、工艺 0.5µm 已过时,仅建议作为架构入门参考,不宜作为现代 FD/SIC 设计依据。

## 核心内容要点
- 发射机由输入级、中间级、斜率控制电路与输出级构成;中间级用 5 级级联反相器提供大驱动电流与小延迟。
- 斜率控制电路以外部电阻 Rs 连续调节充放电电流源,从而调节输出压摆率,便于在不同模式/速率下应用。
- 输出级带短路、过压、欠压保护;接收机为带正反馈的滞回比较器,可有效抑制差分噪声,且温度系数小。

## 怎么读
开放获取(按 CC-BY 提供,经 Scientific.Net 访问),未提供本地 PDF。建议快速浏览发射机/接收机架构与斜率控制原理,作为架构入门;工艺与仿真细节部分按需略读。

## 获取渠道
开放获取论文:经 Scientific.Net 按 DOI 访问(Trans Tech Publications,按 CC-BY 提供)。
DOI: [10.4028/www.scientific.net/AMR.433-440.1895](https://doi.org/10.4028/www.scientific.net/AMR.433-440.1895)

## 参见
- [A highly-digitized automotive CAN transceiver in 0.14µm high-voltage SOI CMOS](../papers/2015-deloge-soi-cmos-transceiver.md)
- [ISO 11898-2 (2016)](../standards/iso-11898-2-2016.md)
- [资源库 — 期刊](../../journals.md)
