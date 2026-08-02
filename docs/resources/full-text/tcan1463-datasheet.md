---
title: TCAN1463-Q1 CAN SIC 收发器(带休眠模式)数据手册(全文查阅)
description: TI TCAN1463-Q1 汽车级信号改善能力 CAN FD 收发器(带休眠模式)数据手册(SLLSFE5C,2020/2022 修订)全文站内版:特性、14 引脚、三电源 VSUP/VCC/VIO、INH/WAKE/INH_MASK/nFAULT 功能、六种工作模式、SWE 定时器、WUP/LWU 唤醒、完整电气/开关特性。
type: 全文查阅
organization: Texas Instruments
year: 2022
tags: [全文查阅, 数据手册]
source: https://www.ti.com/product/TCAN1463-Q1
---

# TCAN1463-Q1 Automotive Signal Improvement Capable CAN FD Transceiver With Sleep Mode(全文查阅)

> **器件**:TCAN1463-Q1(SOT-23-THIN (DYY)、SOIC (D)、VSON (DMT) 封装)
> **文档**:TI Data Sheet SLLSFE5C - MARCH 2020 - REVISED DECEMBER 2022
> **原文 PDF**:[📄 下载原文 PDF](../../files/vendors/TI_TCAN1463-Q1_CAN_SIC_datasheet.pdf)
> **相关资料**:[资源条目页](../_entries/vendors/ti-tcan1463-q1.md)

---

## 1 Features(特性)

- AEC-Q100 (grade 1) qualified for automotive applications
- Functional Safety-Capable:Documentation available to aid in functional safety system design
- Meets the requirements of ISO 11898-2:2016
- Implements Signal Improvement Capability (SIC) as defined in CiA 601-4:Actively improves bus signal by eliminating ringing and enhancing bit symmetry
- Supports classic CAN and CAN FD up to 8 Mbps
- Wide input operational voltage range
- VIO level shifting supports:1.7 V to 5.5 V
- Operating modes:Normal mode;Silent mode;Standby mode;Low-power sleep mode
- High-voltage INH output for system power control
- INH_MASK pin to keep INH disabled during spurious wake-up events
- Local wake-up support via the WAKE pin
- Sleep Wake Error (SWE) timer enables safe transition from standby mode to sleep mode in the event of a system power failure or software fault(Allows for extended power-up time)
- Defined behavior when unpowered:Bus and IO terminals are high impedance (no load to operating bus or application)
- Protection features:
  - ±58-V CAN bus fault tolerant
  - Load dump support on VSUP
  - IEC ESD protection
  - Undervoltage protection
  - Thermal shutdown protection
  - TXD dominant state timeout (TXD DTO)
- Available in a 14-pin leaded (SOT and SOIC) packages,and leadless (VSON) package with wettable flanks for improved automated optical inspection (AOI) capability

## 2 Applications(应用)

- Body electronics and lighting
- Automotive gateway
- Advanced driver assistance systems (ADAS)
- Infotainment and cluster
- Hybrid,electric & powertrain systems
- Personal transport vehicles - Electric bike
- Industrial transportation

## 3 / 5 Description(描述)

The TCAN1463-Q1 is a high-speed Controller Area Network (CAN) transceiver that meets the physical layer requirements of the ISO 11898-2:2016 high-speed CAN specification and the CiA 601-4 SIC specification. The device supports both classical CAN and CAN FD (flexible data rate) data rates up to 8 Megabits per second (Mbps).

The TCAN1463-Q1 reduces signal ringing at the dominant-to-recessive edge and enables higher throughput in complex network topologies. SIC allows the applications to extract the real benefit of CAN FD by operating at 2 Mbps,5 Mbps,or beyond in large networks with multiple unterminated stubs. The device is pin compatible with classical CAN FD transceivers,such as TCAN1043A-Q1 or TCAN1043-Q1 when INH_MASK feature is not used (INH_MASK pin is left floating or connected to GND)。

The TCAN1463-Q1 allows for system-level reductions in battery current consumption by selectively enabling the various power supplies that may be present on a system via the INH output pin. This allows a low-current sleep state in which power is gated to all system components except for the TCAN1463-Q1,while monitoring the CAN bus. When a wake-up event is detected,the TCAN1463-Q1 initiates system start-up by driving INH high.

The TCAN1463-Q1 features an SWE timer that enables a safe transition to Sleep mode after 4 minutes (tINACTIVE) of inactivity in Standby mode. This makes sure the device is transitioned to low-power Sleep mode if the MCU fails to transition the device to Normal mode.

**Package Information**

| PART NUMBER | PACKAGE(1) | BODY SIZE (NOM) |
|---|---|---|
| TCAN1463-Q1 | SOT (DYY) | 4.20 mm × 2.00 mm |
| | SOIC (D) | 8.65 mm × 3.90 mm |
| | VSON (DMT) | 4.50 mm × 3.00 mm |

1. For all available packages,see the orderable addendum at the end of the data sheet。

## 4 Revision History(修订历史)

- Rev * (2021 年 3 月)→ Rev A(2022 年 7 月):数据手册从 Advanced Information 改为 Production data。
- Rev A → Rev B(2022 年 11 月):从 Package Information 表中删除 DYY 封装的 Product Preview 注释。
- Rev B → Rev C(2022 年 12 月):从 Package Information 表中删除 D 封装的 Product Preview 注释;CAN Active 章节中 "The CAN Transceiver blocks its transmitter and receiver" 改为 "blocks its transmitter"。

## 6 Pin Configuration and Functions(引脚配置与功能)

D 与 DYY 封装 14 引脚(顶视):1 TXD,2 GND,3 VCC,4 RXD,5 VIO,6 EN,7 INH,8 nFAULT,9 WAKE,10 VSUP,11 INH_MASK,12 CANL,13 CANH,14 nSTB。

DMT (VSON) 封装 14 引脚(顶视):同左,含热焊盘(散热焊盘连接 PCB 地平面)。

**Table 6-1. Pin Functions**

| NAME | NO. | TYPE(1) | DESCRIPTION |
|---|---|---|---|
| TXD | 1 | I | CAN transmit data input,integrated pull-up |
| GND | 2 | GND | Ground connection |
| VCC | 3 | P | 5 V transceiver supply |
| RXD | 4 | O | CAN receive data output,tri-state when VIO < UVIO |
| VIO | 5 | P | I/O supply voltage |
| EN | 6 | I | Enable input for mode control,integrated pull-down |
| INH | 7 | O | Inhibit pin to control system voltage regulators and supplies,high-voltage |
| nFAULT | 8 | I/O | Fault output,inverted logic |
| WAKE | 9 | I | High-voltage supply from battery |
| VSUP | 10 | P | High-voltage supply from battery |
| INH_MASK | 11 | I | INH_MASK pin used to activate/deactivate INH functionality. Internal pull-down to GND. Can be left floating or connected to GND if INH_MASK functionality is not needed. Do not connect to power supply. |
| CANL | 12 | I/O | Low-level CAN bus input/output line |
| CANH | 13 | I/O | High-level CAN bus input/output line |
| nSTB | 14 | I | Standby mode control input,integrated pull-down |
| Thermal Pad | — | — | Connect the thermal pad to the printed circuit board (PCB) ground plane for thermal relief |

