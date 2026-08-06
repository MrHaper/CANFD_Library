---
title: Controller Area Network (CAN) Bus Transceiver with Authentication Support and Enhanced Rail Converters
description: "SMU 团队在开放获取期刊 Chips (MDPI) 发表的 CAN 收发器安全论文:以相位调制方式把帧级认证签名嵌入主数据并实时输出 GO/NO_GO 鉴权结果,附增强型轨转换器设计,已提供本地 PDF。"

type: 期刊
organization: 美国南卫理公会大学 SMU
year: 2024
access: free
status: verified
download: local
priority: 2
audience: [模拟IC]
tags: [期刊论文, 收发器, 网络, 安全]
source: "https://doi.org/10.3390/chips3040018"

local_file: files/journals/J2024_MDPI_Chips_CAN_transceiver_auth_enhanced_rail.pdf
---

## 是什么
Can Hong、Weizhong Chen、Xianshan Wen 等(美国南卫理公会大学 SMU)发表在开放获取期刊 Chips (MDPI) 2024 年 Vol.3, Issue 4(pp.361-378)的 CAN 收发器安全论文。采用"虚拟辅助数据信道"概念,以相位调制方式把帧级认证签名嵌入主数据,同时保持与现有 CAN 协议及非增强节点兼容,无需改动网络或软件;增强型轨转换器完成单轨/双轨数据转换并保持相位信息,抑制频率漂移、PVT 变化与线缆相位失配带来的相位误差。接收端同时恢复帧数据与签名,实时输出"GO/NO_GO"鉴权结果,且不超出 CAN 时钟抖动规范。

## 为什么值得读
- **模拟IC 工程师**:与 TCAS-I 论文(2025)同源(为其前身/扩展版本),但为**开放获取**,可免费全文阅读,便于细看电路实现。轨转换器与相位误差抑制对高速 CAN 物理层相位/抖动管理有直接启发。
- **嵌入式开发工程师**:理解帧级认证签名的嵌入与实时鉴权(GO/NO_GO)机制,认识物理层安全功能的实现代价。

## 核心内容要点
- 采用"虚拟辅助数据信道"概念,以相位调制方式把帧级认证签名嵌入主数据,无需改动网络或软件。
- 增强型轨转换器完成单轨/双轨数据转换并保持相位信息,抑制频率漂移、PVT 变化与线缆相位失配带来的相位误差。
- 接收端同时恢复帧数据与签名,实时输出"GO/NO_GO"鉴权结果,且不超出 CAN 时钟抖动规范。
- 保持与现有 CAN 协议及非增强节点兼容,可抵御报文注入等攻击。

## 怎么读
开放获取,已提供本地 PDF。建议与同源 TCAS-I 论文(2025)对照阅读:先看本条的完整电路实现,再回到 TCAS-I 看扩展的系统级验证与互操作测试。

[📄 下载本地 PDF](../../../files/journals/J2024_MDPI_Chips_CAN_transceiver_auth_enhanced_rail.pdf)

## 参见
- [Secure Controller Area Network (CAN) Transceiver With Embedded Authentication Support](2025-tcasi-secure-authentication-transceiver.md)(同源 TCAS-I 版本)
- [Controller Area Network (CAN) Bus Transceiver with Authentication Support](../papers/2022-wen-authentication-transceiver.md)(ISCAS 2022 同方向会议论文)
- [资源库 — 期刊](../../journals.md)
