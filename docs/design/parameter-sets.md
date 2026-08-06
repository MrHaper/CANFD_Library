---
title: 参数集与规格基线
description: ISO 11898-2:2024 参数集 A/B/C 与 Annex A(FAST)的规格基线——速率档位、SIC 强制要求、关键参数差异与产品对标层次。
tags: [设计参考, 模拟IC, 专家]
---

# 参数集与规格基线

## 一档速览

| 参数集 | 数据相位速率上限 | 强制能力 | 典型应用 |
| --- | --- | --- | --- |
| Set A | ≤ 2 Mbit/s | 经典 CAN FD | 常规车载 CAN FD 节点 |
| Set B | ≤ 5 Mbit/s | CAN FD 高速数据相位 | 高速 CAN FD 网络 |
| Set C | ≤ 8 Mbit/s | **CAN SIC(信号改善能力)** | 复杂拓扑下的高速 SIC 收发器 |
| Annex A | FAST 模式(≤ 20 Mbit/s 量级) | CAN XL 兼容、SIC 向后兼容 | 下一代 CAN XL 节点(可选叠加) |

!!! note "以标准原文为准"
    不同资料对参数集档位的文字描述略有出入,设计前请以 ISO 11898-2:2024 正文与官方勘误(CiA 140)为准。本站 SIC 专题的数值(Set C 时序窗口、RDIFF_act_rec 等)均取自该口径。

## 设计规格的三个层次

| 层次 | 内容 | 判定依据 |
| --- | --- | --- |
| 基线兼容 | 满足 ISO 11898-2:2024 参数集 A/B/C 电气参数 | ISO 11898-2:2024 |
| SIC 能力 | 有源隐性驱动和/或接收端振铃滤波,抑制显性→隐性振铃 | ISO 11898-2:2024 Set C / Annex A(CiA 601-4 已并入) |
| 产品扩展 | 8 Mbit/s、VIO、低功耗、选择性唤醒、故障诊断等 | TJA146x、TCAN147x 产品规格 |

对标建议:先锁"基线兼容"档位,再决定 SIC 实现路线(TX 侧有源隐性 / RX 侧滤波 / 两者结合),最后按产品定位叠加扩展功能。

## Set C(SIC)关键参数基线

| 参数 | 符号 | 规格 | 设计含义 |
| --- | --- | --- | --- |
| 环回延迟 | tLoop | ≤ 190 ns | 输出级 + 接收器延迟总和,决定 TDC 裕量 |
| TXD→总线延迟 | tprop(TXD_BUS) | ≤ 80 ns | 输出级/预驱动延迟预算 |
| 总线→RXD 延迟 | tprop(BUS_RXD) | ≤ 110 ns | 接收比较器 + RXD 输出级预算 |
| 发送隐性位宽偏差 | ΔtBit(Bus) | −10 ~ +10 ns | 输出级边沿对称性与窗口精度 |
| 接收位宽偏差 | ΔtBit(RxD) | −30 ~ +20 ns | 比较器上升/下降延迟对称 |
| 接收时序对称性 | ΔtRec | −20 ~ +15 ns | 比较器群延迟对称 |
| 有源隐性开始 | tact_rec_start | ≤ 120 ns | SIC 控制逻辑响应时间 |
| 有源隐性结束 | tact_rec_end | ≥ 355 ns | 有源驱动最短保持时间 |
| 被动隐性开始 | tpas_rec_start | ≤ 530 ns | 切换回高阻的最晚时刻 |
| 有源隐性差分阻抗 | RDIFF_act_rec | 75 ~ 133 Ω | 阻尼效果与总线负载的折衷 |

!!! warning "规格≠设计目标"
    上表是**下限/上限规格**,不是设计目标。工程上应留 PVT 余量:例如 tLoop 设计目标建议 ≤ 170 ns、ΔtBit(Bus) 目标 ±6 ns,以覆盖工艺角、温度(−40~150 °C)与电压漂移。

## Annex A(FAST/CAN XL)要点

- FAST 模式收发器需支持 level_0 / level_1 差分电平判别(表 A.6/A.7),接收器需要 **OOB(Out-of-Bounds)比较器**与状态机,避免把 CAN XL 电平误报为 CAN FD 毛刺。
- 若产品声明与 CAN XL 共存,还需评估显性/隐性判决窗口、输入共模范围与 EMI 的叠加要求。
- 详细数值见[ISO 11898-2:2024 关键参数速查](../resources/standards-text/iso-11898-2-2024-key-parameters.md)。

## 参见

- [时序链路预算](timing-budget.md) —— 把上表数值拆到模块
- [输出级设计要点](output-stage.md) / [接收比较器设计要点](receiver.md) / [SIC 控制逻辑设计要点](sic-control.md)
- 知识库:[物理层与 SIC](../knowledge/physical-layer/index.md)、[SIC 设计专题·原理篇](../knowledge/sic-design/principle.md)
- 资源:[ISO 11898-2:2024 条目](../resources/_entries/standards/iso-11898-2-2024.md)、[CiA 140 勘误](../resources/_entries/standards/cia-140-corrigendum.md)、[TJA1463 数据手册全文](../resources/full-text/tja1463-datasheet.md)
