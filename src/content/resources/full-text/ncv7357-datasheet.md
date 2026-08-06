---
title: NCV7357 CAN FD 收发器数据手册(全文查阅)
description: onsemi NCV7357 高速 CAN FD 收发器数据手册(Rev. 1,2023)全文站内版:特性、引脚功能、工作模式、绝对最大额定值、完整电气特性(含 2/5 Mbps 定时)、ISO 11898-2:2016 参数交叉引用与订购信息。
type: 全文查阅
organization: onsemi
year: 2023
tags: [全文查阅, 数据手册]
source: https://www.onsemi.com/pdf/datasheet/ncv7357-d.pdf
---

# NCV7357 CAN FD Transceiver, High Speed — Data Sheet(全文查阅)

> **器件**:NCV7357 CAN FD 收发器(SOIC-8 与 DFNW8 封装)
> **文档**:onsemi Data Sheet,Publication Order Number: NCV7357/D,January 2023 - Rev. 1
> **原文 PDF**:[📄 下载原文 PDF](../../files/vendors/onsemi_NCV7357_CAN_FD_datasheet.pdf)
> **相关资料**:[资源条目页](../_entries/vendors/onsemi-ncv7357.md)

---

## Description(描述)

The NCV7357 CAN FD transceiver is the interface between a controller area network (CAN) protocol controller and the physical bus. The transceiver provides differential transmit capability to the bus and differential receive capability to the CAN controller.

The NCV7357 is an addition to the CAN high-speed transceiver family complementing NCV7344 CAN stand-alone transceivers and previous generations such as AMIS42665, AMIS3066x, etc.

The NCV7357 guarantees additional timing parameters to ensure robust communication at data rates beyond 1 Mbps to cope with CAN flexible data rate requirements (CAN FD). These features make the NCV7357 an excellent choice for all types of HS-CAN networks, in nodes that require only a basic CAN capability.

## Features(特性)

- Compliant with ISO 11898-2:2016
- CAN FD Timing Specified up to 5 Mbps
- VIO Pin on NCV7357-3 Version Allowing Direct Interfacing with 3 V to 5 V Microcontrollers
- Low Current, Listen Only Silent Mode
- Low Electromagnetic Emission (EME) and High Electromagnetic Immunity
- Very Low EME without Common-mode (CM) Choke
- No Disturbance of the Bus Lines with an Unpowered Node
- Transmit Data (TxD) Dominant Timeout Function
- Under All Supply Conditions the Chip Behaves Predictably
- Very High ESD Robustness of Bus Pins, >8 kV System ESD Pulses
- Thermal Protection
- Bus Pins Short Circuit Proof to Supply Voltage and Ground
- Bus Pins Protected Against Transients in an Automotive Environment
- These are Pb-free Devices

**Quality**

- Wettable Flank Package for Enhanced Optical Inspection
- AEC-Q100 Grade 0 Qualified and PPAP Capable

**Typical Applications**

- Automotive
- Industrial Networks

## 封装与标记

- SOIC-8(CASE 751-07,D SUFFIX)与 DFNW8(CASE 507AB,MW SUFFIX)
- Marking 示例:NCV7357-3 / NCV7357-0;标记含器件代码、装配地点、晶圆批号、年份、工作周与 Pb-Free 标识
- 订购信息详见"订购信息"节

## Pin Assignment(引脚分配)

NCV7357MWx(DFNW8,顶视):1 TxD,2 GND,3 VCC,4 RxD,5 NC(-0)/ VIO(-3),6 CANL,7 CANH,8 S,EP 散热焊盘。

NCV7357D1x(SOIC-8,顶视):1 TxD,2 GND,3 VCC,4 RxD,5 NC(-0)/ VIO(-3),6 CANL,7 CANH,8 S。

**Table 1. PIN FUNCTION DESCRIPTION**

| Pin | Name | Description |
|---|---|---|
| 1 | TxD | Transmit data input; low input = dominant driver; internal pull-up current |
| 2 | GND | Ground |
| 3 | VCC | Supply voltage |
| 4 | RxD | Receive data output; dominant transmitter = low output |
| 5 | NC | Not connected. On NCV7357-0 only |
| 5 | VIO | Digital Input / Output pins supply voltage. On NCV7357-3 only |
| 6 | CANL | Low-level CAN bus line (low in dominant mode) |
| 7 | CANH | High-level CAN bus line (high in dominant mode) |
| 8 | S | Silent mode control input; internal pull-up current |
| — | EP | Exposed Pad. Recommended to connect to GND or left floating in application (DFNW8 package only) |

