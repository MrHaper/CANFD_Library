---
title: TJA1463 CAN SIC 收发器(带休眠模式)数据手册(全文查阅)
description: NXP TJA1463 CAN FD 信号改善(SIC)收发器(带 Sleep 模式)数据手册(Rev. 3.0,2025)全文站内版:概述、特性、快速参考数据、系统/CAN 双状态机与五种系统模式、ERR_N 本地诊断、快速/静态/动态特性、ISO 11898-2:2024 参数交叉引用。
type: 全文查阅
organization: NXP Semiconductors
year: 2025
tags: [全文查阅, 数据手册]
source: https://www.nxp.com/products/interfaces/can-transceivers/can-fd-transceivers/sic-transceivers:TJA1463
---

# TJA1463 CAN FD Signal Improvement Transceiver with Sleep Mode(全文查阅)

> **器件**:TJA1463(TJA146x 家族;AEC-Q100 Grade 1;高温变体 TJR1463 支持 150 °C 环境)
> **文档**:NXP Product data sheet,Rev. 3.0 — 12 February 2025
> **原文 PDF**:[📄 下载原文 PDF](../../files/vendors/NXP_TJA1463_CAN_SIC_datasheet.pdf)
> **相关资料**:[资源条目页](../_entries/vendors/nxp-tja1463.md)

---

## 1 General description(概述)

The TJA1463 is a member of the TJA146x family of transceivers that provide an interface between a Controller Area Network (CAN) or CAN FD (Flexible Data rate) protocol controller and the physical two-wire CAN bus. TJA146x transceivers implement the CAN physical layer as defined in ISO 11898-2:2024 third edition and SAE J2284-1 to SAE J2284-5,and are fully interoperable with high-speed Classical CAN and CAN FD transceivers.

The TJA1463 includes CAN signal improvement capability (SIC),as defined in ISO 11898-2:2024 parameter set C. CAN signal improvement significantly reduces signal ringing in a network,allowing reliable CAN FD communication to function in larger topologies. In addition,the TJA1463 features a much tighter bit timing symmetry performance to enable CAN FD communication up to 8 Mbit/s.

The TJA1463 is intended as a simple replacement for high-speed Classical CAN and CAN FD transceivers,such as the TJA1043 and TJA1443 from NXP. It offers pin compatibility and is designed to avoid changes to hardware and software design,allowing the TJA1463 to be easily retrofitted to existing applications.

An AEC-Q100 Grade 0 variant,the TJR1463,is available for high temperature applications,supporting operation at 150 °C ambient temperature.

## 2 Features and benefits(特性与优点)

### 2.1 General

- ISO 11898-2:2024 parameter set A-C,SAE J2284-1 to SAE J2284-5 and SAE J1939-14 compliant
- Implements CAN Signal Improvement Capability as defined in ISO 11898-2:2024 parameter Set C to significantly reduce signal ringing effects in a network
- Tighter bit timing symmetry performance versus standard CAN FD transceivers allowing for data rates up to 8 Mbit/s
- Low Electromagnetic Emission (EME) and high Electromagnetic Immunity (EMI)
- Qualified according to AEC-Q100 Grade 1
- VIO input for interfacing with 3.3 V to 5 V microcontrollers
- Listen-only mode for node diagnosis and failure containment
- Available in SO14 and leadless HVSON14 (3.0 mm × 4.5 mm) packages;HVSON14 with improved Automated Optical Inspection (AOI) capability
- Dark green product (halogen free and RoHS compliant)

### 2.2 Predictable and fail-safe behavior

- Undervoltage detection with defined handling on all supply pins
- Full functionality guaranteed from the undervoltage detection thresholds up to the maximum limiting voltage values
- Defined behavior below the undervoltage detection thresholds
- Transceiver disengages from the bus (high-ohmic) when the battery voltage drops below the Off mode threshold
- Internal biasing of TXD and mode selection input pins,to enable defined fail-safe behavior

### 2.3 Low-power management

- Very low-current Standby and Sleep modes,with local (WAKE pin),bus (CANH/CANL pins) and host (STB/EN pins) wake-up capability
- Entire node with TJA1463 can be powered down while still supporting local,bus and host wake-up
- CAN wake-up receiver powered by VBAT allowing VIO and VCC to be shut down
- CAN wake-up pattern filter time of 0.5 μs to 1.8 μs,meeting Classical CAN and CAN FD requirements

### 2.4 Diagnosis & Protection

- Overtemperature diagnosis
- Transmit Data (TXD) dominant time-out and TXD-to-RXD short-circuit handler with diagnosis
- Bus dominant failure diagnosis
- Cold start diagnosis (first battery connection)
- High ESD handling capability on the bus pins
- Bus pins and VBAT protected against transients in automotive environments
- Thermally protected

## 3 Quick reference data(快速参考数据)

