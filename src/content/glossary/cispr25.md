---
title: CISPR 25(车辆无线电骚扰限值标准)
description: 车辆、船舶与内燃机驱动装置无线电骚扰特性的测量方法与限值标准,车载电子必测。
tags: [进阶, 收发器]
---
- **定义**:CISPR 25《车辆、船舶和内燃机驱动装置—无线电骚扰特性—用于保护车载接收机的限值和测量方法》规定了车载电子部件/整车的传导发射与辐射发射测量方法、频段划分与限值,是车载 EMC 领域的核心标准之一。
- **位置/背景**:CISPR 25 属于整车与部件级 EMC 规范(与 IC 级的 IEC 62228-3 互补);测量通常在电波暗室中进行,频段覆盖 AM/FM 广播等长波到短波范围,并延伸至更高频段。
- **作用与影响**:CAN 收发器网络的发射水平(尤其高速数据相位的高频分量)必须满足 CISPR 25 限值,否则整车型式认证失败;设计阶段需结合共模扼流圈、PCB 布局与收发器沿整形进行发射预估,是车载项目 EMC 验收的必经环节。
- **参见**:
  - [emi-emc.md](emi-emc.md)、[iec-62228-3.md](iec-62228-3.md)、[common-mode-choke.md](common-mode-choke.md)
  - [IEC 62228-3(CAN 收发器 EMC 评估)](../resources/_entries/standards/iec-62228-3-2019.md)
  - [Mizoguchi 2024: 抗扰度评估](../resources/_entries/papers/2024-mizoguchi-immunity-evaluation.md)
