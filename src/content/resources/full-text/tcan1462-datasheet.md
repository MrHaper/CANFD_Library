---
title: TCAN1462-Q1 CAN SIC 收发器数据手册(全文查阅)
description: TI TCAN1462-Q1 汽车级故障保护 CAN FD 收发器(带信号改善能力 SIC 与待机模式)数据手册(SLLSFF2B,2022/2024 修订)全文站内版:特性、引脚、完整电气/开关特性、SIC 工作原理、工作模式、应用设计。
type: 全文查阅
organization: Texas Instruments
year: 2024
tags: [全文查阅, 数据手册]
source: https://www.ti.com/product/TCAN1462-Q1
---

# TCAN1462-Q1 Automotive Fault-Protected CAN FD Transceiver with Signal Improvement Capability (SIC) and Standby Mode(全文查阅)

> **器件**:TCAN1462-Q1 / TCAN1462V-Q1(SOT-23 (DDF)、VSON (DRB)、SOIC (D) 封装)
> **文档**:TI Data Sheet SLLSFF2B - FEBRUARY 2022 - REVISED OCTOBER 2024
> **原文 PDF**:[📄 下载原文 PDF](../../files/vendors/TI_TCAN1462-Q1_CAN_SIC_datasheet.pdf)
> **相关资料**:[资源条目页](../_entries/vendors/ti-tcan1462-q1.md)、[SLLA581 白皮书](slla581-white-paper.md)

---

## 1 Features(特性)

- AEC Q100 (Grade 1):Qualified for automotive applications
- Functional Safety-Capable:Documentation available to aid functional safety system design
- Meets the requirements of ISO 11898-2:2016 and CiA 601-4 standards
- Classical CAN and CAN FD up to 8 Mbps
  - Actively improves the bus signal by reducing ringing effects in complex topologies
  - Backward compatible for use in classic CAN networks
- VIO level shifting supports:1.7V to 5.5V
- Operating Modes:Normal mode;Low-power standby mode supporting remote wake-up request
- Passive behavior when unpowered:Bus and logic terminals are high impedance (no load to operating bus or application);Hot plug capable (power up or down glitch free operation on bus and RXD output);Defined device behavior with floating logic pins and in undervoltage supply conditions
- Protection features:
  - IEC ESD protection on bus pins
  - ±58 V CAN bus fault tolerant
  - Undervoltage protection on VCC and VIO (V variants only) supply terminals
  - TXD dominant state timeout (TXD DTO)
  - Thermal shutdown protection (TSD)
- Available in SOIC (8),small footprint SOT-23 (8) and leadless 3mm × 3mm VSON (8) package with wettable flanks for improved automated optical inspection (AOI) capability

## 2 Applications(应用)

- Automotive gateway
- Advanced driver assistance system (ADAS)
- Body electronics and lighting
- Hybrid, electric & powertrain systems
- Automotive infotainment & cluster

## 3 Description(描述)

The TCAN1462-Q1 is a high speed Controller Area Network (CAN) transceiver that meets the physical layer requirements of the ISO 11898-2:2016 high speed CAN specification and the CiA 601-4 Signal Improvement Capability (SIC) specification. The devices reduce signal ringing at dominant-to-recessive edge and enable higher throughput in complex network topologies. Signal improvement capability allows the applications to extract real benefit of CAN FD (flexible data rate) by operating at 2 Mbps, or operating at 5 Mbps or higher in large networks with multiple unterminated stubs.

The device meets the timing specifications mandated by CiA 601-4; thus, have much tighter bit timing symmetry compared to a regular CAN FD transceivers. This provides larger timing window to sample the correct bit and enables error-free communication in large complex star networks where ringing and bit distortion are inherent.

These devices are pin-compatible to 8-pin CAN FD transceivers, such as TCAN1044A-Q1 or TCAN1042-Q1.

The TCAN1462-Q1 with suffix 'V' includes internal logic level translation via the VIO logic supply terminal to allow for interfacing directly to 1.8V, 2.5V, or 3.3V controllers. The transceivers support low power standby mode which allows remote wake-up via CAN bus compliant with ISO 11898-2:2016 defined wake-up pattern (WUP). The device family also includes many protection features such as undervoltage detection, thermal shutdown (TSD), driver dominant timeout (TXD DTO), and ±58V bus fault protection.

**Package Information**

| PART NUMBER | PACKAGE(1) | PACKAGE SIZE(2) |
|---|---|---|
| TCAN1462-Q1 | SOT-23 (DDF) | 2.9mm × 2.8mm |
| | VSON (DRB) | 3mm × 3 mm |
| | SOIC (D) | 4.9mm × 6mm |

(1) For all available packages, see Section 12。(2) The package size (length × width) is a nominal value and includes pins, where applicable。

## 4 Device Comparison Table(器件对比表)

| Device Number | Bus Fault Protection | Low voltage I/O Logic Support on Pin 5 | Pin 8 Mode Selection |
|---|---|---|---|
| TCAN1462-Q1 | ±58 V | No | Low Power Standby Mode with Remote Wake |
| TCAN1462V-Q1 | ±58 V | Yes | |

## 5 Pin Configurations and Functions(引脚配置与功能)

SOIC (D) 与 SOT-23 (DDF) 8 引脚(顶视):1 TXD,2 GND,3 VCC,4 RXD,5 NC/VIO,6 CANL,7 CANH,8 STB。

VSON (DRB) 8 引脚(顶视):1 TXD,2 GND(热焊盘),3 VCC,4 RXD,5 NC/VIO,6 CANL,7 CANH,8 STB。

**Table 5-1. Pin Functions**

| NAME | NO. | TYPE | DESCRIPTION |
|---|---|---|---|
| TXD | 1 | Digital Input | CAN transmit data input, integrated pull-up |
| GND | 2 | GND | Ground connection |
| VCC | 3 | Supply | 5 V supply voltage |
| RXD | 4 | Digital Output | CAN receive data output, tristate when powered off |
| VIO | 5 | Supply | Logic supply voltage |
| NC | — | No Connect (not internally connected);Devices without VIO |
| CANL | 6 | Bus IO | Low-level CAN bus input/output line |
| CANH | 7 | Bus IO | High-level CAN bus input/output line |
| STB | 8 | Digital Input | Standby mode control input, integrated pull-up |
| Thermal Pad (VSON only) | — | Electrically connected to GND,connect the thermal pad to the PCB ground plane for thermal relief |