**Table 1. Quick reference data**

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| VBAT | battery supply voltage | operating range | 4.5 | - | 28 | V |
| IBAT | battery supply current | Normal or Listen-only mode | - | 80 | 300 | μA |
| | | Standby or Sleep mode | - | 13 | 26 | μA |
| Vuvd(VBAT) | undervoltage detection voltage on pin VBAT | | 4 | - | 4.5 | V |
| VCC | supply voltage | | 4.5 | - | 5.5 | V |
| ICC | supply current | Normal mode,dominant | - | 42 | 70 | mA |
| | | Normal mode,recessive | - | 7 | 10 | mA |
| | | Listen-only mode | - | 5 | 8 | mA |
| | | Standby or Sleep mode | - | - | 2 | μA |
| Vuvd(VCC) | undervoltage detection voltage on pin VCC | VBAT > 4.5 V | 4 | - | 4.5 | V |
| Vuvhys(VCC) | undervoltage hysteresis voltage on pin VCC | | 50 | - | - | mV |
| VIO | supply voltage on pin VIO | | 2.95 | - | 5.5 | V |
| IIO | supply current on pin VIO | Normal mode,dominant;VTXD = 0 V | - | 90 | 250 | μA |
| | | Normal or Listen-only mode,recessive;VTXD = VIO | - | - | 3 | μA |
| | | Standby or Sleep mode | - | - | 2 | μA |
| Vuvd(VIO) | undervoltage detection voltage on pin VIO | VBAT > 4.5 V | 2.65 | - | 2.95 | V |
| Vuvhys(VIO) | undervoltage hysteresis voltage on pin VIO | | 50 | - | - | mV |
| VESD | ESD voltage | IEC 61000-4-2 on pins CANH and CANL | -6 | | +6 | kV |
| VCANH | voltage on pin CANH | limiting value according to IEC 60134 | -36 | | +40 | V |
| VCANL | voltage on pin CANL | limiting value according to IEC 60134 | -36 | | +40 | V |
| Tvj | virtual junction temperature | | -40 | - | +150 | °C |

## 4 Ordering information(订购信息)

**Table 2. Ordering information**

| Type number | Package Name | Description | Version |
|---|---|---|---|
| TJA1463AT | SO14 | plastic small outline package;14 leads;body width 3.9 mm | SOT108-1 |
| TJA1463ATK | HVSON14 | plastic thermal enhanced very thin small outline package;no leads;14 terminals;body 3 × 4.5 × 0.85 mm | SOT1086-2 |

**Table 3. TJA1463 feature overview**(摘要):Normal/Standby/Sleep/Silent(Listen-only)/Selectable Off 模式;VCC、VIO、VBAT 电源;支持 5 Mbit/s 与 8 Mbit/s CAN FD;Signal Improvement(ISO 11898-2:2024 parameter set C);Wake-up source recognition(RXD 唤醒后保持低电平);Short WUP support(0.5-1.8 μs);Single supply pin wake-up(仅需 VBAT);TXD dominant time-out;通过 ERR_N 引脚本地诊断。

## 5 Block diagram(框图)

TJA1463 框图包含:VIO (5)/VCC (3)/VBAT (10) 电源;温度保护;发射器(带 TIME-OUT);5 V 稳压器(VBAT → 5 V);MODE CONTROL AND WAKE-UP CONTROL AND LOCAL FAILURE DETECTION;MUX 与 DRIVER;normal receiver 与 low-power receiver;WAKE-UP FILTER;TXD (1)、WAKE (9)、ERR_N (8)、STB_N (14)、EN (6)、RXD (4)、INH (7)、n.c. (11)、GND (2)、CANH (13)/CANL (12)。

## 6 Pin configuration and description(引脚配置与描述)

SO14 与 HVSON14 14 引脚配置:1 TXD,2 GND,3 VCC,4 RXD,5 VIO,6 EN,7 INH,8 ERR_N,9 WAKE,10 VBAT,11 n.c.,12 CANL,13 CANH,14 STB_N。

**Table 4. Pin description**

| Symbol | Pin | Type[1] | Description |
|---|---|---|---|
| TXD | 1 | I | transmit data input;inputs data (from the CAN controller) to be written to the bus lines |
| GND[2] | 2 | G | ground |
| VCC | 3 | P | 5 V supply voltage input |
| RXD | 4 | O | receive data output;outputs data read from the bus lines (to the CAN controller) |
| VIO | 5 | P | supply voltage input for I/O level adapter |
| EN | 6 | I | enable control input |
| INH | 7 | AO | inhibit output for switching external voltage regulators |
| ERR_N | 8 | O | local failure detection;wake-up source recognition and power-on indication output (active-LOW) |
| WAKE | 9 | AI | local wake-up input |
| VBAT | 10 | P | battery supply voltage input |
| n.c. | 11 | - | not connected |
| CANL | 12 | AIO | LOW-level CAN bus line |
| CANH | 13 | AIO | HIGH-level CAN bus line |
| STB_N | 14 | I | Standby mode control input (active-LOW) |

[1] I:digital input;O:digital output;AI:analog input;AO:analog output;AIO:analog input/output;P:power supply;G:ground。[2] HVSON14 封装芯片地连接 GND 引脚与裸露中心焊盘;建议将中心焊盘焊接到板地。

## 7 Functional description(功能描述)

### 7.1 Operating modes(工作模式)

TJA1463 包含两个独立状态机:系统状态机与 CAN 状态机。两个状态机都受 VCC 欠压状态独立影响。欠压检测定义为 Vx < Vuvd(x) 持续 t > tdet(uv);欠压恢复定义为 Vx > Vuvd(x) 持续 t > trec(uv)。

### 7.1.1 System operating modes(系统工作模式)

系统状态机支持五种系统工作模式,由 STB_N 与 EN 引脚选择。模式转换在 tt(moch) 后完成;失效安全诊断信息经 ERR_N 在 td(moch-ERR_N) 后可用。

**Off mode** — 任何模式下 VBAT 低于欠压检测阈值 Vuvd(VBAT) 时进入;首次连接电池(冷启动)时在上电启动于 Off 模式。Off 模式下 INH 与 ERR_N 高阻。

