---
title: SIC 设计:收发器芯片设计要点
description: CAN SIC 收发器芯片设计要点——输出级三态阻抗、位时序对称性、振铃抑制电路(专利对照)、接收器、SIC 相位控制逻辑、防护与设计检查清单。
tags: [SIC, 收发器, 专家]
---

# SIC 设计:收发器芯片设计要点

> 本篇为 SIC 设计专题·**设计篇**,配套[原理篇](principle.md)与[测试篇](testing.md)。
> 本篇面向**模拟 IC 设计工程师**,从收发器芯片架构出发,拆解 SIC 的核心电路模块设计:输出级/驱动器、振铃抑制电路、接收器、SIC 相位控制逻辑,并给出参数规格对照与设计检查清单。
> 电路实现思路主要取自 12 篇已下载专利(Google Patents 官方 PDF,见[资源库专利分类](../../resources/patents.md))与厂商数据手册。

---

## 1. SIC 收发器芯片架构总览

```
              ┌─────────────────────────────────────────────┐
              │               CAN SIC 收发器                 │
   TXD ──────►│  驱动控制逻辑     ┌───────► 输出级(驱动器)   │──► CANH
              │  (边沿/模式检测)  │                          │──► CANL
              │             ┌────┴────┐   ┌──────────────┐   │
              │             │ SIC 控制│◄──│ 接收器(比较器) │◄──┤
   RXD ◄──────│             │ 时序/   │   └──────────────┘   │
              │             │ 阻抗切换│                      │
              │  VCC/VIO/VBAT 电源管理 / ESD / 保护          │
              └─────────────────────────────────────────────┘
```

三大关键设计域:
1. **输出级(驱动器)**:决定位时序对称性、边沿斜率、SIC 阻抗切换——SIC 性能的核心;
2. **SIC 控制逻辑**:检测显性→隐性转换,按窗口(≤120 ns / ≥355 ns / ≤530 ns)切换有源/被动隐性;
3. **接收器**:比较器迟滞、共模范围、输入阻抗,决定接收对称性 tREC 与抗扰度。

---

## 2. 输出级(驱动器)设计

### 2.1 三态阻抗架构(与原理篇的相位对应)

| 相位 | 输出阻抗 | 驱动行为 | 设计要点 |
|------|---------|---------|---------|
| 显性 dominant | 低(约 50 Ω 量级) | 强制驱动差分 | 大电流、低导通电阻、对称灌/拉 |
| **有源隐性 active recessive** | **约 100 Ω**(RDIFF_act_rec 75~133 Ω) | 主动向隐性放电 | **阻抗精确可控、可定时关断** |
| 被动隐性 passive recessive | 约 60 kΩ | 高阻,总线自然放电 | 高阻漏电要小、与仲裁兼容 |

**设计关键**:有源隐性阻抗必须落在 **75~133 Ω**(RDIFF_act_rec,ISO 11898-2:2024 Set C)——太低会过度加载总线(影响仲裁、增加功耗),太高起不到阻尼作用。这个阻抗通常由并联的辅助驱动支路实现,并**可编程/校准**以覆盖 PVT 变化。

### 2.2 位时序对称性设计(timing symmetry)

SIC 的硬指标(ISO 11898-2:2024 Set C,数据相位 ≤8 Mbit/s):

| 参数 | 符号 | 指标 | 设计含义 |
|------|------|------|---------|
| 发送隐性位宽偏差 | tBit(Bus) | **−10 ~ +10 ns** | 输出级上升/下降边沿对称;边沿整形(edge shaping) |
| 接收时序对称性 | tREC | **−20 ~ +15 ns** | 接收路径滤波/比较器延迟对称 |
| 接收位宽偏差 | tBit(RxD) | **−30 ~ +20 ns** | TX 对称性 + RX 对称性的叠加 |
| 环回延迟 | tLoop | **≤190 ns** | TXD→总线→RXD 总延迟预算 |

**设计含义**:
- 驱动器必须做**对称边沿整形**(dominant→recessive 与 recessive→dominant 的上升/下降时间尽量一致),减小数据相关的时序偏差;
- 传播延迟路径要拆分预算:td(TXD-bus) ≤80 ns、td(bus-RXD) ≤110 ns(TJA1463 数据手册实测 70~120 ns 有源隐性起始);
- 片上延迟应**温度补偿**,因为数据手册保证 -40~150 °C 全温范围(TJA1463 脚注:参数按设计保证,工厂测试用关联测试条件覆盖全温)。

### 2.3 斜率控制(slew rate control)

- 控制输出边沿斜率可降低高频分量 → 减少 EMC 辐射与反射幅度;
- Microchip US11539548B2 给出**分段斜率控制**:串联延迟线逐级关断多个并联电流源,边沿被切成多段缓变;
- 注意斜率与位时间的权衡:边沿过缓会侵占位时序裕量(5 Mbit/s 位时间 200 ns)。

