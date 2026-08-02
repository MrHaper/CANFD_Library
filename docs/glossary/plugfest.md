---
title: plugfest(互操作性测试活动)
description: 多厂商设备在同一总线实测互操作性的活动,用于发现规范与实现的差异。
tags: [专家, 测试]
---
- **定义**:plugfest(互插测试)是由 CiA 等组织举办的互操作性测试活动:多家厂商的收发器、控制器、线束与测试工具接入同一 CAN 总线,按统一测试矩阵实测互操作与兼容性,发现"各自通过一致性测试但仍无法协同工作"的问题。
- **位置/背景**:plugfest 介于一致性测试(ISO 16845)与整车量产之间,是协议演进期(如 CAN FD SIC 推广)的重要验证环节;CiA 常面向 SIC 收发器与 CAN FD 控制器组织此类活动。
- **作用与影响**:芯片或方案发布前参加 plugfest 可提前暴露位定时、TDC 与收发器参数协同问题,是"标准正确性之外的工程正确性"验证;其结果影响产品兼容性口碑与设计修订。
- **参见**:
  - [iso-16845.md](iso-16845.md)、[can-sic.md](can-sic.md)、[tdc.md](tdc.md)
  - [CiA plugfest 认证(资源条目)](../resources/_entries/tools-community/certification-cia-plugfest.md)
  - [CAN FD 一致性测试仪(资源条目)](../resources/_entries/tools-community/canfd-conformance-tester.md)
  - [一致性测试标准(资源条目)](../resources/_entries/tools-community/certification-conformance-standards.md)