## Functional Description(功能描述)

### High speed CAN FD transceiver

NCV7357 implements high-speed physical layer CAN FD transceiver compatible with ISO 11898-2, implementing following optional features or alternatives:

- Extended bus load range
- Transmit dominant timeout, long
- Support of bit rates up to 5 Mbps
- Normal Bus biasing

### Operating Modes

NCV7357 provides two modes of operation as illustrated in Table 2. These modes are selectable through pin S.

**Table 2. OPERATING MODES**

| Pin S | Mode | Pin TxD | BUS | Pin RxD |
|---|---|---|---|---|
| Low | Normal | 0 | Dominant | 0 |
| | | 1 | Recessive | 1 |
| High | Silent | X | Dominant (1) | 0 |
| | | X | Recessive | 1 |

1. CAN BUS driven by another transceiver on the BUS.
2. 'X' = don't care.

**Power-off** — This virtual mode is entered as soon as the VCC or VIO undervoltage condition is detected. The internal logic is reset and the transceiver is disabled. CAN bus pins are kept floating. As soon as both VCC and VIO voltages rise above corresponding undervoltage recovery thresholds, the device proceeds to Normal or Silent mode, depending on S pin state.

**Normal Mode** — In the normal mode, the transceiver is able to communicate via the bus lines. The signals are transmitted and received to the CAN controller via the pins TxD and RxD. The slopes on the bus lines outputs are optimized to give low EME.

**Silent Mode** — In the silent mode, the transmitter is disabled. The bus pins are in recessive state independent of TxD input. Transceiver listens to the bus and provides data to controller, but controller is prevented from sending any data to the bus.

模式切换状态机:任何模式检测到 UV(欠压)→ Power-off(CAN: off(no bias),RxD: High-Z,TxD, S: High-Z);无 UV 且 S = Low → Normal mode(CAN: Tx/Rx,CAN bias: VCC/2);无 UV 且 S = High → Silent mode(CAN: Rx only,CAN bias: VCC/2)。

Notes:

- NCV7357-0:UV detected: VCC < VUVDVCC;No UV: VCC > VUVDVCC
- NCV7357-3:UV detected: VCC < VUVDVCC and/or VIO < VUVDVIO;No UV: VCC > VUVDVCC and VIO > VUVDVIO

### VIO Supply Pin

The VIO pin (available only on NCV7357-3 version) should be connected to microcontroller supply pin. By using VIO supply pin shared with microcontroller the I/O levels between microcontroller and transceiver are properly adjusted.

### Overtemperature Detection

A thermal protection circuit protects the IC from damage by switching off the transmitter if the junction temperature exceeds TJ(sd) value. Because the transmitter dissipates most of the power, the power dissipation and temperature of the IC is reduced. All other IC functions continue to operate. The transmitter off-state resets when the temperature decreases below the shutdown threshold and pin TxD goes high. The thermal protection circuit is particularly needed when a bus line short circuits.

### TxD Dominant Timeout Function

A TxD dominant timeout timer circuit prevents the bus lines being driven to a permanent dominant state (blocking all network communication) if pin TxD is forced permanently low by a hardware and/or software application failure. The timer is triggered by a negative edge on pin TxD. If the duration of the low-level on pin TxD exceeds the internal timer value tdom(TxD), the transmitter is disabled, driving the bus into a recessive state. The timer is reset by a positive edge on pin TxD.

This TxD dominant timeout time tdom(TxD) defines the minimum possible bit rate to 17 kbps.

### Fail Safe Features

A current-limiting circuit protects the transmitter output stage from damage caused by accidental short circuit to either positive or negative supply voltage, although power dissipation increases during this fault condition. Detection of undervoltage on supply pin (VCC or VIO) causes switching off device. After supply voltage is recovered TxD pin must be first released to high to allow sending dominant bits again.

The pins CANH and CANL are protected from automotive electrical transients (according to ISO 7637; see Figure 7). Pins TxD and S are biased internally should the input become disconnected. Pins TxD, S and RxD will be floating, preventing reverse supply should the VCC supply be removed.

## Absolute Maximum Ratings(绝对最大额定值)

**Table 3. ABSOLUTE MAXIMUM RATINGS**