**Standby mode** — 第一级省电模式。VBAT 高于 Vuvd(VBAT) 时开始启动,经 tstartup 后进入 Standby,INH 变高。VIO 高于 Vuvd(VIO) 且 STB_N 与 EN 为高 → Normal;STB_N 高且 EN 低 → Listen-only;STB_N 低 → 保持 Standby。VIO 低于 Vuvd(VIO) 持续 tdet(uv)long 和/或 VCC 低于 Vuvd(VCC) 持续 tdet(uv)long → Sleep。STB_N 保持低且 EN 高持续 th(gotosleep)('go-to-sleep' 命令)也可触发 Standby → Sleep;若 Wake 标志已置位则该命令被否决,器件保持 Standby。

**Normal mode** — STB_N 与 EN 均为高,且 VBAT 与 VIO 存在时选择。INH 保持高,受 INH 控制的稳压器激活。

**Listen-only mode** — STB_N 高、EN 低,且 VBAT 与 VIO 存在时选择。INH 保持高。Listen-only 中接收器使能,发射器禁用。

**Sleep mode** — 第二级省电模式。进入方式:(1) 经 Standby,响应 'go-to-sleep' 命令;(2) 经 Standby,VIO 欠压超过 tdet(uv)long;(3) 从除 Off 外的所有模式,VCC 欠压超过 tdet(uv)long。Sleep 模式行为与 Standby 相同,但 INH 高阻,受其控制的稳压器关断,VBAT 电流降至最低。退出条件:(1) 设置 Wake 标志;(2) STB_N 上升沿(若 VIO > Vuvd(VIO));(3) VCC > Vuvd(VCC)、VIO > Vuvd(VIO)、STB_N 高且 'go-to-sleep' 命令未激活。进入 Standby 后若 STB_N 高则进入 Normal 或 Listen-Only。

**Gap-free operation** — 在所有电压电平下保证已定义行为(Figure 4 供给电压范围映射):VBAT 4.5-28 V 工作范围(4-4.5 V 视是否触发欠压而定,28-40 V 特性不保证);VCC/VIO 欠压检测阈值范围等。

### 7.1.2 CAN operating modes(CAN 工作模式)

CAN 状态机支持六种模式:

- **CAN Off**:系统状态机在 Off 模式时,总线引脚与 RXD 高阻。
- **CAN Offline**:系统在 Sleep/Standby 且 Wake 标志未置位时,总线引脚偏置到地;不能收发,低功耗接收器激活监视唤醒模式,RXD 高。
- **CAN Wake**:系统在 Sleep/Standby 且 Wake 标志置位时,RXD 低反映激活的唤醒请求;总线引脚偏置到地。
- **CAN Pass-through**:系统在 Normal/Listen-only 且 VCC 低于 Vuvd(VCC) 时;不能经总线发送数据,总线引脚偏置到地,差分数据经低功耗接收器转换为数字数据输出到 RXD。
- **CAN Active**:系统在 Normal 且 VCC 高于 Vuvd(VCC) 时;可收发数据。TXD 在首次发送前必须至少为高一次。SIC 功能大幅消除拓扑相关反射与阻抗失配。隐性状态总线引脚输出 VCC/2。
- **CAN Listen-only**:系统在 Listen-only 且 VCC 高于 Vuvd(VCC) 时;发射器禁用,差分接收器将数据转换为 RXD 输出,总线引脚偏置到 VCC/2。

### 7.2 Internal flags(内部标志)

四个内部标志用于失效安全回退控制与系统诊断,可由控制器在 VIO 激活时经 ERR_N 轮询。

**Table 5. Accessing internal flags via pin ERR_N(摘要)**

| Internal flag | Flag available on pin ERR_N(1) | Flag status:set(2) | Flag status:not set(2) | Flag cleared |
|---|---|---|---|---|
| Pwon | Listen-only 模式(来自 Standby 或 Sleep) | VBAT 已上升超过 Vuvd(VBAT) | VBAT 未上升超过 Vuvd(VBAT) | on entering Normal mode |
| Wake | Standby 和 Sleep 模式(VIO 与 VBAT 存在) | 检测到远程或本地唤醒,或 Pwon 标志已置位 | 无远程或本地唤醒 | on entering Normal mode 或长 VIO/VCC 欠压 |
| Wake-up source | Normal 模式 | 本地唤醒或 Pwon 标志已置位 | 远程唤醒或无唤醒 | on leaving Normal mode |
| Local failure | Listen-only 模式(来自 Normal) | 出现 TXD dominant failure / TXD-RXD short circuit / Bus dominant failure / Overtemperature | 无上述条件 | Pwon 置位时,或全部本地故障已解决时(进入 Normal / RXD 显性而 TXD 隐性 / 总线显性故障解决且无其它故障) |

(1) ERR_N 为低有效输出:低电平表示标志已置位,高电平表示未置位。(2) 状态自上次清除以来。

**7.2.1 Pwon flag** — VBAT 上电标志;VBAT 从低于 Vuvd(VBAT) 恢复(通常电池断开后)时置位,用于冷启动诊断。进入 Normal 模式清除。

**7.2.2 Wake flag** — 检测到本地或远程唤醒请求时置位。

- **Local wake-up (via WAKE pin)**:WAKE 引脚逻辑电平变化且新电平保持至少 twake 时登记本地唤醒请求;系统状态机可在 Standby 或 Sleep 模式置位 Wake 标志。置位后立即在 ERR_N 与 RXD(需 VIO 与 VBAT 存在)可见。上电时也置位,进入 Normal 清除。
- **Remote wake-up (via the CAN bus)**:检测到总线上的专用唤醒模式(按 ISO 11898-2:2024 Figure 7)时从 Sleep 唤醒到 Standby。唤醒模式由:至少 twake(busdom) 的显性相 → 至少 twake(busrec) 的隐性相 → 至少 twake(busdom) 的显性相组成;短于 twake(busdom)/twake(busrec) 的位被忽略。完整显-隐-显模式须在 tto(wake)bus 内收到,否则内部唤醒逻辑复位,须重传完整模式。RXD/ERR_N 保持高直到唤醒事件触发,然后分别在 tstartup(RXD)/tstartup(ERR_N) 后变低;INH 保持浮空直到唤醒事件触发,然后 tstartup(INH) 后变高。以下事件发生时不在 RXD 上标志唤醒:接收有效唤醒模式期间器件切换至 Normal、完整模式未在 tto(wake)bus 内收到、检测到 VCC 或 VIO 欠压。

