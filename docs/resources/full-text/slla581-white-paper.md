---
title: TI SLLA581 白皮书 — How Signal Improvement Capability Unlocks the Real Potential of CAN FD Transceivers(全文查阅)
description: TI SLLA581(SLLA581A,2022/2025 修订)技术白皮书全文:讲解 CAN SIC 如何减少总线振铃、释放 CAN FD 收发器在复杂星形网络中的 5 Mbps 潜力,含 CiA 601-4 / ISO 11898-2:2024 Set C 与 Annex A 参数对比、TCAN1462 实验结果与 TI 器件产品线。
type: 全文查阅
organization: Texas Instruments
year: 2022
tags: [全文查阅, 白皮书]
source: https://www.ti.com/lit/pdf/slla581
---

# How Signal Improvement Capability Unlocks the Real Potential of CAN FD Transceivers(全文查阅)

> **文档**:Technical White Paper SLLA581A(2022 年 4 月发布,2025 年 10 月修订)
> **作者**:Vikas Kumar Thawani(Texas Instruments)
> **原文 PDF**:[📄 下载原文 PDF](../../files/vendors/TI_SLLA581_SIC_whitepaper.pdf)
> **相关资料**:[资源条目页](../_entries/vendors/ti-slla581.md)

---

## ABSTRACT(摘要)

Modern-day automobiles perform a plethora of functions to improve vehicle safety, performance, and comfort; from powertrain to advanced driver assistance systems, from body electronics and lighting to infotainment and safety. A large number of electronic control units (ECUs) deployed in vehicles perform these electromechanical functions.

ECUs exchange control and data-log information through in-vehicle network buses. Between Controller Area Network (CAN), Local Interconnect Network (LIN), FlexRay™, and Ethernet, the CAN bus remains the popular choice. The popularity of CAN is due to features like ease of use, good common-mode noise rejection, priority-based messaging, bitwise arbitration to handle bus contention, and error detection and recovery.

A major advantage of CAN networks is that scaling up a vehicle network is easy by adding nodes to an existing CAN bus. This advantage diminishes, however, when networks become complex, such as a star topology connection of CAN nodes. Reflections caused by the unterminated stubs inherently present in these networks can cause faulty signal communication at higher speeds. Therefore, CAN with Flexible Data-Rate (FD) transceivers, although rated for 5 Mbps, have to be used at less than 2 Mbps in actual vehicle networks. Signal improvement capability (SIC) enables the use of CAN FD transceivers at 5 Mbps and beyond for complex star networks without requiring major redesigns.

## 目录

1. What is SIC?
2. The Limitations of Classical CAN and Regular CAN FD
3. How CAN SIC Reduces Bus Ringing
4. Experimental Results on TI's TCAN1462 Device
5. TI's CAN SIC Devices
6. Benefits of CAN SIC
7. Revision History

## 1. What is SIC?

CAN signal improvement capable (CAN SIC) is an improvement added to CAN FD transceivers that enhances the maximum data-rate achievable in complex network topologies by minimizing signal ringing. CAN SIC was first standardized in the CAN in Automation™ (CiA) 601-4 signal improvement specification, as an addition to the existing International Organization for Standardization (ISO) 11898-2:2016 high-speed CAN physical layer standard.

Figure 1-1 shows a regular CAN FD transceiver where the CAN bus signal rings above 900 mV (the dominant threshold of a CAN receiver) and below 500 mV (the recessive threshold of a CAN receiver), resulting in receive data (RXD) glitches. Figure 1-2 shows how a CAN SIC capability transceiver attenuates bus signal ringing, resulting in the correct RXD signal.

> Figure 1-1. CAN Bus and RXD Waveforms Without SIC / Figure 1-2. CAN Bus and RXD Waveforms With SIC

