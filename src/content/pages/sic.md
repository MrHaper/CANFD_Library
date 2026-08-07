---
title: SIC 专题
description: CAN SIC(Signal Improvement Capability)收发器完整专题——振铃机理、三方面改进、关键参数、芯片设计、振铃抑制电路与测试验证,全部内容与 22 张原创技术图整合为站内一页。
tags: [SIC, 模拟IC, 专家]
search: { boost: 2 }
---

# CAN SIC 专题

> 本页把 SIC 收发器的**原理 → 设计 → 测试**完整知识整合为一页,所有关键数值提取自一手资料(ISO 11898-2:2024、TI SLLA581、NXP TJA1463、Adamson 2020 iCC 论文等)并标注出处。配套的模块化设计要点见[设计参考](../design/index.md)。

## 1. 知识地图

![图 17 CAN 知识体系总览](../files/sic-design/images/fig17_can_mindmap.svg)

*图 17:CAN 知识体系总览(SIC 位于"物理层 → 收发器芯片"交汇处)*

![图 18 CAN SIC 全流程知识体系](../files/sic-design/images/fig18_sic_mindmap.svg)

*图 18:SIC 全流程知识体系——原理 → 设计 → 测试*

## 2. 为什么需要 SIC:振铃机理

### 2.1 高速瓶颈

CAN 网络最大的优势是易扩展,但网络复杂化后(星型拓扑、多 stub),未端接 stub 的阻抗突变点产生反射,反射波在网络中来回振荡形成**振铃**。常规 CAN FD 收发器额定支持 5 Mbit/s,但在真实车载网络(长 stub、星型拓扑)中通常只能用到 <2 Mbit/s——因为 5 Mbit/s 数据相位位时间仅 200 ns,振铃在采样点前无法衰减干净。

![图 1 总线振铃现象对比](../files/sic-design/images/fig1_ringing_compare.svg)

*图 1:常规 CAN FD 在显性→隐性转换后振铃越阈;CAN SIC 有源隐性快速压振铃*

![图 4 星型拓扑与 stub 反射](../files/sic-design/images/fig4_star_topology.svg)

*图 4:未端接 stub 末端产生反射,反射波沿 stub 返回总线来回振荡*

### 2.2 为什么隐性位最脆弱

- **显性位**:驱动器低阻(约 50 Ω 量级)强制驱动,信号受控;
- **隐性位**:输出级高阻(约 60 kΩ),总线靠 60 Ω 端接电阻对分布电容放电,无主动驱动;
- 因此**显性→隐性转换是最脆弱的边沿**,任何反射都叠加在 RC 放电曲线上。

![图 12 物理层电平与接收判定](../files/sic-design/images/fig12_levels.svg)

*图 12:显性/隐性电平与接收判定阈值(0.5 V 隐性 / 0.9 V 显性 / ~0.7 V 实际翻转点)*

### 2.3 判据:Allowable Ringing Time

隐性位信号必须在**最早可能采样点之前**降到 0.5 V 以下;这段可允许的振荡时间即 **Allowable Ringing Time**(Adamson 2020)。

![图 5 安全操作区与采样点](../files/sic-design/images/fig5_safe_area.svg)

*图 5:信号可在安全操作区内自由振荡,但必须在最早采样点前回到 0.5 V 以下*

## 3. SIC 的三方面改进与关键参数

CAN SIC 是在 CAN FD 收发器上增加的信号改善能力,三方面协同:

| 改进 | 内容 | 关键参数 |
| --- | --- | --- |
| ① 时序对称性 | tBit/tREC 比常规 CAN FD 收紧约 60 ns | tBit(Bus) −10~+10 ns;tBit(RxD) −30~+20 ns;tREC −20~+15 ns |
| ② 有源隐性驱动 | 显性→隐性后以中等阻抗主动放电 | RDIFF_act_rec 75~133 Ω;tact_rec_start ≤120 ns;tact_rec_end ≥355 ns;tpas_rec_start ≤530 ns |
| ③ 振铃抑制电路 | 各厂商专利方案加速衰减 | nulling/检测阻尼/阻抗匹配 |

![图 2 SIC 事件时序](../files/sic-design/images/fig2_sic_timing.svg)

*图 2:显性 → 有源隐性 → 被动隐性三相位时序(ISO 11898-2:2024 Set C)*