**7.2.3 Wake-up source flag** — 唤醒源识别标志;Wake 标志由 WAKE 引脚本地唤醒置位后设置;Normal 模式经 ERR_N 轮询(见 Table 5)。上电时也置位,离开 Normal 模式时清除。

**7.2.4 Local failure flag** — Normal 与 Listen-only 模式中可区分四种本地故障事件,任一都会置位 Local failure 标志:TXD dominant failures、TXD-to-RXD short circuit、Bus dominant failure、Overtemperature。Listen-only 模式(来自 Normal)经 ERR_N 轮询。清除条件见 Table 5。

### 7.3 Local failure events(本地故障事件)

- **TXD dominant failures**:TXD 保持低超过 tto(dom)TXD 则禁用发射器,释放总线到隐性,防止网络锁死;发射器保持禁用直到 Local failure 标志清除;TXD 变高时定时器复位。
- **TXD-to-RXD short circuit**:RXD 与 TXD 短路会锁死总线在显性;检测到后禁用发射器;直到标志清除前保持禁用。
- **Bus dominant failures**:总线短路(至 VBAT、VCC 或 GND)或其它节点故障导致总线持续显性超过 tto(dom)bus 时置位 Local failure 标志;无需禁用发射器;总线回到隐性时标志复位。
- **Overtemperature**:结温超过 Tj(sd) 时禁用 CAN 总线驱动器;直到结温降至 Tj(sd)rel 以下且 Local failure 标志清除前保持禁用。

### 7.4 I/O levels

VIO 引脚应连接到微控制器同电源电压,使 TXD、RXD、STB_N、EN 与 ERR_N 信号电平与微控制器 I/O 匹配,无需额外胶合逻辑。STB_N 与 EN 上的杂散信号由 tfltr(IO) 滤波时间滤除。

### 7.5 WAKE pin

本地唤醒事件由 WAKE 引脚低→高或高→低转换触发(VWAKE 越过唤醒阈值 Vth(wake) 时),转换后新电平须保持至少 tWAKE。低→高转换:VWAKE < Vth(wake)min → VWAKE > Vth(wake)max,然后 VWAKE > Vth(wake)max 持续 t > tWAKE(max),保证唤醒;持续时间 t < tWAKE(min) 的瞬态(L-H-L 或 H-L-H)保证不唤醒。为降低电流,内部偏置电压在 tWAKE 延迟后跟随引脚逻辑状态:WAKE 高电平后接内部上拉至 5 V,低电平后接内部下拉到 GND。不使用本地唤醒时建议将 WAKE 接 VBAT 或 GND 以获最佳 EMI。

### 7.6 Internal biasing of TXD, STB_N and EN input pins

TXD 内部上拉至 VIO,STB_N 与 EN 内部下拉至 GND,确保悬空时的安全已定义状态;上/下拉电阻在所有状态下存在。EN 的下拉仅在 VBAT 存在时激活。

## 8 Limiting values(极限值)

**Table 6. Limiting values**(按 IEC 60134 绝对最大额定值系统;所有电压参考 GND)

| Symbol | Parameter | Conditions | Min | Max | Unit |
|---|---|---|---|---|---|
| Vx | Voltage on pin x(1) | pins VCC, VIO, TXD, STB_N, EN | -0.3 | +6 | V |
| | | pin VBAT,load dump | - | +7(2) | V |
| | | pin VBAT | - | +40(3) | V |
| | | pin INH | -0.3 | VBAT+0.3(4) | V |
| | | pins CANH, CANL, WAKE | -36 | +40 | V |
| | | pins RXD, ERR_N | -0.3 | VIO+0.3(5) | V |
| IO(INH) | output current on pin INH | | -2 | - | mA |
| Ir(VBAT) | reverse current on pin VBAT | 假设 VBAT 低于地电平 | -10 | - | mA |
| V(CANH-CANL) | voltage between pin CANH and pin CANL | | -40 | +40 | V |
| Vtrt | transient voltage | pins VBAT, WAKE, CANH, CANL(6) | | | |
| | | pulse 1 | -100 | - | V |
| | | pulse 2a | - | +75 | V |
| | | pulse 3a | -150 | - | V |
| | | pulse 3b | - | +100 | V |
| VESD | ESD voltage | IEC 61000-4-2 (150 pF,330 Ω)on pins CANH, CANL(7) | -6 | +6 | kV |
| | | pin VBAT(100 nF 电容)/ WAKE(33 kΩ 电阻)(7) | -8 | +8 | kV |
| | | SAE J2962-2:2019 (330 pF,2k)on pins CANH, CANL(8),powered air discharge | -15 | +15 | kV |
| | | SAE J2962-2,powered contact discharge | -8 | +8 | kV |
| | | HBM(9) on any pin(10) | -4 | +4 | kV |
| | | HBM on pins CANH, CANL | -8 | +8 | kV |
| | | CDM(11),corner pins | -750 | +750 | V |
| | | CDM,any other pin | -500 | +500 | V |
| Tvj | virtual junction temperature(12) | | -40 | +150 | °C |
| Tstg | storage temperature(13) | | -55 | +150 | °C |

