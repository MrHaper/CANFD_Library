---
title: AEC-Q100(车规 IC 可靠性认证)
description: 汽车电子委员会制定的车规集成电路可靠性压力测试标准,车规收发器的准入门槛。
tags: [进阶, 收发器]
---
- **定义**:AEC-Q100(Automotive Electronics Council Q100)是车规集成电路的可靠性压力测试标准,规定温度循环、高温工作寿命、ESD、闩锁、湿度等系列测试条件与失效判据,并按工作温度范围分为 Grade 0~3(如 Grade 0 为 -40 °C ~ +150 °C)。
- **位置/背景**:由汽车电子委员会(AEC)发布,是汽车零部件供应链对 IC 的通用可靠性要求;车规 CAN 收发器需通过 AEC-Q100 相应等级认证,并在数据手册中标注等级。
- **作用与影响**:AEC-Q100 等级决定收发器可应用的整车环境(发动机舱/乘员舱);它约束了芯片设计中的 ESD 防护、闩锁免疫与温度设计裕量,是选型时"能否上车"的首道门槛,也是流片后可靠性验证的框架。
- **参见**:
  - [esd.md](esd.md)、[transceiver.md](transceiver.md)
  - [TI TCAN1463-Q1 CAN SIC 数据手册](../resources/_entries/vendors/ti-tcan1463-q1.md)
  - [NXP TJA1463 CAN SIC 数据手册](../resources/_entries/vendors/nxp-tja1463.md)