!!! note "与位时间的关系"
    5 Mbit/s 数据相位位时间 200 ns,有源隐性覆盖整个隐性位;仲裁相位(如 1 Mbit/s)多位同时发送时,显性位必须能覆盖隐性位,因此窗口上限 530 ns 会限制仲裁速率与网络长度。

## 4. 标准演进

SIC 最早标准化于 CiA 601-4(2019);2023 年 601-4 撤回并入 **ISO 11898-2:2024 第三版**(参数集 Set A/B/C);2024 版 Annex A 引入 FAST 模式与 CAN XL 兼容。

![图 6 SIC 标准演进](../files/sic-design/images/fig6_standard_evolution.svg)

*图 6:CiA 601-4 → ISO 11898-2:2024,参数集 Set A/B/C 与 Annex A*

## 5. 协议与位定时上下文

SIC 设计必须放在协议与位定时语境中理解(帧结构、BRS 速率切换、TDC、错误处理):

![图 7 经典 CAN vs CAN FD 帧格式](../files/sic-design/images/fig7_can_fd_frames.svg)

*图 7:经典 CAN 与 CAN FD 帧格式,EDL/BRS/ESI 三个标志位*

![图 8 位时间结构与采样点](../files/sic-design/images/fig8_bit_timing.svg)

*图 8:位时间结构与采样点(PS1/PS2 边界)*

![图 9 非破坏性位仲裁](../files/sic-design/images/fig9_arbitration.svg)

*图 9:显性覆盖隐性的非破坏性仲裁*

![图 10 故障遏制状态机](../files/sic-design/images/fig10_error_states.svg)

*图 10:error-active / error-passive / bus-off 状态机*

![图 11 TDC 发射器延迟补偿原理](../files/sic-design/images/fig11_tdc.svg)

*图 11:TDC 与二次采样点 SSP——环回延迟 ≤190 ns 是 SIC 设计约束之一*

![图 14 总线唤醒时序](../files/sic-design/images/fig14_wakeup.svg)

*图 14:基本唤醒 / WUP / WUF 时序*

![图 16 网络拓扑类型与端接](../files/sic-design/images/fig16_topologies.svg)

*图 16:总线型 / 星型 / 菊花链与端接经验法则*

![图 19 CAN FD 帧结构思维导图](../files/sic-design/images/fig19_frame_mindmap.svg)

*图 19:CAN FD 帧结构思维导图*

## 6. 芯片架构

SIC 收发器由驱动控制逻辑、输出级、SIC 控制逻辑、接收器、电源管理与保护组成:

![图 3 收发器芯片架构](../files/sic-design/images/fig3_transceiver_arch.svg)

*图 3:CAN SIC 收发器芯片架构*

![图 20 物理层指标体系思维导图](../files/sic-design/images/fig20_phys_mindmap.svg)

*图 20:物理层指标体系(时序/电平/SIC 专项/EMC/测量条件)*

![图 21 收发器芯片设计要点思维导图](../files/sic-design/images/fig21_design_mindmap.svg)

*图 21:收发器芯片设计要点思维导图*

## 7. 模块设计要点

### 7.1 输出级(三态阻抗)

| 相位 | 输出阻抗 | 驱动行为 | 设计要点 |
| --- | --- | --- | --- |
| 显性 | 低(约 50 Ω 量级) | 强制驱动差分 | 大电流、低 Ron、对称灌/拉 |
| 有源隐性 | 75~133 Ω(RDIFF_act_rec) | 主动向隐性放电 | 阻抗精确可控、可编程/校准 |
| 被动隐性 | 约 60 kΩ | 高阻,总线自然放电 | 高阻漏电小、与仲裁兼容 |

详见[输出级设计要点](../design/output-stage.md)。

### 7.2 振铃抑制电路

各厂商在有源隐性基础上,还加专门的振铃抑制电路:

| 路线 | 代表专利 | 思路 |
| --- | --- | --- |
| 隐性抵消 | TI US9606948B2 | 跳变时并联低阻分数驱动器加速泄放;LRN/HRN/混合可编程 |
| 瞬态触发阻尼 | TI US11310072B2 | 振铃经电容耦合到 NMOS 栅极,超阈值导通泄放 |
| 阻抗匹配+分段斜率 | Microchip US11539548B2 | 隐性过渡期接入匹配阻抗 + 延迟线逐级关断电流源 |
| 前馈/振荡抑制 | NXP US10020841B2、Bosch US11068429B2 | 前馈预测边沿/振荡抑制单元 |

