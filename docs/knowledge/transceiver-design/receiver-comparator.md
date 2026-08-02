---
title: 接收比较器:阈值、共模范围与迟滞
description: 收发器接收路径的核心——接收比较器如何把总线差分电压恢复为 RxD 逻辑电平:显性/隐性阈值、共模范围、迟滞与接收路径延迟 tRX。
tags: [专家, 收发器]
---

## 定义

**接收比较器(Receiver / Comparator)** 是 CAN 收发器的接收前端:持续监测 CANH/CANL 的**差分电压**,与显性/隐性判决阈值比较,把总线状态恢复为控制器可读的 **RxD** 逻辑电平。它决定接收路径延迟 **tRX**、共模抑制能力与抗振铃/抗干扰能力,是与输出级并列的收发器两大模拟核心之一。

## 要点

### 显性/隐性阈值

- 接收器按差分电压判别状态:差分电压超过**显性阈值**判为显性(逻辑 0),低于**隐性阈值**判为隐性(逻辑 1);常见阈值在 0.5 V~0.9 V 量级,具体以 ISO 11898-2 与器件数据手册为准。
- 阈值附近是噪声、振铃、共模干扰最容易造成**误判**的区域——振铃峰值越过显性阈值会把隐性位读成显性位,触发错误帧(见[振铃抑制](../physical-layer/ringing-suppression.md))。

### 迟滞(Hysteresis)

- 在阈值附近引入**迟滞窗口**:上升沿与下降沿使用不同判决点,避免输入噪声/振铃在阈值附近反复穿越造成比较器抖动(振荡)。
- 迟滞宽度是抗噪与"误判"的折衷:过宽会改变有效采样边界,过窄则抗扰不足。

### 共模范围与共模抑制

- 接收器须在 CANH/CANL 平均电位(**共模电压**)偏移时仍能正确判别差分电平;经典高速 CAN 收发器共模范围典型覆盖 -12 V ~ +12 V(以标准与手册为准,见[共模范围](../../glossary/common-mode-range.md))。
- 共模抑制的两个层次:
  - **输入级电路**:宽共模摆幅下保持线性与对称。Infineon [US10042807B2(四象限输入电路)](../../resources/_entries/patents/us10042807b2.md)以电流为输入、用共模电流补偿差分电流,在宽共模范围内保持对称;
  - **引脚电容对称**:TI [US7113759B2(电容平衡)](../../resources/_entries/patents/us7113759b2.md)指出 CANH/CANL 节点寄生电容不平衡会让共模瞬态转成差分扰动,是 ISO 共模抑制测试失败的根因,需把两脚电容配平到约 10 pF 内。

### 接收路径延迟 tRX 与对称性

- tRX 是环回延迟 `t_loop = tTX + tBUS + tRX` 的接收段,由比较器带宽、滤波与边沿判决决定。
- 比较器的**传播延迟不对称性**(上升/下降、温度/电压漂移)直接消耗[相位裕度](../bit-timing/phase-margin.md)并限制 TDC 补偿精度——这是接收路径对数据相位可靠性的最大影响。

### 多协议兼容的判决逻辑

NXP [US11588662B1](../../resources/_entries/patents/us11588662b1.md) 面向 CAN FD 与 CAN XL 共存:通过 OOB(out-of-bounds)逻辑 + 状态机对差分电压做超范围判别,只在确认对应协议电平后才向 RxD 输出信令,避免振铃反射在 CAN FD 通信期间造成毛刺——接收器不仅要解调本协议电平,还要"认识并容忍"更高速度协议。

## 与收发器/控制器设计的关联

- **对收发器(模拟 IC)**:接收比较器决定 tRX、共模抑制与阈值健壮性。设计要点:差分输入级在宽共模下的线性与对称、引脚寄生电容配平、迟滞窗口设置、以及和后续解码逻辑(消隐、状态机)的数字-模拟协同。公开专利(US10042807B2、US7113759B2、US11588662B1)覆盖了从输入级到判别逻辑的完整思路。
- **对控制器(嵌入式)**:控制器侧不直接接触比较器,但 TDC 测得的环回延迟包含本节点 tRX,配置 SSP 偏移时以收发器数据手册的环回延迟/对称性指标为准;若总线抖动明显,先检查比较器阈值与迟滞是否落在振铃/共模干扰区(用示波器观察 RxD 抖动)。

## 参见

- 教程:[收发器传播延迟对称性](../../tutorials/09-delay-symmetry.md)、[BRS 与 TDC](../../tutorials/04-brs-tdc.md)
- 词条:[共模范围](../../glossary/common-mode-range.md)、[共模扼流圈](../../glossary/common-mode-choke.md)、[显性/隐性电平](../../glossary/dominant-recessive-levels.md)、[传播延迟对称性](../../glossary/propagation-delay-symmetry.md)、[收发器](../../glossary/transceiver.md)
- 专利:[US10042807B2(四象限输入)](../../resources/_entries/patents/us10042807b2.md)、[US7113759B2(电容平衡)](../../resources/_entries/patents/us7113759b2.md)、[US11588662B1(OOB 判别)](../../resources/_entries/patents/us11588662b1.md)
- 厂商资料:[NXP TJA1044](../../resources/_entries/vendors/nxp-tja1044.md)、[TI TCAN1044-Q1](../../resources/_entries/vendors/ti-tcan1044-q1.md)
- 标准规范:[ISO 11898-2 (2024)](../../resources/_entries/standards/iso-11898-2-2024.md)
- 相邻子域:[收发器延迟补偿(TDC/SSP)](../bit-timing/tdc.md)、[相位裕度与同步](../bit-timing/phase-margin.md)