(1) 器件可在产品寿命内承受至规定值的电压。(2) 6-7 V 之间可承受总计 20 s。(3) 产品寿命内最大 50 小时。(4) 在上述条件下绝对最大 40 V。(5) 见注 1 和 2。(6) 外部测试机构按 IEC TS 62228 4.2.4 验证;标准脉冲参数按 ISO 7637-2。(7) 按 IEC TS 62228 4.3。(8) 按 ISO 10605。(9) 按 AEC-Q100-002。(10) 引脚按参考组(含所有地与电源引脚)施加,模拟应用电路(Figure 10)。(11) 按 AEC-Q100-011。(12) 按 IEC 60747-1;Tvj = Tamb + P × Rth(j-a)。(13) 应用中按 IEC 61360-4;运输存储按 IEC 61760-2。

## 9 Thermal characteristics(热特性)

**Table 7. Thermal characteristics**(JEDEC 2S2P 板自由对流)

| Symbol | Parameter | Conditions(1) | Typ | Unit |
|---|---|---|---|---|
| Rth(j-a) | thermal resistance from junction to ambient | SO14 | 74 | K/W |
| | | HVSON14 | 46 | K/W |
| Rth(j-c) | thermal resistance from junction to case(2) | HVSON14 | 13 | K/W |
| ψj-top | thermal characterization parameter from junction to top of package | HVSON14 | 7 | K/W |

(1) 按 JEDEC JESD51-2/5/7,2s2p 板,2s2p 板带两层内铜层与散热焊盘下过孔阵列。(2) 壳温指封装底部散热片中心。

## 10 Static characteristics(静态特性)

**Table 8. Static characteristics**(Tvj = -40 °C 至 +150 °C;VCC = 4.5-5.5 V;VIO = 2.95-5.5 V;VBAT = 4.5-28 V;RL = 60 Ω,除非另有说明;所有电压相对地;正电流流入 IC。)

**Supply; pin VCC**

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| VCC | supply voltage | | 4.5 | - | 5.5 | V |
| Vuvd | undervoltage detection voltage(2) | | 4 | - | 4.5 | V |
| Vuvhys | undervoltage hysteresis voltage | | 50 | - | - | mV |
| ICC | supply current | Normal mode,dominant;VTXD = 0 V;t < tto(dom)TXD | - | 42 | 70 | mA |
| | | VTXD = 0 V;-3 V < (VCANH = VCANL) < +40 V;总线短路 | - | - | 125 | mA |
| | | Normal mode,recessive;VTXD = VIO | - | 7 | 10 | mA |
| | | Listen-only mode | - | 5 | 8 | mA |
| | | Standby or Sleep mode;Tvj < 85 °C | - | - | 2 | μA |

**I/O level adapter supply; pin VIO**

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| VIO | supply voltage | | 2.95 | - | 5.5 | V |
| Vuvd | undervoltage detection voltage(2) | | 2.65 | - | 2.95 | V |
| Vuvhys | undervoltage hysteresis voltage | | 50 | - | - | mV |
| IIO | supply current | Normal mode,dominant;VTXD = 0 V | - | 90 | 250 | μA |
| | | Normal mode,recessive,VTXD = VIO 或 Listen-only mode | - | - | 3 | μA |
| | | Standby or Sleep mode;Tvj < 85 °C | - | - | 2 | μA |

**Supply; pin VBAT**

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| VBAT | battery supply voltage | | 4.5 | - | 28 | V |
| Vuvd | undervoltage detection voltage(2) | | 4 | - | 4.5 | V |
| IBAT | battery supply current | Normal or Listen-only mode;pin INH left open | - | 80 | 300 | μA |
| | | Normal or Listen-only;INH open;Tvj ≤ 25 °C;VBAT = 14.5 V | - | 80 | 100 | μA |
| | | Standby mode;INH open;VWAKE = VBAT or GND;Tvj < 85 °C | - | 13 | 26 | μA |
| | | Sleep mode;VWAKE = VBAT or GND;Tvj < 85 °C | - | 13 | 26 | μA |

**CAN transmit data input; pin TXD**

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| VIH | HIGH-level input voltage | | 0.7VIO | - | - | V |
| VIL | LOW-level input voltage | | - | - | 0.3VIO | V |
| Vhys(TXD) | hysteresis voltage on pin TXD | | 50 | - | - | mV |
| Rpu | pull-up resistance | | 20 | - | 80 | kΩ |
| Ci | input capacitance | | - | - | 10 | pF |

**CAN receive data output; pin RXD**:IOH(VRXD = VIO - 0.4 V)-10 至 -1 mA;IOL(VRXD = 0.4 V)1 至 10 mA。

**Standby and enable control inputs; pins STB_N and EN**:VIH ≥ 0.7VIO,VIL ≤ 0.3VIO;Vhys ≥ 50 mV;Rpd 下拉 20-80 kΩ;Ci ≤ 10 pF。

**Local failure detection and power-on indication output; pin ERR_N**:IOH(VERR_N = VIO - 0.4 V)-50 至 -4 mA;IOL(VERR_N = 0.4 V)0.1 至 2 mA。

**Local wake-up input; pin WAKE**:Rpu 上拉(VWAKE > Vth(wake)(max) 持续 t > twake(max))100-400 kΩ;Rpd 下拉(VWAKE < Vth(wake)(min))100-400 kΩ;Vth(wake) 唤醒阈值 1.8-2.6 V(Sleep/Standby);Vhys ≥ 90 mV。