## 6 Specifications(规格)

### 6.1 Absolute Maximum Ratings(绝对最大额定值)

| | | MIN | MAX | UNIT |
|---|---|---|---|---|
| VCC | Supply voltage | -0.3 | 6 | V |
| VIO | Supply voltage IO level shifter (Devices with the "V" suffix) | -0.3 | 6 | V |
| VBUS | CAN bus IO voltage range on CANH and CANL | -58 | 58 | V |
| VDIFF | Max differential voltage between CANH and CANL;VDIFF = (CANH - CANL) | -58 | 58 | V |
| VLogic_Input | Logic pin input voltage (TXD, STB) | -45 | 45 | V |
| VRXD | Logic output voltage range (RXD) | -0.3 | 6 | V |
| IO(RXD) | RXD output current | -8 | 8 | mA |
| TJ | Junction temperature | -40 | 165 | °C |
| TSTG | Storage temperature | -65 | 165 | °C |

(1) Operation outside the Absolute Maximum Ratings may cause permanent device damage.(2) All voltage values, except differential I/O bus voltages, are with respect to ground terminal。

### 6.2 ESD Ratings

| VESD | Electrostatic discharge | Human-body model (HBM),per AEC Q100-002(1),HBM classification level 3A for all pins | ±4000 V |
|---|---|---|---|
| | | HBM classification level 3B for global pins CANH and CANL | ±10000 V |
| | | Charged-device model (CDM),per AEC Q100-011,CDM classification level C5 for all pins with respect to GND | ±750 V |

(1) AEC Q100-002 indicates that HBM stressing shall be in accordance with the ANSI/ESDA/JEDEC JS-001 specification。

### 6.3 ESD Ratings, IEC Transients

| VESD | System level ESD,CAN bus terminals (CANH, CANL) to GND | SAE J2962-2 per ISO 10605,Powered contact discharge | ±8000 V |
|---|---|---|---|
| | | SAE J2962-2 per ISO 10605,Powered air discharge | ±15000 V |
| | | IEC 62228-3 per ISO 10605 | ±8000 V |
| VTran | ISO 7637-2 Transient immunity(1) | Pulse 1 / 2a / 3a / 3b | -100 V / +75 V / -150 V / +100 V |
| | Direct capacitor coupling,SAE J2962-2 per ISO 7637-3(2) | DCC slow transient pulse | ±30 V |

(1) Tested according to IEC 62228-3:2019 CAN Transceivers,Section 6.3;standard pulses parameters defined in ISO 7637-2 (2011)。(2) Tested according to SAE J2962-2。

### 6.4 Recommended Operating Conditions(推荐工作条件)

| VCC | Supply voltage | MIN 4.5 | NOM 5 | MAX 5.5 | UNIT V |
|---|---|---|---|---|---|
| VIO | Supply voltage for IO level shifter (Devices with VIO) | 1.7 | | 5.5 | V |
| IOH(RXD) | RXD terminal high-level output current | -1.5 | | | mA |
| IOL(RXD) | RXD terminal low-level output current | | | 1.5 | mA |
| TJ | Junction temperature | -40 | | 150 | °C |

### 6.5 Thermal Characteristics(热特性)

| THERMAL METRIC(1) | D (SOIC) | DRB (VSON) | DDF (SOT) | UNIT |
|---|---|---|---|---|
| RθJA | Junction-to-ambient thermal resistance | 57.8 | 52.8 | 58.9 | °C/W |
| RθJC(top) | Junction-to-case (top) thermal resistance | 64.2 | 115.3 | 25.2 | °C/W |
| RθJB | Junction-to-board thermal resistance | 13.1 | 56.2 | 1.8 | °C/W |
| ψJT | Junction-to-top characterization parameter | 63.3 | 38 | 25.2 | °C/W |
| ψJB | Junction-to-board characterization parameter | - | 1.8 | 9.3 | °C/W |
| RθJC(bot) | Junction-to-case (bottom) thermal resistance | - | 37.7 | - | °C/W |