| Symbol | Parameter | Conditions | Min | Max | Unit |
|---|---|---|---|---|---|
| VSUP | Supply voltage VCC, VIO | | -0.3 | +6.0 | V |
| VCANH | DC voltage at pin CANH | 0 < VCC < 5.5 V; no time limit | -42 | +42 | V |
| VCANL | DC voltage at pin CANL | 0 < VCC < 5.5 V; no time limit | -42 | +42 | V |
| VCANH - CANL | DC voltage between CANH and CANL | | -42 | +42 | V |
| VIN | DC voltage at pin TxD, S | | -0.3 | +6.0 | V |
| VOUT | DC voltage at pin RxD | | -0.3 | VSUP + 0.3 | V |
| VesdHBM | ESD voltage at all pins, Component HBM | (Note 3) | -6 | +6 | kV |
| VesdCDM | ESD voltage at all pins, Component CDM | (Note 4) | -750 | +750 | V |
| VesdIEC | ESD voltage at pins CANH and CANL, System HBM | (Note 5,6) | -8 | +8 | kV |
| Vschaff | Voltage transients, pins CANH, CANL. Test Pulses According to ISO 7637-2, Class C | test pulses 1 / 2a / 3a / 3b | -100 / — / -150 / — | — / +75 / — / +100 | V |
| Latch-up | Static latch-up at all pins | (Note 7) | | 150 | mA |
| Tstg | Storage temperature | | -55 | +150 | °C |
| TJ | Maximum junction temperature | | -40 | +170 | °C |
| MSLSOIC | Moisture sensitivity level for SOIC-8 | | 2 | | - |
| MSLDFN | Moisture sensitivity level for DFNW8 | | 1 | | - |

Stresses exceeding those listed in the Maximum Ratings table may damage the device. If any of these limits are exceeded, device functionality should not be assumed, damage may occur and reliability may be affected.

3. Standardized human body model ESD pulses in accordance to EIA-JESD22. Equivalent to discharging a 100 pF capacitor through a 1.5 kΩ resistor.
4. Standardized charged device model ESD pulses when tested according to AEC-Q100-011.
5. System human body model ESD pulses in accordance to IEC 61000-4-2. Equivalent to discharging a 150 pF capacitor through a 330 Ω resistor referenced to GND.
6. Results were verified by external test house.
7. Static latch-up immunity: Static latch-up protection level when tested according to EIA/JESD78.

**Table 4. THERMAL CHARACTERISTICS**

| Parameter | Symbol | Value | Unit |
|---|---|---|---|
| Thermal Resistance Junction-to-Air, SOIC-8, Free air, 1S0P PCB (Note 9) | RθJA | 131 | °C/W |
| Thermal Resistance Junction-to-Air, SOIC-8, Free air, 2S2P PCB (Note 10) | RθJA | 81 | °C/W |
| Thermal Resistance Junction-to-Air, DFNW8, Free air, 1S0P PCB (Note 9) | RθJA | 125 | °C/W |
| Thermal Resistance Junction-to-Air, DFNW8, Free air, 2S2P PCB (Note 10) | RθJA | 58 | °C/W |

8. Refer to ELECTRICAL CHARACTERISTICS, RECOMMENDED OPERATING RANGES and/or APPLICATION INFORMATION for Safe Operating parameters.
9. Values based on test board according to EIA/JEDEC Standard JESD51-3, signal layer with 10% trace coverage.
10. Values based on test board according to EIA/JEDEC Standard JESD51-7, signal layers with 10% trace coverage.

## Electrical Characteristics(电气特性)

**Table 5. ELECTRICAL CHARACTERISTICS**(VCC = 4.75 V to 5.25 V;VIO = 2.8 V to 5.5 V;for typical values TA = 25 °C,for min/max values TJ = -40 to +150 °C;RLT = 60 Ω,CRxD = 15 pF;unless otherwise noted. All voltages are referenced to GND (pin 2). Positive currents flow into the respective pin.)