**Inhibit output; pin INH**:VH = VBAT - VINH,IINH = -1 mA:0-1 V;IINH = -2 mA:0-2 V;IL 泄漏(Sleep/Off)-2 至 +2 μA;IO(sc) 短路电流(VINH = 0 V)≤ -15 mA。

**Bus lines; pins CANH and CANL**

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| VO(dom) | dominant output voltage | VTXD = 0 V;t < tto(dom)TXD;VCC = 4.75-5.25 V | | | | |
| | | pin CANH;RL = 50-65 Ω | 2.89 | 3.5 | 4.26 | V |
| | | pin CANL;RL = 50-65 Ω | 0.77 | 1.5 | 2.13 | V |
| VTXsym | transmitter voltage symmetry | VTXsym = VCANH + VCANL;CSPLIT = 4.7 nF;fTXD = 250 kHz,1 MHz or 2.5 MHz | 0.9VCC | - | 1.1VCC | V |
| Vcm(step) | common mode voltage step | | -150 | - | +150 | mV |
| Vcm(p-p) | peak-to-peak common mode voltage | | -300 | - | +300 | mV |
| VO(dif) | differential output voltage | dominant;Normal;VTXD = 0 V;t < tto(dom)TXD;VCC = 4.75-5.25 V | | | | |
| | | RL = 50-65 Ω | 1.5 | - | 2.75 | V |
| | | RL = 45-70 Ω | 1.4 | - | 3.3 | V |
| | | RL = 2×240 Ω | 1.5 | - | 5 | V |
| | | recessive;no load;Normal or Listen-only;VTXD = VIO | -50 | - | +50 | mV |
| | | Standby or Sleep mode | -0.2 | - | +0.2 | V |
| VO(rec) | recessive output voltage | Normal or Listen-only;VTXD = VIO;no load | 2 | 2.5 | 3 | V |
| | | Standby or Sleep mode;no load | -0.1 | 0 | +0.1 | V |
| Vth(RX)dif | differential receiver threshold voltage | -12 V ≤ VCANH ≤ +12 V;-12 V ≤ VCANL ≤ +12 V | | | | |
| | | Normal or Listen-only mode | 0.5 | - | 0.9 | V |
| | | Standby or Sleep mode | 0.4 | - | 1.1 | V |
| Vrec(RX) | receiver recessive voltage | Normal or Listen-only | -8 | - | +0.5 | V |
| | | Standby or Sleep | -8 | - | +0.4 | V |
| Vdom(RX) | receiver dominant voltage | Normal or Listen-only | 0.9 | - | 9 | V |
| | | Standby or Sleep | 1.1 | - | 9 | V |
| Vhys(RX)dif | differential receiver hysteresis voltage | Normal or Listen-only | 100 | - | - | mV |
| IO(sc) | short-circuit output current | -15 V ≤ VCANH ≤ +40 V;-15 V ≤ VCANL ≤ +40 V | - | - | 115 | mA |
| IO(sc)rec | recessive short-circuit output current | -27 V ≤ VCANH ≤ +32 V;-27 V ≤ VCANL ≤ +32 V;Normal or Listen-only;VTXD = VIO | -3 | - | +3 | mA |
| IL | leakage current | VCC = VIO = VBAT = 0 V 或经 47 kΩ 短路至 GND;VCANH = VCANL = 5 V | -10 | - | +10 | μA |
| Ri | input resistance | -2 V ≤ VCANL ≤ +7 V;-2 V ≤ VCANH ≤ +7 V;passive recessive | 25 | 40 | 50 | kΩ |
| Ri | input resistance deviation | 0 V ≤ VCANL ≤ +5 V;0 V ≤ VCANH ≤ +5 V;passive recessive | -3 | - | +3 | % |
| Ri(dif) | differential input resistance | -2 V ≤ VCANL ≤ +7 V;-2 V ≤ VCANH ≤ +7 V;passive recessive | 50 | 80 | 100 | kΩ |
| Ci(cm) | common-mode input capacitance | | - | - | 30 | pF |
| Ci(dif) | differential input capacitance | | - | - | 15 | pF |

**Signal Improvement function on CANH or CANL**(+4.75 V ≤ VCC ≤ +5.25 V;see Figure 9)

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| Ri(dom) | dominant phase input resistance | bus dominant | - | - | 30 | Ω |
| Ri(dif)dom | dominant phase differential input resistance | VCC-1.6 V ≤ VCANH ≤ VCC-1.2 V;+1.2 V ≤ VCANL ≤ +1.6 V;Ri(dif)dom = Ri(dom)CANH + Ri(dom)CANL | - | - | 62.5 | Ω |
| Ri(actrec) | active recessive phase input resistance(9) | bus dominant-to-recessive transition | 37.5 | - | 60 | Ω |
| Ri(dif)actrec | active recessive phase differential input resistance(9) | +1.5 V ≤ VCANH ≤ VCC-1.5 V;+1.5 V ≤ VCANL ≤ VCC-1.5 V | 75 | - | 125 | Ω |

**Temperature detection**:Tj(sd) 关断结温 180-200 °C(典型 190 °C);Tj(sd)rel 释放关断结温 175-195 °C(典型 185 °C)。

(注:表注 [2]-[10] 详见原文;参数集 C 与 A/B 说明见动态特性。)

## 11 Dynamic characteristics(动态特性)

**Table 9. Dynamic characteristics**(Tvj = -40 °C 至 +150 °C;VCC = 4.5-5.5 V;VIO = 2.95-5.5 V;VBAT = 4.5-28 V;RL = 60 Ω,除非另有说明)