---

## 3. 振铃抑制电路实现(专利对照)

这是 SIC 设计的"秘密武器",各家实现路线不同,均有专利保护。**建议按"先懂物理、再对照电路"的方式阅读下列专利**(全部已下载,见[资源库专利分类](../../resources/patents.md))。

### 3.1 TI:Recessive Nulling(隐性抵消)— US9606948B2(已过期,LRN/HRN 模式)

- **思想**:显性→隐性转换瞬间,额外并联一段低阻通路,加速泄放总线分布电容,让差分波形更快衰减到隐性阈值。
- **实现**:主驱动器旁并联 "recessive nulling driver",在转换后选定时长内保持低阻;分两种模式:
  - **LRN(light recessive nulling)**:只影响隐性位起始的一段;
  - **HRN(heavy recessive nulling)**:整个隐性位都保持低阻(含连续隐性位);
  - 混合模式按总线阻抗特征选择 nulling 时长,**必须在采样点前终止**。
- **设计启发**:nulling 时长可由寄存器编程;终止时刻的时序精度(与采样点错开)是设计重点;额外低阻通路会增加转换瞬间电流,需评估 EMC/共模电流。
- 专利条目:[US9606948B2](../../resources/_entries/patents/us9606948b2.md)

### 3.2 TI:瞬态触发振铃抑制 — US11310072B2

- **思想**:不靠精确定时,而是**检测振铃本身**:显性→隐性跳变后,振铃信号经电容耦合到 NMOS 栅极,幅度超过阈值即让管子导通,把振铃能量泄放到 VCC/GND。
- **实现**:驱动器 M1–M6(含高压/负压保护串联管)+ 脉冲发生器(约 200 ns)驱动 recessive nulling 将内部节点拉到 VCM + 电容耦合的振铃检测/阻尼通路;脉冲宽度固定或可编程。
- **设计启发**:"电平检测 + 自动导通阻尼"结构省功耗且对 PVT 鲁棒,不需要精确计时;关键是耦合电容取值(让振铃过阈值但不误触发)与泄放管的尺寸。
- 专利条目:[US11310072B2](../../resources/_entries/patents/us11310072b2.md)

### 3.3 Microchip:阻抗匹配 + 分段斜率 — US11539548B2(权利要求明确标注 CAN SIC)

- **思想**:振铃根源是隐性期阻抗失配 → 在转换期间及之后短时把**匹配阻抗接入总线**(显性态断开);同时用分段斜率控制减小高频成分。
- **实现**:阻抗匹配单元用 **OTA(跨导放大器)** 或"背靠背 regulated 晶体管对 + 栅控制电路"实现可控电阻;斜率控制用串联延迟线逐级关断并联电流源/电阻开关。
- **设计启发**:OTA 实现的可控阻抗可在 PVT 下保持振铃抑制性能;阻抗接入/断开的时序与显性态完全隔离,避免影响显性驱动。
- 专利条目:[US11539548B2](../../resources/_entries/patents/us11539548b2.md)

### 3.4 NXP:前馈振铃抑制 — US10020841B2

- **思想**:**前馈(feedforward)** 方式——在转换发生时主动注入抑制信号,而非等振铃出现再检测,响应更快。
- 与 TI 的"反馈检测"路线形成对比:前馈依赖精确的转换时刻检测,反馈更鲁棒但略慢。
- 专利条目:[US10020841B2](../../resources/_entries/patents/us10020841b2.md)

### 3.5 Bosch:振荡抑制单元 — US11068429B2(另有申请公开版 US20200364171A1)

- 针对显性↔隐性位状态切换时的振荡趋势,用**振荡抑制单元**在切换瞬间改变驱动特性。
- 设计启发:与仲裁(多节点同时驱动)的兼容性设计——振荡抑制不能破坏显性优先仲裁。
- 专利条目:[US11068429B2](../../resources/_entries/patents/us11068429b2.md)

### 3.6 Elmos:加速状态转换驱动器 — US11048657B2

- 显性→隐性**加速过渡**的输出级设计,与 TI nulling 思路互补。
- 专利条目:[US11048657B2](../../resources/_entries/patents/us11048657b2.md)

### 3.7 学术/行业实现参考

| 方案 | 来源 | 特点 |
|------|------|------|
| 振铃抑制电路(星型拓扑 8 ECU) | [DENSO Mori 2014](../../resources/_entries/papers/2014-mori-ringing-suppression.md),IEEE EMC Europe(DOI 10.1109/EMCEurope.2014.6930940) | SIC 思想的学术前身,必读背景 |
| 峰值电压检测+阻抗切换动态振铃抑制 | UNIST 硕士论文 2020(开放获取) | 芯片内振铃抑制电路学位论文,少见 |
| 串联阻尼电阻连接器 | KAIST Park 2020,IEEE EDAPS(DOI 10.1109/EDAPS50281.2020.9312922) | 网络级(连接器)阻尼方案,与芯片内方案对照 |

