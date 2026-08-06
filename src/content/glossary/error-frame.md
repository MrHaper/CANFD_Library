---
title: 错误帧(Error Frame)
description: 节点检测到协议错误时向全网广播的故障指示帧,由错误标志与错误分隔符组成。
tags: [入门, 协议]
---
- **定义**:错误帧(Error Frame)是节点检测到协议错误时主动发送的帧,用于通知全网"本帧已被破坏"。它由错误标志(Error Flag)+ 错误分隔符(Error Delimiter)组成:Error Active 节点发送 6 个显性位的主动错误标志,Error Passive 节点发送 6 个隐性位的被动错误标志,其后是 8 个隐性位的错误分隔符。
- **位置/背景**:错误帧没有固定位置,从节点检测到错误的位之后立即开始发送,可插入任何帧(含正在传输的数据帧)之中;错误标志故意违反位填充规则,迫使其他节点也检测到错误。
- **作用与影响**:CAN 的五类错误(位错误、填充错误、CRC 错误、格式错误、ACK 错误)最终都通过错误帧传播;错误标志会使整帧作废并触发发送节点重发,是 CAN 高可靠性机制的一部分。错误帧期间总线被拉向显性,持续破坏填充规则,因此全网节点同步进入错误处理。
- **参见**:
  - [arbitration.md](arbitration.md)、[crc.md](crc.md)、[bit-stuffing.md](bit-stuffing.md)、[bus-off.md](bus-off.md)
  - [ISO 11898-1 (2015)](../resources/_entries/standards/iso-11898-1-2015.md)
  - [ISO 11898-1 (2024)](../resources/_entries/standards/iso-11898-1-2024.md)