(1) I = input,O = output,P = power,GND = ground。

## 7 Specifications(规格)

### 7.1 Absolute Maximum Ratings(绝对最大额定值)

| | | MIN | MAX | UNIT |
|---|---|---|---|---|
| VSUP | Supply voltage(2) | -0.3 | 45 | V |
| VCC | Supply voltage | -0.3 | 6 | V |
| VIO | Supply voltage I/O level shifter | -0.3 | 6 | V |
| VBUS | CAN bus I/O voltage (CANH, CANL) | -58 | 58 | V |
| VDIFF | CAN bus differential voltage (VDIFF = VCANH - VCANL) | -58 | 58 | V |
| VWAKE | WAKE input voltage | -45 | 45 且 ≤ VSUP+0.3 | V |
| VINH | INH pin voltage | -0.3 | 45 且 ≤ VSUP+0.3 | V |
| VLOGIC | Logic pin voltage | -0.3 | 6 | V |
| IO(LOGIC) | Logic pin output current | | 8 | mA |
| IO(INH) | Inhibit pin output current | | 6 | mA |
| IO(WAKE) | WAKE pin output current | | 3 | mA |
| TJ | Junction temperature | -40 | 165 | °C |
| TSTG | Storage temperature | -65 | 150 | °C |

(1) 超过绝对最大额定值可能造成永久损坏。(2) Able to support load dumps of up to 45 V for 300 ms。

### 7.2 ESD Ratings

| VESD | Electrostatic discharge | Human body model (HBM),per AEC Q100-002(1):VSUP, CANH, CANL,and WAKE with respect to ground,HBM ESD classification level 3B | ±8000 V |
|---|---|---|---|
| | | All pins except VSUP, CANH, CANL,and WAKE,HBM ESD classification level 3A | ±4000 V |
| | | Charged device model (CDM),per AEC Q100-011:All pins,CDM ESD classification level C5 | ±750 V |

(1) AEC Q100-002 indicates that HBM stressing shall be in accordance with the ANSI/ESDA/JEDEC JS-001 specification。

### 7.3 ESD Ratings - IEC Specifications

| VESD | ESD,CANH, CANL,VSUP,and WAKE terminal to GND | Unpowered Contact Discharge per ISO 10605(1) | ±8000 V |
|---|---|---|---|
| | | SAE J2962-2 per ISO 10605,Powered Contact Discharge | ±15000 V |
| | | SAE J2962-2 per ISO 10605,Powered Air discharge | ±15000 V |
| VTRAN | Transient voltage per ISO-7637-2(1):CAN, VSUP,WAKE terminal to GND | Pulse 1 / 2 / 3a / 3b | -100 V / +75 V / -150 V / +100 V |
| | Transient voltage per ISO-7637-3(2) | Direct coupling capacitor "slow transient pulse" with 100 nF coupling capacitor - powered | ±30 V |

(1) IEC 62228-3 结果,测试由 IBEE Zwickau 执行。(2) SAE J2962-2,测试由 OEM 认可的独立第三方执行。

### 7.4 Recommended Operating Conditions(推荐工作条件)

| VSUP | Supply voltage | MIN 4.5 | MAX 40 | UNIT V |
|---|---|---|---|---|
| VIO | I/O supply voltage | 1.7 | 5.5 | V |
| VCC | CAN transceiver supply voltage | 4.5 | 5.5 | V |
| IOH(DO) | Digital output high-level current | -2 | | mA |
| IOL(DO) | Digital output low-level current | | 2 | mA |
| IO(INH) | Inhibit output current | | 4 | mA |
| TJ | Operating junction temperature | -40 | 150 | °C |
| TSDR / TSDF / TSD(HYS) | 热关断温度 / 释放温度 / 迟滞 | 175 / 160 / 10 | | °C |

### 7.5 Thermal Information(热特性)

| THERMAL METRIC(1) | D (SOIC) | DMT (VSON) | DYY (SOT) | UNIT |
|---|---|---|---|---|
| RθJA | Junction-to-ambient thermal resistance | 87.1 | 41.8 | 91.0 | °C/W |
| RθJC(top) | Junction-to-case (top) thermal resistance | 41.8 | 43.7 | 41.7 | °C/W |
| RθJB | Junction-to-board thermal resistance | 43.7 | 8.5 | 25.6 | °C/W |
| ψJT | Junction-to-top characterization parameter | 43.3 | 15.9 | 25.4 | °C/W |
| ψJB | Junction-to-board characterization parameter | N/A | 0.9 | 1.1 | °C/W |
| RθJC(bot) | Junction-to-case (bottom) thermal resistance | N/A | 15.9 | N/A | °C/W |

### 7.6 Power Dissipation Ratings(耗散额定值)

| PARAMETER | TEST CONDITIONS | POWER DISSIPATION |
|---|---|---|
| PD Average power dissipation | VSUP = 14 V,VCC = 5 V,VIO = 5 V,TJ = 27 °C,RL = 60 Ω,nSTB = 5 V,EN = 5 V,CL_RXD = 15 pF。典型 CAN 工作条件,500 kbps,25% 发送(显性)占空比 | 62 mW |
| | VSUP = 14 V,VCC = 5.5 V,VIO = 5.5 V,TJ = 150 °C,RL = 50 Ω,nSTB = 5.5 V,EN = 5.5 V,CL_RXD = 15 pF。典型高负载 CAN 工作条件,1 Mbps,50% 发送(显性)占空比,满载网络 | 135 mW |

### 7.7 Power Supply Characteristics(电源特性)

参数条件:TJ = -40 °C 至 150 °C,典型值在 25 °C、VSUP = 12 V、VIO = 3.3 V、VCC = 5 V、RL = 60 Ω。

| PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| ISUP_NORMAL Supply current,CAN active | Normal mode,silent mode,and go-to-sleep mode | | | 140 | μA |
| ISUP_STBY Supply current,Standby mode | Standby mode(2),CAN autonomous:inactive | | 60 | | μA |
| ISUP_SLEEP Supply current | Sleep mode,CAN autonomous:inactive | 18 | | 30 | μA |
| ISUP_BIAS Supply current | 5.5 V < VSUP ≤ 28 V(1),Additional current when in CAN autonomous:active | | 50 | | μA |
| UVSUP(R) | Undervoltage VSUP threshold rising,Ramp up | 3.85 | | 4.4 | V |
| UVSUP(F) | Undervoltage VSUP threshold falling,Ramp down | 3.5 | | 4.25 | V |
| ICC_NORMAL Supply current Normal mode | CAN active:dominant,TXD = 0 V,RL = 60 Ω,CL = open | | | 60 | mA |
| | TXD = 0 V,RL = 50 Ω,CL = open | | | 70 | mA |
| | Dominant with bus fault,TXD = 0 V,RL = open,CL = open,CANH = -25 V | | | 110 | mA |
| | CAN active:recessive,TXD = 0 V,RL = 50 Ω,CL = open | | | 5 | mA |
| ICC_STBY Supply current | Standby mode,CAN autonomous:inactive,EN = nSTB = 0 V | | | 2 μA(TJ ≤ 85 °C)/ 5 μA(TJ ≤ 150 °C) |
| ICC_SILENT Supply current | Silent and go-to-sleep mode,TXD = nSTB = VIO,RL = 50 Ω,CL = open | | | 2.5 | mA |
| ICC_SLEEP Supply current | Sleep mode,CAN autonomous:inactive,EN = 0 V or VIO,nSTB = 0 V | | | 2 μA(TJ ≤ 85 °C)/ 5 μA(TJ ≤ 150 °C) |
| UVCC(R) / UVCC(F) | Undervoltage VCC threshold rising / falling | 4.1 / 3.5 | | 4.4 / 3.9 | V |
| VHYS(UVCC) | Hysteresis voltage on UVCC | 50 | 250 | 320 | mV |
| IIO_NORMAL I/O supply current | Normal mode,RXD floating,TXD = 0 V | | | 350 | μA |
| | Normal/standby/go-to-sleep,RXD floating,TXD = VIO | | | 5 | μA |
| IIO_SLEEP I/O supply current | Sleep mode,nSTB = 0 V | | | 2.5 μA(TJ ≤ 85 °C)/ 5 μA(TJ ≤ 150 °C) |
| UVIO(R) / UVIO(F) | Under voltage VIO threshold rising / falling | 1.4 / 1 | | 1.65 / 1.25 | V |
| VHYS(UVIO) | Hysteresis voltage on UVIO | 30 | 60 | 160 | mV |

(1) ISUP(BIAS) 由 CAN autonomous inactive 与 CAN autonomous active 模式电流之差计算。(2) 有效唤醒后,CAN 收发器进入 CAN autonomous active 模式,需在 CAN autonomous inactive 模式 ISUP 电流基础上加上 ISUP(BIAS)。

### 7.8 Electrical Characteristics(电气特性)

参数条件:推荐工作条件内,TJ = -40 °C 至 150 °C;典型值在 25 °C、VSUP = 12 V、VIO = 3.3 V、VCC = 5 V、RL = 60 Ω。

**CAN Driver Characteristics(总线偏置激活)**

| PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| VO(D) Dominant output voltage | CANH,TXD = 0 V,50 Ω ≤ RL ≤ 65 Ω,CL = open,RCM = open | 2.75 | | 4.5 | V |
| | CANL | 0.5 | | 2.25 | V |
| VO(R) Recessive output voltage | TXD = VIO,RL = open (no load),RCM = open | 2 | | 3 | V |
| VSYM Driver symmetry (VO(CANH)+VO(CANL))/VCC | nSTB = VIO,RL = 60 Ω,CSPLIT = 4.7 nF,CL = Open,RCM = Open,TXD = 250 kHz,1 MHz,2.5 MHz | 0.9 | | 1.1 | V/V |
| VSYM_DC DC Driver symmetry,VCC - VO(CANH) - VO(CANL) | nSTB = VIO,RL = 60 Ω,CL = open | -400 | | 400 | mV |
| VOD(DOM) Differential output voltage,Dominant | CANH - CANL,nSTB = VIO,TXD = 0 V,50 Ω ≤ RL ≤ 65 Ω,CL = open | 1.5 | | 3 | V |
| | nSTB = VIO,TXD = 0 V,45 Ω ≤ RL ≤ 70 Ω,CL = open | 1.4 | | 3.3 | V |
| | nSTB = VIO,TXD = 0 V,RL = 2×240 Ω,CL = open | 1.5 | | 5 | V |
| VOD(REC) Differential output voltage,Recessive | CANH - CANL,nSTB = VIO,TXD = VIO,RL = open,CL = open | -50 | | 50 | mV |
| VOD(STB) Differential output voltage,Bus biasing inactive | CANH,nSTB = 0 V,TXD = VIO,RL = open,CL = open | -0.1 | | 0.1 | V |
| | CANL | -0.1 | | 0.1 | V |
| | CANH - CANL | -0.2 | | 0.2 | V |
| IOS(DOM) Short-circuit steady-state output current,Dominant | nSTB = VIO,TXD = 0 V,-15 V ≤ V(CANH) ≤ 40 V | -100 | | | mA |
| | nSTB = VIO,TXD = 0 V,-15 V ≤ V(CANL) ≤ 40 V | | | 100 | mA |
| IOS(REC) Short-circuit steady-state output current,Recessive | nSTB = VIO,VBUS = CANH = CANL,-27 V ≤ VBUS ≤ 42 V | -3 | | 3 | mA |
| RID(dom) Differential input resistance in dominant phase | 见 Figure 9-2 | | | 40 | Ω |
| RID(active_rec) Differential input resistance in active recessive drive phase | nSTB = VIO,-12 V ≤ VCM ≤ 12 V | | | 60 | Ω |

**CAN Receiver Characteristics(总线偏置激活)**

| PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| VIT(DOM) Receiver dominant state input voltage range | nSTB = VIO | | | 8 | V |
| VIT(REC) Receiver recessive state input voltage range | nSTB = VIO | | | 0.5 | V |
| VHYS Hysteresis voltage for input threshold | | | | 135 | mV |
| VDIFF(DOM) Receiver dominant state input voltage range,Bus biasing inactive | nSTB = 0 V,-12 V ≤ VCM ≤ 12 V | 1.150 | | 8 | V |
| VDIFF(REC) Receiver recessive state input voltage range,Bus biasing inactive | nSTB = 0 V,-12 V ≤ VCM ≤ 12 V | -3 | | 0.4 | V |
| VCM Common mode range | nSTB = VIO | -12 | | 12 | V |
| IOFF(LKG) Power-off (unpowered) bus input leakage | VSUP = 0 V,CANH = CANL = 5 V,TXD = VCC = VIO | | | 2.5 | μA |
| CI Input capacitance to ground (CANH or CANL) | TXD = VCC = VIO | | | 40 | pF |
| CID Differential input capacitance | TXD = VCC = VIO | | | 20 | pF |
| RID Differential input resistance | -12 V ≤ VCM ≤ 12 V | 30 | | 70 | kΩ |
| RIN Input resistance (CANH or CANL) | V(CANH) = V(CANL) = 5 V,RCM = RL,CL = open | 15 | | 45 | kΩ |
| RIN(M) Input resistance matching [1 - RIN(CANH)/RIN(CANL)] × 100% | TXD = VIO = 5.5 V | -3 | | 3 | % |
| RCBF Valid differential load impedance range for bus fault circuitry | TXD = 0 V,VIO = 5.5 V | 0.7 | | 100 | kΩ |

