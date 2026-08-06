---
title: 示波器 + CAN/CAN FD 解码
description: 观察总线波形、眼图、振铃、位定时;多数高端示波器自带 CAN FD 触发与解码
type: 工具
organization: Keysight / Tektronix / R&S
access: paid
status: verified
download: link
priority: 1
audience: [模拟IC]
tags: [硬件设备]
source: "https://www.keysight.com"

---

## 是什么
带 CAN / CAN FD 触发与解码功能的**示波器**(Keysight、Tektronix、R&S 等厂商),用于观察总线波形、眼图、振铃与位定时;多数高端示波器自带 CAN FD 触发与协议解码,是物理层验证的核心设备。

## 为什么值得读
- **模拟IC 工程师**:观察总线波形、眼图、振铃、位定时,是 SIC 收发器物理层验证的必备手段。
- **嵌入式开发工程师**:用示波器解码定位协议/时序问题,与逻辑分析仪互补。

## 核心内容要点
- **用途**:抓取总线波形/眼图/振铃,验证位定时与信号完整性;多数高端示波器自带 CAN FD 触发与解码。
- **免费/付费**:付费(硬件设备,按需选型/实验室配备)。
- **适用场景**:测试——物理层信号验证。
- 选型要点:带宽、采样率、CAN FD 触发解码能力、眼图/测量功能。

## 怎么读
按 07 工具与社区 README 第五节建议:示波器抓 dominant→recessive 边沿,对比普通 CAN FD 与 SIC 收发器(如 TJA1463 vs TJA1044)的振铃差异,直观理解 SIC 价值。

## 获取渠道
Keysight 官网(示波器选型):<https://www.keysight.com>;Tektronix、R&S 官网同样可查示波器产品与 CAN 解码选件(资料库暂以 Keysight 为默认来源)。

## 参见
- [阻抗/网络分析仪](impedance-network-analyzer.md)
- [EMC 测试系统(传导发射 / 抗扰度)](emc-test-system.md)
- [资源库 — 工具与社区](../../tools-community.md)