(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application report。

### 6.6 Supply Characteristics(电源特性)

参数在推荐工作条件下有效,环境温度 -40 ≤ TJ ≤ 150(典型值 VCC = 5 V,VIO = 3.3 V,环境 27 °C),除非另有说明。

| PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| ICC supply current normal mode,Dominant | TXD = 0 V,STB = 0 V,RL = 60 Ω,CL = open | | 45 | 70 | mA |
| | TXD = 0 V,STB = 0 V,RL = 50 Ω,CL = open | | 49 | 80 | mA |
| Recessive | TXD = VIO,STB = 0 V,RL = 50 Ω,CL = open | | 4.5 | 8 | mA |
| Dominant with bus fault | TXD = 0 V,STB = 0 V,CANH = CANL = ±25 V,RL = open,CL = open | | | 130 | mA |
| Supply current standby mode (devices with VIO) | TXD = STB = VIO,RL = 50 Ω,CL = open | 0.2 | | 2 μA(Tj ≤ 85 °C)/ 5 μA(Tj ≤ 125 °C)/ 14 μA(Tj ≤ 150 °C) |
| Supply current standby mode (devices without VIO) | TXD = STB = VCC,RL = 50 Ω,CL = open | | | 16 μA(Tj ≤ 125 °C)/ 21 μA(Tj ≤ 150 °C) |
| IIO IO supply current normal mode,Dominant | TXD = 0 V,STB = 0 V,RL = 60 Ω,RXD floating | | 125 | 300 | μA |
| Recessive | TXD = VIO,STB = 0 V,RL = 60 Ω,RXD floating | | 25 | 48 | μA |
| IIO IO supply current standby mode (devices with VIO) | TXD = VIO,STB = VIO,RL = 60 Ω,RXD floating | | 8.5 | 15 | μA |
| UVCC(R) | Undervoltage detection VCC rising,Ramp up | | 4.2 | 4.4 | V |
| UVCC(F) | Undervoltage detection on VCC falling,Ramp down | 3.5 | 4 | | V |
| UVIO(R) | Undervoltage detection VIO rising (Devices with VIO),Ramp up | | 1.6 | 1.65 | V |
| UVIO(F) | Undervoltage detection on VIO falling (Devices with VIO),Ramp down | 1.4 | 1.5 | | V |

### 6.7 Dissipation Ratings(耗散额定值)

| PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| PD Average power dissipation Normal mode | VCC = 5 V,VIO = 3.3 V,TJ = 27 °C,RL = 60 Ω,CL_RXD = 15 pF,TXD input = 250 kHz 50% duty cycle square wave | | | 60 | mW |
| | VCC = 5.5 V,VIO = 5.5 V,TJ = 150 °C,RL = 50 Ω,CL_RXD = 15 pF,TXD input = 2.5 MHz 50% duty cycle square wave | | | 120 | mW |
| TTSD | Thermal shutdown temperature | | | 192 | °C |
| TTSD_HYS | Thermal shutdown hysteresis | | | 10 | °C |

### 6.8 Electrical Characteristics(电气特性)

参数在推荐工作条件下有效,环境温度 -40 ≤ TJ ≤ 150(典型值 VCC = 5 V,VIO = 3.3 V),除非另有说明。

**Driver Electrical Characteristics(驱动器电气特性)**

| PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| VO(DOM) Dominant output voltage | CANH,TXD = 0 V,STB = 0 V,50 Ω ≤ RL ≤ 65 Ω,CL = open | 2.75 | | 4.5 | V |
| | CANL,TXD = 0 V,STB = 0 V,50 Ω ≤ RL ≤ 65 Ω,CL = open | 0.5 | | 2.25 | V |
| VO(REC) Recessive output voltage | CANH and CANL,TXD = VIO,STB = 0 V,RL = open,CL = open | 2 | 0.5 VCC | 3 | V |
| VSYM Driver symmetry (VO(CANH) + VO(CANL))/VCC | TXD = 250 kHz,1 MHz,2.5 MHz,STB = 0 V,RL = 60 Ω,CSPLIT = 4.7 nF,CL = open | 0.9 | | 1.1 | V/V |
| VSYM_DC DC output symmetry (VCC - VO(CANH) - VO(CANL)) | STB = 0 V,RL = 60 Ω,CL = open | -400 | | 400 | mV |
| RID(DOM) Differential input resistance in dominant phase | TXD = 0 V,STB = 0 V | | | 40 | Ω |
| RID(ACTIVE_REC) Differential input resistance in active recessive drive phase | Duration from TXD low-to-high edge to elapse of active recessive drive period (tSIC_TX_base) | | | 100 | Ω |
| VOD(DOM) Differential output voltage normal mode | CANH - CANL,TXD = 0 V,STB = 0 V,50 Ω ≤ RL ≤ 65 Ω,CL = open | 1.5 | | 3 | V |
| | TXD = 0 V,STB = 0 V,45 Ω ≤ RL ≤ 70 Ω,CL = open | 1.4 | | 3.3 | V |
| | TXD = 0 V,STB = 0 V,RL = 2×240 Ω,CL = open | 1.5 | | 5 | V |
| VOD(REC) Differential output voltage normal mode,Recessive | CANH - CANL,TXD = VIO,STB = 0 V,RL = 60 Ω,CL = open | -50 | | 50 | mV |
| | TXD = VIO,STB = 0 V,RL = open,CL = open | -120 | | 12 | mV |
| VO(STB) Bus output voltage standby mode | CANH:TX D= STB = VIO,RL = open,CL = open | -0.1 | | 0.1 | V |
| | CANL | -0.1 | | 0.1 | V |
| | CANH - CANL | -0.2 | | 0.2 | V |
| IOS Short-circuit bus output current | V(CANH) = -15 V to 40 V,CANL = open,TXD = 0 V or VIO or 250 kHz,2.5 MHz square wave,normal mode | -115 | | 115 | mA |
| | V(CAN_L) = -15 V to 40 V,CANH = open,同上 | -115 | | 115 | mA |

**Receiver Electrical Characteristics(接收器电气特性)**

| PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| VIT Input threshold voltage normal mode | -12 V ≤ VCM ≤ 12 V,STB = 0 V | 500 | | 900 | mV |
| VIT(STB) Input threshold standby mode | -12 V ≤ VCM ≤ 12 V,STB = VIO | 400 | | 1150 | mV |
| VDOM Normal mode dominant state differential input voltage range | -12 V ≤ VCM ≤ 12 V,STB = 0 V | 0.9 | | 9 | V |
| VREC Normal mode recessive state differential input voltage range | -12 V ≤ VCM ≤ 12 V,STB = 0 V | -4 | | 0.5 | V |
| VDOM(STB) Standby mode dominant state differential input voltage range | STB = VIO,-12 V ≤ VCM ≤ 12 V | 1.15 | | 9 | V |
| VREC(STB) Standby mode recessive state differential input voltage range | STB = VIO,-12 V ≤ VCM ≤ 12 V | -4 | | 0.4 | V |
| VHYS Hysteresis voltage for input threshold normal mode | -12 V ≤ VCM ≤ 12 V,STB = 0 V | | | 100 | mV |
| VCM Common mode range normal and standby modes | | -12 | | 12 | V |
| ILKG(IOFF) Unpowered bus input leakage current | CANH = CANL = 5 V,VCC = VIO = GND | | | 5 | μA |
| CI Input capacitance to ground (CANH or CANL) | TXD = VIO | | | 40 | pF |
| CID Differential input capacitance | | | | 20 | pF |
| RID Differential input resistance | TXD = VIO,STB = 0 V,-12 V ≤ VCM ≤ 12 V | 40 | | 90 | kΩ |
| RIN (CANH or CANL) Single ended input resistance | Delta V/Delta I | 20 | | 45 | kΩ |
| RIN(M) Input resistance matching [1 - (RIN(CANH)/RIN(CANL))] × 100% | V(CAN_H) = V(CAN_L) = 5 V | -1 | | 1 | % |

**TXD Terminal (CAN Transmit Data Input)**

| PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| VIH High-level input voltage | Devices without VIO | 0.7 VCC | | | V |
| | Devices with VIO | 0.7 VIO | | | V |
| VIL Low-level input voltage | Devices without VIO | | | 0.3 VCC | V |
| | Devices with VIO | | | 0.3 VIO | V |
| IIH High-level input leakage current | TXD = VCC = VIO = 5.5 V | -2.5 | 0 | 1 | μA |
| IIL Low-level input leakage current | TXD = 0 V,VCC = VIO = 5.5 V | -200 | -100 | -20 | μA |
| ILKG(OFF) Unpowered leakage current | TXD = 5.5 V,VCC = VIO = 0 V | -1 | 0 | 1 | μA |
| CI Input capacitance | VIN = 0.4·sin(2π·2×10⁶·t)+2.5 V | | | 5 | pF |

**RXD Terminal (CAN Receive Data Output)**

| PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| VOH High-level output voltage | Devices without VIO,IO = -1.5 mA | 0.8 VCC | | | V |
| | Devices with VIO,IO = -1.5 mA | 0.8 VIO | | | V |
| VOL Low-level output voltage | Devices without VIO,IO = 1.5 mA | | | 0.2 VCC | V |
| | Devices with VIO,IO = 1.5 mA | | | 0.2 VIO | V |
| ILKG(OFF) Unpowered leakage current | RXD = 5.5 V,VCC = VIO = 0 V | -1 | 0 | 1 | μA |

**STB Terminal (Standby Mode Input)**

| PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| VIH High-level input voltage | Devices without VIO | 0.7 VCC | | | V |
| | Devices with VIO | 0.7 VIO | | | V |
| VIL Low-level input voltage | Devices without VIO | | | 0.3 VCC | V |
| | Devices with VIO | | | 0.3 VIO | V |
| IIH High-level input leakage current | VCC = VIO = STB = 5.5 V | -2 | | 2 | μA |
| IIL Low-level input leakage current | VCC = VIO = 5.5 V,STB = 0 V | -20 | | -2 | μA |
| ILKG(OFF) Unpowered leakage current | STB = 5.5 V,VCC = VIO = 0 V | -1 | 0 | 1 | μA |

### 6.9 Switching Characteristics(开关特性)

参数在推荐工作条件下有效(典型值 VCC = 5 V,VIO = 3.3 V),除非另有说明。

**Device Switching Characteristics(器件开关特性)**

| PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| tPROP(LOOP1) Total loop delay,driver input (TXD) to receiver output (RXD),recessive to dominant | VIO = 4.5 V to 5.5 V,RL = 60 Ω,CL = 100 pF,CL(RXD) = 15 pF | | 95 | 145 | ns |
| | VIO = 3 V to 3.6 V | | 100 | 155 | ns |
| | VIO = 2.25 V to 2.75 V | | 105 | 170 | ns |
| | VIO = 1.71 V to 1.89 V | | 120 | 190 | ns |
| tPROP(LOOP2) Total loop delay,driver input (TXD) to receiver output (RXD),dominant to recessive | VIO = 4.5 V to 5.5 V | | 110 | 150 | ns |
| | VIO = 3 V to 3.6 V | | 115 | 160 | ns |
| | VIO = 2.25 V to 2.75 V | | 120 | 175 | ns |
| | VIO = 1.71 V to 1.89 V | | 135 | 190 | ns |
| tMODE Mode change time,from normal to standby or from standby to normal | | | | 30 | μs |
| tWK_FILTER Filter time for a valid wake-up pattern | | 0.5 | | 1.8 | μs |
| tWK_TIMEOUT Bus wake-up timeout value | | 0.8 | | 6 | ms |
| Tstartup Time duration after VCC or VIO has cleared rising undervoltage threshold,and device can resume normal operation | | | | 1.5 | ms |
| Tfilter(STB) Filter on STB pin to filter out any glitches | | 0.5 | 1 | 2 | μs |

**Driver Switching Characteristics(驱动器开关特性)**

| PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| tprop(TxD-busrec) Propagation delay time,low-to-high TXD edge to driver recessive (dominant to recessive) | STB = 0 V,RL = 60 Ω,CL = 100 pF,VIO = 4.5 V to 5.5 V | | 50 | 70 | ns |
| | VIO = 3 V to 3.6 V | | 50 | 70 | ns |
| | VIO = 2.25 V to 2.75 V | | 55 | 75 | ns |
| | VIO = 1.71 V to 1.89 V | | 55 | 80 | ns |
| tprop(TxD-busdom) Propagation delay time,high-to-low TXD edge to driver dominant (recessive to dominant) | VIO = 4.5 V to 5.5 V | | 45 | 75 | ns |
| | VIO = 3 V to 3.6 V | | 50 | 75 | ns |
| | VIO = 2.25 V to 2.75 V | | 50 | 80 | ns |
| | VIO = 1.71 V to 1.89 V | | 55 | 80 | ns |
| tsk(p) Pulse skew (\|tprop(TxD-busrec) - tprop(TxD-busdom)\|) | STB = 0 V,RL = 60 Ω,CL = 100 pF | | 3.5 | 10 | ns |
| tR Differential output signal rise time | STB = 0 V,RL = 60 Ω,CL = 100 pF | | 20 | 30 | ns |
| tF Differential output signal fall time | 同上 | | 30 | 40 | ns |
| tTXD_DTO Dominant timeout | STB = 0 V,RL = 60 Ω,CL = 100 pF | 1.2 | | 4.0 | ms |

**Receiver Switching Characteristics(接收器开关特性)**

| PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| tprop(busrec-RXD) Propagation delay time,bus recessive input to RXD high output (dominant to recessive) | STB = 0 V,CL(RXD) = 15 pF,VIO = 4.5 V to 5.5 V | | 60 | 85 | ns |
| | VIO = 3 V to 3.6 V | | 65 | 95 | ns |
| | VIO = 2.25 V to 2.75 V | | 70 | 105 | ns |
| | VIO = 1.71 V to 1.89 V | | 80 | 110 | ns |
| tprop(busdom-RXD) Propagation delay time,bus dominant input to RXD low output (recessive to dominant) | 各 VIO 档位 | 与上表对称,约 55-110 ns | | | ns |

### 6.10 Typical Characteristics(典型特性)

- Figure 6-1:VOD(DOM) 随温度变化(VCC = 5 V,VIO = 3.3 V,RL = 60 Ω,CL = Open,STB = Low)
- Figure 6-2:VOD(DOM) 随 VCC 变化(TA = 25 °C,RL = 60 Ω,CL = Open)
- Figure 6-3:ICC(standby) 随温度变化(VCC = 5 V,VIO = 3.3 V,STB = High,RL = 50 Ω)
- Figure 6-4:IIO(standby) 随温度变化(VCC = 5 V,VIO = 3.3 V,STB = High)
- Figure 6-5:总环路延迟 tPROP(LOOP1)/tPROP(LOOP2) 随温度变化(VCC = 5 V,VIO = 3.3 V,RL = 60 Ω,CL = 100 pF,CL_RXD = 15 pF,STB = Low)

## 7 Parameter Measurement Information(参数测量信息)

- Figure 7-1:ICC 测试电路(TXD → 收发器,RL/CL 在 CANH/CANL)
- Figure 7-2:驱动器测试电路与测量(驱动 VO(CANH)/VO(CANL)/VOD,测量 tprop(TXD-busdom)/tprop(TXD-busrec)/tR/tF)
- Figure 7-3:接收器测试电路与测量(VO(RXD),测量 tprop(busdom-RXD)/tprop(busrec-RXD)/tR/tF)
- Figure 7-4:发送器与接收器定时行为测试电路与测量(TXD 30%/70% 基准,tprop(TXD-busdom)/tprop(TXD-busrec),VDIFF 900 mV/500 mV,tPROP(LOOP1)/tPROP(LOOP2),tBIT(BUS)/tBIT(RXD);n = 1 to 5;TXD rise/fall time < 10 ns)
- Figure 7-5:tMODE 测试电路与测量(STB/RXD 切换)
- Figure 7-6:TXD 显性超时(tTXD_DTO)测试电路与测量
- Figure 7-7:驱动器短路电流(IOS)测试电路与测量

## 8 Detailed Description(详细说明)

### 8.1 Overview(概述)

The devices meet or exceed the specifications of the ISO 11898-2:2016 high speed CAN physical layer standard and CiA 601-4 Signal Improvement capability (SIC) specification. The devices are data rate agnostic making them backward compatible for supporting classical CAN applications while also supporting CAN FD networks up to 8 Mbps. These devices have standby mode support which puts the transceiver in ultra-low current consumption mode. Upon receiving a valid wake-up pattern (WUP) on the CAN bus, the device signals to the microcontroller through the RXD pin. The MCU can then put the device into normal mode using the STB pin.

The TCAN1462V-Q1 has two separate supply rails,VCC bus-side supply and VIO logic supply for logic-level translation for interfacing directly to 1.8V,2.5V,3.3V,or 5V controllers.

### 8.1.1 Signal Improvement(信号改善)

Signal improvement is an additional capability added to CAN FD transceiver that enhances the maximum data rate achievable in complex star topologies by minimizing signal ringing. Signal ringing is the result of reflections caused by impedance mismatch at various points in a CAN network due to the nodes that act as stubs. An example of a complex network is shown in Figure 8-1 (CAN Network:Star topology)。

Recessive-to-dominant signal edge is usually clean as it is strongly driven by the transmitter. Transmitter output impedance of CAN transceiver is ~50 Ω and matches to the network characteristic impedance. For a regular CAN FD transceiver, dominant-to-recessive edge is when the driver output impedance goes to ~60 kΩ and signal reflected back experiences impedance mismatch which causes ringing. TCAN1462-Q1 resolves this issue by TX-based Signal improvement capability (SIC). The device continues to drive the bus recessive until tSIC_TX_base so that reflections die down and recessive bit is clean at sampling point. In the active recessive phase, transmitter output impedance is low (~100 Ω). After this phase is over and device goes to passive recessive phase, driver output impedance goes to high-Z. This phenomenon is explained with Figure 8-2 (TX based SIC)。

For more information on TI's signal improvement technology, and how it compares with similar devices in market, please refer to the white paper How Signal Improvement Capability Unlocks the Real Potential of CAN-FD Transceivers。

### 8.2 Functional Block Diagram(功能框图)

功能框图包含:VCC (3)、NC or VIO (5)、TXD (1)、STB (8)、RXD (4) 逻辑输出、MUX、WUP Monitor、Low Power Receiver、TSD、Dominant SIC time-out、Mode Select、UVP,输出 CANH (7)/CANL (6),GND (2)。

### 8.3 Feature Description(功能描述)

**8.3.1 Pin Description**

- **TXD**:The TXD input is a logic-level signal from a CAN controller to the transceiver. It is referenced to VCC for TCAN1462-Q1 or to VIO for TCAN1462V-Q1 devices.
- **GND**:GND is the ground pin of the transceiver,it must be connected to the PCB ground.
- **VCC**:VCC provides the 5-V power supply to the CAN transceiver.
- **RXD**:The RXD output is a logic-level signal from the CAN transceiver to the CAN controller. It is referenced to VCC for TCAN1462-Q1 and VIO for TCAN1462V-Q1 devices. For TCAN1462V-Q1,RXD is only driven once VIO is present. When a wake event takes place,RXD is driven low.
- **VIO (only for TCAN1462V-Q1)**:The VIO pin provides the digital I/O voltage to match the CAN controller voltage thus avoiding the requirement for a level shifter. It supports wide range of controller interface voltage levels from 1.7 V to 5.5 V.
- **CANH and CANL**:These are the CAN high and CAN low differential bus pins. These pins are connected to the CAN transceiver and the low-voltage WUP CAN receiver.
- **STB (Standby)**:The STB pin is an input pin used for mode control of the transceiver. If normal mode is the only intended mode of operation,then the STB pin can be tied directly to GND.

**8.3.2 CAN Bus States**

The CAN bus has two logical states during operation:recessive and dominant. A dominant bus state occurs when the bus is driven differentially and corresponds to a logic low on the TXD and RXD pins. A recessive bus state occurs when the bus is biased to VCC/2 via the high-resistance internal input resistors (RIN) of the receiver and corresponds to a logic high on the TXD and RXD pins. A dominant state overwrites the recessive state during arbitration. Multiple CAN nodes may be transmitting a dominant bit at the same time during arbitration,and in this case the differential voltage of the bus is greater than the differential voltage of a single driver.

The TCAN1462-Q1 transceiver implements a low-power standby (STB) mode which enables a third bus state where the bus pins are weakly biased to ground via the high resistance internal resistors of the receiver (see Figure 8-4 Bus States and Figure 8-5 Simplified Recessive Common Mode Bias Unit and Receiver)。

**8.3.3 TXD Dominant Timeout (DTO)**

During normal mode,the only mode where the CAN driver is active,the TXD DTO circuit prevents the local node from blocking network communication in the event of a hardware or software failure where TXD is held dominant longer than the timeout period tTXD_DTO. The TXD DTO circuit is triggered by a falling edge on TXD. If no rising edge is seen before the timeout period of the circuit,tTXD_DTO,the CAN driver is disabled. This frees the bus for communication between other nodes on the network. The CAN driver is reactivated when a recessive signal is seen on the TXD pin,thus clearing the dominant time out. The receiver remains active and biased to VCC/2 and the RXD output reflects the activity on the CAN bus during the TXD DTO fault.

The minimum dominant TXD time allowed by the TXD DTO circuit limits the minimum possible transmitted data rate of the device. The CAN protocol allows a maximum of eleven successive dominant bits (on TXD) for the worst case,where five successive dominant bits are followed immediately by an error frame. The minimum transmitted data rate may be calculated:

**Minimum Data Rate = 11 bits / tTXD_DTO = 11 bits / 1.2 ms = 9.2 kbps**(1)

**8.3.4 CAN Bus Short-circuit Current Limiting**

The TCAN1462-Q1 has several protection features that limit the short-circuit current when a CAN bus line is shorted. These include CAN driver current limiting in the dominant and recessive states and TXD dominant state timeout which prevents permanently having the higher short-circuit current of a dominant state in case of a system fault. During CAN communication the bus switches between the dominant and recessive states;thus,the short-circuit current may be viewed as either the current during each bus state or as a DC average current. When selecting termination resistors or a common mode choke for the CAN design the average power rating,IOS(AVG),should be used. The percentage dominant is limited by the TXD DTO and the CAN protocol which has forced state changes and recessive bits due to bit stuffing,control fields,and inter frame space.

The average short-circuit current of the bus depends on the ratio of recessive to dominant bits and their respective short-circuit currents:

**IOS(AVG) = % Transmit × [(% REC_Bits × IOS(SS)_REC) + (% DOM_Bits × IOS(SS)_DOM)] + [% Receive × IOS(SS)_REC]**(2)

其中:IOS(AVG) 平均短路电流;% Transmit 节点发送消息的百分比;% Receive 接收百分比;% REC_Bits 发送消息中隐性位占比;% DOM_Bits 显性位占比;IOS(SS)_REC 隐性稳态短路电流;IOS(SS)_DOM 显性稳态短路电流。

This short-circuit current and the possible fault cases of the network should be taken into consideration when sizing the power supply used to generate the transceivers VCC supply.

**8.3.5 Thermal Shutdown (TSD)**

If the junction temperature of the TCAN1462-Q1 exceeds the thermal shutdown threshold,TTSD,the device turns off the CAN driver circuitry and blocks the TXD to bus transmission path. The shutdown condition is cleared when the junction temperature of the device drops below TTSD. The CAN bus pins are biased to VCC/2 during a TSD fault and the receiver to RXD path remains operational. The TCAN1462-Q1 TSD circuit includes hysteresis which prevents the CAN driver output from oscillating during a TSD fault.

**8.3.6 Undervoltage Lockout**

The supply pins,VCC and VIO,have undervoltage detection that places the device into a protected state. This protects the bus during an undervoltage event on either supply pin.

**Table 8-1. Undervoltage Lockout - TCAN1462-Q1**

| VCC | DEVICE STATE | BUS | RXD PIN |
|---|---|---|---|
| > UVVCC | Normal | Per TXD | Mirrors bus |
| < UVVCC | Protected | High impedance | High impedance |

**Table 8-2. Undervoltage Lockout - TCAN1462V-Q1**

| VCC | VIO | DEVICE STATE | BUS | RXD PIN |
|---|---|---|---|---|
| > UVVCC | > UVVIO | Normal | Per TXD | Mirrors bus |
| < UVVCC | > UVVIO | STB = VIO:standby mode | VIO:Remote wake request(1) | Recessive |
| > UVVCC | < UVVIO | STB = GND:Protected | High impedance | High impedance |
| < UVVCC | < UVVIO | Protected | High impedance | High impedance |

(1) See Remote Wake Request via Wake-Up Pattern (WUP) in Standby Mode。

Once the undervoltage condition is cleared and tMODE has expired,the TCAN1462-Q1 transitions to normal mode and the host controller can send and receive CAN traffic again.

**8.3.7 Unpowered Device**

The TCAN1462-Q1 is designed to be an ideal passive or no load to the CAN bus if the device is unpowered. The bus pins were designed to have low leakage currents when the device is unpowered,so they do not load the bus. This is critical if some nodes of the network are unpowered while the rest of the network remains operational. The logic pins also have low leakage currents when the device is unpowered,so they do not load other circuits which may remain powered.

**8.3.8 Floating pins**

The TCAN1462-Q1 has internal pull-ups on critical pins which place the device into known states if the pin floats. This internal bias should not be relied upon by design though,especially in noisy environments,but instead should be considered a failsafe protection feature.

When a CAN controller supporting open-drain outputs is used,an adequate external pull-up resistor must be chosen. This makes sure the TXD output of the CAN controller maintains acceptable bit time to the input of the CAN transceiver.

**Table 8-3. Pin Bias**

| Pin | Pull-up or Pull-down | Comment |
|---|---|---|
| TXD | Pull-up | Weakly biases TXD towards recessive to prevent bus blockage or TXD DTO triggering |
| STB | Pull-up | Weakly biases STB towards low-power standby mode to prevent excessive system power |

### 8.4 Device Functional Modes(器件工作模式)

**8.4.1 Operating Modes**

The TCAN1462-Q1 has two main operating modes;normal mode and standby mode. Operating mode selection is made by applying a high or low level to the STB pin.

**Table 8-4. Operating Modes**

| STB | Device Mode | Driver | Receiver | RXD Pin |
|---|---|---|---|---|
| High | Low current standby mode with bus wake-up | Disabled | Low-power receiver and bus monitor enable | High (recessive) until valid WUP is received (1) |
| Low | Normal Mode | Enabled | Enabled | Mirrors bus state |

(1) See Remote Wake Request via Wake-Up Pattern (WUP) in Standby Mode。

**8.4.2 Normal Mode** — 正常工作模式:CAN 驱动与接收器完全工作,双向通信。驱动器将 TXD 数字输入转换为 CANH/CANL 差分输出;接收器将差分信号转换为 RXD 数字输出。

**8.4.3 Standby Mode** — 低功耗模式:驱动与主接收器关断,双向通信不可用。低功耗接收器与总线监视电路使能,可通过 CAN 总线实现 RXD 唤醒请求。收到唤醒请求后,本地 CAN 协议控制器应监视 RXD 高→低转换,并将 STB 拉低使器件回到正常模式。该模式下 CAN 总线引脚弱拉至 GND(见 Figure 8-4/8-5)。待机模式只需 VIO 供电,因此可关断 VCC 以进一步省电。

**8.4.3.1 Remote Wake Request via Wake-Up Pattern (WUP) in Standby Mode**

The device uses the multiple filtered dominant wake-up pattern (WUP) from the ISO 11898-2:2016 standard to qualify bus activity. Once a valid WUP has been received,the wake request is indicated to the controller by a falling edge and low period corresponding to a filtered dominant on the RXD output.

The WUP consists of a filtered dominant pulse,followed by a filtered recessive pulse,and finally by a second filtered dominant pulse. The first filtered dominant initiates the WUP,and the bus monitor then waits on a filtered recessive;other bus traffic does not reset the bus monitor. Once a filtered recessive is received the bus monitor is waiting for a filtered dominant and again,other bus traffic does not reset the bus monitor. Immediately upon reception of the second filtered dominant the bus monitor recognizes the WUP and drives the RXD output low every time an additional filtered dominant signal is received from the bus.

For a dominant or recessive to be considered filtered,the bus must be in that state for more than the tWK_FILTER time. Bus state times less than tWK_FILTER(MIN) are never detected as part of a WUP;between tWK_FILTER(MIN) and tWK_FILTER(MAX) may be detected;greater than tWK_FILTER(MAX) are always detected. The pattern and tWK_FILTER time prevent noise and bus stuck dominant faults from causing false wake-up requests while allowing any valid message to initiate a wake-up request.

The ISO 11898-2:2016 standard has defined times for a short and long wake-up filter time. The tWK_FILTER timing has been picked to be within the minimum and maximum values of both filter ranges. This timing has been chosen such that a single bit time at 500 kbps,or two back-to-back bit times at 1 Mbps triggers the filter in either bus state. Any CAN frame at 500 kbps or less would contain a valid WUP.

For an additional layer of robustness and to prevent false wake-ups,the device implements a wake-up timeout feature. For a remote wake-up event to successfully occur,the entire WUP must be received within the timeout value t ≤ tWK_TIMEOUT. If not,the internal logic is reset and the transceiver remains in its current state without waking up. (见 Figure 8-7 Wake-Up Pattern (WUP) with tWK_TIMEOUT 时序图)

**8.4.4 Driver and Receiver Function**

The digital logic input and output levels for the TCAN1462-Q1 are CMOS levels with respect to VCC. For TCAN1462V-Q1,these are referred to VIO for compatibility with MCUs having 1.8 V,2.5 V,3.3 V,or 5 V supply.

**Table 8-5. Driver Function Table**

| Device Mode | TXD Input(1) | CANH | CANL | Driven Bus State(2) |
|---|---|---|---|---|
| Normal | Low | High | Low | Dominant |
| | High or open | High impedance | High impedance | Biased recessive |
| Standby | X | High impedance | High impedance | Biased to ground |

(1) X = irrelevant。(2) For bus state and bias see Figure 8-4 and Figure 8-5。

**Table 8-6. Receiver Function Table Normal and Standby Mode**

| Device Mode | CAN Differential Inputs VID = VCANH - VCANL | Bus State | RXD Pin |
|---|---|---|---|
| Normal | VID ≥ 0.9 V | Dominant | Low |
| | 0.5 V < VID < 0.9 V | Undefined | Undefined |
| | VID ≤ 0.5 V | Recessive | High |
| Standby | VID ≥ 1.15 V | Dominant | High |
| | 0.4 V < VID < 1.15 V | Undefined | Low if a remote wake event occurred (见 Figure 8-7) |
| | VID ≤ 0.4 V | Recessive | |
| Any | Open (VID ≈ 0 V) | Open | High |

## 9 Application and Implementation(应用与实现)

> 注:以下应用信息不属于 TI 器件规格的一部分,TI 不保证其准确性或完整性;客户负责确定元件是否适合其用途,并验证与测试其设计实现。

### 9.1 / 9.2 Typical Application(典型应用)

The TCAN1462-Q1 transceiver can be used in applications with a host controller or FPGA that includes the link layer portion of the CAN protocol. Figure 9-1 shows a typical configuration for 5 V controller applications (5-V 稳压器 → VCC/TXD/RXD/STB → CANH/CANL,可选端接节点、滤波/瞬态/ESD)。

**9.2.1.1 CAN Termination** — Termination may be a single 120-Ω resistor at each end of the bus,either on the cable or in a terminating node. If filtering and stabilization of the common-mode voltage of the bus is desired then split termination may be used (Figure 9-2)。Split termination improves the electromagnetic emissions behavior of the network by filtering higher-frequency common-mode noise that may be present on the differential signal lines。

**9.2.2.1 Bus Loading, Length and Number of Nodes** — A typical CAN application may have a maximum bus length of 40 meters and maximum stub length of 0.3 m. However,with careful design,users can have longer cables,longer stub lengths,and many more nodes to a bus. A high number of nodes requires a transceiver with high input impedance such as the TCAN1462-Q1. Additionally,since TCAN1462(V)-Q1 has SIC,in a given network size,higher data rate can be achieved because signal ringing is attenuated.

Many CAN organizations and standards have scaled the use of CAN for applications outside the original ISO 11898-2 standard (ARINC 825,CANopen,DeviceNet,SAE J2284,SAE J1939,NMEA 2000)。

A CAN network system design is a series of tradeoffs. In the ISO 11898-2:2016 specification,the driver differential output is specified with a bus load that can range from 50 Ω to 65 Ω where the differential output must be greater than 1.5 V. The TCAN1462-Q1 family is specified to meet the 1.5-V requirement down to 50 Ω and is specified to meet 1.4-V differential output at 45 Ω bus load. The differential input resistance of the TCAN1462-Q1 is a minimum of 40 kΩ. If 100 TCAN1462-Q1 transceivers are in parallel on a bus,this is equivalent to a 400-Ω differential load in parallel with the nominal 60 Ω bus termination which gives a total bus load of approximately 52 Ω. Therefore,the TCAN1462-Q1 family theoretically supports over 100 transceivers on a single bus segment. However,for a CAN network design margin must be given for signal loss across the system and cabling,parasitic loadings,timing,network imbalances,ground offsets and signal integrity thus a practical maximum number of nodes is often lower. Bus length may also be extended beyond 40 meters by careful system design and data rate tradeoffs (e.g.,CANopen allows up to 1 km with changes in termination resistance,cabling,less than 64 nodes and significantly lowered data rate)。

### 9.3 System Examples(系统示例)

Figure 9-6 显示 TCAN1462V-Q1 在 1.8 V / 2.5 V / 3.3 V 控制器应用中的典型接法(VCC 5V、VIO 1.8V/2.5V/3.3V)。

### 9.4 Power Supply Recommendations(电源建议)

The TCAN1462-Q1 transceiver is designed to operate with a main VCC input voltage supply range between 4.5V and 5.5V. The TCAN1462V-Q1 implements an I/O level shifting supply input,VIO,designed for a range between 1.8V and 5.5V. Both supply inputs must be well regulated. A decoupling capacitance,typically 100 nF,should be placed near the CAN transceiver main VCC supply pin in addition to bypass capacitors. A decoupling capacitor,typically 100 nF,should be placed near the CAN transceiver VIO supply pin in addition to bypass capacitors.

### 9.5 Layout(布局)

**Layout Guidelines:**

- 将保护与滤波电路靠近总线连接器放置,防止瞬态、ESD 与噪声传入板内;可选 TVS 二极管 D1 与总线滤波电容 C4、C5。
- 总线保护元件按信号路径方向设计,不要让瞬态电流偏离信号路径才能到达保护器件。
- 去耦电容尽量靠近收发器的 VCC 与 VIO 电源引脚。
- 电源与地至少使用两个过孔连接,减小走线与过孔电感。
- 高频率流走最小阻抗路径,而非最小电阻路径。
- 示例展示了分裂端接(Split Termination)在 CAN 节点上的实现:R4、R5 分裂电阻,中心抽头经 C3 接 GND,提供共模滤波。

## 10 Device and Documentation Support / 11 Revision History

- 修订历史:Rev * (2022 年 2 月)→ Rev A(2022 年 6 月):数据手册从 Advanced information 改为 Production data;Rev A → Rev B(2024 年 10 月):从数据手册标题与页眉中删除 TCAN1462V-Q1 型号。

## 12 Mechanical, Packaging, and Orderable Information(封装与订购信息)

**PACKAGING INFORMATION(可订购料号):**

| Orderable part number | Package \| Pins | Package qty \| Carrier | MSL rating/Peak reflow | Op temp (°C) | Part marking |
|---|---|---|---|---|---|
| TCAN1462DRBRQ1 | SON (DRB) \| 8 | 3000 \| LARGE T&R | Level-2-260C-1 YEAR | -40 to 125 | 1462 |
| TCAN1462DRQ1 | SOIC (D) \| 8 | 3000 \| LARGE T&R | Level-1-260C-UNLIM | -40 to 125 | 1462 |
| TCAN1462VDRBRQ1 | SON (DRB) \| 8 | 3000 \| LARGE T&R | Level-2-260C-1 YEAR | -40 to 125 | 1462V |
| TCAN1462VDRQ1 | SOIC (D) \| 8 | 3000 \| LARGE T&R | Level-1-260C-UNLIM | -40 to 125 | 1462V |

封装大纲:
- **DRB0008J**:VSON - 1 mm max height,塑料 QFN-无引线封装;外形 3.0 mm × 3.0 mm(2.9-3.1),含 PCB 布局图、钢网设计、焊盘图形示例。
- **D0008A**:SOIC - 1.75 mm max height,外形 4.81-5.00 × 3.81-3.98 mm,引脚间距 1.27 mm,参考 JEDEC MS-012 变体 AA。
- 带卷与盒尺寸信息、焊盘材料信息详见原文。

---

## 附录:重要声明(IMPORTANT NOTICE AND DISCLAIMER)

TI 以"按原样"提供技术与可靠性数据、设计资源、应用或其它设计建议、web 工具、安全信息等,并否认所有明示或暗示的保证。这些资源面向使用 TI 产品进行设计的资深开发者;用户对(1)选择合适 TI 产品、(2)设计、验证、测试应用、(3)满足适用标准及安全、安保、法规要求负全部责任。这些资源如有变更恕不另行通知;TI 仅授权将这些资源用于开发使用所描述 TI 产品的应用,禁止其它复制与展示。TI 产品受 TI 销售条款等适用条款约束。TI 反对并拒绝用户提出的任何附加或不同条款。Copyright © 2025,Texas Instruments Incorporated。