**TXD / RXD / nSTB / nFAULT / INH_MASK / EN / WAKE / INH Characteristics(各引脚特性摘要)**

- **TXD**:VIH ≥ 0.7 VIO,VIL ≤ 0.3 VIO;IIH(-2.5 至 1 μA)、IIL(-1 至 1 μA);ILKG(OFF) ±1 μA;RPU 上拉电阻至 VIO(40-80 kΩ);CI ≤ 5 pF。
- **RXD**:VOH ≥ 0.7 VIO,VOL ≤ 0.2 VIO;ILKG(OFF) ±1 μA。
- **nSTB**:VIH ≥ 0.7 VIO,VIL ≤ 0.3 VIO;RPD 下拉至 GND(40-80 kΩ)。
- **nFAULT**:VOH ≥ 0.7 VIO,VOL ≤ 0.2 VIO;ILKG(OFF) ±1 μA。
- **INH_MASK**:VIH ≥ 0.7 VIO,VIL ≤ 0.3 VIO;RPD 下拉至 GND(60-80 kΩ)。
- **EN**:VIH ≥ 0.7 VIO,VIL ≤ 0.3 VIO;RPD 下拉至 GND(40-80 kΩ)。
- **WAKE**:VIH ≥ VSUP - 2 V,VIL ≤ VSUP - 3.5 V(Sleep mode);IIH/IIL 最大 ±3 μA。
- **INH**:VH(VSUP - VINH)≤ 0.5/1 V(IINH = -6 mA);ILKG(INH) ±0.5 μA(Sleep mode);RPD 下拉 2.5-5.6 MΩ(Sleep mode,典型 4 MΩ)。

### 7.9 Timing Requirements(定时要求)

| PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| tPWRUP Time required for INH active after VSUP > UVSUP(R) | | | | 340 | μs |
| tUV Undervoltage filter time VCC and VIO(1) | VCC ≤ UVCC or VIO ≤ UVIO | 100 | | 350 | ms |
| tUV(RE-ENABLE) Re-enable time after undervoltage event(1) | | | | 200 | μs |
| tPROP(LOOP1) Total loop delay,recessive to dominant | RL = 60 Ω,CL = 100 pF,CL(RXD) = 15 pF | | 100 | 190 | ns |
| tPROP(LOOP2) Total loop delay,dominant to recessive | 同上 | | 110 | 190 | ns |
| tWK(TIMEOUT) Bus wake-up timeout value(1) | | 0.8 | | 2 | ms |
| tWK(FILTER) Bus time to meet filtered bus requirements for wake-up request(1) | | 0.5 | | 1.8 | μs |
| tSILENCE Timeout for bus inactivity(1) | Timer is reset and restarted,when bus changes from dominant to recessive or vice versa | 0.6 | | 1.2 | s |
| tINACTIVE Standby mode hardware timer for power-up inactivity | | 3 | 4 | 5 | min |
| tBIAS Bus bias reaction time(1) | 显性-隐性-显性序列(每相 6 s)开始至 VSYM ≤ 0.1;nSTB = EN = 0 V,RL = 60 Ω,CSPLIT = 4.7 nF | | | 200 | μs |
| tCBF Bus fault-detection time | 45 Ω ≤ RCM ≤ 70 Ω,CL = open | | | 2.5 | μs |
| tWAKE_HT Hold time for WAKE pin voltage stable after rising or falling edge to recognize LWU | | 5 | | 50 | μs |
| tINH_SLP_STB Time after WUP or LWU event until INH asserted(1) | | | | 100 | μs |
| tINH_MASK Hold time for INH_MASK stable to enable/disable INH function | | | | 50 | μs |
| tMODE1 Mode change time from leaving Sleep to entering Normal or Silent(1) | VCC 与 VIO 越过 UV 阈值起算 | | | 20 | μs |
| tMODE2 Mode change time between normal,silent,standby,and from sleep to standby(1) | | | | 10 | μs |
| tGOTOSLEEP Minimum hold time for transition to sleep mode(1) | EN = H and nSTB = L | 20 | | 50 | μs |

(1) 由设计规定并经台架表征验证。

### 7.10 Switching Characteristics(开关特性)

| PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| tprop(TxD-busdom) Propagation delay,high-to-low TXD edge to bus dominant | RL = 60 Ω,CL = 100 pF,RCM = open | | | 80 | ns |
| tprop(TxD-busrec) Propagation delay,low-to-high TXD edge to bus recessive | 同上 | | | 80 | ns |
| tsk(p) Pulse skew | | | | 3 | ns |
| tR / tF Differential output signal rise / fall time | RL = 60 Ω,CL = 100 pF,RCM = open | | | 25 | ns |
| tTXDDTO Dominant timeout | TXD = 0 V,RL = 60 Ω,CL = open | 1.2 | | 3.8 | ms |
| tprop(busdom-RxD) Propagation delay,bus dominant input to RxD low output | CL(RXD) = 15 pF | | | 110 | ns |
| tprop(busrec-RxD) Propagation delay,bus recessive input to RxD high output | 同上 | | | 110 | ns |

### 7.11 Typical Characteristics(典型特性)

- Figure 7-x:VOD(DOM) 随温度 / VCC 变化曲线;ICC 各模式电流随温度变化曲线;环路延迟随温度变化曲线等(具体曲线坐标数据略,详见原文)。

## 8 Parameter Measurement Information(参数测量信息)

- Figure 8-1:驱动/接收器测试电路(含 RCM 共模电阻)。
- Figure 8-4:驱动器测试电路与测量(tprop(TxD-busdom)/tprop(TxD-busrec)/tR/tF,VOD 0.9 V/0.5 V 阈值)。
- Figure 8-5:接收器测试电路与测量(tprop(busrec-RxD)/tprop(busdom-RxD),0.5 V/0.9 V 阈值)。
- Figure 8-6:发送器与接收器定时行为测试电路(tPROP(LOOP1)/tPROP(LOOP2),TXD 30%/70%,tBIT(BUS)/tBIT(RXD),VDIFF 900 mV/500 mV;5 × tBIT(TXD))。
- Figure 8-7:TXD 显性超时测试电路与测量(tTXDDTO)。
- Figure 8-8:驱动器短路电流测试与测量。
- Figure 8-9:Bias Reaction Time 测量。
- Figure 8-10 / 8-11:INH_MASK 禁用 / 使能 INH 的时序(tINH_MASK、tINH_SLP_STB)。
- Figure 8-12:上电时序(tPWRUP)。

## 9 Detailed Description(详细说明)

### 9.1 Overview(概述)

The TCAN1463-Q1 is a high-speed CAN transceiver that meets the physical layer requirements of the ISO 11898-2:2016 and CiA 601-4 high speed CAN specifications. It is data rate agnostic making it backward compatible for supporting classical CAN applications while also supporting CAN FD networks up to 8 Mbps.

