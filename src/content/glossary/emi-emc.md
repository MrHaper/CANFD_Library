---
title: EMI / EMC(电磁干扰 / 电磁兼容)
description: EMI 是设备产生的非期望电磁发射;EMC 是设备在电磁环境中正常工作且不干扰他人的能力。
tags: [进阶, 收发器]
---
- **定义**:EMI(Electromagnetic Interference,电磁干扰)指设备产生的非期望电磁发射,可能干扰其他设备;EMC(Electromagnetic Compatibility,电磁兼容)指设备在其电磁环境中正常工作且不对环境产生不可承受干扰的能力,涵盖发射(EMI)与抗扰度(Immunity)两个方向。
- **位置/背景**:在 CAN FD 语境中,EMC 主要落在收发器与 PCB 层:收发器输出沿、共模扼流圈、PCB 布局与屏蔽决定发射水平;ISO 11452 系列(整车级抗扰度)与 IEC 62228-3(IC 级测试)规定测试方法,CISPR 25 规定发射限值。
- **作用与影响**:车规级 CAN 节点必须通过发射与抗扰度测试;高速数据相位带来的陡峭边沿会恶化 EMI,因此 SIC 收发器的沿整形与共模滤波是 EMC 设计关键。EMC 问题通常在系统集成阶段暴露,设计阶段就应预留测试板与滤波措施。
- **参见**:
  - [cispr25.md](cispr25.md)、[iec-62228-3.md](iec-62228-3.md)、[common-mode-choke.md](common-mode-choke.md)、[slew-rate.md](slew-rate.md)
  - [IEC 62228-3(CAN 收发器 EMC 评估)](../resources/_entries/standards/iec-62228-3-2019.md)
  - [Nishida 2022: EMC 评估](../resources/_entries/papers/2022-nishida-emc-evaluation.md)