In terms of electrical parameters, a CAN SIC transceiver has a much tighter bit-timing symmetry and loop-delay specification compared to a regular CAN FD transceiver, as shown in Table 1-1. The segregation of delays of transmit and receive paths can help system designers clearly calculate network propagation delay in the presence of other signal chain components. One thing to note is that the timing specified in CiA 601-4 (and ISO 11898-2:2024 Set C and Annex A) is data-rate agnostic and holds true for both 2 Mbps and 5 Mbps operation.

**Table 1-1. Comparing the CiA 601-4 and ISO 11898-2 Timing Specifications**

| Parameter | Notation | CiA 601-4 Min [ns] | CiA 601-4 Max [ns] | ISO 11898-2:2016 Min [ns] | ISO 11898-2:2016 Max [ns] |
|---|---|---|---|---|---|
| Signal improvement time TX-based | tSIC_TX_base | N/A | 530 | — | — |
| Transmitted bit-width variation | tBit(Bus) | -10 | 10 | -65 (2 Mbps) / -45 (5 Mbps) | 30 (2 Mbps) / 10 (5 Mbps) |
| Received bit width | tBit(RxD) | -30 | 20 | -100 (2 Mbps) / -80 (5 Mbps) | 50 (2 Mbps) / 20 (5 Mbps) |
| Receiver timing symmetry | tREC | -20 | 15 | -65 (2 Mbps) / -45 (5 Mbps) | 40 (2 Mbps) / 15 (5 Mbps) |
| Propagation delay from TXD to bus dominant | tprop(TxD-busdom) | N/A | 80 | Only loop delay, TXD to bus to RXD, is specified at 255 ns max | — |
| Propagation delay from TXD to bus recessive | tprop(TxD-busrec) | N/A | 80 | — | — |
| Propagation delay from bus to RXD dominant | tprop(busdom-RxD) | N/A | 110 | — | — |
| Propagation delay from bus to RXD recessive | tprop(busrec-RxD) | N/A | 110 | — | — |

In 2024, CAN SIC was integrated into the overall ISO 11898-2:2024 high-speed CAN physical layer standard, with updated CAN SIC specifications. Within ISO 11898-2:2024, there are three sets of parameters with increasing data-rate: Set A, Set B, and Set C. Set C contains the governing parameters for CAN SIC transceivers (referenced as SIC mode) and now specifies the minimum SIC on time and differential SIC impedance to address theoretical corner cases and to maintain a minimum amount of ringing suppression duration. Table 1-2 shows these updated parameters.

**Table 1-2. Parameters Updated in ISO 11898-2:2024 Set C**

| Parameter | Notation | ISO 11898-2:2024 Set C Min | ISO 11898-2:2024 Set C Max |
|---|---|---|---|
| Differential internal resistance (CANH to CANL) | RDIFF_act_rec | 75 | 133 |
| Start time of active signal improvement phase | tact_rec_start | N/A | 120 ns |
| End time of active signal improvement phase | tact_rec_end | 355 ns | N/A |
| Start time of passive recessive phase | tpas_rec_start | N/A | 530 ns |

Derived from ISO 11898-2:2024, Annex A builds on the specifications in Set C, introducing FAST mode. This FAST mode enables CAN XL, and the updates to the timing and voltage symmetry for SIC mode transceivers enable CAN XL compatibility for SIC networks and simplify migration to faster speeds. While Annex A is backward compatible to Set C, Annex A adds forward compatibility with CAN XL. The relationship between these standards is shown in Figure 1-3.

> Figure 1-3. CAN SIC Standards Compatibility: ISO 11898-2:2024 Annex A(CAN SIC & CAN XL compatibility)→ ISO 11898-2:2024 Set A, B, and C CAN SIC → CiA 601-4 CAN SIC

Annex A allows not only compatibility with current CAN SIC networks, but can be used in future CAN XL networks. Figure 1-4 visualizes this (CAN SIC node / CAN FD node system diagram).

> Figure 1-4. System Diagram