The transceiver has three separate supply inputs,VSUP,VCC,and VIO. By using VIO,the TCAN1463-Q1 can interface directly to a 1.8 V,2.5 V,3.3 V,or 5 V controller without the need for a level shifter. The TCAN1463-Q1 allows for system-level reductions in battery current consumption by selectively enabling the various power supplies that may be present in the system via the INH output pin. This enables a low-current sleep state in which power is gated to all system components except for the TCAN1463-Q1,which remains in a low-power state while monitoring the CAN bus. When a wake-up pattern is detected on the bus or when a local wake up is requested via the WAKE input,the device initiates node start-up by driving INH high.

The TCAN1463-Q1 includes many protection and diagnostic features including undervoltage detection,CAN bus fault detection,SWE timer,battery connection detection,thermal shutdown (TSD),driver dominant timeout (TXD DTO),and bus fault protection up to ±58 V。

**9.1.1 Signal Improvement** — SIC 增强复杂星形拓扑中可实现的最大数据速率,通过最小化信号振铃。显性→隐性边沿是常规 CAN FD 收发器振铃的来源:驱动器输出阻抗升至 ~60 kΩ,反射信号遭遇阻抗失配产生振铃。TCAN1463-Q1 通过 TX-based SIC 解决:持续强力驱动隐性总线直到 tSIC_TX_base,使反射衰减、采样点处隐性位干净;主动隐性相中发射机输出阻抗低(RID(active_rec));此后进入被动隐性相,驱动器高阻。

### 9.2 Functional Block Diagram(功能框图)

含 VSUP (10)/VCC (3)/VIO (5) 三电源、VLDO 稳压、TXD (1)、INH (7)(Sleep 模式下 INH 上有典型 4 MΩ 下拉电阻)、WAKE (9)、nSTB (14)、EN (6)、nFAULT (8)、INH_MASK (11)、RXD (4) 逻辑输出 MUX、Dominant Time Out、SIC Driver、Over Temp、High Speed Receiver、Low Power Receiver、WUP Detect、Under Voltage 检测、CANH (13)/CANL (12)、GND (2)。

### 9.3 Feature Description(功能描述)

**9.3.1 Supply Pins** — 三个独立电源输入:VSUP(电池供电,支持内部稳压器与低功耗 CAN 接收器)、VCC(5 V 收发器供电)、VIO(数字 I/O 电压,1.7 V 至 5.5 V,匹配 CAN FD 控制器 I/O)。

**9.3.2 Digital Inputs and Outputs**

- **TXD**:逻辑输入,参考 VIO;内部偏置到 VIO 电平,引脚悬空时强制隐性。
- **RXD**:逻辑输出,参考 VIO;有效 VIO 存在时逻辑高;上电或唤醒事件时拉低。
- **nFAULT**:逻辑输出,参考 VIO;传输器件状态指示标志;Sleep 模式为高阻以省电。
- **EN**:逻辑输入,参考 VIO,与 nSTB 共同选择模式;内部下拉以防过度功耗与误唤醒。
- **nSTB**:逻辑输入,参考 VIO,与 EN 共同选择模式;内部下拉。
- **INH_MASK**:逻辑输入,参考 VIO;可在 Silent 模式下禁用/使能 INH 功能,用于避免低功耗模式中因伪唤醒事件而给耗电系统块上电。若 INH 控制收发器或其后控制器的供电,则不应使用 INH_MASK。INH_MASK 有下拉电阻,冷启动时强制 INH 为使能;须在 Silent 模式下将 INH_MASK 拉高 t > tINH_MASK 以禁用 INH,器件锁存该值并保持至 VCC/VIO 电源周期与状态转换;VSUP 欠压会丢失锁存值。INH_MASK 状态变化通过 Silent 模式下 nFAULT 拉低报告给系统控制器。
- **GND**:接地引脚,须连接 PCB 地。

**9.3.4 INH Pin** — 高压输出,用于控制外部稳压器。INH 在所有模式都开启,除 Sleep 模式外;Sleep 模式下 INH 关断为高阻,使节点处于最低功耗状态。可加 100 kΩ 负载加速从驱动高到低的转换并防止悬空。该端子是高压逻辑端子而非功率输出,应驱动系统电源管理器件的 EN 端子,不应作为电源开关;不具备反接电池保护,不应连接出模块。

**9.3.5 WAKE Pin** — 高压反向阻断输入,用于本地唤醒(LWU)。双向边沿触发,WAKE 引脚上升沿或下降沿都识别 LWU。未使用时拉至 VSUP 或地,避免寄生唤醒。外部串联电阻 RSERIES ≥ VSUPMAX/IIO(WAKE) = 45 V / 3 mA = 15 kΩ;RBIAS < ((VSUPMAX - VIH)/IIH) - RSERIES < 330 kΩ;推荐 RSERIES < 50 kΩ。LWU 电路在 Sleep 模式有效,Normal 模式关闭。

**9.3.6 CAN Bus Pins** — CANH/CANL 差分总线引脚,内部连接 CAN 收发器与低压唤醒接收器。

**9.3.7 Faults(故障)**

**Table 9-1. TCAN1463-Q1 Transceiver Status Indicator(状态指示标志摘要)**

| EVENT | FLAG NAME | CAUSE | INDICATORS(1) | FLAG IS CLEARED | COMMENT |
|---|---|---|---|---|---|
| Power-up | PWRON | Power up on VSUP and any return of VSUP after it has been below UVSUP | nFAULT = low upon entering silent mode from standby or sleep mode | After a transition to normal mode | 冷启动产生本地唤醒 WAKERQ、WAKESR 与 PWRON 标志 |
| Wake-up Request | WAKERQ(2) | Wake-up event on CAN bus,state transition on WAKE pin,or initial power up | nFAULT = RXD = low after wake-up upon entering standby mode | After a transition to normal mode or VCC < UVCC(F) or VIO < UVIO(F) for t ≥ tUV | 唤醒请求只能从 standby、go-to-sleep 或 sleep 模式设置;重置 UVVCC/UVVIO 定时器 |
| Wake-up Source Recognition(3) | WAKESR | 本地(WAKE 引脚)或远程(CAN 总线)唤醒 | nFAULT = low 表示本地唤醒,nFAULT = high 表示远程唤醒 | After four recessive-to-dominant edges on TXD in normal mode,leaving normal mode,or VCC/VIO UV | 反映第一个唤醒源 |
| INH_MASK Change | INHMASK | INH_MASK value changed | nFAULT = low after entering silent mode | A mode transition into normal,standby,go-to-sleep,or sleep modes | nFAULT 须先为高(无既有故障)才能作为应答 |
| Undervoltage | UVCC / UVIO / UVSUP | VCC < UVCC(F) / VIO < UVIO(F) / VSUP < UVSUP(F) | Not externally indicated | 电源恢复或唤醒请求 | 内部标志 |
| CAN Bus Fault | CBF | 六种总线故障(见 Table 9-2) | nFAULT = low in normal mode only(5) | Upon leaving normal mode,或 normal 模式下四个连续显性→隐性转换无故障 | CAN 驱动器保持使能 |
| Local Faults | TXDCLP | TXD low when CAN active mode is entered | nFAULT = low upon entering silent mode from normal mode | RXD = low & TXD = high 等 | CAN 驱动器禁用直到故障清除 |
| | TXDDTO | TXD dominant time out,dominant (low) signal for t ≥ tTXDDTO | 同上 | 下一显性→隐性转换或进入各模式 | CAN 驱动器禁用,接收器保持有效 |
| | TXDRXD | TXD and RXD pins are shorted together for t ≥ tTXDDTO | 同上 | 下一显性→隐性转换(TXD high & RXD low)或进入各模式 | CAN 驱动器禁用直到清除 |
| | CANDOM | CAN bus dominant fault,when dominant bus signal received for t ≥ tBUSDOM | 同上 | RXD 下一显性→隐性转换或进入各模式 | CAN 驱动器保持使能 |
| | TSD | Thermal shutdown,TJ ≥ TSDR | 同上 | TJ < TSDF 且 RXD = low & TXD = high 或模式转换 | CAN 驱动器禁用直到 TSD 清除 |

