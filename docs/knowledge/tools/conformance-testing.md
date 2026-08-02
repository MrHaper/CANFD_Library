---
title: 一致性测试:ISO 16845 / IEC 62228-3 / plugfest
description: CAN FD 芯片如何被认证——协议一致性(ISO 16845-1/-2)、收发器 EMC 评估(IEC 62228-3)、CiA plugfest 互操作测试与第三方实验室认证路径。
tags: [专家, 测试]
---

## 定义

**一致性测试(Conformance Testing)** 是按标准规定的用例,验证控制器/收发器实现与规范**一致**的测试体系:CAN FD 控制器按 **ISO 16845**(协议一致性),收发器物理层按 **ISO 16845-2**(HS-MAU)与 **IEC 62228-3**(EMC 评估),另以 **CiA plugfest** 做多厂商**互操作验证**——"一致性"保证实现符合文本,"互操作"保证实际互联可用,两者缺一不可。

## 要点

### 协议一致性:ISO 16845

| 标准 | 对象 | 内容 |
|---|---|---|
| [ISO 16845-1](../../resources/_entries/standards/iso-16845-1-2016.md) | 数据链路层 | 一致性测试计划 Part 1:帧格式、仲裁、错误处理、位填充、CRC 等用例,含 Classical CAN 与 CAN FD |
| [ISO 16845-2](../../resources/_entries/standards/iso-16845-2-2018.md) | 物理层(HS-MAU) | 针对 ISO 11898-2:2016 高速介质访问单元的静态与动态测试(电平、时序、延迟) |

执行载体:Vector 等厂商的 **CAN FD 一致性测试系统**运行规范用例脚本,输出逐项 PASS/FAIL 报告。

### 收发器 EMC 评估:IEC 62228-3 与 CISPR 25

- **IEC 62228-3**:CAN 收发器集成电路的 EMC 评估标准——规定**传导发射**与**射频抗扰度**测试方法,是车规 EMC 认证依据,覆盖引脚级发射/抗扰测试台架与限值。
- **CISPR 25**:整车零部件电磁发射限值(车规级),与回波损耗、共模扼流圈布局共同决定收发器系统级 EMC 表现,见[回波损耗与 EMC](../physical-layer/return-loss-emc.md)。
- 厂商数据手册常以 IEC 62228-3 测试结果(如 NXP TJA146x、TI TCAN146x 的 EME/EMI 特性)展示器件的 EMC 竞争力。

### 互操作验证:CiA plugfest

- **plugfest / interoperability 测试**是 CiA 定期组织的多厂商互操作活动:CAN FD、CAN SIC 收发器与控制器在真实网络里互联测试,暴露"各自符合文本、放在一起不通"的问题。
- 对自研芯片团队,plugfest 是量产前验证与主流收发器互联的关键活动(见[CiA plugfest 条目](../../resources/_entries/tools-community/certification-cia-plugfest.md))。

### 认证路径与第三方实验室

```
设计 → 厂商自测(一致性测试系统/内部台架)→ 独立第三方实验室(一致性/EMC/车规)
     → plugfest 互操作 → AEC-Q100 可靠性(内部或认证机构)
```

- 第三方实验室(TÜV、SGS、广电计量、赛宝等)承接收发器一致性、EMC 与车规认证;AEC-Q100 可靠性可在认证机构或内部完成。

## 与收发器/控制器设计的关联

- **对收发器(模拟 IC)**:一致性测试是流片后的"期末考试"——ISO 16845-2 的时序/电平用例、IEC 62228-3 的 EMC 台架、plugfest 的互操作,逐项验证输出级、接收比较器、ESD/共模设计是否达标;建议在量产前把测试用例反推成设计 Spec 的对照清单(厂商数据手册即是对标模板)。
- **对控制器(嵌入式)**:控制器侧关注 ISO 16845-1 协议一致性(位定时配置、错误处理状态机),嵌入式工程师通过一致性测试报告确认控制器/驱动配置合法,配合[位定时配置实战](../../tutorials/06-bit-timing-config.md)落地。

## 参见

- 教程:[一致性测试与 plugfest:芯片如何被认证](../../tutorials/11-conformance-plugfest.md)
- 词条:[ISO 16845](../../glossary/iso-16845.md)、[IEC 62228-3](../../glossary/iec-62228-3.md)、[plugfest](../../glossary/plugfest.md)、[CISPR 25](../../glossary/cispr25.md)、[CAN SIC](../../glossary/can-sic.md)、[AEC-Q100](../../glossary/aec-q100.md)
- 标准规范:[ISO 16845-1](../../resources/_entries/standards/iso-16845-1-2016.md)、[ISO 16845-2](../../resources/_entries/standards/iso-16845-2-2018.md)、[IEC 62228-3](../../resources/_entries/standards/iec-62228-3-2019.md)、[ISO 11898-2 (2024)](../../resources/_entries/standards/iso-11898-2-2024.md)
- 工具条目:[CAN FD 一致性测试系统](../../resources/_entries/tools-community/canfd-conformance-tester.md)、[CiA plugfest](../../resources/_entries/tools-community/certification-cia-plugfest.md)、[一致性测试标准](../../resources/_entries/tools-community/certification-conformance-standards.md)、[第三方实验室](../../resources/_entries/tools-community/certification-third-party-lab.md)
- 相邻子域:[回波损耗与 EMC](../physical-layer/return-loss-emc.md)、[示波器抓帧](scope-capture.md)