> 论文条目:[Mori 2014 振铃抑制电路](../../resources/_entries/papers/2014-mori-ringing-suppression.md)

---

## 4. 接收器设计

### 4.1 关键指标与电路

| 指标 | 典型值/要求 | 设计要点 |
|------|------------|---------|
| 显性/隐性阈值 | 0.9 V / 0.5 V(差分) | 比较器翻转点精度,避免振铃误判 |
| 共模输入范围 | 宽共模(高 EMI,如 TLE9371 强调) | 输入级结构(如 Infineon US10042807B2 四象限输入电路) |
| 接收对称性 tREC | −20 ~ +15 ns | 滤波与比较器延迟对称;迟滞 |
| 输入阻抗 | 隐性期高阻 | 与总线负载/节点数相关 |

- **迟滞比较器**:抑制差分噪声抖动,温度系数要小(吉林大学 AMR 2012 论文有经典实现);
- **共模电容平衡**(TI US7113759B2):改善接收器共模抑制,对 EMC 抗扰关键;
- 接收路径的**延迟对称性**直接决定 tREC——上升/下降路径、滤波器的群延迟必须对称。

### 4.2 共模与 EMC(收发器级)

- 共模发射抑制:TI US7183793B2(降低 CAN 收发器电磁辐射的系统与方法);
- 输出共模电压 VCM 对称性:TJA1463 有 Vcm(step) symmetry 指标;
- 测试标准:IEC 62228-3(见[测试篇](testing.md))。

---

## 5. SIC 相位控制逻辑(数字/模拟混合)

SIC 时序窗口(ISO 11898-2:2024 Set C / TJA1463 实测):

| 事件 | 符号 | 指标 | 实现 |
|------|------|------|------|
| TXD→总线有源隐性开始 | tact_rec_start | 70~120 ns(≤120) | 边沿检测 + 单稳定时器 |
| TXD→总线有源隐性结束 | tact_rec_end | 355~480 ns(≥355) | 定时窗口;可编程微调 |
| TXD→总线被动隐性开始 | tpas_rec_start | 415~530 ns(≤530) | 输出阻抗切回高阻 |

**设计要点**:
1. **边沿检测**:准确捕捉 TXD 的显性→隐性沿(抗抖、抗毛刺滤波);
2. **可编程窗口**:窗口长短需可调以覆盖不同网络(短 stub 可短、长网络需长);寄存器配置;
3. **阻抗切换的连续性**:有源→被动切换时不能产生毛刺(glitch-free switch);
4. **与仲裁兼容**:多位同时驱动时,有源隐性必须能被显性覆盖(TXD 变 LOW 立即回显性——TJA1463 注释:"If TXD goes LOW before the recessive transition has been completed, the bus switches to dominant");
5. **TXD 显性超时保护**:tto(dom)TXD 0.8~9 ms(防止 TXD 卡死拉死总线)。

---

## 6. 可靠性/防护设计(车规必做)

| 项目 | 典型指标 | 参考 |
|------|---------|------|
| 总线引脚容错 | ±58 V(TI/NXP 新一代);−36~40 V(旧) | 高侧/低侧钳位、串联器件 |
| 总线 ESD | ≥8 kV HBM/IEC | 片内 ESD 结构 + 片外 TVS 协同([IEEE TDMR 2017 论文](../../resources/_entries/journals/2017-tdmr-esd-tvs-can-transceiver.md)) |
| TXD 显性超时 | 0.8~9 ms | 数字看门狗 |
| 欠压/过温保护 | UVLO、TSD | 电源管理 |
| 工艺选择 | 0.14 µm HV SOI([NXP Deloge 2015](../../resources/_entries/papers/2015-deloge-soi-cmos-transceiver.md))、0.15 µm BCD(北方工大 2026)、0.18 µm CMOS([TCAS-I 2025](../../resources/_entries/journals/2025-tcasi-secure-authentication-transceiver.md)) | 高压器件集成度 vs 成本 |

---

## 7. 竞品规格对照(设计 Spec 对标用)

| 参数 | NXP TJA1463 | TI TCAN1462/63 | TI TCAN1472(新) | Infineon TLE9371 |
|------|------------|----------------|-----------------|------------------|
| SIC 标准 | ISO 11898-2:2024 Set C | CiA 601-4 + ISO 2024 | ISO 11898-2:2024 Annex A | CiA 601-4 + ISO 11898-2:2016 |
| 数据速率 | ≤8 Mbit/s | ≤8 Mbps | ≤8 Mbit/s | ≤8 Mbit/s |
| 环回延迟 | ≤190 ns | ≤190 ns | 190 ns max | — |
| 总线容错 | ±58 V | ±58 V | ±58 V | ±58 V |
| 总线 ESD | 8 kV | 8 kV | 8 kV | ±8 kV |
| VIO 范围 | 2.95~5.5 V | 1.7~5.5 V(TCAN1462) | 1.7~5.5 V | 3.3/5 V |
| 特点 | Sleep 模式、ASIL(1464) | INH/WAKE、SOT-23 | 1.8V 逻辑、SOT-23 | 高共模 EMI |