**CAN timing characteristics according to ISO 11898-2:2024**(see Figure 8 and Figure 11)

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| td(TXDL-RXDL) | delay time from TXD LOW to RXD LOW | Normal mode | - | - | 255 | ns |
| td(TXDH-RXDH) | delay time from TXD HIGH to RXD HIGH | Normal mode | - | - | 255 | ns |

**VCC = 4.75 V to 5.25 V**

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| td(TXD-busdom) | delay time from TXD to bus dominant | Normal mode | - | - | 80 | ns |
| td(TXD-busrec) | delay time from TXD to bus recessive | Normal mode | - | - | 80 | ns |
| td(busdom-RXD) | delay time from bus dominant to RXD | Normal or Listen-Only mode | - | - | 110 | ns |
| td(busrec-RXD) | delay time from bus recessive to RXD | Normal or Listen-Only mode | - | - | 110 | ns |
| td(TXDL-RXDL) | delay time from TXD LOW to RXD LOW | Normal mode | - | - | 190 | ns |
| td(TXDH-RXDH) | delay time from TXD HIGH to RXD HIGH | Normal mode | - | - | 190 | ns |
| td(TXD-buspasrec)start | delay time from TXD to bus passive recessive start | Normal mode(2) | 415 | - | 530 | ns |
| td(TXD-busactrec)start | delay time from TXD to bus active recessive start | Normal mode(2) | 70 | - | 120 | ns |
| td(TXD-busactrec)end | delay time from TXD to bus active recessive end | Normal mode(2) | 355 | - | 480 | ns |

**CAN FD timing characteristics per parameter set C(tbit(TXD) ≥ 125 ns,up to 8 Mbit/s)(4)**

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| tbit(bus) | transmitted recessive bit width deviation,tbit(bus) = tbit(bus) - tbit(TXD) | | -10 | - | +10 | ns |
| trec | receiver timing symmetry,trec = tbit(RXD) - tbit(bus) | | -20 | - | +15 | ns |
| tbit(RXD) | received recessive bit width deviation,tbit(RXD) = tbit(RXD) - tbit(TXD) | | -30 | - | +20 | ns |

**CAN FD timing characteristics(tbit(TXD) ≥ 200 ns,up to 5 Mbit/s)(5)**

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| tbit(bus) | transmitted recessive bit width deviation | | -30 | - | +30 | ns |
| trec | receiver timing symmetry | | -45 | - | +15 | ns |
| tbit(RXD) | received recessive bit width deviation | | -50 | - | +40 | ns |

**Dominant time-out times**(VTXD = 0 V;Normal mode)

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| tto(dom)TXD | TXD dominant time-out time(6) | | 0.8 | - | 9 | ms |
| tto(dom)bus | bus dominant time-out time | VO(dif) > 0.9 V;Normal or Listen-Only mode | 0.8 | - | 9 | ms |

**Bus wake-up times; pins CANH and CANL**(see Figure 6)

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| twake(busdom) | bus dominant wake-up time | Standby or Sleep mode(7) | 0.5 | - | 1.8 | μs |
| twake(busrec) | bus recessive wake-up time | Standby or Sleep mode(7) | 0.5 | - | 1.8 | μs |
| tto(wake)bus | bus wake-up time-out time | Standby or Sleep mode(6) | 0.8 | - | 9 | ms |

**Mode transitions**(see Section 7.1 and Figure 6)

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| tt(moch) | mode change transition time | | - | - | 50 | μs |
| tstartup | start-up time | | - | - | 1.5 | ms |
| tstartup(RXD) | RXD start-up time | after local or remote wake-up detected(8) | 4 | - | 50 | μs |
| tstartup(INH) | INH start-up time | after local or remote wake-up detected;transition from Sleep to Standby(9) | 4 | - | 50 | μs |
| tstartup(ERR_N) | ERR_N start-up time | after local or remote wake-up detected | 4 | - | 50 | μs |
| th(gotosleep) | go-to-sleep hold time | STB_N = LOW and EN = HIGH hold time for entering Sleep mode(10) | 24 | - | - | μs |
| td(moch-ERR_N) | delay time from mode change to ERR_N stable | | - | - | - | - |

**Local wake-up input; pin WAKE**:tWAKE 唤醒时间(响应 WAKE 引脚上升/下降沿;Standby 或 Sleep 模式)20-50 μs(11)。

**IO filter; pins STB_N, EN**:tfltr(IO) I/O 滤波时间 1-5 μs(12)。

**Undervoltage detection**(see Section 7.1.1 and Figure 5)

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| tdet(uv) | undervoltage detection time | on pin VBAT / VCC / VIO | - | - | 30 | μs |
| tdet(uv)long | long undervoltage detection time | on pins VCC and/or VIO | 100 | - | 150 | ms |
| trec(uv) | undervoltage recovery time | on pin VCC / VIO | - | - | 50 | μs |

(注:表注 [1]-[13] 详见原文,涵盖参数集 C 与 A/B 的从属关系、位定时对称性居中说明(AH2002 应用提示)、超时 min/max 保证、RXD/INH 启动时间保证等。)

Figure 8 为符合 ISO 11898-2:2024 的 CAN 收发器时序图;Figure 9 为符合 ISO 11898-2:2024 parameter set C 的显性→被动隐性转换发射器阻抗与定时图(主动隐性相与释放相)。

## 12 Application information(应用信息)

- **Application diagram(Figure 10)**:典型 3.3 V 微控制器应用:VBAT (10)→ INH (7) 控制外部稳压器 on/off;VCC (3) 5 V、VIO (5) 3.3 V;WAKE (9);STB_N (14)/EN (6)/ERR_N (8)/RXD (4)/TXD (1) 连接微控制器端口;CANH (13)/CANL (12) 接 CAN 总线;GND (2)。
- **Application hints**:进一步应用信息见 NXP 应用提示 AH2002 'TJx144x/TJx146x Application Hints'(可向 NXP 索取)。

