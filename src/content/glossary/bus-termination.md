---
title: 总线终端(Bus Termination)
description: 在总线两端各接一个 120 Ω 终端电阻,与双绞线特征阻抗匹配以抑制反射。
tags: [入门, 收发器]
---
- **定义**:总线终端(Bus Termination)指在 CAN 总线物理两端(而非中间节点)各放置一个约 120 Ω 的终端电阻,使其与 120 Ω 特征阻抗的双绞线匹配,吸收到达末端的信号能量,抑制反射。
- **位置/背景**:CAN 网络为多点共享总线结构,终端电阻通常集成在两端节点的收发器引脚旁(部分收发器内置可切换终端);SAE J2284 与 OEM 规范对拓扑、桩线长度与终端位置有具体要求。
- **作用与影响**:缺少或错放终端会造成信号反射、振铃、眼图收窄与采样错误;终端电阻值也影响显性电平幅度与功耗。CAN SIC 网络支持改善的终端方案,但标准两端 120 Ω 仍是基线配置,是排查"长总线高速率下位错误"时的首要检查项。
- **参见**:
  - [return-loss.md](return-loss.md)、[ringing-suppression.md](ringing-suppression.md)、[common-mode-choke.md](common-mode-choke.md)
  - [SAE J2284-4(500 kbps 仲裁 + 2 Mbps 数据)](../resources/_entries/standards/sae-j2284-4-2016.md)
  - [Hancock 2020: Characterizing the physical layer of CAN FD](../resources/_entries/papers/2020-hancock-physical-layer.md)