(1) VIO 与 VSUP 存在。(2) WAKERQ 清除前阻止进入 go-to-sleep 模式。(3) 反映第一个唤醒源。(4) 标志指示仅在该模式清除前有效。(5) CAN 总线故障标志在 TXD 四个显性→隐性边沿后指示。

**9.3.7.1.1 Power-Up (PWRON Flag)** — 检测到新电池连接时置位,表示冷启动。VSUP < UVSUP(F) 的任何欠压都被视为冷启动。VSUP > UVSUP(R) 时置位 PWRON。通过从 standby/sleep 进入 silent 模式时 nFAULT 拉低指示;进入 normal 模式清除。

**9.3.7.1.2 Wake-Up Request (WAKERQ Flag)** — 可在 standby、go-to-sleep 或 sleep 模式置位;有效 LWU、有效远程唤醒请求或 VSUP 上电时置位。进入 normal 模式或 VCC/VIO 欠压事件清除。设置该标志会清除 UVCC/UVIO 故障检测的 tUV 定时器。

**9.3.7.1.3 Undervoltage Faults** — 所有电源端子(VSUP、VCC、VIO)都有欠压检测;欠压标志为内部标志,不在 nFAULT 上指示。

**9.3.7.1.4 CAN Bus Fault (CBF Flag)** — 可在发送显性信号时检测六种故障条件并拉低 nFAULT 通知控制器(Table 9-2):1 CANH Shorted to VBAT,2 CANH Shorted to VCC,3 CANH Shorted to GND,4 CANL Shorted to VBAT,5 CANL Shorted to VCC,6 CANL Shorted to GND。故障持续四个连续显性→隐性位转换则 nFAULT 指示 CAN 总线故障;CAN 驱动器保持使能。总线故障检测是系统级情形;收发器在 CAN 总线故障期间保持 CAN active 模式,使 ECU 仍可收发。总线故障检测电路可检测 RCBF 范围内的差分电阻负载,时间大于 tCBF。

**9.3.7.1.5/6/7/8 TXDCLP / TXDDTO / TXDRXD / CANDOM 标志** — 见 Table 9-1。

**9.3.8 Local Faults(本地故障)** — normal 与 silent 模式均检测,但仅在 normal → silent 转换时经 nFAULT 指示;其它模式转换清除本地故障标志。

- **TXDCLP**:进入 CAN active 模式前 TXD 被钳位为低,则禁用 CAN 驱动器将总线释放为隐性。进入 normal 模式且 TXD 隐性、或 TXD 隐性且 RXD 显性、或上电时重新激活。故障期间高速接收器保持有效,RXD 镜像总线。
- **TXD DTO**:CAN 驱动器 active 模式中,TXD 显性超过 tTXDDTO 则禁用驱动器释放总线;下一显性→隐性转换重新激活。接收器保持有效。最小数据率 = 11 bits/tTXDDTO = 11/1.2 ms = 9.2 kbps。
- **Thermal Shutdown (TSD)**:结温超过关断阈值则关闭 CAN 驱动器;总线端子偏置为隐性;结温降至 TSDF 以下清除;迟滞防止振荡;故障经 nFAULT 指示。
- **Undervoltage Lockout (UVLO)**:VSUP/VIO/VCC 欠压进入保护状态,总线引脚对总线无负载。VSUP 欠压 → CAN off 状态;VCC 欠压 → normal/silent 模式但 CAN 收发器进入 CAN autonomous active 状态(有 VIO 时 RXD 保持高);欠压持续超过 tUV → sleep 模式;VIO 欠压 → standby 模式,超过 tUV → sleep。欠压清除后约 200 μs 恢复正常。
- **Unpowered Devices**:未上电时总线与逻辑引脚低漏电,对总线/电路无负载。
- **Floating Terminals**:关键引脚内部上/下拉确保已知行为(Table 9-3):TXD 弱上拉至 VIO;EN、nSTB 弱下拉至 GND;INH_MASK 弱下拉至 GND(60 kΩ)。这些内部偏置是失效保护,不应作为设计依赖;使用开漏输出 CAN FD 控制器时,须选择合适的外部上拉保证位定时。
- **CAN Bus Short-Circuit Current Limiting**:显性/隐性态电流限制 + TXD DTO 防止系统故障时长期显性短路电流。平均短路电流按占空比加权计算:**IOS(AVG) = %Transmit × [(%REC_Bits × IOS(SS)_REC) + (%DOM_Bits × IOS(SS)_DOM)] + [%Receive × IOS(SS)_REC]**。选择端接电阻与共模扼流圈时应考虑平均额定功率。

### 9.4 Device Functional Modes(器件工作模式)

TCAN1463-Q1 有六种工作模式:normal、standby、silent、go-to-sleep、sleep、off。通过 nSTB 与 EN 引脚结合电源条件、温度条件与唤醒事件控制。

**状态机要点(Figure 9-6):**

- Normal Mode:(EN = low 且 nSTB = low)或 VIO < UVIO 时进入;CAN bus bias active,INH:VSUP level,SWE timer inactive,INH_MASK Input:Ignored。
- Silent Mode:EN = high 且 nSTB = high(且 VIO > UVIO);CAN bus bias active,INH:VSUP level,SWE timer inactive/active,INH_MASK Input:Disable/Enables INH。
- Standby Mode:EN = low 且 nSTB = high;CAN bus bias autonomous,WAKE sources:WUP & LWU,INH:VSUP level,SWE timer active,INH_MASK Input:Ignored。
- Go-To-Sleep Mode:EN = high 且 nSTB = low;CAN bus bias autonomous,WAKE sources:WUP & LWU,INH:VSUP level,SWE timer inactive。
- Sleep Mode:(EN = low 且 t < tGOTOSLEEP)或 WUP/LWU 后;CAN bus bias autonomous,EN:x,WAKE sources:WUP & LWU,INH:High impedance,nFAULT:High impedance,SWE timer inactive。VCC 或 VIO 低于 UV 阈值持续 tUV 时也从任意模式进入。
- Power Off:VSUP < UVVSUP(F);CAN:High impedance,INH:High impedance,RXD:High impedance。

