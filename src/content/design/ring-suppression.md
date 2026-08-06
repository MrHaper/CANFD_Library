---
title: 振铃抑制电路参数设计要点
description: CAN SIC 收发器振铃抑制电路的参数设计要点——recessive nulling(LRN/HRN)、瞬态检测阻尼、阻抗匹配与分段斜率,各厂商专利路线对照。
tags: [设计参考, 模拟IC, 专家]
---

# 振铃抑制电路参数设计要点

## 模块职责

振铃抑制电路在**显性→隐性转换后**加速总线信号回到隐性阈值以下,并把反射振荡阻尼掉。SIC 的"有源隐性驱动"是系统级机制,振铃抑制电路则是各厂商在输出级内部的具体实现:在窗口内提供低阻泄放/匹配通路,让反射波看到近似匹配阻抗。

## 四条公开专利路线

| 路线 | 代表专利 | 电路思路 | 适用场景 |
| --- | --- | --- | --- |
| 隐性抵消(recessive nulling) | TI [US9606948B2](../resources/full-text/us9606948b2-recessive-nulling.md) | 跳变时短时并联基于 VCC/2 的低阻分数驱动器,加速泄放分布电容电荷 | 通用 SIC;LRN/HRN/混合可编程 |
| 瞬态触发阻尼 | TI [US11310072B2](../resources/full-text/us11310072b2-ring-suppression.md) | 振铃经电容耦合到 NMOS 栅极,幅度超阈值即导通,把振铃能量泄放 | 不依赖精确定时,自适应 |
| 阻抗匹配 + 分段斜率 | Microchip [US11539548B2](../resources/full-text/us11539548b2-microchip-sic.md) | 隐性过渡期接入匹配阻抗(总 Ron=总线特征阻抗,带温度补偿)+ 延迟线逐级关断电流源 | 5 Mbit/s 及以上 |
| 前馈/振荡抑制 | NXP [US10020841B2](../resources/full-text/us10020841b2-feedforward.md)、Bosch [US11068429B2](../resources/full-text/us11068429b2-bosch-osc.md) | 前馈预测边沿/振荡抑制单元 | 与主驱动协同 |

## 参数设计要点表

| 参数/设计项 | 目标 | 设计要点 |
| --- | --- | --- |
| 抑制窗口 | 与 SIC 窗口一致(≤120/≥355/≤530 ns) | 见[sic-control](sic-control.md);nulling 必须在采样点前终止 |
| nulling 阻抗 | 与总线特征阻抗同量级(数十 Ω) | 过低加载总线,过高无阻尼;建议可编程 |
| nulling 时长 | LRN:仅隐性位起始段;HRN:整个隐性位 | 连续隐性位场景 HRN 需重新触发/维持;终止时序精度是关键 |
| 振铃检测阈值 | 耦合后幅度超过内部阈值即触发 | 检测通路带宽与阈值要防误触发(噪声/正常边沿) |
| 泄放路径 | 振铃能量泄放到 VCC/GND | 电流路径阻抗与 EMC 折衷;转换瞬间电流要评估 |
| 温度补偿 | 匹配阻抗全温稳定 | Ron 温度补偿(Microchip 思路) |
| 与采样点错开 | nulling 终止时刻必须早于采样点 | 终止过早振铃未净,过晚影响后续位 |

## 关键设计点

### 1. Recessive Nulling(TI 路线)

- **LRN(light recessive nulling)**:只在隐性位起始的一段接入低阻,之后释放;适合大多数拓扑。
- **HRN(heavy recessive nulling)**:整个隐性位保持低阻;仅限单主/无仲裁拓扑,混用网络慎用。
- **混合模式**:按总线阻抗特征选择 nulling 时长,终止时刻必须与采样点错开。
- 设计启发:nulling 时长可寄存器编程;终止时刻的时序精度(与采样点错开)是设计重点;额外低阻通路会增加转换瞬间电流,需评估 EMC/共模电流。

### 2. 瞬态触发阻尼(TI 路线)

- 思路:不靠精确定时,而是**检测振铃本身**——显性→隐性跳变后,振铃信号经电容耦合到 NMOS 栅极,幅度超过阈值即让管子导通,把振铃能量泄放。
- 实现要点:驱动器 M1~M6(含高压/负压保护串联管)+ 脉冲发生器(约 200 ns)驱动 nulling,将内部节点拉到 VCM;振铃检测/阻尼通路电容耦合;脉冲宽度固定或可编程。
- 优点:对网络拓扑自适应;风险:检测阈值/带宽需防正常信号误触发。

### 3. 阻抗匹配 + 分段斜率(Microchip 路线)

- 显性态保持低阻输出;隐性过渡期接入匹配阻抗(OTA 或背靠背 Ron 受控晶体管对,总 Ron = 总线特征阻抗,带温度补偿)。
- 以串联延迟线逐级关断并联电流源做分段斜率控制;不改变总线差分阻抗,与阻抗匹配可独立或组合使用。

### 4. 与接收端滤波的关系

ISO 11898-2:2024 Annex A 允许两种实现:发送侧抑制振铃、接收侧滤波振铃,或两者结合。若芯片采用接收端滤波:

- 明确滤波器启动窗口与采样点之间的时序关系;
- 验证与不支持 SIC 的节点混用时的兼容性;
- 接收滤波不能解决本节点作为发送方时的总线振铃对其他节点的影响。

## 常见陷阱

- **nulling 终止晚于采样点**:直接把后续位拉偏,比不抑制更糟。
- **阻抗不匹配**:阻抗偏离总线特征阻抗,反射阻尼效果有限。
- **转换瞬间电流过大**:nulling 支路导通瞬间的大电流冲击引入新的 EMC 问题。
- **只做 TX 侧或只做 RX 侧且不验证混用**:与普通收发器互操作时行为未定义。

## 参见

- [SIC 控制逻辑设计要点](sic-control.md) / [输出级参数设计要点](output-stage.md)
- 知识库:[振铃抑制:SIC 核心能力](../knowledge/physical-layer/ringing-suppression.md)、[SIC 设计专题·设计篇](../knowledge/sic-design/design.md)
- 教程:[振铃抑制原理与测量](../tutorials/08-ringing-suppression.md)
- 专利全文:[US9606948B2](../resources/full-text/us9606948b2-recessive-nulling.md)、[US11310072B2](../resources/full-text/us11310072b2-ring-suppression.md)、[US11539548B2](../resources/full-text/us11539548b2-microchip-sic.md)、[US10020841B2](../resources/full-text/us10020841b2-feedforward.md)、[US11068429B2](../resources/full-text/us11068429b2-bosch-osc.md)
