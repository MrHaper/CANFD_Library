---
title: ESD(静电放电)
description: 静电积累导致的瞬间放电,可损伤收发器引脚;车规器件按 HBM/CDM 与整车线束等级防护。
tags: [入门, 收发器]
---
- **定义**:ESD(Electrostatic Discharge,静电放电)指静电积累后通过器件引脚瞬间释放的高压电流,可能造成栅氧击穿、结损伤或闩锁。CAN 收发器按标准模型分级防护:人体模型(HBM,典型 ≥ ±8 kV)、充电器件模型(CDM)与 ISO 10605(整车环境线束放电)等。
- **位置/背景**:CANH/CANL 直接暴露于线束与连接器,是整车中最易受 ESD 冲击的引脚之一;防护由片上 ESD 结构、外围 TVS 二极管与 PCB 布局共同实现。
- **作用与影响**:ESD 防护等级决定现场存活率与 AEC-Q100 认证结果;防护不当表现为间歇性通信异常或器件损坏。设计时需核对收发器引脚 ESD 等级,并按需增加 TVS,同时注意 TVS 寄生电容对高速数据相位信号质量的影响。
- **参见**:
  - [aec-q100.md](aec-q100.md)、[transceiver.md](transceiver.md)、[common-mode-range.md](common-mode-range.md)
  - [TI SLVAFC1: CAN 总线 ESD 防护](../resources/_entries/vendors/ti-slvafc1.md)
  - [NXP AH1308: CAN 应用提示](../resources/_entries/vendors/nxp-ah1308.md)