**状态机注释:**
1. Sleep 模式下 EN 可高可低,但因内部下拉,悬空或外部拉低功耗最低。
2. 上电时 VCC/VIO 欠压定时器禁用,允许更长上电时间(至 tINACTIVE);VCC/VIO 须高于 UVCC(R)/UVIO(R) 才启用 tUV 定时器。
3. SWE 定时器在进入 Standby 时启动,Normal 时停止并复位;从 Standby 进 Silent 不停表,须在 SWE 到期前进入 Normal;从 Normal 进 Silent 则 Silent 中 SWE 不激活。
4. 从 Go-To-Sleep 或 UVCC/UVIO 事件进入 Sleep 后,须 nSTB 上升沿才能进入 Normal 或 Silent(EN 高 → Normal,EN 低 → Silent);VIO 须高于 UVIO(R)。
5. 因 SWE 超时进入 Sleep 时,须额外条件:进 Normal 需 nSTB 高且 EN 上升沿;进 Silent 需 nSTB 高且 EN 下降沿。若进 Sleep 时 nSTB 已高,须先在 nSTB 低时对 EN 进行一次转换(见 Figure 9-7)。VIO 须高于 UVIO(R)。
6. 器件仅在 Silent 模式识别 INH_MASK 状态变化,锁存该值并在模式转换间保持;仅 UVSUP 事件丢失锁存值。其余模式忽略 INH_MASK。

**Table 9-4. Mode Overview(模式总览)**

| MODE | VCC and VIO | VSUP | EN | nSTB | WAKERQ FLAG | DRIVER | RECEIVER | RXD | INH |
|---|---|---|---|---|---|---|---|---|---|
| Normal | > UVCC 且 > UVIO | > UVSUP | X | X | X | Enabled | Enabled | Mirrors bus state | On |
| Silent | > UVCC 且 > UVIO | > UVSUP | High | High | X | Disabled | Enabled | Mirrors bus state | On |
| | > UVCC 且 > UVIO | > UVSUP | Low | High | X | Disabled | Enabled | Low signals wake-up | On |
| Standby | > UVCC 且 > UVIO | > UVSUP | High | Low | Set | Disabled | Low power bus monitor enabled | High or high impedance (no VIO) | On(2) |
| | > UVCC 且 < UVIO | > UVSUP | Low | Low | X | Disabled | Low power bus monitor enabled | | On(2) |
| Go-to-sleep(1) | > UVCC 且 > UVIO | > UVSUP | High | Low | Cleared | Disabled | Low power bus monitor enabled | | |
| Sleep(3) / Protected | > UVCC 且 > UVIO;或 < UVCC/<UVIO | > UVSUP | X | X | X | Disabled | Low power bus monitor enabled | High or high impedance (no VIO) | High impedance |
| | X | < UVSUP | X | X | X | Disabled | Disabled | High impedance | High impedance |

(1) Go-to-sleep:EN = H,nSTB = L 的过渡模式,直至 tGOTOSLEEP 定时器到期。(2) INH 在 tGOTOSLEEP 定时器到期后转为高阻。(3) go-to-sleep → sleep 在 tGOTOSLEEP 到期后。

**9.4.1.1 Normal Mode** — CAN 驱动与接收器完全工作,双向通信;进入时清除 WAKERQ 与 PWRON;SWE 定时器停止并复位。

**9.4.1.2 Silent Mode** — 监听模式(只接收):CAN 驱动器禁用,接收器完全工作,RXD 输出总线信号;Silent 模式中 PWRON 与本地故障标志经 nFAULT 指示;从 standby 进入 silent 时 SWE 定时器不停表,须在到期前进入 normal,否则转 sleep。

**9.4.1.3 Standby Mode** — 低功耗模式:驱动与接收器禁用;INH 开启允许系统恢复。Standby 期间唤醒请求(WAKERQ)以 RXD 拉低指示;唤醒源在返回 normal 后经 nFAULT 识别。SWE(Sleep Wake Error)定时器使能:系统控制器须在到期前将收发器配置到 normal 模式,否则 tINACTIVE 后自动转至最低功耗 sleep 模式。

**9.4.1.4 Go-To-Sleep Mode** — 过渡模式:驱动与接收器禁用,INH 保持有效以给 VIO 控制器提供使能;保持 t ≥ tGOTOSLEEP 则转 sleep 且 INH 关断为高阻。唤醒事件持续时保持 standby,直到进入 normal 清除待处理唤醒事件。

**9.4.1.5 Sleep Mode** — 最低功耗模式:CAN 发射器与主接收器关断,不能收发数据;低功耗接收器监视总线以验证 WUP,WAKE 监视电路监视 WAKE 端子状态变化以检测 LWU。CAN autonomous inactive 时 ISUP 电流最小。INH 关断使受控电源关闭。退出条件:有效 WUP 经 CAN 总线引脚、本地 WAKE(LWU)事件、或 nSTB 低→高转换。因 SWE 超时进入 Sleep 时退出需额外 EN/nSTB 序列(见状态机注释 5)。

**9.4.1.5.1 Remote Wake Request via Wake-Up Pattern (WUP)** — 低功耗唤醒接收器使用 ISO 11898-2:2016 定义的多重滤波显性唤醒模式(WUP):滤波显性 → 滤波隐性 → 滤波显性。每个状态须持续 ≥ tWK(FILTER)。小于 tWK(FILTER) 最小值的状态绝不触发;介于最小与最大之间可能触发;大于最大值必定触发。模式与 tWK(FILTER) 防止噪声与总线卡显性造成伪唤醒,同时任何有效 CAN/CAN FD 消息都能发起唤醒。tWK(FILTER) 选取在短/长滤波范围的最小/最大值之间,使 500 kbps 的单个位时间或 1 Mbps 的两个背靠背位时间在任一总线状态触发滤波。tWK(TIMEOUT) 提供额外鲁棒性:整个 WUP 须在该超时内收到,否则内部逻辑复位,收发器保持 sleep。tWK(TIMEOUT) 到期时若总线为显性,下一个 WUP 模式须以至少 tWK(FILTER) 的隐性分隔。

**9.4.1.5.2 Local Wake-Up (LWU) via WAKE Input Terminal** — WAKE 端子是双向高压反电池保护输入,用于本地唤醒请求,低→高或高→低转换均触发(双向输入阈值)。可接 VSUP 或地开关。未使用时拉至 VSUP 或地。LWU 电路在 sleep 模式有效;WAKE 电路在 normal 模式关闭。

**9.4.2 CAN Transceiver(收发器子状态机)**

支持 ISO 11898-2:2016 自主总线偏置方案,在 CAN active、CAN autonomous active、CAN autonomous inactive 之间切换以降低 RF 发射。四个收发器子状态:

