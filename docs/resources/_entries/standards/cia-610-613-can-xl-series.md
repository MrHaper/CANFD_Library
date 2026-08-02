---
title: CiA 610 / 611 / 612 / 613 系列
description: CAN XL(第三代 CAN)规范与测试计划体系。注意:CiA 610~613 并非 CAN FD SIC 收发器测试规范。
type: 标准规范
organization: CiA
access: member
status: verified
download: link
priority: 1
audience: [模拟IC]
tags: [标准规范, CiA 610 / 611 / 612 / 613]
source: https://www.can-cia.org/can-knowledge/cia-610-series-can-xl-specification-and-test-plans
---

## 是什么
CiA 610~613 系列构成第三代 CAN(CAN XL)的完整规范体系:610 系列为 CAN XL 规范与测试计划,611 系列为高层功能,612 系列为指南与应用说明,613 系列为附加服务。**注意:这些文档均与 CAN XL 相关,并非 CAN FD SIC 收发器测试规范**(CAN SIC 收发器的规范本体是 ISO 11898-2:2024)。

## 为什么值得读
- **模拟IC 工程师**:CAN XL 与 CAN SIC XL 共享 ISO 11898-2:2024 的物理层底座,若未来向 SIC XL/FAST 模式(PWM、20 Mbit/s)扩展,610-3、612-2、612-3 是直接参考。
- **嵌入式开发工程师**:了解 CAN XL 高层功能与 CANsec 等附加服务。

## 核心内容要点
- 610 系列:CAN XL 规范与测试计划(610-1 DLL+PCS、610-3 CAN XL SIC PMA,已并入 ISO 11898-1/-2:2024;610-2/610-4 一致性测试;610-5 互操作测试)。
- 611 系列:CAN XL 高层功能(611-1 SDT、611-2 多 PDU)。
- 612 系列:CAN XL 指南(612-1 系统设计、612-2 RXD/TXD 引脚、612-3 SIC 仲裁位率建议)。
- 613 系列:CAN XL 附加服务(613-1 SEC、613-2 CANsec、613-3 LLC 分片)。
- 多为 WD/DSP 工作草案,仅 CiA 成员可见。

## 怎么读
CAN FD SIC 设计无需此系列;仅当面向 CAN XL / SIC XL 扩展时按需阅读相关部分。

## 参见
- [ISO 11898-2 (2024)](iso-11898-2-2024.md)
- [CiA 601-4(SIC)](cia-601-4-sic.md)
- [资源库 — 标准规范](../../standards.md)