**SUPPLY (Pin VCC)**

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| VCC | Power supply voltage | (Note 11) | 4.75 | 5.0 | 5.25 | V |
| ICC | Supply current in Normal mode | Dominant; VTxD = Low | 30 | 45 | 55 | mA |
| | | Recessive; VTxD = High | 2.0 | 5.0 | 10 | mA |
| | | Normal mode, Dominant; VTxD = 0 V; one of bus wires shorted -3 V (VCANH, VCANL) +18 V | 2.0 | - | 105 | mA |
| ICCS | Supply current in silent mode, NCV7357-3 version | | 0.1 | - | 1.3 | mA |
| | Supply current in silent mode, NCV7357-0 version | | 0.1 | - | 1.5 | mA |
| VUVDVCC | Undervoltage detection on VCC pin | | 3.5 | 4.0 | 4.3 | V |

**VIO SUPPLY VOLTAGE (Pin VIO) Only for NCV7357-3 version**

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| VIO | Supply voltage on pin VIO | | 2.8 | - | 5.5 | V |
| IIOS | Supply current on pin VIO in silent mode | VTxD = VIO | - | 120 | 200 | μA |
| IIONM | Supply current on pin VIO during normal mode | Dominant; VTxD = Low / Recessive; VTxD = High | - | 700 / 460 | 900 / 600 | μA |
| VUVDVIO | Undervoltage detection voltage on VIO pin | | 2.0 | 2.3 | 2.6 | V |

**TRANSMITTER DATA INPUT (Pin TxD)**

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| VIH | High-level input voltage | Output recessive | 2.0 | - | - | V |
| VIL | Low-level input voltage | Output dominant; VTxD = VCC / VIO | -0.3 | - | 0.8 | V |
| IIH | High-level input current | VTxD = 0 V (Note 12) | -5.0 | 0 | 5.0 | μA |
| IIL | Low-level input current | | -300 | -150 | -75 | μA |
| Ci | Input capacitance | | - | 5 | 10 | pF |

**TRANSMITTER DATA INPUT (Pin S)**

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| VIH | High-level input voltage | Silent mode | 2.0 | - | - | V |
| VIL | Low-level input voltage | Normal mode; VS = VCC / VIO | -0.3 | - | 0.8 | V |
| IIH | High-level input current | VS = 0 V (Note 12) | -1.0 | 0 | 1.0 | μA |
| IIL | Low-level input current | | -15 | - | -1.0 | μA |
| Ci | Input capacitance | | - | 5 | 10 | pF |

**RECEIVER DATA OUTPUT (Pin RxD)**

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| IOH | High-level output current | Normal mode; VRxD = VCC / VIO - 0.4 V | -8.0 | -3.0 | -1.0 | mA |
| IOL | Low-level output current | VRxD = 0.4 V | 1.0 | 6.0 | 12 | mA |

**CAN TRANSMITTER (PINS CANH AND CANL)**

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| Vo(dom)(CANH) | Dominant output voltage at pin CANH | Normal mode; VTxD = Low; t < tdom(TxD); 50 Ω < RLT < 65 Ω | 2.75 | 3.5 | 4.5 | V |
| Vo(dom)(CANL) | Dominant output voltage at pin CANL | Normal mode; VTxD = Low; t < tdom(TxD); 50 Ω < RLT < 65 Ω | 0.5 | 1.5 | 2.25 | V |
| Vo(rec) | Recessive output voltage at pins CANH and CANL | Normal or Silent mode; VTxD = High or VTxD = Low and t > tdom(TxD); no load | 2.0 | 2.5 | 3.0 | V |
| Vo(dom)(diff) | Differential dominant output voltage (VCANH - VCANL) | Normal mode; VTxD = Low; t < tdom(TxD); 45 Ω < RLT < 65 Ω | 1.5 | 2.25 | 3.0 | V |
| Vo(dom)(diff)_ARB | Differential dominant output voltage | Normal mode; VTxD = Low; t < tdom(TxD); RLT = 2 x 240 Ω (Note 12) | 1.5 | - | 5.0 | V |
| Vo(rec)(diff) | Differential recessive output voltage (VCANH - VCANL) | Normal or Silent mode; VTxD = High or VTxD = Low and t > tdom(TxD); no load | -50 | 0 | +50 | mV |
| Vo(dom)(sym) | Dominant output voltage driver symmetry; Vo(dom)(sym) = Vo(CANH)(dom) + Vo(CANL)(dom) | TxD = square wave up to 1 MHz; CST = 4.7 nF | 0.9 | 1.0 | 1.1 | VCC |
| Io(sc)(CANH) | Short circuit output current at pin CANH in dominant | Normal mode; TxD = Low; t < tdom(TxD); -3 V ≤ VCANH ≤ +18 V | -100 | -70 | +1.0 | mA |
| Io(sc)(CANL) | Short circuit output current at pin CANL in dominant | Normal mode; TxD = Low; t < tdom(TxD); -3 V ≤ VCANL ≤ +36 V | -1.0 | +70 | +100 | mA |
| Io(sc)(rec) | Short circuit output current at pins CANH and CANL in recessive | Normal or Silent mode; TxD = High; -27 V < VCANH, VCANL < +32 V | -5.0 | - | +5.0 | mA |