- **CAN Off**:VSUP < UVSUPF 时进入;总线真正浮空,对总线无负载并防止电池/地丢失时的反向电流。
- **CAN Autonomous: Inactive / Active**:standby/go-to-sleep/sleep 模式中偏置电路可为 inactive(总线偏置到 GND)或 active(远程 WUP 发生后偏置到 2.5 V,收发器进入 autonomous active)。控制器未在 tSILENCE 前转回 normal 则回到 inactive。从 normal/silent 转 standby/go-to-sleep/sleep 时,若总线在模式转换前 inactive t < tSILENCE 则进入 autonomous active,否则 inactive;VCC < UVCC(F) 或 VIO < UVIO(F) 也切换。
- **CAN Active**:normal 或 silent 模式下;normal 中驱动与接收器完全工作,silent 中驱动关闭接收器工作。CAN 偏置电压来自 VCC,保持 VCC/2。进入 CAN active 后若 TXD 在离开 standby 前已被拉低,则阻止发送器(TXDCLP 保护)。

**Table 9-5. Driver Function Table**:Normal/Silent/Standby/Sleep 模式中,TXD Low → CANH High/CANL Low(Dominant);TXD High or Open → 高阻/自主偏置;Silent/Standby/Sleep 模式中 x → 高阻 + 自主偏置。

**Table 9-6. Receiver Function Table**:

| DEVICE MODE | VID = VCANH - VCANL | BUS STATE | RXD TERMINAL |
|---|---|---|---|
| Normal / Silent / Standby / Sleep / Go-to-sleep(1) | VID ≥ 0.9 V | Dominant | Low |
| | 0.5 V < VID < 0.9 V | Indeterminate | Indeterminate |
| | VID ≤ 0.5 V | Recessive | High |
| | Open (VID ≈ 0 V) | Open | High |
| Standby / Sleep(低功耗接收) | VID ≥ 1.15 V | Dominant | High |
| | 0.4 V < VID < 1.15 V | Indeterminate | Low if wake-up event persists |
| | VID ≤ 0.4 V | Recessive | |
| | Open (VID ≈ 0 V) | Open | Tri-state if VIO or VSUP are not present |

(1) Low power wake-up receiver is active。

**CAN Bus States(总线状态)** — 显性/隐性两种逻辑状态。显性:总线差分驱动,TXD/RXD 逻辑低;隐性:经接收器高阻内部输入电阻(RIN)偏置到收发器供电电压一半,TXD/RXD 逻辑高。仲裁时显性覆盖隐性;多个节点同时发送显性位时总线差分电压大于单驱动。低功耗 standby/sleep 模式提供第三总线状态:总线 inactive 超过 tSILENCE 后,总线引脚经接收器高阻内部电阻偏置到地。

## 10 Application Information(应用信息)

> 注:以下应用信息不属于 TI 器件规格的一部分;客户负责确定元件适用性并验证测试设计。

- **典型应用(Figure 10-1)**:单个 5-V 稳压器可同时驱动 VCC 与 VIO,或独立 5-V/3.3-V 稳压器分别驱动;INH 控制系统电源。
- **使用 INH_MASK 的应用(Figure 10-2)**:INH 控制耗电系统块的电源,VREG EN 输入由 INH 驱动,INH_MASK 由 MCU GPIO 控制。
- **Bus Loading, Length and Number of Nodes**:典型 40 m 总线 / 0.3 m 桩线;高输入阻抗收发器(如 TCAN1463-Q1)支持更多节点。差分输入电阻 RID 最小 50 kΩ;100 个 TCAN1463-Q1 并联等效 500 Ω 差分负载与 60 Ω 端接并联约 54 Ω,理论上支持超过 100 个收发器;实际受信号损耗、寄生负载、时序等限制。CANopen 指南允许 1 km 网络(调整端接、线缆、<64 节点、显著降低速率)。
- **CAN Termination**:每端单个 120 Ω,或分裂端接(Figure 10-3)改善共模噪声滤波与 EMC。
- **Power Supply Recommendations**:三个电源轨 VSUP(VBAT)、VCC(4.5-5.5 V)、VIO(1.7-5.5 V);每个电源引脚尽量近放置 100 nF 去耦电容。
- **Layout Guidelines**:保护与滤波电路靠近总线连接器;TVS(D1)、可选总线滤波电容(C6/C7)、CANH/CANL 上串共模扼流圈(CMC);信号路径方向设计保护元件;电源与地平面低电感;至少两个过孔;去耦/体电容靠近 VCC/VIO/VSUP;分裂端接 R3/R4 + C5 中心抽头接地;INH (7) 可加 100 kΩ 到地;WAKE (9) 配置 C8 (22 nF) 到地、R5 (33 kΩ)、R6 (3 kΩ)。

## 11 Device and Documentation Support / 12 Mechanical, Packaging, and Orderable Information

**可订购料号(PACKAGE OPTION ADDENDUM 摘要):**

| Orderable part number | Package \| Pins | Package qty \| Carrier | MSL rating/Peak reflow | Op temp (°C) | Part marking |
|---|---|---|---|---|---|
| TCAN1463DMTRQ1 | VSON (DMT) \| 14 | 3000 \| LARGE T&R | Level-2-260C-1 YEAR | -40 to 125 | 1463 |
| TCAN1463DRQ1 | SOIC (D) \| 14 | 2500 \| LARGE T&R | Level-1-260C-UNLIM | -40 to 125 | 1463 |
| TCAN1463DYYRQ1 | SOT-23-THIN (DYY) \| 14 | 3000 \| LARGE T&R | Level-1-260C-UNLIM | -40 to 125 | 1463 |

封装大纲:
- **DYY0014A**:SOT-23-THIN,1.1 mm max height;外形 4.1-4.3 × 1.9-2.1 mm,引脚间距 0.5 mm;参考 JEDEC MO-345 变体 AB。
- **D0014A**:SOIC,1.75 mm max height;外形 8.55-8.75 × 3.8-4.0 mm,引脚间距 1.27 mm。
- **DMT0014A**:VSON,无引线封装,含 PCB 布局图与钢网设计。
- 带卷与盒尺寸、焊盘材料信息详见原文。

---

## 附录:重要声明(IMPORTANT NOTICE AND DISCLAIMER)

TI 以"按原样"提供技术与可靠性数据、设计资源、应用或其它设计建议、web 工具、安全信息等,并否认所有明示或暗示的保证。这些资源面向使用 TI 产品进行设计的资深开发者;用户对(1)选择合适 TI 产品、(2)设计、验证、测试应用、(3)满足适用标准及安全、安保、法规要求负全部责任。这些资源如有变更恕不另行通知;TI 仅授权将这些资源用于开发使用所描述 TI 产品的应用,禁止其它复制与展示。TI 产品受 TI 销售条款等适用条款约束。TI 反对并拒绝用户提出的任何附加或不同条款。Copyright © 2022,Texas Instruments Incorporated。
