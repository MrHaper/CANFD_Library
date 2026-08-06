---
title: 收发器设计
description: 输出级、接收比较器、ESD 保护与共模抑制——CAN FD 收发器模拟电路设计的权威知识点,主要面向模拟 IC 设计工程师。
tags: [收发器]
---

# 收发器设计

本子域整理 CAN FD **收发器电路设计**的权威知识点:从输出级如何形成显性/隐性电平与斜率控制,到接收比较器的阈值/共模范围/迟滞,再到 ESD 保护与共模抑制的健壮性设计。这里是把[物理层与SIC](../physical-layer/index.md)的系统级规范"翻译"成具体电路模块的地方,专利条目是理解电路思路的公开素材。

!!! tip "需要"设计手册版"?"
    [设计参考](../../design/index.md)板块按模块提供**参数设计要点与流片前自查清单**(规格基线 → 时序预算 → 输出级 → 接收比较器 → SIC 控制 → 振铃抑制 → ESD → 电源唤醒),与本文档互链使用。

## 知识点

| 知识点 | 难度 | 定位 |
|---|---|---|
| [输出级:差分驱动与显性/隐性电平](output-stage.md) | 专家 | 显性/隐性电平的形成、差分驱动结构、斜率控制与高速数据相位的加速隐性过渡方案 |
| [接收比较器:阈值、共模范围与迟滞](receiver-comparator.md) | 专家 | 显性/隐性阈值与迟滞、共模范围与共模抑制、接收路径延迟 tRX 与对称性 |
| [ESD 保护与共模抑制](esd-common-mode.md) | 专家 | 片内 ESD 与片外 TVS 的分工、共模发射抑制(复制电路)与相关测试方法 |

## 相关入口

- 教程:[SIC 是什么](../../tutorials/07-what-is-sic.md)、[振铃抑制原理与测量](../../tutorials/08-ringing-suppression.md)、[收发器传播延迟对称性](../../tutorials/09-delay-symmetry.md)
- 术语:[收发器类词条](../../glossary/index.md)
- 专利:[US9606948B2(隐性抵消)](../../resources/_entries/patents/us9606948b2.md)、[US10042807B2(四象限接收器)](../../resources/_entries/patents/us10042807b2.md)、[US7183793B2(共模发射抑制)](../../resources/_entries/patents/us7183793b2.md)
- 厂商资料:[NXP TJA1044](../../resources/_entries/vendors/nxp-tja1044.md)、[TI TCAN1044-Q1](../../resources/_entries/vendors/ti-tcan1044-q1.md)、[TI SLVAFC1(ESD 防护)](../../resources/_entries/vendors/ti-slvafc1.md)
- 相邻子域:[物理层与SIC](../physical-layer/index.md)、[位定时与同步](../bit-timing/index.md)