**CAN RECEIVER (Pins CANH and CANL)**

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| ILEAK(off) | Input leakage current | 0 Ω < R(VCC to GND) < 1 MΩ; VCANH = VCANL = 5 V | -5.0 | 0 | +5.0 | μA |
| | | VCC = VIO = 0 V; VCANH = VCANL = 5 V | -5.0 | 0 | +5.0 | μA |
| Vi(rec)(diff)_NM | Differential input voltage range, recessive state | Normal or Silent mode; -12 V ≤ VCANH, VCANL ≤ +12 V; no load | -3.0 | - | 0.5 | V |
| Vi(dom)(diff)_NM | Differential input voltage range, dominant state | Normal or Silent mode; -12 V ≤ VCANH, VCANL ≤ +12 V; no load | 0.9 | - | 8.0 | V |
| Vi(th)(diff)_NM | Differential receiver threshold voltage | Normal or Silent mode; -12 V ≤ VCANH, VCANL ≤ +12 V; no load | 0.5 | - | 0.9 | V |
| Vi(th)(diff)_NM_E | Differential receiver threshold voltage | Normal or Silent mode; extended, -30 V ≤ VCANH, VCANL ≤ +35 V; no load | 0.4 | - | 1.0 | V |
| Ri(cm) | Common-mode input resistance at pins CANH and CANL | -2 V ≤ VCANH, VCANL ≤ +7 V | 15 | 25 | 37 | kΩ |
| Ri(cm)(m) | Matching between pin CANH and CANL common mode input resistance | VCANH = VCANL = +5 V | -1 | 0 | +1 | % |
| Ri(diff) | Differential input resistance; Ri(diff) = Ri(cm)(CANH) + Ri(cm)(CANL) | | 25 | 50 | 75 | kΩ |
| Ci | Input capacitance at pins CANH and CANL | -2 V ≤ VCANH, VCANL ≤ +7 V; VTxD = High (Note 12) | - | 7.5 | 20 | pF |
| Ci(diff) | Differential input capacitance | VTxD = High (Note 12) | - | 3.75 | 10 | pF |

**TIMING CHARACTERISTICS**(see Figure 5, Figure 6 and Figure 8)

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| td(TxD-BUSon) | Propagation delay TxD to bus active | Normal mode (Note 13) | - | 75 | - | ns |
| td(TxD-BUSoff) | Propagation delay TxD to bus inactive | Normal mode (Note 13) | - | 85 | - | ns |
| td(BUSon-RxD) | Propagation delay bus active to RxD | Normal or Silent mode (Note 13) | - | 24 | - | ns |
| td(BUSoff-RxD) | Propagation delay bus inactive to RxD | Normal or Silent mode (Note 13) | - | 32 | - | ns |
| tpd_dr | Propagation delay TxD to RxD dominant to recessive transition | Normal mode (Note 13) | 50 | 100 | 210 | ns |
| tpd_rd | Propagation delay TxD to RxD recessive to dominant transition | Normal mode (Note 13) | 50 | 120 | 210 | ns |
| td(s-nm) | Operating mode change delay | Silent mode to Normal mode | 5.0 | 11 | 50 | ms |
| tdom(TxD) | TxD dominant timeout | Normal mode; VTxD = Low | 1.0 | - | 10 | ms |
| tbit(RxD) | Bit time on RxD pin | tbit(TxD) = 500 ns (Note 13) | 400 | - | 550 | ns |
| | | tbit(TxD) = 200 ns (Note 13) | 120 | - | 220 | ns |
| tbit(Vi(diff)) | Bit time on bus (CANH - CANL pin) | tbit(TxD) = 500 ns (Note 13) | 435 | - | 530 | ns |
| | | tbit(TxD) = 200 ns (Note 13) | 155 | - | 210 | ns |
| Δtrec | Receiver timing symmetry; trec = tbit(RxD) - tbit(Vi(diff)) | tbit(TxD) = 500 ns (Note 13) | -65 | - | 40 | ns |
| | | tbit(TxD) = 200 ns (Note 13) | -45 | - | 15 | ns |