All CAN SIC transceivers must meet or exceed specifications set forth in ISO 11898-2:2024 Set C, with the option to add additional requirements outlined in Annex A. An exception is CAN SIC transceivers released prior to 2024, which must be compliant to CiA 601-4, the governing standard at the time. The CAN SIC specifications within ISO 11898-2:2024 are slightly modified and have generally superseded the CiA specification for new architectures and designs.

The parameters and benefits of ISO 11898-2:2024 Annex A are shown in Table 1-3.

**Table 1-3. Parameters and Benefits Included in ISO 11898-2:2024 Annex A**

| Parameter | Notation | ISO 11898-2:2024 Set C Specification | ISO 11898-2:2024 Annex A Specification | Benefit |
|---|---|---|---|---|
| Differential load range | RL | 50-65 | 45-65 | A widened load range allows different cable types to be used in the network. |
| Differential voltage on differential load, minimum | VOD_MIN | 1.4 V | 1.5 V | A wider, stronger signal, that is less susceptible to dissipation. |
| Wake filter time | tWK_FILTER | 0.5 to 1.8 μs | 0.5 to 0.95 μs | A tightened wake filter-time allows for arbitration rates of 1 Mbps, while still tolerant to differential noise and glitches of 0.5 μs. |
| Driver symmetry | Vsymmetry | ±10% | ±5% | Tighter results in lower emissions. |
| Wake-up pattern | N/A | D-R-D | D-R-D-R | More resilient to false wake-up events. |

## 2. The Limitations of Classical CAN and Regular CAN FD

The first-generation CAN protocol, ISO 11898-2, also known as classical CAN, was released around 1993. The protocol allowed only 8 bytes of payload data transfer, and a maximum specified data-rate of 1 Mbps. These limitations were quickly realized in automotive applications, where vehicles have a number of electronic nodes that communicate with each other using the CAN bus.

The CAN FD protocol specification was released around 2015, which increased the payload length to 64 bytes and the maximum signaling rate in the data phase to 5 Mbps. However, the arbitration phase signaling rate was still limited to 1 Mbps for backwards compatibility with classical CAN.

While CAN FD brought the advantages of a faster data-rate and a longer payload, these advantages were not sufficient to keep pace with the ever-increasing number of ECUs added to vehicle CAN bus networks. Designers realized that harnessing the real potential of CAN FD transceivers was not possible, as bus ringing (resulting from complex star networks) affected correct signal communication. Figure 2-1 is an example of star topology.

> Figure 2-1. CAN Nodes Connected in a Star Network

In complex star topologies with multiple stubs, a signal traveling on the bus experiences an impedance mismatch which causes reflections. These reflections distort the CAN bus and cause oscillations, resulting in an incorrect CAN bus level and RXD at the sampling point. Although these network effects were not specific to CAN FD networks, at the lower-speed operation of classical CAN, the bit duration was longer, and the bus ringing diminished such that sampling the correct bit was possible (as shown in Figure 2-2) resulting in correct communication.

> Figure 2-2. CAN Bus Ringing and RXD Glitch for Classical CAN Speeds(500 kbps bit time = 2000 ns,80% sample point = 1600 ns)

For a 5 Mbps CAN FD operation, a 200 ns bit duration was much too small for the ringing in complex star topologies to disappear, hampering reliable data communication. This deterred system designers from using CAN FD at 5 Mbps.

With an increase in the exchange of network data and faster throughput demands in modern-day vehicles, CAN SIC paves the way for a next-generation in-vehicle communication bus technology that is faster and provides more network flexibility and scalability.

## 3. How CAN SIC Reduces Bus Ringing

The CAN bus has two logical states during normal operation: recessive and dominant, as shown in Figure 3-1.

> Figure 3-1. CAN Bus Voltage Levels

