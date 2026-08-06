---
title: TLE9255W CAN FD 收发器(Partial Networking)数据手册
description: "Infineon HS CAN 收发器数据手册,带 Partial Networking 部分网络唤醒;注意:TLE9255 是 CAN FD 收发器而非 CAN SIC。经 alldatasheet 第三方验证。"

type: 厂商资料
organization: Infineon
year: 2018
access: free
status: verified
download: link
priority: 1
audience: [模拟IC]
tags: [Infineon, 数据手册]
source: "https://www.alldatasheet.com/datasheet-pdf/pdf/1046719/INFINEON/TLE9255W.html"

---

## 是什么
Infineon TLE9255W / TLE9255VLE 是 HS CAN 收发器数据手册(100 页, Rev 1.02, 2018-02-02),带 **Partial Networking(部分网络唤醒)**,基于 ISO 11898-2 CAN FD,支持选择性唤醒与低静态电流,面向 12 V/24 V 汽车节点。

!!! warning "注意:TLE9255 不是 CAN SIC"
    **TLE9255 是 CAN FD(partial networking)收发器,不是 CAN SIC**,中文网络上常见混淆。如需 Infineon 的 CAN SIC 产品,请使用 **TLE9371**(见本分类对应条目)。

## 为什么值得读
- **模拟IC 工程师**:Partial networking 的"选择性唤醒 + 高阻总线脱离"实现,对设计带休眠功能的收发器有参考价值。
- **嵌入式开发工程师**:理解部分网络唤醒在整车节电架构中的角色,避免在 SIC 选型时误用此器件。

## 核心内容要点
- HS CAN 收发器带 **Partial Networking(部分网络唤醒)**,基于 ISO 11898-2 CAN FD。
- 支持选择性唤醒与低静态电流,面向 12 V/24 V 汽车节点。
- ⚠️ 该器件是 CAN FD 收发器,**不是 CAN SIC**;Infineon 的 CAN SIC 产品为 TLE9371。
- 数据手册 100 页,详细参数以原文为准。

## 怎么读
按需阅读:若研究部分网络唤醒/低功耗架构,重点读选择性唤醒与总线脱离相关章节;若目标是 SIC 学习,请转向 TLE9371V 条目。

## 获取渠道
alldatasheet 聚合页(免费):<https://www.alldatasheet.com/datasheet-pdf/pdf/1046719/INFINEON/TLE9255W.html>
Infineon 官网产品搜索(浏览器访问):<https://www.infineon.com>。官网抓取受反爬限制,资料库以第三方验证为准。

## 参见
- [TLE9371V CAN SIC 收发器数据手册](infineon-tle9371v.md)
- [TLE9471 Lite CAN SBC 数据手册](infineon-tle9471.md)
- [资源库 — 厂商资料](../../vendors.md)