![图 15 振铃抑制电路原理](../files/sic-design/images/fig15_ring_suppress_circuit.svg)

*图 15:振铃抑制电路原理(recessive nulling + 振铃检测阻尼)*

详见[振铃抑制电路设计要点](../design/ring-suppression.md)。

### 7.3 SIC 控制逻辑

- 检测 TXD 显性→隐性边沿,生成有源隐性窗口(tact_rec_start ≤120 ns / tact_rec_end ≥355 ns / tpas_rec_start ≤530 ns);
- 阻抗切换必须 glitch-free;TXD 变 LOW 立即回显性(仲裁覆盖);
- 窗口建议可编程/校准,覆盖 PVT。

详见[SIC 控制逻辑设计要点](../design/sic-control.md)。

### 7.4 接收器与 ESD/电源

- 接收比较器:阈值 0.5~0.9 V、迟滞 ≥100 mV、共模 −12~+12 V、ΔtRec −20~+15 ns;详见[接收比较器设计要点](../design/receiver.md);
- ESD/总线保护:片内两级保护、输入衰减网络与 80V 耐压设计;详见[ESD 与总线保护设计要点](../design/esd-protection.md);
- 电源/唤醒:UVLO、VIO、WUP/WUF 与 CAN FD passive;详见[电源与唤醒设计要点](../design/power-wake.md)。

## 8. 测试与验证

![图 13 HS-PMA 标准测试电路](../files/sic-design/images/fig13_test_circuit.svg)

*图 13:HS-PMA 标准测试电路(RL=60 Ω、C2=100 pF、CRXD=15 pF)*

![图 22 验证测试体系思维导图](../files/sic-design/images/fig22_test_mindmap.svg)

*图 22:验证测试体系(芯片级参数 → 一致性 → EMC → 网络级 → 测试计划)*

### 8.1 芯片级参数测量

| 参数 | 符号 | 测量方法 | 指标(Set C) |
| --- | --- | --- | --- |
| 环回延迟 | tLoop | TXD 边沿 → RXD 边沿 | ≤190 ns |
| 发送隐性位宽偏差 | tBit(Bus) | 总线隐性位宽与 TXD 理想位宽比较 | −10~+10 ns |
| 接收时序对称性 | tREC | RXD 位宽偏差 | −20~+15 ns |
| SIC 窗口 | tact_rec_start/end、tpas_rec_start | 示波器测量总线阻抗/波形拐点 | ≤120 / ≥355 / ≤530 ns |

### 8.2 一致性 / EMC / 网络级

- 一致性:ISO 16845-1/-2、ISO 11898-2:2024 Set C、CiA plugfest;
- EMC:IEC 62228-3、CISPR 25;
- 网络级:多节点星型拓扑实测(0.5 V 判据)、Safe Operating Area 仿真+台架、位模式 1D1R+5D1R+1D1R。

## 9. 常见陷阱

- 只做 TX 侧或只做 RX 侧且不验证混用网络;
- tSIC 窗口过短(振铃未衰减完)或过长(挤占位时间/妨碍仲裁);
- 有源隐性阻抗偏离 75~133 Ω(偏小加载总线、偏大失去阻尼);
- nulling 终止晚于采样点;
- 8 Mbit/s 下环回延迟对称性不足;
- 未实现 CAN FD passive 导致睡眠节点误唤醒。

## 10. 配套资源

- 设计参考总览:[../design/index.md](../design/index.md)
- 知识库 SIC 专题(三篇拆分版):[原理篇](../knowledge/sic-design/principle.md)、[设计篇](../knowledge/sic-design/design.md)、[测试篇](../knowledge/sic-design/testing.md)
- 关键规范:[ISO 11898-2:2024](../resources/standards/iso-11898-2-2024.md)、[Bosch CAN FD Spec](../resources/standards/bosch-2012-canfd-spec.md)
- 厂商资料:[TI SLLA581 白皮书全文](../resources/full-text/slla581-white-paper.md)、[NXP TJA1463 数据手册全文](../resources/full-text/tja1463-datasheet.md)
- 专利全文:[US9606948B2](../resources/full-text/us9606948b2-recessive-nulling.md)、[US11310072B2](../resources/full-text/us11310072b2-ring-suppression.md)、[US11539548B2](../resources/full-text/us11539548b2-microchip-sic.md)
