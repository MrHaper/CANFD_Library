---
title: 资源库 — 教材书籍
description: CAN FD / CAN SIC 方向的教材与专业书籍书单:CAN 总线原理、车载网络、CAN 系统级专著、CANopen 应用层共 11 部,均经豆瓣读书 / Open Library / CiA 官网 / 当当核实,含书目信息、获取渠道与对模拟IC工程师的阅读价值。
tags: [教材]
---

# 资源库 — 教材书籍

> **特别提示:CAN FD 专门书籍稀缺**(引自 05 教材书籍 README)
>
> 截至 2026-07,**尚未有覆盖 ISO 11898-2:2016/2024 CAN SIC 物理层的正式英文或中文专著**出版。CiA 官网「CAN-related books」收录的 25 部书籍中绝大多数基于 CAN 2.0(CAN CC),唯一明确覆盖 CAN FD 的书目是德文版《Kommunikationssysteme im Automobil: LIN, CAN, CAN FD, CAN XL, FlexRay. Automotive Ethernet》(Mathias Rausch,2022,ISBN 未验证)。
>
> **因此,CAN FD 系统学习请配合标准与 CiA 技术文档**——物理层以 [ISO 11898-2 (2024)](_entries/standards/iso-11898-2-2024.md) 与 CiA 601 系列为纲,本书单中 CAN 相关专著用于建立协议与系统级基础(学习路径见文末)。

CAN FD (SIC) 收发器设计方向的教材与专业书籍书单,收录 CAN 总线原理与现场总线、车载网络、CAN 系统级专著、CANopen 应用层共 11 部。全部条目经豆瓣读书 / Open Library / CiA 官网 / 当当等渠道核实(详见各条目页),无本地 PDF,也不提供任何电子书下载链接,请通过官方渠道购买或借阅。按优先级排序:**推荐 ★★☆** 为系统级组网与位定时理论,**选读 ★☆☆** 为入门/综述/专项补充。

## 必读(★★★)

本书单暂无必读级条目——截至 2026-07 尚无覆盖 ISO 11898-2 SIC 物理层的正式专著。CAN FD / SIC 物理层学习的"必读"以标准与 CiA 技术文档为准,请参见 [资源库 — 标准规范](standards.md)。

## 推荐(★★☆)

| 书名 | 作者 | 出版社 | 年份 | ISBN | 获取渠道 |
|---|---|---|---|---|---|
| [CAN 总线设计及分布式控制](_entries/books/2011-zhangpeiren-can-distributed-control.md) | 张培仁 | 清华大学出版社 | 2011 | 978-7-302-27542-8 | 京东/图书馆 |
| [Understanding and Using the Controller Area Network Communication Protocol](_entries/books/2012-dinatale-can-protocol.md) | Marco Di Natale 等 | Springer | 2012 | 978-1-4614-0314-2 | Springer Link/Amazon |

## 选读(★☆☆)

| 书名 | 作者 | 出版社 | 年份 | ISBN | 获取渠道 |
|---|---|---|---|---|---|
| [现场总线 CAN 原理与应用技术(第 2 版)](_entries/books/2007-raoyuntao-can-principles.md) | 饶运涛 | 北京航空航天大学出版社 | 2007 | 978-7-81124-229-4 | 京东/当当/图书馆 |
| [汽车 CAN 总线系统原理、设计与应用](_entries/books/2010-luofeng-automotive-can-bus.md) | 罗峰、苏泽才 | 电子工业出版社 | 2010 | 978-7-121-09777-5 | 京东/当当/豆瓣阅读(官方电子版) |
| [CAN 现场总线系统设计技术](_entries/books/2004-shijiugen-can-fieldbus-design.md) | 史久根、张培仁、陈真勇 | 国防工业出版社 | 2004 | 978-7-118-03572-8 | 京东/图书馆 |
| [现场总线技术及其应用](_entries/books/1999-yangxianhui-fieldbus-technology.md) | 阳宪惠 | 清华大学出版社 | 1999 | 978-7-302-03384-4 | 京东/图书馆 |
| [CAN 总线轻松入门与实践](_entries/books/2011-lizhenhua-can-quick-start.md) | 李真花、崔健 | 北京航空航天大学出版社 | 2011 | 978-7-5124-0268-3 | 京东/图书馆 |
| [CAN System Engineering — From Theory to Practical Applications(第 2 版)](_entries/books/2013-lawrenz-can-system-engineering.md) | Wolfhard Lawrenz 主编 | Springer | 2013 | 978-1-4471-5612-3 | Springer Link/Amazon |
| [Controller Area Network Prototyping with Arduino](_entries/books/2014-voss-can-arduino-prototyping.md) | Wilfried Voss | Copperhill Media | 2014 | 978-1-938581-16-8 | Copperhill 官网/Amazon |
| [A Comprehensible Guide to Controller Area Network](_entries/books/2005-voss-comprehensible-can-guide.md) | Wilfried Voss | Copperhill Technologies | 2005 | 978-0-9765116-0-1 | Copperhill 官网/Amazon |
| [Embedded Networking with CAN and CANopen](_entries/books/2003-pfeiffer-can-canopen-networking.md) | Olaf Pfeiffer 等 | Annabooks/RTC Books | 2003 | 978-0-929392-78-3 | Copperhill 官网/Amazon |

## CAN FD / SIC 学习路径建议(引自 05 教材书籍 README)

1. **入门 / 建立协议直觉**:饶运涛《现场总线 CAN 原理与应用技术》、Voss《A Comprehensible Guide to Controller Area Network》(经典 CAN),再读 CiA 白皮书《CAN FD — The basic idea》(免费)。
2. **位定时与同步深入**:Di Natale 等《Understanding and Using the Controller Area Network Communication Protocol》与 [CiA 601 系列 Part 3](_entries/standards/cia-601-3-bit-timing.md)(位定时配置与评估工具)。
3. **物理层 / SIC 本体(核心)**:[ISO 11898-2:2024](_entries/standards/iso-11898-2-2024.md) 标准文本 + CiA 601 系列(Part 1 物理接口、Part 4 Signal Improvement 即 SIC 规范,已于 2023-09-01 并入 ISO 11898-2:2024)+ CAN Newsletter 收发器专题文章。
4. **系统集成视角**:Lawrenz《CAN System Engineering — From Theory to Practical Applications》、罗峰《汽车 CAN 总线系统原理、设计与应用》。

## 获取渠道说明

- **中文教材**:京东 / 当当 / 公共图书馆有售或馆藏;罗峰《汽车 CAN 总线系统原理、设计与应用》在豆瓣阅读有官方电子版(付费),请通过官方渠道购买,支持正版。
- **英文专著**:Springer Link(机构订阅或购买)与 Amazon;Copperhill Media 官网(copperhilltech.com)直销。
- **本书单不提供任何电子书下载链接**,请勿使用非授权渠道获取。

## 延伸阅读

- [资源库 — 标准规范](standards.md)(ISO 11898 系列、CiA 601 系列,CAN FD/SIC 学习的核心资料)
- [ISO 11898-2 (2024)](_entries/standards/iso-11898-2-2024.md)(高速 CAN / CAN SIC 物理层现行标准)
- [CiA 601 系列 Part 4 — Signal Improvement](_entries/standards/cia-601-4-sic.md)(CAN SIC 补充要求)
- [CiA 601 系列 Part 1 — 物理接口](_entries/standards/cia-601-1-physical-interface.md)
