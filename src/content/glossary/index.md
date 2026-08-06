---
title: 术语表
description: CAN/CAN FD 协议、物理层、位定时与工具术语的中文释义与中英对照,按字母 A-Z 索引。
tags: [术语表]
---
# 术语表

本术语表覆盖 **CAN / CAN FD 协议、物理层、位定时与工具** 等领域的核心术语,按字母 A-Z 分组索引。每条词条包含:定义、位置/背景、作用与影响、参见(相关词条与资源)。难度标签:入门 / 进阶 / 专家。

> 技术内容以 ISO 11898-1/-2、CiA 文档与厂商数据手册为准;涉及具体数值(如采样点百分比、延迟指标)处均注明"视配置/以标准与器件手册为准"。

## A

- [ACK 场(ACK Slot)](ack-slot.md) — 帧尾确认机制
- [AEC-Q100(车规 IC 可靠性认证)](aec-q100.md) — 车规 IC 可靠性压力测试标准
- [仲裁(Arbitration)](arbitration.md) — 多节点总线竞争机制

## B

- [比特率(Bit Rate)](bit-rate.md) — 单位时间传输的位数
- [位填充(Bit Stuffing)](bit-stuffing.md) — 防止长串相同位的编码规则
- [位时间(Bit Time)](bit-time.md) — 一位的标称持续时间与段划分
- [BRS(Bit Rate Switch)](brs.md) — 数据相位高速率切换标志位
- [Bus-off(离线状态)](bus-off.md) — 节点错误计数超限后的隔离状态
- [总线终端(Bus Termination)](bus-termination.md) — 两端 120 Ω 终端匹配
- [BusMaster(开源 CAN 分析工具)](busmaster.md) — Windows 平台开源分析软件

## C

- [can-utils(CAN 调试工具集)](can-utils.md) — Linux 命令行 CAN 工具
- [CAN FD(CAN with Flexible Data-rate)](can-fd.md) — 可变数据速率 CAN 协议
- [CAN SIC(Signal Improvement Capability)](can-sic.md) — 信号改善能力收发器
- [CAN XL(第三代 CAN)](can-xl.md) — 2048 字节数据字段的下一代 CAN
- [CANopen FD(CAN FD 高层协议)](canopen-fd.md) — CiA 1301 应用层规范
- [CiA 601 系列(CAN FD 节点与系统设计)](cia-601.md) — 设计与评估指南
- [CISPR 25(车辆无线电骚扰限值标准)](cispr25.md) — 车载发射限值与测量
- [Classical CAN(经典 CAN / CAN 2.0)](classical-can.md) — 原始 CAN 协议
- [共模扼流圈(Common-mode Choke)](common-mode-choke.md) — 共模滤波组件
- [共模范围(Common-mode Range)](common-mode-range.md) — 接收器共模容忍能力
- [CRC(循环冗余校验,17/21 位)](crc.md) — 帧错误检测字段

## D

- [DBC(数据库文件)](dbc.md) — CAN 网络描述文件格式
- [DLC(Data Length Code)](dlc.md) — 4 位数据长度码
- [显性/隐性电平(Dominant/Recessive Levels)](dominant-recessive-levels.md) — 总线差分两级电平

## E

- [EDL(Extended Data Length)](edl.md) — CAN FD 帧格式标志位
- [EMI / EMC(电磁干扰 / 电磁兼容)](emi-emc.md) — 发射与抗扰度
- [错误帧(Error Frame)](error-frame.md) — 故障广播机制
- [ESD(静电放电)](esd.md) — 静电损伤与防护
- [ESI(Error State Indicator)](esi.md) — 发送方错误状态标志位

## I

- [IEC 62228-3(IC 级收发器 EMC 评估)](iec-62228-3.md) — 芯片级 EMC 测试标准
- [ISO 11898-1(数据链路层 + 物理编码子层)](iso-11898-1.md) — 帧格式与位定时权威标准
- [ISO 11898-2(高速物理介质连接子层)](iso-11898-2.md) — 收发器要求与 CAN SIC
- [ISO 16845(CAN 一致性测试计划)](iso-16845.md) — 协议与收发器一致性测试

## L

- [环路延迟(Loop Delay)](loop-delay.md) — TxD→总线→RxD 总延迟

## O

- [过载帧(Overload Frame)](overload-frame.md) — 流量控制与过载报告

## P

- [相位裕度(Phase Margin)](phase-margin.md) — 采样点的可容忍相位偏差
- [plugfest(互操作性测试活动)](plugfest.md) — 多厂商实测互操作
- [传播延迟对称性(Tx/Rx Delay Symmetry)](propagation-delay-symmetry.md) — 收发器双向延迟之差
- [传播段(Propagation Segment)](propagation-segment.md) — 传播延迟补偿段
- [python-can(CAN 访问库)](python-can.md) — 跨平台 Python CAN 库

## R

- [重同步跳转宽度(RJW / SJW)](re-sync-jump-width.md) — 重同步最大调整量
- [远程帧(Remote Frame)](remote-frame.md) — 请求数据的无数据帧
- [回波损耗(Return Loss)](return-loss.md) — 阻抗匹配度量
- [振铃抑制(Ringing Suppression)](ringing-suppression.md) — SIC 核心信号改善能力

## S

- [采样点(Sample Point)](sample-point.md) — 总线电平采样时刻
- [压摆率(Slew Rate)](slew-rate.md) — 输出沿陡峭程度
- [SocketCAN(Linux CAN 子系统)](socketcan.md) — 内核 CAN 协议栈
- [同步段(Sync Segment)](sync-segment.md) — 位时间第一段

## T

- [TDC(Transmitter Delay Compensation)](tdc.md) — 数据相位收发器延迟补偿
- [时间量子(Time Quantum, TQ)](time-quantum.md) — 位定时最小单位
- [收发器(Transceiver)](transceiver.md) — 控制器与总线之间的接口芯片

---

## 按主题速查

- **帧与协议**:[CAN FD](can-fd.md) · [Classical CAN](classical-can.md) · [EDL](edl.md) · [BRS](brs.md) · [ESI](esi.md) · [DLC](dlc.md) · [CRC](crc.md) · [位填充](bit-stuffing.md) · [错误帧](error-frame.md) · [仲裁](arbitration.md) · [TDC](tdc.md)
- **位定时**:[时间量子](time-quantum.md) · [位时间](bit-time.md) · [采样点](sample-point.md) · [相位裕度](phase-margin.md) · [传播段](propagation-segment.md) · [重同步跳转宽度](re-sync-jump-width.md)
- **物理层与收发器**:[CAN SIC](can-sic.md) · [振铃抑制](ringing-suppression.md) · [回波损耗](return-loss.md) · [传播延迟对称性](propagation-delay-symmetry.md) · [共模范围](common-mode-range.md) · [显性/隐性电平](dominant-recessive-levels.md) · [总线终端](bus-termination.md) · [EMC/CISPR 25](cispr25.md) · [IEC 62228-3](iec-62228-3.md) · [AEC-Q100](aec-q100.md) · [收发器](transceiver.md)
- **工具与标准**:[SocketCAN](socketcan.md) · [DBC](dbc.md) · [CANopen FD](canopen-fd.md) · [ISO 11898-1](iso-11898-1.md) · [ISO 11898-2](iso-11898-2.md) · [ISO 16845](iso-16845.md) · [CiA 601](cia-601.md) · [plugfest](plugfest.md)
