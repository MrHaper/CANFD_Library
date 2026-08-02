---
title: SocketCAN:Linux 原生 CAN 协议栈
description: Linux 内核内置的 CAN/CAN FD 协议栈——设备抽象、PF_CAN 套接字、can-utils 工具链与 python-can 库的使用。
tags: [入门, 控制器]
---

## 定义

**SocketCAN** 是 Linux 内核原生支持的 CAN 协议栈:把 CAN 控制器抽象为网络设备(`can0`、`can1`…),通过 **PF_CAN 协议族套接字**编程访问,并提供标准的配置命令(如 `ip link set can0 up type can bitrate 500000 dbitrate 5000000 fd on`)。它与 can-utils、python-can 配合,是嵌入式 Linux 与 PC 端 CAN/CAN FD 开发的事实标准。

## 要点

### 架构分层

```
应用(cansend / candump / python-can …)
  ↓
套接字层 PF_CAN(CAN_RAW / CAN_BCM / CAN_ISOTP …)
  ↓
内核 CAN 核心(can-raw 模块、过滤器、canfd 帧支持)
  ↓
网络设备 can0 ← 驱动绑定底层 CAN 控制器(MCU 内置 / USB-CAN 卡)
```

- **设备抽象**:CAN 接口作为 netdev 管理,`ip link`/`ip -details link` 可查看与配置(速率、FD 使能、环回模式)。
- **套接字类型**:`CAN_RAW`(裸收发帧)、`CAN_BCM`(广播管理,周期/变化发送)、`CAN_ISOTP`(传输层,ECU 诊断常用)。
- **CAN FD 支持**:FD 帧(含 BRS、ESI)在内核 3.6+ 原生支持,RAW 套接字直接收发 FD 帧。

### 常用工具链(can-utils)

| 工具 | 作用 |
|---|---|
| `candump` | 抓取/记录总线报文,支持 CAN FD 显示与过滤 |
| `cansend` | 发送单条报文(经典与 FD) |
| `cangen` | 按规则周期性/随机生成流量 |
| `canfdtest` | 环回/两端对测:验证接口与收发器数据通路的连通性 |
| `canbusload` | 统计总线负载率 |

### python-can 桥接

python-can 提供统一的 Python API,后端可接 SocketCAN、PCAN、Vector、Kvaser、ZLG 等接口——同一套脚本既能跑 Linux 本地也能连 Windows 下的商业硬件,适合写数据分析与自动化测试脚本。

### 典型使用流程

```
# 1. 配置并启用 CAN FD 接口(1M 仲裁 / 5M 数据)
ip link set can0 type can bitrate 1000000 dbitrate 5000000 fd on
ip link set can0 up

# 2. 抓包
candump can0

# 3. 发送 FD 帧
cansend can0 123##11122334455667788
```

完整动手流程见教程[用 SocketCAN 5 分钟跑通 CAN FD 回环](../../tutorials/05-socketcan-loopback.md)。

## 与收发器/控制器设计的关联

- **对控制器(嵌入式)**:SocketCAN 是嵌入式工程师与 CAN FD 打交道的入口——位定时/TDC 参数、FD 模式开关、环回模式都通过接口配置;`ip -details link show can0` 的时序参数与[控制器寄存器与 TDC 配置](register-tdc-config.md)一一对应,错误计数(`ip -s -details link show can0`)可验证位定时/TDC 配置是否生效。
- **对收发器(模拟 IC)**:`canfdtest` 回环测试与 `candump` 抓帧构成收发器环回延迟、位时序正确性的快速验证手段;上位机侧的 SocketCAN 数据分析与[示波器抓帧](../tools/scope-capture.md)互为印证。

## 参见

- 教程:[用 SocketCAN 5 分钟跑通 CAN FD 回环](../../tutorials/05-socketcan-loopback.md)、[CAN FD 位定时配置实战](../../tutorials/06-bit-timing-config.md)
- 词条:[SocketCAN](../../glossary/socketcan.md)、[can-utils](../../glossary/can-utils.md)、[python-can](../../glossary/python-can.md)
- 工具条目:[SocketCAN](../../resources/_entries/tools-community/socketcan.md)、[can-utils](../../resources/_entries/tools-community/can-utils.md)、[python-can](../../resources/_entries/tools-community/python-can.md)、[CAN 接口卡](../../resources/_entries/tools-community/can-interface-card.md)
- 相邻子域:[控制器寄存器与 TDC 配置](register-tdc-config.md)、[总线分析工具对比](../tools/tool-comparison.md)
