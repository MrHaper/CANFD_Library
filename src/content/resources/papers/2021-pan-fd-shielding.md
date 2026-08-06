---
title: Realization of CAN FD Shielding in High Speed CAN Transceiver for Partial Networking
description: ISNE 2021 论文,在支持部分网络的高速 CAN 收发器中实现 CAN FD Shielding (FD shield) 功能,非目标报文时保持总线静止以降低功耗。
type: 论文
organization: IEEE
year: 2021
access: paid
status: verified
download: link
priority: 1
audience: [模拟IC]
tags: [学术论文, CAN FD, 收发器, 网络]
source: "https://doi.org/10.1109/isne48910.2021.9493645"

---

## 是什么
Jian Pan、Liang Xie、Xiangliang Jin 在 2021 年第 9 届下一代电子国际研讨会 (ISNE 2021) 发表的论文,在支持部分网络 (Partial Networking) 的高速 CAN 收发器中实现 CAN FD Shielding (FD shield) 功能:通过识别 CAN FD 报文特征,在非目标报文(如非唤醒报文)时保持总线静止,降低功率。

## 为什么值得读
- **模拟IC 工程师**:FD shield 是 SIC 之外另一种重要的智能收发器功能,与部分网络唤醒、低功耗模式相关,是收发器功能集设计(数字状态机 + 模拟前端协同)的参考案例。
- **嵌入式开发工程师**:理解部分网络与 FD shield 对整车功耗管理的意义。

## 核心内容要点
- 在支持部分网络的高速 CAN 收发器中实现 CAN FD Shielding (FD shield) 功能。
- 通过识别 CAN FD 报文特征,在非目标报文(如非唤醒报文)时保持总线静止,降低功率。
- 给出实现结构与验证结果。

## 怎么读
重点看 FD shield 的实现结构与报文识别逻辑,思考数字状态机与模拟前端的接口划分。

## 获取渠道
付费论文(IEEE):通过 IEEEXplore 按 DOI 访问,需机构订阅或单篇购买。
DOI: [10.1109/isne48910.2021.9493645](https://doi.org/10.1109/isne48910.2021.9493645)

## 参见
- [Controller Area Network (CAN) Bus Transceiver with Authentication Support](2022-wen-authentication-transceiver.md)
- [资源库 — 论文](../../papers.md)
