---
title: 共模扼流圈(Common-mode Choke)
description: 串接在 CANH/CANL 上的共模电感,抑制共模干扰、改善 EMC,但会引入额外延迟。
tags: [进阶, 收发器]
---
- **定义**:共模扼流圈(Common-mode Choke, CMC)是串接在 CANH/CANL 两条总线线上的共模电感:对共模电流(两线同向)呈现高阻抗以抑制共模噪声,对差模信号(两线反向)呈现低阻抗以尽量不影响正常通信。
- **位置/背景**:安装在 PCB 上收发器与连接器(或总线)之间,是车载 CAN 节点 EMC 设计的标准组件;其寄生参数会影响信号上升/下降沿,并增加传播延迟。
- **作用与影响**:共模扼流圈显著降低共模发射并提高抗外部干扰能力(改善传导/辐射 EMC),但引入的额外传播延迟必须计入延迟预算,否则会消耗相位裕度;高速数据相位下需要选择寄生电容/漏感更小的型号。
- **参见**:
  - [emi-emc.md](emi-emc.md)、[bus-termination.md](bus-termination.md)、[loop-delay.md](loop-delay.md)
  - [NXP AH1308: CAN 应用提示](../resources/_entries/vendors/nxp-ah1308.md)
  - [IEC 62228-3(CAN 收发器 EMC 评估)](../resources/_entries/standards/iec-62228-3-2019.md)