> 详细数据以各数据手册为准:
> - [NXP TJA1463](../../resources/_entries/vendors/nxp-tja1463.md)、[TJA1462](../../resources/_entries/vendors/nxp-tja1462.md)、[TJA1464(ASIL B)](../../resources/_entries/vendors/nxp-tja1464.md)
> - [TI TCAN1462-Q1](../../resources/_entries/vendors/ti-tcan1462-q1.md)、[TCAN1463-Q1](../../resources/_entries/vendors/ti-tcan1463-q1.md)
> - [Infineon TLE9371](../../resources/_entries/vendors/infineon-tle9371v.md)、[onsemi NCV7357](../../resources/_entries/vendors/onsemi-ncv7357.md)

---

## 8. 设计检查清单(流片前对照)

**功能/性能**

- [ ] tBit(Bus) −10~+10 ns、tREC −20~+15 ns、tBit(RxD) −30~+20 ns(Set C)
- [ ] RDIFF_act_rec 75~133 Ω;tact_rec_start ≤120 ns;tact_rec_end ≥355 ns;tpas_rec_start ≤530 ns
- [ ] 环回延迟 ≤190 ns;TD 拆分:td(TXD-bus) ≤80 ns、td(bus-RXD) ≤110 ns
- [ ] 有源隐性可被显性覆盖(仲裁兼容);glitch-free 阻抗切换
- [ ] TXD 显性超时 0.8~9 ms

**鲁棒性**

- [ ] 总线引脚 ±58 V 容错、8 kV ESD、欠压/过温保护
- [ ] EMC:IEC 62228-3 传导发射/抗扰预算;共模对称
- [ ] PVT 角覆盖(−40~150 °C);阻抗可校准/编程

**可测性(为[测试篇](testing.md)预留)**

- [ ] SIC 窗口(120/355/530 ns)测试引脚或模式暴露
- [ ] 环回延迟/对称性测试电路、眼图模板测试点
- [ ] 按 ISO 16845-2 测试项预留测点

---

## 9. 参考资料

- 专利(全部已下载):[资源库专利分类](../../resources/patents.md)(US9606948B2、US11310072B2、US11539548B2、US10020841B2、US11068429B2、US11048657B2、US10042807B2、US7113759B2、US7183793B2、US9471528B2、US10084617B2、US11588662B1)
- 数据手册:[NXP TJA1462/63/64](../../resources/_entries/vendors/nxp-tja1463.md)、[TI TCAN1462/63](../../resources/_entries/vendors/ti-tcan1463-q1.md)、[onsemi NCV7357](../../resources/_entries/vendors/onsemi-ncv7357.md)
- 芯片级论文:[Deloge 2015 NXP SOI 收发器](../../resources/_entries/papers/2015-deloge-soi-cmos-transceiver.md)、[TCAS-I 2025 安全收发器](../../resources/_entries/journals/2025-tcasi-secure-authentication-transceiver.md)、[MDPI Chips 2024](../../resources/_entries/journals/2024-chips-authentication-rail-converters.md)、[IEICE ELEX 2025 过冲设计](../../resources/_entries/journals/2025-ieice-overshoot.md)
- 补充文献:IEEE EDAPS 2020(串联阻尼)、UNIST 2020(动态振铃抑制)、[DENSO 2014(振铃抑制电路)](../../resources/_entries/papers/2014-mori-ringing-suppression.md)——DOI 见[资源库论文分类](../../resources/papers.md)与调研记录

---

## 关联

- **词条**:[CAN SIC](../../glossary/can-sic.md)、[振铃抑制](../../glossary/ringing-suppression.md)、[回波损耗](../../glossary/return-loss.md)、[收发器](../../glossary/transceiver.md)、[传播延迟对称性](../../glossary/propagation-delay-symmetry.md)、[环回延迟](../../glossary/loop-delay.md)
- **教程**:[振铃抑制原理与测量](../../tutorials/08-ringing-suppression.md)、[收发器传播延迟对称性](../../tutorials/09-delay-symmetry.md)
- **知识库**:[收发器设计 子域](../transceiver-design/index.md)(输出级、接收比较器、ESD 与共模抑制)、[物理层与SIC 子域](../physical-layer/index.md)
- **专题内**:原理见[原理篇](principle.md),验证见[测试篇](testing.md)
