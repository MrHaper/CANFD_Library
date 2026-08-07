---
title: 模拟 IC 设计教材知识总结
description: 面向 CAN FD / CAN SIC 收发器设计的模拟 IC 教材知识地图——器件与工艺、放大器/比较器、输出级、ESD/闩锁、版图、反馈稳定性、噪声、电源与基准,按收发器模块映射经典教材章节。
tags: [模拟IC, 教材, 收发器]
---

# 模拟 IC 设计教材知识总结

> 本页把 CAN FD / CAN SIC 收发器设计需要的**模拟 IC 基本功**整理成知识地图,并给出经典教材的导读映射。教材版权归原作者/出版社,本站不托管全文,请通过正规渠道获取;本站[资源库·教材书籍](../../resources/books/)收录的是 CAN/现场总线方向的教材,可作为系统层补充。

## 一、为什么需要这些基础

收发器芯片 = 输出级(大电流驱动)+ 接收比较器(高速比较)+ 偏置/基准 + ESD/保护 + 版图匹配。每一个模块都对应模拟 IC 的经典知识:

| 收发器模块 | 对应模拟 IC 基础 |
| --- | --- |
| 输出级(驱动器) | 大电流输出级、推挽/AB 类、驱动能力与导通电阻 |
| 接收比较器 | 高速比较器、迟滞、失调与失配 |
| 偏置/基准/UVLO | Bandgap、电流镜、上电复位 |
| ESD/总线保护 | ESD 器件、钳位、闩锁防护 |
| 共模抑制/输入匹配 | 差分对、版图匹配、电容平衡 |
| 斜率/对称性 | 开关电容?不——是电流镜精度、时序整形 |

## 二、知识地图(按主题)

### 1. 器件与工艺

- MOS 器件模型:阈值、跨导、输出电阻、亚阈值;工艺角(TT/SS/FF)与温度对电路的影响。
- 高压器件:**LDMOS/DMOS**、SOI 工艺——CAN 总线引脚需承受 −27~+40 V(扩展 ±58 V),输出级与输入网络的高压管击穿电压要留裕量(80 V 规格建议 BV ≥ 100 V)。
- 失配与工艺波动:**蒙特卡洛**、失配模型是阈值/迟滞/对称性设计的基础。

### 2. 单级放大器与差分对

- 共源/共栅/共漏、差分对的增益与共模范围、电流镜精度。
- 接收比较器的输入级(四象限输入、宽共模)本质是差分结构;输入失调直接移动阈值(0.5/0.9 V 窗口)。

### 3. 反馈与稳定性

- 负反馈、环路增益、相位裕度、单位增益带宽。
- 输出级/预驱动中的缓冲与偏置环路、LDO/电源管理都需要稳定性分析;带宽不足会拖慢 TX 通路延迟。

### 4. 比较器与迟滞

- 开环比较器、正反馈迟滞(施密特结构)、传播延迟与失调。
- 收发器接收比较器要求:阈值 0.5~0.9 V、迟滞 ≥100 mV、tRX ≤110 ns、ΔtRec −20~+15 ns。

### 5. 输出级与大电流驱动

- A/B/AB 类、推挽结构、交越失真、驱动能力(Ron)、灌/拉对称。
- CAN 输出级显性差分 1.5~3 V、驱动电流数十 mA 量级、Vsym 0.9~1.1;SIC 三态阻抗(50 Ω/100 Ω/60 kΩ)是"可控电阻输出"的经典应用。

### 6. ESD 与闩锁

- ESD 器件(HBM/CDM)、钳位二极管、ggNMOS/SCR、两级保护;闩锁(Latch-up)机理与防护(well tie、guard ring)。
- CAN 总线 ESD 等级(HBM ±8 kV、IEC 61000-4-2 ±6~8 kV、SAE J2962-2 ±15 kV 空气放电)是片内保护结构的设计输入。

### 7. 版图与匹配

- 匹配(共心、叉指)、寄生电容/电阻、guard ring、高压爬电间距。
- CANH/CANL 输入网络匹配 mR ±0.03、引脚电容配平约 10 pF——这是共模抑制的物理基础,也是版图课的经典考题。

### 8. 噪声与电源

- 热噪声、1/f 噪声、噪声系数;比较器噪声与迟滞的折衷。
- 电源:带隙基准、LDO、UVLO、上电时序;Standby µA 级电流需要低功耗偏置设计。

## 三、教材导读映射表

!!! note "获取方式"
    以下经典教材均为**外部参考**,请通过出版社/图书馆/正版电子平台获取;本站不托管其全文。

| 主题 | 建议教材(经典) | 对应收发器模块 |
| --- | --- | --- |
| CMOS 模拟电路综合 | Razavi《Design of Analog CMOS Integrated Circuits》 | 全模块基础 |
| CMOS 电路设计与版图 | Baker《CMOS: Circuit Design, Layout, and Simulation》 | 版图、匹配、数字接口 |
| 模拟电路分析与设计 | Allen & Holberg《CMOS Analog Circuit Design》 | 放大器、比较器、偏置 |
| 模拟与混合信号 | Gray & Meyer《Analysis and Design of Analog Integrated Circuits》 | 输出级、反馈、噪声 |
| 模拟设计精要 | Sansen《Analog Design Essentials》 | 精读各模块的速查 |
| 模拟版图艺术 | Hastings《The Art of Analog Layout》 | 匹配、ESD、guard ring |
| ESD 与闩锁 | Voldman《ESD: Circuits and Devices》等 | 总线引脚保护 |
| CAN/总线系统层 | Lawrenz《CAN System Engineering》、饶运涛《CAN 原理》等(本站收录) | 网络/协议视角 |

## 四、本站配套学习路径

1. **先读[设计参考](../../design/index.md)的模块页**,把参数规格(Set A/B/C)变成设计目标;
2. **按模块回查教材章节**(上表),只精读与当前模块相关的部分;
3. **用专利/论文当电路案例**:本站[专利全文](../../resources/full-text/index.md)收录了 TI/Microchip/Bosch/NXP 的振铃抑制、阻抗匹配、共模抑制等电路方案,是"教材理论 → 实际电路"的最佳桥梁;
4. **版图与验证**:对照[ESD 与总线保护设计要点](../../design/esd-protection.md)与[测试篇](../sic-design/testing.md)做闭环。

## 参见

- 设计参考:[TX 模块设计要点](../../design/tx-module.md)、[输出级设计要点](../../design/output-stage.md)、[接收比较器设计要点](../../design/receiver.md)、[ESD 与总线保护设计要点](../../design/esd-protection.md)
- 知识库:[收发器设计子域](index.md)、[SIC 设计专题](../sic-design/index.md)
- 资源:[教材书籍分类](../../resources/books/)、[专利全文](../../resources/full-text/index.md)
