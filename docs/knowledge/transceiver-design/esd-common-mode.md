---
title: ESD 保护与共模抑制
description: 收发器总线引脚的健壮性设计——片内 ESD 结构、片外 TVS 与共模扼流圈的分工,以及共模范围与共模发射抑制的电路思路。
tags: [专家, 收发器]
---

## 定义

**ESD 保护与共模抑制**是收发器面向车载线束环境的两个健壮性维度:**ESD 保护**让 CANH/CANL 引脚扛住静电放电与过压事件;**共模抑制**让接收器在地电位差、耦合干扰下仍能正确判别差分电平,并压低收发器自身的共模发射。二者共同决定收发器在整车中的存活率与 EMC 合规性。

## 要点

### ESD 保护:分级模型与片内/片外分工

| 层次 | 内容 |
|---|---|
| 分级模型 | HBM(典型 ≥ ±8 kV)、CDM、IEC 61000-4-2、ISO 10605(整车线束放电);具体等级以器件数据手册与 AEC-Q100 要求为准 |
| 片内防护 | 收发器引脚内置 ESD 结构,承受连接器/线束的直接冲击;部分器件宣称系统级 ESD(如 ±58 V 总线容错、8 kV) |
| 片外协同 | 外围 **TVS 二极管**承接更大能量、**共模扼流圈**抑制共模电流;注意 TVS 寄生电容对高速数据相位信号质量的影响 |

TI [SLVAFC1 应用笔记](../../resources/_entries/vendors/ti-slvafc1.md)系统讲解 CAN 总线瞬态与 ESD 耦合路径、IEC 61000-4-2 / ISO 7637 测试方法、TVS 与共模扼流圈选型及 PCB 布局;NXP [AH1308](../../resources/_entries/vendors/nxp-ah1308.md)给出含完整 ESD/EMC 防护的应用电路与 PCB 规则——这两份是"从芯片到系统"的 ESD 落地方案教材。

### 共模抑制:接收端的两个层次

- **共模范围**:接收比较器须在共模电压偏移(地电位差、线束耦合、故障注入)下正确判别,典型覆盖 -12 V ~ +12 V(以标准与手册为准,见[共模范围](../../glossary/common-mode-range.md))。
- **引脚电容对称**:TI [US7113759B2](../../resources/_entries/patents/us7113759b2.md) 证明 CANH/CANL 寄生电容不平衡会让共模瞬态转成差分扰动(ISO 共模抑制测试失败的根因),需把两脚电容配平到约 10 pF 内——版图对称与电容配平是共模抑制的物理基础,详见[接收比较器](receiver-comparator.md)。

### 共模发射抑制:输出端的两个分量

TI [US7183793B2](../../resources/_entries/patents/us7183793b2.md) 把驱动器共模发射分为两个分量分别治理:

| 分量 | 机理 | 治理手段 |
|---|---|---|
| 稳态共模差 ΔVoc | 显性/隐性两稳态之间共模电压差,主要造成 AM 频段辐射 | **DC 复制电路(DC replica)**:采样显性态共模,在隐性态强制拉回同一共模电平 |
| 转换期共模摆幅 Voc(pp) | 状态转换期间的共模峰值摆动,主要造成 FM 频段辐射 | **动态 AC 复制电路**:转换期间采样共模并与参考比较、修正驱动电流 |

配合偏置电流斜坡(ramp)控制,构成控制输出共模的经典模拟方法,对 SIC 高 dV/dt 场景下的辐射预算同样适用。

### 测试方法

- 收发器 EMC 评估按 **IEC 62228-3**(传导发射与射频抗扰度),车规整机按 **CISPR 25**;测量方法见[回波损耗与 EMC](../physical-layer/return-loss-emc.md)与本页厂商资料。
- 芯片级 ESD/EFT 台架方法与共模注入测试方法在 SLVAFC1、AH1308 中有实操步骤。

## 与收发器/控制器设计的关联

- **对收发器(模拟 IC)**:ESD/共模是"看不见的性能":片内 ESD 结构(钳位器件、限流)与输入级共模抑制(四象限输入、电容配平)在版图与器件层面决定健壮性;共模发射抑制(复制电路 + 电流斜坡)是 EMC 设计的模拟核心。专利(US7113759B2、US7183793B2)是公开的设计思路。
- **对控制器(嵌入式)**:控制器侧主要在系统层配合:PCB 上 TVS 与共模扼流圈的选型、地平面处理、线束屏蔽;以及评估地电位差对共模范围预算的占用。故障(对电源/对地短路)场景下收发器进入保护,控制器应能识别总线故障状态并恢复。

## 参见

- 教程:[收发器传播延迟对称性](../../tutorials/09-delay-symmetry.md)、[示波器抓 CAN FD 帧](../../tutorials/10-scope-capture.md)(观察共模/振铃)
- 词条:[ESD](../../glossary/esd.md)、[共模范围](../../glossary/common-mode-range.md)、[共模扼流圈](../../glossary/common-mode-choke.md)、[EMI/EMC](../../glossary/emi-emc.md)、[CISPR 25](../../glossary/cispr25.md)、[AEC-Q100](../../glossary/aec-q100.md)
- 专利:[US7113759B2(电容平衡)](../../resources/_entries/patents/us7113759b2.md)、[US7183793B2(共模发射抑制)](../../resources/_entries/patents/us7183793b2.md)
- 厂商资料:[TI SLVAFC1(ESD 防护)](../../resources/_entries/vendors/ti-slvafc1.md)、[NXP AH1308(应用提示)](../../resources/_entries/vendors/nxp-ah1308.md)、[TI TCAN1044-Q1](../../resources/_entries/vendors/ti-tcan1044-q1.md)
- 标准规范:[IEC 62228-3](../../resources/_entries/standards/iec-62228-3-2019.md)、[ISO 11898-2 (2024)](../../resources/_entries/standards/iso-11898-2-2024.md)
- 相邻子域:[回波损耗与 EMC](../physical-layer/return-loss-emc.md)、[接收比较器](receiver-comparator.md)
