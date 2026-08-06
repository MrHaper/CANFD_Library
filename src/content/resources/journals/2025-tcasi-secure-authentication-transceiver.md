---
title: Secure Controller Area Network (CAN) Transceiver With Embedded Authentication Support
description: "南卫理公会大学在 TCAS-I 发表的 CAN 收发器芯片级安全论文:通过 NRZ 波形上升沿选择性延迟,在物理层叠加与每帧同时传输的认证签名信道,0.18µm CMOS 流片并验证向后兼容。"

type: 期刊
organization: 美国南卫理公会大学 SMU,电气与计算机工程系 / 计算机科学系
year: 2025
access: paid
status: verified
download: link
priority: 2
audience: [模拟IC]
tags: [期刊论文, 收发器, 网络, 安全]
source: "https://doi.org/10.1109/TCSI.2025.3538844"

---

## 是什么
Weizhong Chen、Xianshan Wen、Can Hong 等(美国南卫理公会大学 SMU,电气与计算机工程系 / 计算机科学系)发表在 IEEE Transactions on Circuits and Systems I: Regular Papers (TCAS-I) 2025 年 Vol.72(pp.3753-3765)的芯片级论文。汽车与工业控制总线安全威胁增多,促使在保持既有标准兼容的前提下设计带增强安全功能的 CAN 总线组件。本文用新型收发器替换标准 CAN 收发器,实现对 CAN 帧的自动认证:通过在 NRZ 波形中选择性延迟上升沿,在物理层"虚拟"叠加一条与每帧同时传输认证签名的辅助通信信道。电路采用 0.18µm CMOS 工艺流片,并完成 PVT 角与同非安全收发器互操作的验证,证明向后兼容。

## 为什么值得读
- **模拟IC 工程师**:TCAS-I 上少见的 CAN 收发器芯片级论文。上升沿延迟调制/解调、轨转换器相位保持、时钟抖动预算约束等设计点,对 SIC 收发器物理层(边沿斜率、时序裕量、抖动、总线信号质量)设计均有借鉴价值;同时展示了"收发器层做安全功能"这一趋势。
- **嵌入式开发工程师**:理解"认证下沉到物理层"的安全收益——安全机制不依赖(可能被攻破的)主机。

## 核心内容要点
- 用新型收发器替换标准 CAN 收发器,实现对 CAN 帧的自动认证。
- 通过在 NRZ 波形中选择性延迟上升沿,在物理层"虚拟"叠加一条与每帧同时传输认证签名的辅助通信信道。
- 电路包含认证签名生成器/比较器、上升沿时间域调制/解调电路与相位保持型轨转换器。
- 采用 0.18µm CMOS 工艺流片,完成 PVT 角与同非安全收发器互操作验证,证明向后兼容。

## 怎么读
付费期刊论文。建议先通读认证签名叠加的基本原理,再重点看上升沿时间域调制/解调电路与轨转换器的相位保持设计,最后对照同源开放获取版本(Chips 2024,见参见)细看电路实现。

## 获取渠道
付费论文(IEEE):通过 IEEEXplore 按 DOI 访问,需机构订阅或单篇购买。
DOI: [10.1109/TCSI.2025.3538844](https://doi.org/10.1109/TCSI.2025.3538844)

## 参见
- [Controller Area Network (CAN) Bus Transceiver with Authentication Support and Enhanced Rail Converters](2024-chips-authentication-rail-converters.md)(同源开放获取版本)
- [Controller Area Network (CAN) Bus Transceiver with Authentication Support](../papers/2022-wen-authentication-transceiver.md)(ISCAS 2022 同方向会议论文)
- [资源库 — 期刊](../../journals.md)