## 13 Test information(测试信息)

- Figure 11:CAN 收发器时序测试电路(TXD → 收发器 → CANH/CANL → RL 60 Ω/CL 100 pF;RXD 15 pF)。
- Figure 12:收发器驱动对称性测量测试电路(CSPLIT 4.7 nF,RL 2×30 Ω)。
- **Quality information**:本产品按 AEC-Q100 Rev-H 标准认证,适用于汽车应用。

## 14 Package outline(封装外形)

- **SO14(SOT108-1)**:塑料小外形封装,14 引线,体宽 3.9 mm;外形尺寸约 8.55-8.75 × 3.8-4.0 mm,引脚间距 1.27 mm;参考 JEDEC MS-012。
- **HVSON14(SOT1086-2)**:塑料热增强超薄小外形无引线封装,14 端子,体 3 × 4.5 × 0.85 mm;参考 JEDEC MO-229。

## 15-16 Handling and soldering(处理与焊接,摘要)

所有输入/输出引脚在正常处理下受 ESD 保护(按 JESD625-A)。焊接说明:波峰焊与回流焊简介;回流焊峰值温度按 J-STD-020D 分类(表 10/11 SnPb 与无铅工艺);湿敏等级注意事项。详见应用笔记 AN10365。

## 17 Appendix: ISO 11898-2:2024 parameter cross-reference lists(附录:ISO 参数交叉引用)

**Table 12. ISO 11898-2:2024 to NXP data sheet parameter conversion(关键映射)**

| ISO 11898-2:2024 Parameter | Notation | NXP Symbol | NXP Parameter |
|---|---|---|---|
| HS-PMA maximum ratings of VCAN_H, VCAN_L and VDiff | VDiff / VCAN_H / VCAN_L | V(CANH-CANL) / Vx | voltage between pin CANH and CANL / voltage on pin x |
| Recessive output characteristics | VCAN_H / VCAN_L / VDiff | VO(rec) / VO(dif) | recessive output voltage / differential output voltage |
| Dominant output characteristics | VCAN_H / VCAN_L / VDiff | VO(dom) / VO(dif) | dominant output voltage / differential output voltage |
| Maximum HS-PMA driver output current | ICAN_H / ICAN_L | IO(sc) | short-circuit output current |
| Static receiver input characteristics | VDiff | Vth(RX)dif / Vrec(RX) / Vdom(RX) | differential receiver threshold / recessive / dominant voltage |
| Receiver input resistance (matching) | RDIFF_pas_rec / RSE_pas_rec / mR | Ri(dif) / Ri / Ri | differential / input resistance / deviation |
| Maximum leakage currents, unpowered | ICAN_H / ICAN_L | IL | leakage current |
| Driver symmetry | Vsym_vcc | VTXsym | transmitter voltage symmetry |
| Transmit dominant time-out | tdom | tto(dom)TXD | TXD dominant time-out time |
| Loop delay for parameter sets A and B | tLoop | td(TXDH-RXDH) | delay time from TXD HIGH to RXD HIGH |
| Loop delay for parameter set C | tLoop | td(TXDL-RXDL) | delay time from TXD LOW to RXD LOW |
| Propagation delay TXD to bus (set C) | tprop(TXD_BUS) | td(TXD-busdom) / td(TXD-busrec) | delay time from TXD to bus dominant / recessive |
| Propagation delay bus to RXD (set C) | tprop(BUS_RXD) | td(busdom-RXD) / td(busrec-RXD) | delay time from bus dominant / recessive to RXD |
| Transmitted recessive bit width variation | tBit(Bus) | tbit(bus) | transmitted recessive bit width deviation |
| Received recessive bit width variation | tBit(RXD) | tbit(RXD) | received recessive bit width deviation |
| Receiver timing symmetry | tREC | trec | receiver timing symmetry |
| SIC timing and impedance (set C) | RDIFF_act_rec / RSE_act_rec / tact_rec_start / tact_rec_end / tpas_rec_start | Ri(dif)actrec / Ri(actrec) / td(TXD-busactrec)start / td(TXD-busactrec)end / td(TXD-buspasrec)start | active recessive phase 差分/输入电阻;主动隐性相开始/结束;被动隐性相开始 |
| CAN activity filter time, long/short | tFilter | twake(busdom) / twake(busrec) | bus dominant / recessive wake-up time |
| Wake-up time-out | tWake | tto(wake)bus | bus wake-up time-out time |
| Wake-up pattern signaling | tFlag | tstartup(RXD) / tstartup(INH) / tstartup(ERR_N) | 各启动时间 |
| Time-out for bus inactivity | tSilence | tto(silence) | bus silence time-out time |
| Bus bias reaction time | tBias | td(busact-bias) | bus bias reaction time |

(注:部分 NXP 专有参数与 ISO 11898-2:2024 参数等价但符号不同;本转换表允许将 ISO 参数与其 NXP 对应参数交叉引用。)

## 18 Appendix: TJx14(41/42/43/48)x, TJx14(62/63)x, TJF1441 family overview(附录:家族特性总览)

完整 TJx14(41/42/43/48)x、TJx14(62/63)x、TJF1441 家族特性总览表见原文 Table 13(各器件模式、电源、数据率、信号改善、唤醒功能等对比)。

---

## 法律声明(摘要)

NXP B.V. 版权所有。本文档所有信息受法律免责声明约束。产品数据表 Rev. 3.0 — 12 February 2025。© 2025 NXP B.V. All rights reserved。