A dominant bus state occurs when driving the bus differentially and corresponds to a logic low on the TXD and RXD pins. A recessive bus state occurs when the bus is biased to VCC/2 through the high-value internal input resistors (RIN) of the receiver and corresponds to a logic high on the TXD and RXD pins. A dominant state overwrites the recessive state during arbitration. The recessive-to-dominant signal edge on the CAN bus is usually clean, as this edge is strongly driven by the transmitter. The differential transmitter output impedance of the CAN transceiver during the dominant phase is approximately 50 Ω and closely matches the network characteristic impedance. For a regular CAN FD transceiver, the dominant-to-recessive edge is when the driver differential output impedance suddenly goes to approximately 60 kΩ, and the signal reflected back experiences an impedance mismatch, which causes ringing.

The transmitter-based SIC detects the dominant-to-recessive edge on TXD and activates ringing suppression circuitry on the driver output. The CAN driver continues driving the bus recessive strongly until tSIC_TX_base, so that reflections diminish and the recessive bit is clean at the sampling point. In this active recessive phase, the transmitter output impedance is low (approximately 100 Ω). Since the reflected signal does not see a huge impedance mismatch, ringing is attenuated considerably. After this phase ends and the device enters a passive-recessive phase, the driver output impedance rises to approximately 60 kΩ. Figure 3-2 shows this phenomenon.

> Figure 3-2. CAN SIC Technology: Sequence of Events(TXD,VDIFF,RID 60 kΩ → active recessive 100 Ω)

Importantly, the active recessive phase strongly driving the bus is only expected to last for a maximum of 530 ns (tSIC_TX_base, as listed in Table 1-1). The data phase of the CAN FD protocol only lasts for 200 ns max (if operated at 5 Mbps), so this ringing suppression is only active for the entire recessive bit duration, resulting in correct CAN bus and RXD signals. For the arbitration phase, however — where the fastest bit duration is 1 μs for a 1 Mbps operation — multiple transmitters can transmit simultaneously, and the dominant bit has to overwrite the recessive bit. The duration of ringing suppression can place some limits on the overall network length and arbitration speed. See the CiA 601-4 specification for more details.

## 4. Experimental Results on TI's TCAN1462 Device

To showcase the ringing-suppression functionality of the Texas Instruments (TI) eight-pin TCAN1462 CAN SIC transceiver, Texas Instruments conducted an experiment with the following setup:

- Two-node point-to-point communication, where node 1 is the TCAN1462 and node 2 is the TCAN1044A, a regular CAN FD transceiver, as shown in Figure 4-1. The ringing network (specified by CiA 601-4) emulating a complex star topology is connected across the CAN bus terminals. As the waveforms in Figure 4-2 and Figure 4-3 show, the CAN bus and RXD signals look clean when the TCAN1462 is driving. But when the TCAN1044A is driving, there is considerable ringing on the bus and RXD glitches.

> Figure 4-1. Network with Two Node and Ringing Circuit / Figure 4-2. Waveforms with CAN FD Driving the Network / Figure 4-3. Waveforms with CAN SIC Driving the Network

The hugely negative-going VOD is not a problem and there is no overshoot on VOD, resulting in clean RXD.

## 5. TI's CAN SIC Devices

TI has released CAN SIC devices compliant to both CiA 601-4 and ISO 11898-2:2024 Annex A, including the eight-pin TCAN1472-Q1 with standby mode support, and the 14-pin TCAN1473-Q1 and TCAN1473A-Q1 with sleep mode and a WAKE/INH capability. TI also offers the TCAN1473C-Q1 and TCAN1473AC-Q1, which are 14-pin CAN transceivers with sleep mode and a Wake/INH capability compliant to ISO 11898-2:2024 Set C, without including the additional CAN XL compatibility requirements outlined in Annex A. TI's ISO 11898-2:2024 CAN SIC devices are shown below in Table 5-1.

**Table 5-1. TI's CAN SIC Transceiver Portfolio**

