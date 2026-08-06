---
title: Controller Area Network (CAN) Bus Transceiver with Authentication Support
description: SMU 在 ISCAS 2022 设计并实现集成消息认证功能的 CAN 收发器芯片,安全机制不依赖(可能被攻破的)主机。
type: 论文
organization: SMU
year: 2022
access: paid
status: verified
download: link
priority: 1
audience: [模拟IC]
tags: [学术论文, 收发器, 网络, 安全]
source: "https://doi.org/10.1109/iscas48785.2022.9937839"

---

## 是什么
Xianshan Wen 等人 (Southern Methodist University, SMU) 在 2022 IEEE ISCAS 设计并实现一款将认证功能集成进物理层收发器的 CAN 收发器芯片,在收发器层面提供消息认证,让安全机制不依赖(可能被攻破的)主机,并给出电路实现与实测结果。

## 为什么值得读
- **模拟IC 工程师**:体现 CAN 收发器从纯模拟 PHY 走向"智能收发器"(集成 FD shield、认证、安全监控等数字功能)的趋势,可作为收发器片上数字功能集成的设计参照。
- **嵌入式开发工程师**:理解认证下沉到物理层的安全收益与实现代价。

## 核心内容要点
- 将认证功能集成进物理层收发器,在收发器层面提供消息认证。
- 安全机制不依赖(可能被攻破的)主机。
- 给出电路实现与实测结果,展示在满足 CAN 时序约束前提下嵌入认证逻辑的可行性。

## 怎么读
关注电路实现与实测结果部分,思考数字逻辑嵌入模拟收发器时如何满足 CAN 时序约束。

## 获取渠道
付费论文(IEEE):通过 IEEEXplore 按 DOI 访问,需机构订阅或单篇购买。
DOI: [10.1109/iscas48785.2022.9937839](https://doi.org/10.1109/iscas48785.2022.9937839)

## 参见
- [Realization of CAN FD Shielding in High Speed CAN Transceiver for Partial Networking](2021-pan-fd-shielding.md)
- [A highly-digitized automotive CAN transceiver in 0.14µm high-voltage SOI CMOS](2015-deloge-soi-cmos-transceiver.md)
- [资源库 — 论文](../../papers.md)