**THERMAL SHUTDOWN**

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| TJ(sd) | Shutdown junction temperature | Junction temperature rising | 160 | 180 | 200 | °C |

Product parametric performance is indicated in the Electrical Characteristics for the listed test conditions, unless otherwise noted. Product performance may not be indicated by the Electrical Characteristics if operated under different conditions.

11. In the range between VUVDVCC and 4.75 V and from 5.25 V to 6 V the chip is fully functional; some parameters may be outside of the specification.
12. Values based on design and characterization, not tested in production.
13. CLT = 100 pF, CST not present, CRxD = 15 pF.

## Measurements Setups and Definitions(测量设置与定义)

**Figure 5. Transceiver Timing Diagram - Propagation Delays**

TxD:recessive → dominant(0.7 × VIO\*)→ recessive;CANH/CANL 900 mV/500 mV;Vi(diff) = VCANH - VCANL;RxD 0.3/0.7 × VIO\*;测 td(TxD-BUSon)、td(BUSon-RXD)、td(TxD-BUSoff)、td(BUSoff-RXD)。Edge length below 10 ns。\*On NCV7357-0 version VIO is replaced by VCC。

**Figure 6. Transceiver Timing Diagram - Loop Delay and Recessive Bit Time**

TxD 0.3/0.7 × VIO\*;5 × tbit(TxD);tbit(TxD);tpd_rd;Vi(diff) 900 mV/500 mV;tbit(Vi(diff));RxD 0.7/0.3 × VIO\*;tpd_dr;tbit(RxD)。Edge length below 10 ns。\*On NCV7357-0 version VIO is replaced by VCC。

**Figure 7. Test Circuit for Automotive Transients / Figure 8. Test Circuit for Timing Characteristics**

- 图 7:NCV7357-3 应用电路(VIO/VCC 各接 100 nF 去耦、总线接瞬态发生器,含 15 pF RxD 负载)。
- 图 8:定时特性测试电路(总线 CANH/CANL 各接 RLT/2、CLT 100 pF、CST,RLT/2 = 2 × 30 Ω)。

## Table 6. ISO 11898-2:2016 Parameter Cross-Reference Table