| Device | Description | Pin Count | Set C or Annex A? | Pin-to-Pin CAN FD Device |
|---|---|---|---|---|
| TCAN1472-Q1 | CAN SIC transceiver with standby mode | 8 | Annex A | TCAN1044A-Q1 / TCAN1043N-Q1 / TCAN1043A-Q1 |
| TCAN1473-Q1 | CAN SIC transceiver with Wake/INH functionality | 14 | Set C | TCAN1043N-Q1 / TCAN1043A-Q1 |
| TCAN1473A-Q1 | CAN SIC transceiver with Wake/INH functionality | 14 | Annex A | TCAN1046AV-Q1 / TCAN1145-Q1 / TCAN1146-Q1 |
| TCAN1473C-Q1 | CAN SIC transceiver with Wake/INH functionality | 14 | Set C | — |
| TCAN1473AC-Q1 | CAN SIC transceiver with Wake/INH functionality | 14 | Annex A | — |
| TCAN1476V-Q1 | Dual CAN SIC transceiver with standby mode | 14 | — | — |
| TCAN1575-Q1 | CAN SIC transceiver with selective wake/partial networking functionality | 14 | — | — |
| TCAN1576-Q1 | CAN SIC transceiver with selective wake/partial networking functionality, watchdog, and bus fault diagnostics | 14 | — | — |

The TCAN1472 is available in two variants: the TCAN1472 for 5V bus/logic levels and the TCAN1472V with 1.8V to 5V logic-level support. These devices have major benefits compared to competing devices in the market, as shown in Table 5-2.

**Table 5-2. The TCAN1462 Compared to the Nearest Competing Device**

| Parameter | Competing Device | TCAN1472 | End System Implication |
|---|---|---|---|
| VIO (logic supply) range | 3V to 5.5V | 1.7V to 5.5V | TI is future ready for 1.8V logic I/O support |
| SIC timing / Minimum Vod of 1.5V | Only meets with ±5% VCC | With ±10% VCC | TI does not need a tightly regulated supply to meet important SIC parameters required by standard |
| Bus fault protection | -36V to 40V | ±58V | A high bus fault means more resistant to faults. Also, TI supports bus faults for 24V systems, enabling reuse across platforms |
| ESD on bus pins | ±6kV | ±8kV | Higher ESD protection |
| Small outline transistor-23 package | No | Yes | TI offers a smaller footprint package option |

## 6. Benefits of CAN SIC

CAN SIC transceivers provide significant system benefits over regular CAN FD transceivers without the need for design changes on the physical or application layer. These transceivers enable operation at faster bit rates, with more freedom in choosing a network topology, while reducing vehicle cost and weight.

CAN SIC is interoperable with CAN FD and high-speed (HS) CAN nodes, so CAN SIC transceivers can operate on the same bus as CAN FD and HS CAN transceivers.

As shown in Table 1-1, CAN SIC transceivers significantly improve bit-timing symmetry, which enables more margin for any network effects that can deteriorate CAN signals. The transceiver introduces much less degradation to the transmitted and received bits, reducing the bit duration to operate reliably at 8 Mbps. And finally, the loop delay of CAN SIC transceivers is 190 ns max, compared to 255 ns max for CAN FD transceivers, helping extend the maximum network length.

## 7. Revision History

NOTE: Page numbers for previous revisions may differ from page numbers in the current version.

Changes from Revision \* (April 2022) to Revision A (October 2025):

- Added FlexRay trademark.
- Added Section 1 on newly released ISO 11898-2:2024 standardization.
- Added CiA trademark.
- Updated device list in Section 5.

---

## 附录:重要声明

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATA SHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.

These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you will fully indemnify TI and its representatives against, any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI's products are provided subject to TI's Terms of Sale or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products.

TI objects to and rejects any additional or different terms you may have proposed. IMPORTANT NOTICE.

Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265. Copyright © 2025, Texas Instruments Incorporated.