| ISO 11898-2:2016 Specification Parameter | Notation | NCV7357 Datasheet Symbol |
|---|---|---|
| **DOMINANT OUTPUT CHARACTERISTICS** | | |
| Single ended voltage on CAN_H / CAN_L | VCAN_H / VCAN_L | Vo(dom)(CANH) / Vo(dom)(CANL) |
| Differential voltage on normal bus load | VDiff | Vo(dom)(diff) |
| Differential voltage on effective resistance during arbitration | VDiff | Vo(dom)(diff)_ARB |
| Differential voltage on extended bus load range (optional) | VDiff | Vo(dom)(diff) |
| Driver symmetry | VSYM | Vo(dom)(sym) |
| **DRIVER OUTPUT CURRENT** | | |
| Absolute current on CAN_H / CAN_L | ICAN_H / ICAN_L | Io(SC)(CANH) / Io(SC)(CANL) |
| **RECEIVER OUTPUT CHARACTERISTICS, BUS BIASING ACTIVE** | | |
| Single ended output voltage on CAN_H / CAN_L | VCAN_H / VCAN_L | Vo(rec) |
| Differential output voltage | VDiff | Vo(rec)(diff) |
| **RECEIVER OUTPUT CHARACTERISTICS, BUS BIASING INACTIVE** | | |
| Single ended output voltage on CAN_H / CAN_L | VCAN_H / VCAN_L | NA |
| Differential output voltage | VDiff | NA |
| **OPTIONAL TRANSMIT DOMINANT TIMEOUT** | | |
| Transmit dominant timeout, long | tdom | tdom(TxD) |
| Transmit dominant timeout, short | tdom | NA |
| **STATIC RECEIVER INPUT CHARACTERISTICS, BUS BIASING ACTIVE/INACTIVE** | | |
| Recessive state differential input voltage range | VDiff | Vi(rec)(diff)_NM |
| Dominant state differential input voltage range | VDiff | Vi(dom)(diff)_NM |
| **RECEIVER INPUT RESISTANCE** | | |
| Differential internal resistance | RDiff | Ri(diff) |
| Single ended internal resistance | RCAN_H / RCAN_L | Ri(cm) |
| Matching of internal resistance | mR | Ri(cm)(m) |
| **IMPLEMENTATION LOOP DELAY REQUIREMENT** | | |
| Loop delay | tLoop | tpd_rd / tpd_dr |
| **OPTIONAL IMPLEMENTATION DATA SIGNAL TIMING REQUIREMENTS FOR USE WITH BIT RATES ABOVE 1 MBIT/S AND UP TO 2 MBIT/S** | | |
| Transmitted recessive bit width @ 2 Mbit/s | tBit(Bus) | tbit(Vi(diff)) |
| Received recessive bit width @ 2 Mbit/s | tBit(RXD) | tbit(RxD) |
| Receiver timing symmetry @ 2 Mbit/s | ΔtRec | Δtrec |
| **OPTIONAL IMPLEMENTATION DATA SIGNAL TIMING REQUIREMENTS FOR USE WITH BIT RATES ABOVE 2 MBIT/S AND UP TO 5 MBIT/S** | | |
| Transmitted recessive bit width @ 5 Mbit/s | tBit(Bus) | tbit(Vi(diff)) |
| Received recessive bit width @ 5 Mbit/s | tBit(RXD) | tbit(RxD) |
| Receiver timing symmetry @ 5 Mbit/s | ΔtRec | Δtrec |
| **MAXIMUM RATINGS OF VCAN_H, VCAN_L AND VDIFF** | | |
| Maximum rating VDiff | VDiff | VCANH - CANL |
| General maximum rating VCAN_H and VCAN_L | VCAN_H / VCAN_L | VCANH / VCANL |
| Optional: Extended maximum rating VCAN_H and VCAN_L | VCAN_H / VCAN_L | NA |
| **MAXIMUM LEAKAGE CURRENTS ON CAN_H AND CAN_L, UNPOWERED** | | |
| Leakage current on CAN_H, CAN_L | ICAN_H, ICAN_L | ILEAK(off) / NA |
| **BUS BIASING CONTROL TIMINGS** | | |
| CAN activity filter time, long / short | tFilter | NA |
| Wake-up timeout, short / long | tWake | NA |
| Timeout for bus inactivity (Required for selective wake-up implementation only) | tSilence | NA |
| Bus Bias reaction time (Required for selective wake-up implementation only) | tBias | NA |

## Table 7. ORDERING INFORMATION

| Part Number | Description | Temperature Range | Package |
|---|---|---|---|
| NCV7357D10R2G | High Speed CAN FD Transceiver | -40 °C to +150 °C | SOIC-8 (Matte Sn, JEDEC MS-012) (Pb-Free) |
| NCV7357D13R2G | High Speed CAN FD Transceiver with VIO pin | -40 °C to +150 °C | SOIC-8 |
| NCV7357MW0R2G | High Speed CAN FD Transceiver | -40 °C to +150 °C | DFNW8 Wettable Flank (Pb-Free) |
| NCV7357MW3R2G | High Speed CAN FD Transceiver with VIO pin | -40 °C to +150 °C | DFNW8 Wettable Flank |

Shipping:3000 / Tape & Reel。

## 机械封装尺寸(摘要)

- **DFNW8 3x3,0.65P**(CASE 507AB,ISSUE E):封装外形、标记图(通用标记:器件代码、ALYWG)、文档号 98AON14978G。
- **SOIC-8 NB**(CASE 751-07,ISSUE AK):含封装尺寸表(如 A 4.80–5.00 mm,B 3.80–4.00 mm,C 1.35–1.75 mm,D 0.33–0.51 mm,G 1.27 BSC,H 0.10–0.25 mm,J 0.19–0.25 mm,K 0.40–1.27 mm,N 0.25–0.50 mm,S 5.80–6.20 mm)、焊接足迹、通用标记图(IC / Discrete)、引脚样式(Style 1–30 通用定义)、文档号 98ASB42564B。

## 声明与版权

onsemi 商标信息、免责声明(产品适用性不提供担保、买受人自行负责产品与应用合规、不授予任何知识产权许可)、联系方式(技术文库 www.onsemi.com/design/resources/technical-documentation、在线支持 www.onsemi.com/support)。© Semiconductor Components Industries, LLC。
