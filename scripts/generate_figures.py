#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CAN FD 知识库 SIC 专题 22 张原创 SVG 技术图生成器 v2。

设计原则:
- 所有文本自动换行,节点尺寸由内容决定,保证零重叠;
- 思维导图用递归子树高度布局,边先画、点后画;
- 波形/框图按“车道 + 固定间距”布局,标注放在独立区域。

用法:python scripts/generate_figures.py [输出目录]
"""

import math
import os
import sys

W = 1200
BRAND = "#0f4c81"
BRAND2 = "#0a3a63"
ACCENT = "#d97706"
INK = "#1f2933"
MUTED = "#64748b"
LINE = "#cbd5e1"
LIGHT = "#eaf1fb"
AMBER = "#fff3dd"
GREEN = "#e7f6ef"
RED = "#b45309"
OK = "#16a34a"
WHITE = "#ffffff"
FONT = "'PingFang SC','Microsoft YaHei','Noto Sans SC','Helvetica Neue',Arial,sans-serif"


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def cjk_w(ch):
    return 1.0 if ord(ch) > 0x2E80 else 0.55


def text_w(s, size):
    return sum(cjk_w(c) for c in s) * size


def wrap(s, size, max_w):
    """按估算宽度换行,返回行列表。"""
    words = []
    for seg in str(s).split("\n"):
        words.extend(seg.split(" "))
    lines, cur = [], ""
    for wd in words:
        trial = (cur + " " + wd).strip()
        if cur and text_w(trial, size) > max_w:
            lines.append(cur)
            cur = wd
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines or [""]


def T(x, y, s, size=15, fill=INK, weight="normal", anchor="middle"):
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONT}" font-size="{size}" '
        f'fill="{fill}" font-weight="{weight}" text-anchor="{anchor}">{esc(s)}</text>'
    )


def TL(x, y, lines, size=14, lh=1.35, fill=INK, weight="normal", anchor="middle"):
    return "\n".join(T(x, y + i * size * lh, ln, size, fill, weight, anchor) for i, ln in enumerate(lines))


def R(x, y, w, h, rx=10, fill=WHITE, stroke=LINE, sw=1.3, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'


def L(x1, y1, x2, y2, stroke=MUTED, sw=1.5, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw}"{d}/>'


def ARR(x1, y1, x2, y2, color=BRAND, sw=1.8, dash=None, marker="arr"):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{sw}" marker-end="url(#{marker})"{d}/>'


def PATH(d, stroke=BRAND, sw=1.8):
    return f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="{sw}"/>'


def DEFS():
    return f"""<defs>
<marker id="arr" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
  <path d="M0,0 L8,3 L0,6 Z" fill="{BRAND}"/></marker>
<marker id="arrA" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
  <path d="M0,0 L8,3 L0,6 Z" fill="{ACCENT}"/></marker>
<marker id="arrG" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
  <path d="M0,0 L8,3 L0,6 Z" fill="{OK}"/></marker>
</defs>"""


def open_svg(h, title, subtitle=""):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" font-family="{FONT}">
<rect x="0" y="0" width="{W}" height="{h}" fill="#ffffff"/>
<rect x="0" y="0" width="{W}" height="66" fill="{BRAND2}"/>
<text x="36" y="32" font-size="22" font-weight="bold" fill="#ffffff">{esc(title)}</text>
<text x="36" y="53" font-size="13" fill="#c7d6ea">{esc(subtitle)}</text>
{DEFS()}
"""


def close_svg():
    return "</svg>\n"


def box_text(cx, cy, w, h, title, sub=None, tsize=15, ssize=12.5, fill=WHITE, stroke=LINE, tfill=INK):
    """盒内文本:标题 + 可选多行说明,自动换行,保证不溢出。"""
    out = [R(cx - w / 2, cy - h / 2, w, h, fill=fill, stroke=stroke)]
    out.append(T(cx, cy - (8 if sub else 0), title, tsize, tfill, "bold"))
    if sub:
        lines = wrap(sub, ssize, w - 18)
        out.append(TL(cx, cy + 14, lines, ssize, fill=MUTED))
    return "\n".join(out)


def hline(x0, x1, y, color=MUTED, sw=1.3, dash="6 4"):
    return L(x0, y, x1, y, color, sw, dash)


def wave(segs, x0, y0, amp, color=BRAND, sw=2.2):
    """segs: [(宽, 电平0/1)] 电平0在下,电平1在上。"""
    pts = [(x0, y0 + segs[0][1] * amp)]
    x = x0
    for wdt, lv in segs:
        x += wdt
        pts.append((x, y0 + lv * amp))
    d = f"M {pts[0][0]:.1f} {pts[0][1]:.1f}"
    for i in range(1, len(pts)):
        d += f" L {pts[i][0]:.1f} {pts[i-1][1]:.1f} L {pts[i][0]:.1f} {pts[i][1]:.1f}"
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linejoin="round"/>'


def damped(x0, x1, y_start, y_end, freq=2.8, decay=5.0, amp=0.42, color=BRAND, sw=2.2):
    n = 140
    pts = []
    for i in range(n + 1):
        t = i / n
        xx = x0 + (x1 - x0) * t
        yy = y_end + (y_start - y_end) * math.exp(-decay * t) * math.cos(2 * math.pi * freq * t)
        pts.append((xx, yy))
    return f'<path d="M ' + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts) + f'" fill="none" stroke="{color}" stroke-width="{sw}"/>'


# ---------------------------------------------------------------- 图 1

def fig1():
    h = 700
    s = open_svg(h, "图 1 总线振铃现象对比", "常规 CAN FD 显性→隐性转换后振铃越阈;CAN SIC 有源隐性快速压振铃")
    x0, x1 = 240, 1080
    # 常规 lane
    s += T(90, 165, "常规 CAN FD(无 SIC)", 16, INK, "bold", "start")
    s += hline(x0, x1, 250, RED, 1.2, "5 4")
    s += T(x1 - 8, 242, "0.9 V 显性阈值", 12.5, RED, anchor="end")
    s += hline(x0, x1, 300, MUTED, 1.2, "5 4")
    s += T(x1 - 8, 292, "0.5 V 隐性阈值", 12.5, MUTED, anchor="end")
    s += L(x0, 210, 440, 210, BRAND, 2.2)
    s += damped(440, 800, 210, 315, freq=2.6, decay=3.8, amp=0.5, color=BRAND, sw=2.2)
    s += L(800, 315, x1, 315, BRAND, 2.2)
    s += T(660, 365, "振铃反复越过 0.9 V / 0.5 V → RXD 出现伪毛刺", 13.5, RED)
    # SIC lane
    s += T(90, 425, "CAN SIC(有源隐性)", 16, OK, "bold", "start")
    s += hline(x0, x1, 510, RED, 1.2, "5 4")
    s += T(x1 - 8, 502, "0.9 V 显性阈值", 12.5, RED, anchor="end")
    s += hline(x0, x1, 560, MUTED, 1.2, "5 4")
    s += T(x1 - 8, 552, "0.5 V 隐性阈值", 12.5, MUTED, anchor="end")
    s += L(x0, 470, 440, 470, OK, 2.2)
    s += damped(440, 720, 470, 575, freq=2.0, decay=7.0, amp=0.3, color=OK, sw=2.2)
    s += L(720, 575, x1, 575, OK, 2.2)
    s += T(660, 620, "有源隐性快速拉低并阻尼反射 → 采样前已低于 0.5 V", 13.5, OK)
    s += T(660, 668, "5 Mbit/s 数据相位位时间 = 200 ns,振铃必须在采样点前衰减干净", 13, MUTED)
    return s + close_svg()


# ---------------------------------------------------------------- 图 2

def fig2():
    h = 700
    s = open_svg(h, "图 2 SIC 事件时序", "显性 → 有源隐性 → 被动隐性三相位,参数取 ISO 11898-2:2024 Set C")
    x0 = 150
    scale = 880 / 700.0  # 0..700ns -> 880px
    def tx(t): return x0 + t * scale
    s += T(90, 175, "TXD", 15, INK, "bold", "start")
    s += wave([(tx(90) - x0, 0), (tx(700) - tx(90), 1)], x0, 205, 55, BRAND, 2.2)
    s += T(90, 285, "总线", 15, INK, "bold", "start")
    s += wave([(tx(90) - x0, 0), (tx(700) - tx(90), 1)], x0, 315, 55, BRAND2, 2.2)
    # 相位条
    y = 420
    s += R(x0, y, tx(90) - x0, 42, rx=8, fill=AMBER, stroke=ACCENT)
    s += T((x0 + tx(90)) / 2, y + 26, "显性 R≈50 Ω", 13, "#5b3a12", "bold")
    s += R(tx(90), y, tx(430) - tx(90), 42, rx=8, fill=LIGHT, stroke=BRAND)
    s += T((tx(90) + tx(430)) / 2, y + 26, "有源隐性 R≈100 Ω(RDIFF_act_rec 75~133 Ω)", 13, BRAND2, "bold")
    s += R(tx(430), y, tx(700) - tx(430), 42, rx=8, fill="#f1f5f9", stroke=MUTED)
    s += T((tx(430) + tx(700)) / 2, y + 26, "被动隐性 R≈60 kΩ", 13, MUTED, "bold")
    # 窗口标注(独立带)
    s += ARR(tx(90), y + 70, tx(90), y + 110, ACCENT, 1.5, marker="arrA")
    s += T(tx(90) + 110, y + 104, "tact_rec_start ≤ 120 ns", 12.5, ACCENT)
    s += ARR(tx(430), y + 70, tx(430), y + 110, BRAND, 1.5)
    s += T(tx(430) + 110, y + 104, "tact_rec_end ≥ 355 ns", 12.5, BRAND)
    s += ARR(tx(560), y + 70, tx(560), y + 110, MUTED, 1.5)
    s += T(tx(560) + 110, y + 104, "tpas_rec_start ≤ 530 ns", 12.5, MUTED)
    # 时间轴
    for t, lbl in [(0, "0 ns"), (200, "200 ns"), (400, "400 ns"), (600, "600 ns")]:
        s += L(tx(t), 610, tx(t), 622, MUTED, 1.2)
        s += T(tx(t), 638, lbl, 12, MUTED)
    s += T(660, 672, "tSIC(+300~+530 ns,自 TXD 上升沿 50% 阈值起测)覆盖数据相位隐性位", 13, MUTED)
    return s + close_svg()


# ---------------------------------------------------------------- 图 3

def fig3():
    h = 680
    s = open_svg(h, "图 3 收发器芯片架构", "CAN SIC 收发器内部模块:驱动、SIC 控制、接收器、电源与保护")
    # 引脚
    s += T(85, 220, "TXD", 15, INK, "bold")
    s += ARR(130, 215, 210, 215, BRAND, 2)
    s += T(85, 330, "RXD", 15, INK, "bold")
    s += ARR(210, 330, 130, 330, BRAND, 2)
    s += T(1115, 250, "CANH", 15, INK, "bold")
    s += ARR(1020, 245, 1090, 245, BRAND, 2)
    s += T(1115, 300, "CANL", 15, INK, "bold")
    s += ARR(1020, 295, 1090, 295, BRAND, 2)
    # 芯片框
    s += R(210, 120, 810, 460, rx=18, fill="#fbfdff", stroke=BRAND, sw=2)
    s += T(615, 148, "CAN SIC 收发器芯片", 18, BRAND2, "bold")
    # 2x2 模块
    s += box_text(360, 220, 250, 92, "驱动控制逻辑", "边沿检测 / 模式控制 / 斜率控制", fill=LIGHT, stroke=BRAND)
    s += box_text(860, 220, 250, 92, "输出级(驱动器)", "显性/有源隐性/被动隐性三态", fill=AMBER, stroke=ACCENT)
    s += box_text(360, 390, 250, 92, "SIC 控制逻辑", "窗口 ≤120/≥355/≤530 ns · 阻抗切换", fill=LIGHT, stroke=BRAND)
    s += box_text(860, 390, 250, 92, "接收器(比较器)", "迟滞 / 共模范围 / 输入阻抗", fill=GREEN, stroke=OK)
    s += box_text(615, 510, 560, 56, "电源管理与保护", "VCC/VIO/VBAT · ESD · 总线容错 · TXD 超时 · 唤醒", tsize=14, ssize=12, fill="#f1f5f9", stroke=MUTED)
    # 连接(沿车道,不穿文字)
    s += L(485, 220, 540, 220, MUTED, 1.6)
    s += ARR(540, 220, 735, 220, MUTED, 1.6)
    s += L(985, 220, 1000, 220, MUTED, 1.6)
    s += L(1000, 220, 1000, 245, MUTED, 1.6)
    s += L(1000, 245, 1000, 295, MUTED, 1.6)
    s += L(1000, 245, 1020, 245, BRAND, 2)
    s += L(1000, 295, 1020, 295, BRAND, 2)
    s += L(360, 270, 360, 344, MUTED, 1.5)
    s += L(860, 270, 860, 344, MUTED, 1.5)
    s += L(735, 390, 600, 390, MUTED, 1.5)
    s += L(600, 390, 600, 330, MUTED, 1.5)
    s += L(600, 330, 210, 330, MUTED, 1.5)
    s += L(360, 436, 360, 482, MUTED, 1.5)
    s += L(615, 436, 615, 482, MUTED, 1.5)
    s += T(615, 640, "三大设计域:输出级(对称性/斜率/SIC 阻抗)· SIC 控制(时序窗口)· 接收器(tREC/抗扰)", 13.5, MUTED)
    return s + close_svg()


# ---------------------------------------------------------------- 图 4

def fig4():
    h = 640
    s = open_svg(h, "图 4 星型拓扑与 stub 反射", "未端接 stub 末端产生反射,反射波在网络中来回振荡形成振铃")
    y = 300
    s += L(140, y, 1060, y, BRAND, 3)
    s += T(600, y - 24, "总线主干 CANH / CANL", 15, INK, "bold")
    s += R(90, y - 18, 72, 36, rx=8, fill=AMBER, stroke=ACCENT)
    s += T(126, y + 7, "60 Ω", 13, "#5b3a12", "bold")
    s += R(1038, y - 18, 72, 36, rx=8, fill=AMBER, stroke=ACCENT)
    s += T(1074, y + 7, "60 Ω", 13, "#5b3a12", "bold")
    stubs = [(330, "stub 1(短,已端接)", False), (600, "stub 2(中)", False), (870, "stub 3(长,未端接)", True)]
    for sx, label, open_end in stubs:
        s += L(sx, y, sx, 420, MUTED, 2)
        s += R(sx - 78, 420, 156, 44, rx=10, fill=LIGHT, stroke=BRAND)
        s += T(sx, 446, label, 13, BRAND2, "bold")
    # 反射(上方独立带)
    s += ARR(870, 250, 870, 190, ACCENT, 2, marker="arrA")
    s += T(870, 172, "阻抗突变 → 反射", 13.5, ACCENT, "bold")
    s += damped(560, 900, 255, 255, freq=2.2, decay=3.2, amp=55, color=RED, sw=2.0)
    s += T(640, 150, "反射波沿 stub 返回总线,在网络中来回振荡", 14, RED, "bold")
    s += T(600, 530, "stub 越长、数量越多,等效电容越大,振荡越持久,采样点前难以衰减干净", 13.5, MUTED)
    s += T(600, 580, "SIC 的目标:不改拓扑与协议,把复杂拓扑下可用速率提升到 5~8 Mbit/s", 13.5, INK, "bold")
    return s + close_svg()


# ---------------------------------------------------------------- 图 5

def fig5():
    h = 660
    s = open_svg(h, "图 5 安全操作区与采样点", "信号可在安全操作区内自由振荡,但必须在最早隐性采样点前回到 0.5 V 以下")
    x0, x1 = 150, 1060
    s += hline(x0, x1, 260, RED, 1.2, "5 4")
    s += T(x1 - 8, 252, "0.9 V(显性阈值)", 12.5, RED, anchor="end")
    s += hline(x0, x1, 330, MUTED, 1.2, "5 4")
    s += T(x1 - 8, 322, "0.5 V(隐性阈值)", 12.5, MUTED, anchor="end")
    s += R(560, 340, 500, 110, rx=12, fill="rgba(22,163,74,0.10)", stroke=OK, dash="5 4")
    s += T(810, 372, "安全操作区", 15, OK, "bold")
    s += T(810, 398, "信号可自由振荡,只要在最早采样点前", 12.5, MUTED)
    s += T(810, 420, "回到 0.5 V 以下(Allowable Ringing Time)", 12.5, MUTED)
    s += L(x0, 220, 400, 220, BRAND, 2.2)
    s += damped(400, 1060, 220, 365, freq=2.2, decay=3.2, amp=0.5, color=BRAND, sw=2.2)
    for sx, lbl in [(680, "最早采样点"), (930, "最晚采样点")]:
        s += L(sx, 120, sx, 580, BRAND, 1.4, "4 4")
        s += T(sx, 108, lbl, 13, BRAND, "bold")
        s += T(sx, 596, "▼", 15, BRAND)
    s += ARR(400, 470, 680, 470, OK, 1.8, marker="arrG")
    s += T(540, 500, "允许振铃时间", 13.5, OK, "bold")
    s += T(600, 620, "SIC 价值:① 收紧对称性 → 扩大安全区;② 快速压振铃 → 尽早进入安全区", 13.5, MUTED)
    return s + close_svg()


# ---------------------------------------------------------------- 图 6

def fig6():
    h = 620
    s = open_svg(h, "图 6 SIC 标准演进", "CAN FD → CAN SIC → CAN XL:参数集 Set A/B/C 与 Annex A")
    nodes = [
        (160, "2012", "Bosch CAN FD Spec v1.0", "CAN FD 协议源头(免费 PDF)", LIGHT, BRAND),
        (360, "2016", "ISO 11898-2:2016", "常规 CAN FD 收发器参数", LIGHT, BRAND),
        (560, "2019", "CiA 601-4", "SIC 原始规范 v2.0.0", AMBER, ACCENT),
        (760, "2023", "CiA 601-4 撤回", "内容并入 ISO 11898-2", "#f1f5f9", MUTED),
        (960, "2024", "ISO 11898-2:2024", "Set A/B/C(SIC)+ Annex A", LIGHT, BRAND),
    ]
    for cx, yr, name, desc, fill, stroke in nodes:
        s += R(cx - 105, 150, 210, 120, rx=12, fill=fill, stroke=stroke, sw=1.5)
        s += T(cx, 180, yr, 15, BRAND2, "bold")
        s += T(cx, 210, name, 13.5, INK, "bold")
        s += TL(cx, 236, wrap(desc, 11.5, 190), 11.5, fill=MUTED)
    s += L(160, 330, 960, 330, BRAND, 2)
    for cx in [160, 360, 560, 760, 960]:
        s += L(cx, 322, cx, 338, BRAND, 2)
    s += ARR(560, 390, 760, 390, ACCENT, 1.8, marker="arrA")
    s += T(660, 378, "并入(2023)", 13, ACCENT, "bold")
    s += ARR(760, 430, 960, 430, BRAND, 1.8)
    s += T(860, 418, "发布", 13, BRAND, "bold")
    s += R(930, 470, 230, 84, rx=12, fill=GREEN, stroke=OK, sw=1.5)
    s += T(1045, 502, "Annex A / FAST 模式", 14, "#0b4b37", "bold")
    s += T(1045, 528, "≤20 Mbit/s · CAN XL 兼容", 12, "#0b4b37")
    s += ARR(960, 338, 1045, 470, OK, 1.8, marker="arrG")
    return s + close_svg()


# ---------------------------------------------------------------- 图 7

def fig7():
    h = 700
    s = open_svg(h, "图 7 经典 CAN vs CAN FD 帧格式", "CAN FD 的秘密在控制场:EDL / BRS / ESI 三个标志位")
    rows = [
        (120, "经典 CAN 数据帧", [
            (80, "SOF", "1 位"),
            (210, "仲裁场", "11/29 位 ID + RTR"),
            (170, "控制场", "IDE·r1 + DLC"),
            (170, "数据场", "0~8 字节"),
            (180, "CRC 场", "15 位 + 分隔符"),
            (110, "ACK", "slot + del"),
            (100, "EOF", "7 位隐性"),
        ], LIGHT, BRAND),
        (360, "CAN FD 数据帧", [
            (80, "SOF", "1 位"),
            (210, "仲裁场", "ID + RRS"),
            (230, "控制场", "IDE·EDL·res·BRS·ESI·DLC"),
            (180, "数据场", "0~64 字节"),
            (180, "CRC 场", "17/21 位 + 填充"),
            (110, "ACK", "slot + del"),
            (100, "EOF", "7 位隐性"),
        ], AMBER, ACCENT),
    ]
    for y, title, fields, fill, stroke in rows:
        s += T(90, y - 26, title, 16, INK, "bold", "start")
        x = 90
        for w, name, sub in fields:
            s += R(x, y, w, 58, rx=8, fill=fill, stroke=stroke, sw=1.4)
            s += T(x + w / 2, y + 23, name, 13.5, BRAND2, "bold")
            s += TL(x + w / 2, y + 42, wrap(sub, 11, w - 10), 11, fill=MUTED)
            x += w
    # BRS 标注(两行之间独立带)
    s += ARR(410, 320, 410, 360, ACCENT, 1.8, marker="arrA")
    s += T(510, 340, "BRS 隐性 → 数据相位高速率(如 2/5 Mbit/s)", 13, ACCENT, "bold")
    s += ARR(630, 320, 630, 360, MUTED, 1.8)
    s += T(740, 340, "CRC delimiter 切回仲裁速率", 12.5, MUTED)
    s += T(600, 470, "一句话记忆:EDL 决定「这是什么帧」,BRS 决定「数据段跑多快」,ESI 报告「发送方状态」", 14, INK, "bold")
    # 相位条
    s += R(90, 520, 330, 36, rx=8, fill="#f1f5f9", stroke=MUTED)
    s += T(255, 542, "仲裁相位(经典速率,如 500 kbit/s)", 12.5, MUTED)
    s += R(420, 520, 230, 36, rx=8, fill=GREEN, stroke=OK)
    s += T(535, 542, "数据相位(高速率)", 12.5, "#0b4b37", "bold")
    s += R(650, 520, 280, 36, rx=8, fill="#f1f5f9", stroke=MUTED)
    s += T(790, 542, "仲裁速率(ACK/EOF)", 12.5, MUTED)
    s += T(600, 620, "DLC 非连续映射:0~8 直映,9~15 → 12/16/20/24/32/48/64 字节", 13, MUTED)
    return s + close_svg()


# ---------------------------------------------------------------- 图 8

def fig8():
    h = 640
    s = open_svg(h, "图 8 位时间结构与采样点", "一位时间 = Sync_Seg + Prop_Seg + Phase_Seg1 + Phase_Seg2,采样点在 PS1/PS2 边界")
    segs = [
        (140, 120, "Sync_Seg", "1 tq", "同步段", LIGHT, BRAND),
        (260, 300, "Prop_Seg", "1~8 tq", "传播段", "#f1f5f9", MUTED),
        (560, 300, "Phase_Seg1", "1~8 tq", "相位段 1", AMBER, ACCENT),
        (860, 220, "Phase_Seg2", "2~8 tq", "相位段 2", LIGHT, BRAND),
    ]
    y = 210
    for x, w, name, tq, cn, fill, stroke in segs:
        s += R(x, y, w, 54, rx=8, fill=fill, stroke=stroke, sw=1.5)
        s += T(x + w / 2, y + 23, name, 14, INK, "bold")
        s += T(x + w / 2, y + 43, tq, 11.5, MUTED)
        s += T(x + w / 2, y + 78, cn, 12.5, MUTED)
    sx = 860
    s += L(sx, 130, sx, 430, BRAND, 1.8, "5 4")
    s += T(sx, 118, "采样点", 13.5, BRAND, "bold")
    s += T(sx + 150, 345, "PS1/PS2 边界", 12.5, BRAND)
    s += L(140, 360, 1080, 360, MUTED, 1.2)
    s += T(610, 390, "一位时间 tBit = m × tq(tq = 节点时钟周期 × 预分频)", 13.5, INK)
    s += ARR(560, 470, 470, 470, ACCENT, 1.6, marker="arrA")
    s += ARR(470, 505, 560, 505, ACCENT, 1.6, marker="arrA")
    s += T(515, 486, "SJW 调整", 12.5, ACCENT)
    s += T(610, 545, "再同步:相位误差超过容差时,PS1/PS2 可伸缩 ≤ SJW(1~4 tq)", 13, MUTED)
    s += T(610, 590, "配置范围示例(ISO 11898-1:2024 Table 12,支持 FD 的实现)", 13, MUTED)
    return s + close_svg()


# ---------------------------------------------------------------- 图 9

def fig9():
    h = 640
    s = open_svg(h, "图 9 非破坏性位仲裁", "显性(0)覆盖隐性(1):ID 数值小者优先,仲裁失败节点自动转为接收")
    lanes = [
        ("节点 A(TxD)", 170, BRAND),
        ("节点 B(TxD)", 310, "#8b9bb4"),
        ("总线结果", 450, BRAND2),
    ]
    for label, y, color in lanes:
        s += T(85, y + 22, label, 14, INK, "bold", "start")
        if "A" in label:
            s += wave([(200, 0), (300, 1), (300, 1)], 140, y, 55, color, 2.2)
        elif "B" in label:
            s += wave([(200, 0), (150, 1), (450, 0)], 140, y, 55, color, 2.2)
        else:
            s += wave([(200, 0), (150, 1), (450, 0)], 140, y, 55, color, 2.6)
    # 位编号
    for xx, lbl in [(240, "ID10"), (340, "ID9"), (490, "ID8")]:
        s += L(xx, 540, xx, 552, MUTED, 1.1)
        s += T(xx, 570, lbl, 12, MUTED)
    s += L(490, 140, 490, 540, ACCENT, 1.4, "4 4")
    s += T(490, 128, "A 发隐性,B 发显性 → B 胜出", 13, ACCENT, "bold")
    s += T(610, 606, "非破坏性:胜者继续发送,无需重发;失败节点在帧间空间后自动重发", 13.5, MUTED)
    return s + close_svg()


# ---------------------------------------------------------------- 图 10

def fig10():
    h = 620
    s = open_svg(h, "图 10 故障遏制状态机", "error-active → error-passive → bus-off,恢复请求 + 128 次空闲回到 active")
    states = [
        (240, "error-active", ["TEC≤127 且 REC≤127", "正常收发,主动错误帧"], GREEN, OK),
        (600, "error-passive", ["REC>127 或 TEC>127", "被动错误帧 + suspend 8 位"], AMBER, ACCENT),
        (960, "bus-off", ["TEC>255", "不发送 / 不应答 / 不拉显性"], "#fde8e8", RED),
    ]
    for cx, name, lines, fill, stroke in states:
        s += box_text(cx, 230, 260, 110, name, " ".join(lines), tsize=16, ssize=12.5, fill=fill, stroke=stroke)
    s += ARR(380, 230, 470, 230, ACCENT, 2, marker="arrA")
    s += T(425, 214, "T2", 13.5, ACCENT, "bold")
    s += ARR(470, 260, 380, 260, MUTED, 1.6)
    s += T(425, 278, "T3", 12.5, MUTED, "bold")
    s += ARR(740, 230, 830, 230, RED, 2)
    s += T(785, 214, "T4", 13.5, RED, "bold")
    s += PATH("M 960 300 C 960 420 240 420 240 300", BRAND, 1.6)
    s += ARR(240, 300, 240, 288, BRAND, 1.8)
    s += T(600, 430, "T5:恢复请求 + 128 次空闲(11 连续隐性位)→ 计数清零", 13.5, BRAND, "bold")
    s += T(600, 520, "计数增减(§8.1.4):成功收发递减,错误递增;主动/被动节点规则不同", 13, MUTED)
    s += T(600, 560, "故障遏制保证单个故障节点不会拖垮总线", 13.5, INK, "bold")
    return s + close_svg()


# ---------------------------------------------------------------- 图 11

def fig11():
    h = 660
    s = open_svg(h, "图 11 TDC 发射器延迟补偿原理", "SSP = 测得环回延迟 + 可编程 TDC 偏移(以 tq 为单位)")
    lanes = [
        ("控制器 TXD", 180, BRAND),
        ("总线", 320, BRAND2),
        ("收发器 RXD(回读)", 460, OK),
    ]
    for label, y, color in lanes:
        s += T(85, y + 22, label, 14, INK, "bold", "start")
        s += wave([(150, 0), (240, 1), (240, 1), (240, 0)], 150, y, 55, color, 2.2)
    # 延迟箭头(右侧独立列,不与波形相交)
    s += ARR(1060, 210, 1060, 290, MUTED, 1.6)
    s += T(1160, 252, "td(TXD→bus)", 12.5, MUTED, "end")
    s += ARR(1060, 350, 1060, 430, MUTED, 1.6)
    s += T(1160, 392, "td(bus→RXD)", 12.5, MUTED, "end")
    s += ARR(1030, 200, 1030, 480, ACCENT, 1.5, marker="arrA", dash="5 4")
    s += T(1030, 560, "环回延迟 tLoop ≤ 190 ns", 13.5, ACCENT, "bold")
    # 采样点
    for sx, lbl, col in [(520, "正常采样点", BRAND), (760, "SSP 二次采样点", OK)]:
        s += L(sx, 100, sx, 560, col, 1.4, "4 4")
        s += T(sx, 88, lbl, 12.5, col, "bold")
    s += ARR(520, 590, 760, 590, OK, 1.8, marker="arrG")
    s += T(640, 606, "TDC 偏移(可编程,tq 为单位)", 12.5, OK, "bold")
    s += T(600, 640, "数据相位位时间 ≤1000 ns 时应使用 TDC;环回延迟越小、对称性越好,SSP 裕量越大", 13, MUTED)
    return s + close_svg()


# ---------------------------------------------------------------- 图 12

def fig12():
    h = 660
    s = open_svg(h, "图 12 物理层电平与接收判定", "显性/隐性电平、接收阈值与迟滞判定区")
    x0, x1 = 220, 900
    y0 = 560
    s += L(x0, y0, x1, y0, INK, 1.6)
    s += L(x0, y0, x0, 80, INK, 1.6)
    s += T(70, 330, "V / mV", 13, MUTED, anchor="start")
    for val, y in [(0, 560), (500, 480), (900, 416), (1500, 320), (3000, 80)]:
        s += L(x0 - 6, y, x0, y, INK, 1.2)
        s += T(x0 - 16, y + 4, str(val), 12, MUTED, anchor="end")
    s += R(x0 + 40, 80, 600, 240, rx=10, fill="rgba(15,76,129,0.10)", stroke=BRAND, dash="5 4")
    s += T(880, 200, "显性区:差分 1.5~3 V", 13.5, BRAND2, "bold", "end")
    s += R(x0 + 40, 520, 600, 40, rx=10, fill="rgba(100,116,139,0.10)", stroke=MUTED, dash="5 4")
    s += T(880, 545, "隐性区:−0.5~+0.05 V", 13.5, MUTED, "bold", "end")
    for y, col in [(480, RED), (448, ACCENT), (416, MUTED)]:
        s += hline(x0 + 40, x1 - 20, y, col, 1.2, "5 4")
    legend = [(480, "0.5 V:隐性判定阈值", RED), (448, "~0.7 V:实际比较器翻转点", ACCENT), (416, "0.9 V:显性判定阈值", MUTED)]
    for i, (y, lbl, col) in enumerate(legend):
        lx = 260 + i * 300
        s += hline(lx, lx + 60, 600, col, 2.2, "5 4")
        s += T(lx + 80, 604, lbl, 12.5, col, "start")
    s += T(560, 640, "判据:隐性位必须在最早采样点前降到 0.5 V 以下,振荡时间即 Allowable Ringing Time", 13.5, MUTED)
    return s + close_svg()


# ---------------------------------------------------------------- 图 13

def fig13():
    h = 640
    s = open_svg(h, "图 13 HS-PMA 标准测试电路", "DUT + 固定负载 RL=60 Ω 与测试电容,测量点 TXD/RXD/总线")
    s += box_text(250, 260, 260, 150, "DUT 收发器", "驱动 + 接收 + SIC", fill=LIGHT, stroke=BRAND)
    s += T(100, 230, "TXD", 14, INK, "bold", "end")
    s += ARR(150, 225, 170, 225, BRAND, 2)
    s += T(100, 300, "RXD", 14, INK, "bold", "end")
    s += ARR(170, 300, 150, 300, BRAND, 2)
    s += ARR(430, 220, 470, 220, BRAND, 2)
    s += ARR(430, 290, 470, 290, BRAND, 2)
    s += L(470, 220, 550, 220, BRAND, 2)
    s += L(470, 290, 550, 290, BRAND, 2)
    s += T(500, 204, "CANH", 13, BRAND2, "bold")
    s += T(500, 274, "CANL", 13, BRAND2, "bold")
    s += box_text(680, 260, 260, 130, "RL = 60 Ω ±1%", "固定差分负载", fill="#f1f5f9", stroke=MUTED)
    s += box_text(980, 210, 180, 64, "C2 = 100 pF", "CANH 对地", fill=AMBER, stroke=ACCENT)
    s += box_text(980, 310, 180, 64, "C1 = 0", "CANL 对地", fill=AMBER, stroke=ACCENT)
    s += L(810, 225, 890, 225, MUTED, 1.5)
    s += L(810, 295, 890, 295, MUTED, 1.5)
    s += L(890, 240, 890, 278, MUTED, 1.2)
    s += box_text(680, 470, 260, 70, "CRXD = 15 pF", "RXD 测试点负载", fill=GREEN, stroke=OK)
    s += L(300, 335, 300, 430, OK, 1.5)
    s += L(300, 430, 680, 430, OK, 1.5)
    s += L(680, 430, 680, 435, OK, 1.5)
    s += T(560, 555, "测量点:示波器探头 → 总线差分 / RXD 边沿", 13, MUTED)
    s += T(600, 595, "时序测量条件(Table 17 脚注):RL=60 Ω、C1=0、C2=100 pF、CRXD=15 pF,TXD 沿 <10 ns", 13, MUTED)
    return s + close_svg()


# ---------------------------------------------------------------- 图 14

def fig14():
    h = 660
    s = open_svg(h, "图 14 总线唤醒时序", "基本唤醒(单显性 ≥ tFilter)、WUP(双显性)与 WUF(帧 ID 过滤)")
    s += T(85, 165, "总线", 14, INK, "bold", "start")
    s += wave([(140, 0), (170, 1), (60, 1), (90, 0), (50, 1), (90, 0), (60, 1), (140, 0)], 130, 195, 55, BRAND, 2.2)
    s += T(300, 112, "显性 ≥ tFilter", 12.5, ACCENT)
    s += T(520, 112, "隐性 ≥ tFilter", 12.5, MUTED)
    s += T(700, 112, "显性 ≥ tFilter", 12.5, ACCENT)
    s += R(300, 280, 400, 40, rx=8, fill=AMBER, stroke=ACCENT)
    s += T(500, 305, "唤醒模式 WUP:两个显性脉冲", 13, "#5b3a12", "bold")
    s += T(85, 400, "RXD(唤醒输出)", 14, INK, "bold", "start")
    s += wave([(140, 1), (470, 0), (230, 1), (150, 0)], 130, 430, 55, OK, 2.2)
    s += R(130, 510, 380, 90, rx=10, fill=LIGHT, stroke=BRAND)
    s += T(320, 540, "tFilter:长 0.5~5.0 µs / 短 0.15~1.8 µs", 13, BRAND2, "bold")
    s += T(320, 566, "tWake:800 µs ~ 10 ms(可选)", 12.5, MUTED)
    s += R(560, 510, 380, 90, rx=10, fill=GREEN, stroke=OK)
    s += T(750, 540, "选择性唤醒 WUF:按帧 ID 过滤", 13, "#0b4b37", "bold")
    s += T(750, 566, "Standby/Sleep 模式均依赖唤醒机制", 12.5, "#0b4b37")
    s += T(600, 632, "设计关联:唤醒滤波器决定抗毛刺与唤醒延迟的折衷", 13, MUTED)
    return s + close_svg()


# ---------------------------------------------------------------- 图 15

def fig15():
    h = 660
    s = open_svg(h, "图 15 振铃抑制电路原理", "显性→隐性转换瞬间的低阻泄放通路 + 振铃检测阻尼(各厂商专利思路)")
    s += box_text(200, 170, 240, 90, "驱动器输出级", "M1~M6 含高压/负压保护", fill=LIGHT, stroke=BRAND)
    s += box_text(560, 170, 220, 90, "总线", "CANH / CANL", fill="#f1f5f9", stroke=MUTED)
    s += box_text(940, 170, 210, 90, "振铃检测 / 阻尼", "电容耦合 · 超阈值导通", fill=GREEN, stroke=OK)
    s += box_text(200, 360, 240, 90, "Recessive Nulling", "LRN / HRN 可编程泄放", fill=AMBER, stroke=ACCENT)
    s += box_text(560, 360, 220, 90, "脉冲发生器(~200 ns)", "内部节点拉到 VCM", fill=AMBER, stroke=ACCENT)
    s += box_text(940, 360, 210, 90, "VCM 参考", "内部共模电平", fill="#f1f5f9", stroke=MUTED)
    s += ARR(320, 170, 450, 170, BRAND, 1.8)
    s += ARR(670, 215, 835, 215, OK, 1.8, marker="arrG")
    s += L(560, 260, 560, 300, MUTED, 1.5)
    s += L(560, 300, 320, 300, MUTED, 1.5)
    s += ARR(320, 300, 320, 315, MUTED, 1.5)
    s += ARR(320, 360, 450, 360, ACCENT, 1.8, marker="arrA")
    s += ARR(670, 360, 835, 360, MUTED, 1.5)
    s += ARR(940, 215, 1045, 215, MUTED, 1.5)
    s += T(600, 490, "设计要点:nulling 时长可寄存器编程;终止时刻必须与采样点错开;转换瞬间电流需评估 EMC", 13, MUTED)
    s += T(600, 530, "对应专利:TI US9606948B2(recessive nulling)、US11310072B2(瞬态触发)、Microchip US11539548B2(阻抗匹配)", 13, MUTED)
    return s + close_svg()


# ---------------------------------------------------------------- 图 16

def fig16():
    h = 620
    s = open_svg(h, "图 16 网络拓扑类型与端接", "总线型 / 星型 / 菊花链:两端 60 Ω 端接,stub 越短越好")
    def node(cx, cy, label):
        return R(cx - 28, cy - 18, 56, 36, rx=8, fill=LIGHT, stroke=BRAND) + T(cx, cy + 5, label, 12, BRAND2)
    def term(x, y):
        return R(x, y, 56, 30, rx=6, fill=AMBER, stroke=ACCENT) + T(x + 28, y + 19, "60 Ω", 11.5, "#5b3a12", "bold")
    # 面板 1:总线型
    s += T(260, 120, "总线型(推荐)", 15, INK, "bold")
    s += L(140, 240, 420, 240, BRAND, 2.4)
    s += node(280, 240, "节点 1")
    s += node(370, 240, "节点 2")
    s += term(110, 206)
    s += term(452, 206)
    # 面板 2:星型
    s += T(620, 120, "星型(注意 stub)", 15, INK, "bold")
    s += R(460, 160, 80, 40, rx=20, fill=BRAND, stroke=BRAND)
    s += T(500, 186, "集线点", 12, "#fff", "bold")
    s += L(500, 200, 500, 260, BRAND, 2.4)
    s += L(440, 220, 500, 220, BRAND, 2.4)
    s += L(560, 220, 500, 220, BRAND, 2.4)
    s += node(440, 260, "节点 A")
    s += node(500, 260, "节点 B")
    s += node(560, 260, "节点 C")
    s += T(500, 310, "星型按分支评估端接", 12, MUTED)
    # 面板 3:菊花链
    s += T(980, 120, "菊花链(较长)", 15, INK, "bold")
    s += L(840, 240, 1120, 240, BRAND, 2.4)
    s += node(880, 260, "节点 1")
    s += node(960, 260, "节点 2")
    s += node(1040, 260, "节点 3")
    s += term(810, 206)
    s += term(1152, 206)
    s += T(600, 380, "经验法则:HS-CAN 500 kbps 能工作的网络 → CAN SIC 2 Mbps 也能工作;", 13, INK)
    s += T(600, 410, "HS-CAN 2 Mbps 能工作的网络 → CAN SIC 5 Mbps 也能工作(Adamson 2020)", 13, INK)
    s += T(600, 470, "端接:总线两端各 60 Ω(等效 120 Ω);stub 越短越好;线缆阻抗 110~140 Ω(CiA 601-6)", 13, MUTED)
    s += T(600, 510, "PVC 绝缘线缆阻抗温度敏感、传播延迟大,会放大振铃,SIC 仅部分补偿", 13, MUTED)
    return s + close_svg()


# ---------------------------------------------------------------- 思维导图基础

class Node:
    def __init__(self, label, children=None, sub="", fill=WHITE, stroke=LINE):
        self.label = label
        self.sub = sub
        self.children = children or []
        self.fill = fill
        self.stroke = stroke
        self.lines = []
        self.sub_lines = []
        self.h = 40.0
        self.w = 220.0
        self.x = 0.0
        self.y = 0.0


def measure(n, tsize=13.5, ssize=11.5, max_w=200, pad=18):
    n.lines = wrap(n.label, tsize, max_w - 12)
    n.sub_lines = wrap(n.sub, ssize, max_w - 12) if n.sub else []
    n.h = len(n.lines) * tsize * 1.35 + (len(n.sub_lines) * ssize * 1.3 if n.sub_lines else 0) + pad
    for c in n.children:
        measure(c, tsize, ssize, max_w, pad)


def subtree_h(n, gap=18):
    if not n.children:
        return n.h
    return sum(subtree_h(c, gap) for c in n.children) + gap * (len(n.children) - 1)


def layout(n, x, y_top, col_step, gap):
    h = subtree_h(n, gap)
    n.x = x
    n.y = y_top + h / 2
    cy = y_top
    for c in n.children:
        ch = subtree_h(c, gap)
        layout(c, x + col_step, cy, col_step, gap)
        cy += ch + gap


def draw_mindmap(root, title, subtitle):
    measure(root)
    height = subtree_h(root) + 190
    start_x = 180
    col_step = 270
    layout(root, start_x, 120, col_step, 20)
    parts = []
    # 先画边,再画节点,保证不压字
    def edges(n):
        for c in n.children:
            px, py = n.x + n.w / 2, n.y
            cx, cy = c.x - c.w / 2, c.y
            mx = (px + cx) / 2
            parts.append(PATH(f"M {px:.1f} {py:.1f} C {mx:.1f} {py:.1f} {mx:.1f} {cy:.1f} {cx:.1f} {cy:.1f}", MUTED, 1.6))
            edges(c)
    edges(root)
    def nodes(n):
        x, y, w, h = n.x - n.w / 2, n.y - n.h / 2, n.w, n.h
        parts.append(R(x, y, w, h, rx=12, fill=n.fill, stroke=n.stroke, sw=1.5))
        ty = n.y - (8 if n.sub_lines else 4)
        parts.append(TL(n.x, ty, n.lines, 13.5, fill=INK, weight="bold"))
        if n.sub_lines:
            parts.append(TL(n.x, ty + len(n.lines) * 13.5 * 1.35 + 4, n.sub_lines, 11.5, fill=MUTED))
        for c in n.children:
            nodes(c)
    nodes(root)
    return open_svg(height, title, subtitle) + "\n".join(parts) + close_svg()


# ---------------------------------------------------------------- 图 17~22

def fig17():
    root = Node("CAN 知识体系", [
        Node("协议层", [
            Node("帧格式", sub="经典 / FD / XL"),
            Node("仲裁与错误", sub="非破坏性仲裁 · 五类错误"),
            Node("位定时", sub="采样点 · 相位裕度"),
            Node("TDC", sub="SSP 二次采样"),
        ], fill=LIGHT, stroke=BRAND),
        Node("物理层", [
            Node("电平", sub="显性 / 隐性"),
            Node("终端与拓扑", sub="60 Ω · stub"),
            Node("EMC", sub="CISPR 25 · 共模"),
            Node("振铃", sub="反射 · 阻尼"),
        ], fill=AMBER, stroke=ACCENT),
        Node("收发器芯片", [
            Node("输出级", sub="斜率 · 对称性"),
            Node("接收比较器", sub="迟滞 · 共模"),
            Node("ESD / 保护", sub="80 V 耐压"),
            Node("SIC", sub="三态阻抗"),
        ], fill=GREEN, stroke=OK),
        Node("工具与测试", [
            Node("示波器", sub="眼图 · 解码"),
            Node("SocketCAN", sub="vcan / can-utils"),
            Node("一致性", sub="ISO 16845 · plugfest"),
        ], fill="#f1f5f9", stroke=MUTED),
        Node("标准与资料", [
            Node("ISO 11898", sub="-1 / -2 / -3"),
            Node("CiA 601", sub="设计指南"),
            Node("Bosch Spec", sub="CAN FD 源头"),
        ], fill="#fde8e8", stroke=RED),
    ])
    return draw_mindmap(root, "图 17 CAN 知识体系总览", "协议 → 物理层 → 收发器 → 工具测试 → 标准资料")


def fig18():
    root = Node("CAN SIC 全流程", [
        Node("原理", [
            Node("振铃机理", sub="RC 放电 · 反射"),
            Node("三方面改进", sub="对称性 · 有源隐性 · 抑制电路"),
            Node("系统概念", sub="安全区 · Allowable Ringing"),
            Node("标准演进", sub="601-4 → ISO 11898-2:2024"),
        ], fill=LIGHT, stroke=BRAND),
        Node("设计", [
            Node("芯片架构", sub="驱动 / 接收 / SIC 控制"),
            Node("输出级", sub="三态阻抗"),
            Node("振铃抑制电路", sub="nulling · 检测阻尼"),
            Node("接收器", sub="tREC · 抗扰"),
        ], fill=AMBER, stroke=ACCENT),
        Node("测试", [
            Node("时序参数", sub="tLoop · tBit · tREC"),
            Node("电平参数", sub="VOD · 阈值 · RDIFF"),
            Node("一致性", sub="ISO 16845 · plugfest"),
            Node("EMC / 网络级", sub="IEC 62228-3 · 多节点"),
        ], fill=GREEN, stroke=OK),
    ])
    return draw_mindmap(root, "图 18 CAN SIC 全流程知识体系", "原理 → 设计 → 测试 完整知识链")


def fig19():
    root = Node("CAN FD 帧", [
        Node("仲裁场", [
            Node("11/29 位 ID"),
            Node("RRS(恒显性)"),
        ], fill=LIGHT, stroke=BRAND),
        Node("控制场", [
            Node("EDL = 1 → FD 帧"),
            Node("BRS = 1 → 数据相位提速"),
            Node("ESI = 发送方错误状态"),
            Node("DLC:9~15 → 12/16/20/24/32/48/64"),
        ], fill=AMBER, stroke=ACCENT),
        Node("数据场", [
            Node("0~64 字节"),
        ], fill=LIGHT, stroke=BRAND),
        Node("CRC 场", [
            Node("≤16 B → CRC-17"),
            Node(">16 B → CRC-21"),
            Node("含固定填充位"),
        ], fill=GREEN, stroke=OK),
        Node("ACK + EOF", [
            Node("ACK slot + delimiter"),
            Node("EOF:7 位隐性"),
        ], fill="#f1f5f9", stroke=MUTED),
    ])
    return draw_mindmap(root, "图 19 CAN FD 帧结构思维导图", "SOF → 仲裁 → 控制 → 数据 → CRC → ACK → EOF")


def fig20():
    root = Node("物理层指标体系", [
        Node("时序", [
            Node("tBit(Bus):−10~+10 ns"),
            Node("tBit(RxD):−30~+20 ns"),
            Node("tREC:−20~+15 ns"),
            Node("tLoop:≤190 ns"),
        ], fill=LIGHT, stroke=BRAND),
        Node("电平", [
            Node("显性差分 1.5~3 V"),
            Node("隐性差分 −0.5~+0.05 V"),
            Node("阈值 0.5 / 0.9 V"),
        ], fill=AMBER, stroke=ACCENT),
        Node("SIC 专项", [
            Node("tact_rec_start ≤120 ns"),
            Node("tact_rec_end ≥355 ns"),
            Node("tpas_rec_start ≤530 ns"),
            Node("RDIFF_act_rec 75~133 Ω"),
        ], fill=GREEN, stroke=OK),
        Node("EMC / 防护", [
            Node("回波损耗"),
            Node("共模抑制"),
            Node("ESD / 80 V 耐压"),
        ], fill="#fde8e8", stroke=RED),
        Node("测量条件", [
            Node("RL=60 Ω · C2=100 pF"),
            Node("CRXD=15 pF · 激励沿 <10 ns"),
        ], fill="#f1f5f9", stroke=MUTED),
    ])
    return draw_mindmap(root, "图 20 物理层指标体系思维导图", "ISO 11898-2:2024 Set C 关键参数速查")


def fig21():
    root = Node("收发器设计要点", [
        Node("输出级", [
            Node("三态阻抗:50 / 100 Ω / 60 kΩ"),
            Node("边沿斜率与对称性"),
            Node("大电流灌/拉能力"),
        ], fill=LIGHT, stroke=BRAND),
        Node("SIC 控制逻辑", [
            Node("显性→隐性边沿检测"),
            Node("窗口 ≤120 / ≥355 / ≤530 ns"),
            Node("阻抗切换精度"),
        ], fill=AMBER, stroke=ACCENT),
        Node("振铃抑制电路", [
            Node("Recessive Nulling(TI)"),
            Node("瞬态检测阻尼(Bosch/NXP)"),
            Node("阻抗匹配(Microchip)"),
        ], fill=GREEN, stroke=OK),
        Node("接收器", [
            Node("比较器迟滞"),
            Node("共模范围与输入阻抗"),
            Node("tREC 对称性"),
        ], fill="#f1f5f9", stroke=MUTED),
        Node("电源 / 保护 / 模式", [
            Node("VCC / VIO / VBAT 管理"),
            Node("ESD · 总线容错 · TXD 超时"),
            Node("Standby / Sleep / Listen-Only"),
        ], fill="#fde8e8", stroke=RED),
        Node("设计检查清单", [
            Node("竞品参数逐项对标"),
            Node("专利风险排查"),
            Node("流片前 Review 项"),
        ], fill=LIGHT, stroke=BRAND),
    ])
    return draw_mindmap(root, "图 21 收发器芯片设计要点思维导图", "输出级 → SIC 控制 → 振铃抑制 → 接收器 → 电源保护 → 检查清单")


def fig22():
    root = Node("验证测试体系", [
        Node("芯片级参数", [
            Node("时序:tLoop · tBit · tREC · SIC 窗口"),
            Node("电平:VOD · 阈值 · RDIFF_act_rec"),
            Node("保护:ESD · 总线容错"),
        ], fill=LIGHT, stroke=BRAND),
        Node("一致性测试", [
            Node("ISO 16845-1 / -2"),
            Node("ISO 11898-2:2024 Set C"),
            Node("CiA plugfest 互操作"),
        ], fill=AMBER, stroke=ACCENT),
        Node("EMC 测试", [
            Node("IEC 62228-3"),
            Node("CISPR 25 发射限值"),
            Node("共模 / 差分抗扰"),
        ], fill=GREEN, stroke=OK),
        Node("网络级验证", [
            Node("多节点星型拓扑实测"),
            Node("Safe Operating Area 仿真+台架"),
            Node("位模式:1D1R / 5D1R / 1D1R"),
        ], fill="#f1f5f9", stroke=MUTED),
        Node("测试计划", [
            Node("参数 → 条件 → 判据 → 记录"),
            Node("示波器测量流程(Hancock 2020)"),
        ], fill="#fde8e8", stroke=RED),
    ])
    return draw_mindmap(root, "图 22 验证测试体系思维导图", "芯片级 → 一致性 → EMC → 网络级 → 测试计划")


# ---------------------------------------------------------------- 图 23~26 显隐转换工作过程

def fig23():
    h = 800
    s = open_svg(h, "图 23 显性→隐性转换:SIC 工作过程总览",
                 "TXD 边沿后输出级依次进入显性、有源隐性、被动隐性,总线电压被主动拉回隐性阈值以下")

    def tx(t):
        return 120 + t * 1.2

    # TXD 车道
    s += T(60, 185, "TXD", 15, INK, "bold", "start")
    s += wave([(tx(60) - tx(0), 0), (tx(700) - tx(60), 1)], tx(0), 210, 55, BRAND, 2.2)
    s += ARR(tx(60), 150, tx(60), 185, ACCENT, 1.6, marker="arrA")
    s += T(tx(60) + 90, 142, "TXD 上升沿(t = 0)", 12.5, ACCENT)
    # 总线电压车道
    s += T(60, 330, "总线 Vdiff", 15, INK, "bold", "start")
    s += hline(tx(0), tx(700), 353, RED, 1.2, "5 4")
    s += T(tx(700) - 8, 345, "0.9 V 显性阈值", 12, RED, "end")
    s += hline(tx(0), tx(700), 374, MUTED, 1.2, "5 4")
    s += T(tx(700) - 8, 366, "0.5 V 隐性阈值", 12, MUTED, "end")
    s += L(tx(0), 296, tx(60), 296, BRAND2, 2.4)
    s += damped(tx(60), tx(430), 296, 390, freq=2.2, decay=4.0, amp=0.45, color=BRAND2, sw=2.2)
    s += L(tx(430), 390, tx(700), 390, BRAND2, 2.4)
    s += T(180, 282, "显性 ≈2 V", 12, BRAND2, "bold")
    # 输出阻抗车道
    s += T(60, 470, "输出阻抗", 15, INK, "bold", "start")
    s += L(tx(0), 455, tx(60), 455, BRAND, 2.4)
    s += L(tx(60), 455, tx(60), 478, BRAND, 2.4)
    s += L(tx(60), 478, tx(430), 478, ACCENT, 2.4)
    s += L(tx(430), 478, tx(430), 501, MUTED, 2.4)
    s += L(tx(430), 501, tx(700), 501, MUTED, 2.4)
    s += T(tx(30), 443, "≈50 Ω", 12.5, BRAND, "bold")
    s += T(tx(240), 466, "≈100 Ω(有源隐性)", 12.5, ACCENT, "bold")
    s += T(tx(560), 489, "≈60 kΩ(被动隐性)", 12.5, MUTED, "bold")
    # 相位条
    y = 560
    s += R(tx(0), y, tx(60) - tx(0), 42, rx=8, fill=AMBER, stroke=ACCENT)
    s += T(tx(30), y + 26, "显性", 13, "#5b3a12", "bold")
    s += R(tx(60), y, tx(430) - tx(60), 42, rx=8, fill=LIGHT, stroke=BRAND)
    s += T(tx(245), y + 26, "有源隐性(主动拉回 + 阻尼)", 13, BRAND2, "bold")
    s += R(tx(430), y, tx(700) - tx(430), 42, rx=8, fill="#f1f5f9", stroke=MUTED)
    s += T(tx(560), y + 26, "被动隐性(自然放电)", 13, MUTED, "bold")
    # 参数箭头
    s += ARR(tx(120), y + 70, tx(120), y + 108, ACCENT, 1.5, marker="arrA")
    s += T(tx(120) + 120, y + 102, "tact_rec_start ≤ 120 ns", 12.5, ACCENT)
    s += ARR(tx(430), y + 70, tx(430), y + 108, BRAND, 1.5)
    s += T(tx(430) + 120, y + 102, "tact_rec_end ≥ 355 ns", 12.5, BRAND)
    s += ARR(tx(560), y + 70, tx(560), y + 108, MUTED, 1.5)
    s += T(tx(560) + 90, y + 136, "tpas_rec_start ≤ 530 ns", 12.5, MUTED)
    # 时间轴
    for t, lbl in [(0, "0"), (200, "200 ns"), (400, "400 ns"), (600, "600 ns")]:
        s += L(tx(t), 720, tx(t), 732, MUTED, 1.2)
        s += T(tx(t), 748, lbl, 12, MUTED)
    s += T(560, 778, "5 Mbit/s 位时间 200 ns:有源隐性覆盖整个隐性位,采样点前信号已低于 0.5 V", 13.5, MUTED)
    return s + close_svg()


def fig24():
    h = 660
    s = open_svg(h, "图 24 显性→隐性转换:输出级三态阻抗切换",
                 "显性低阻驱动 → 有源隐性中等阻抗主动拉回 → 被动隐性高阻释放")
    # 状态切换序列
    s += box_text(200, 110, 220, 54, "显性", "低阻 ≈50 Ω", tsize=15, ssize=12, fill=AMBER, stroke=ACCENT)
    s += box_text(600, 110, 220, 54, "有源隐性", "≈100 Ω", tsize=15, ssize=12, fill=LIGHT, stroke=BRAND)
    s += box_text(1000, 110, 220, 54, "被动隐性", "≈60 kΩ", tsize=15, ssize=12, fill="#f1f5f9", stroke=MUTED)
    s += ARR(310, 110, 490, 110, ACCENT, 1.8, marker="arrA")
    s += T(400, 96, "≤120 ns", 12, ACCENT)
    s += ARR(710, 110, 890, 110, MUTED, 1.8)
    s += T(800, 96, "≥355 / ≤530 ns", 12, MUTED)
    # 三面板
    panels = [
        (200, "强制差分", "CANH 高 · CANL 低", "电流 I 从 CANH 流向 CANL", AMBER, ACCENT),
        (600, "主动拉回隐性", "两线靠近 2.5 V 中点", "≈100 Ω 支路阻尼反射", LIGHT, BRAND),
        (1000, "自然放电", "输出级高阻", "总线由 60 Ω 终端放电", "#f1f5f9", MUTED),
    ]
    for cx, state, cond, note, fill, stroke in panels:
        s += T(cx, 220, state, 14, INK, "bold")
        s += R(cx - 130, 250, 260, 74, rx=10, fill=fill, stroke=stroke)
        s += T(cx, 284, cond, 12.5, BRAND2, "bold")
        s += T(cx, 306, note, 12, MUTED)
        s += L(cx - 120, 370, cx + 120, 370, BRAND, 2.6)
        s += L(cx - 120, 420, cx + 120, 420, BRAND2, 2.6)
        if cx == 200:
            s += T(cx - 140, 395, "+", 18, RED, "bold")
            s += T(cx + 130, 395, "−", 18, BRAND2, "bold")
            s += ARR(cx - 60, 395, cx + 60, 395, RED, 2, marker="arrA")
            s += T(cx, 448, "I", 13, RED, "bold")
        elif cx == 600:
            s += T(cx, 395, "≈0 V 差分", 12, BRAND2)
            s += damped(cx - 100, cx + 100, 395, 395, freq=2.0, decay=5.5, amp=18, color=OK, sw=2.0)
            s += T(cx, 448, "反射被阻尼", 12.5, OK)
        else:
            s += T(cx, 395, "≈0 V 差分", 12, MUTED)
            s += T(cx - 100, 430, "— —", 12, MUTED)
            s += T(cx, 448, "靠网络放电", 12.5, MUTED)
    s += T(600, 560, "仲裁兼容:有源隐性相位中 TXD 变 LOW 必须立即切回显性(显性覆盖隐性)", 13.5, INK, "bold")
    s += T(600, 600, "RDIFF_act_rec 75~133 Ω:过低加载总线,过高失去阻尼;建议可编程/校准覆盖 PVT", 13, MUTED)
    return s + close_svg()


def fig25():
    h = 800
    s = open_svg(h, "图 25 显性→隐性转换:反射波如何被有源隐性阻抗吸收",
                 "无 SIC:反射在开放端几乎全反射、来回振荡;有 SIC:反射波进入 ≈100 Ω 有源隐性被阻尼")
    # 左:无 SIC
    s += T(290, 130, "无 SIC(被动隐性 ≈60 kΩ)", 16, RED, "bold")
    s += L(70, 260, 510, 260, MUTED, 2.4)
    s += L(290, 260, 290, 400, MUTED, 2)
    s += R(236, 400, 108, 40, rx=8, fill="#f1f5f9", stroke=MUTED)
    s += T(290, 425, "stub 末端(开放)", 12, MUTED)
    s += ARR(290, 380, 290, 300, RED, 2, marker="arrA")
    s += ARR(290, 300, 200, 250, RED, 2, marker="arrA")
    s += ARR(200, 250, 330, 300, RED, 2, marker="arrA")
    s += T(290, 200, "反射近乎全反射,来回振荡", 13, RED, "bold")
    s += R(70, 150, 90, 50, rx=10, fill="#f1f5f9", stroke=MUTED)
    s += T(115, 180, "驱动器", 12, MUTED)
    # 右:有 SIC
    s += T(890, 130, "有 SIC(有源隐性 ≈100 Ω)", 16, OK, "bold")
    s += L(690, 260, 1130, 260, BRAND, 2.4)
    s += L(910, 260, 910, 400, MUTED, 2)
    s += R(856, 400, 108, 40, rx=8, fill="#f1f5f9", stroke=MUTED)
    s += T(910, 425, "stub 末端(开放)", 12, MUTED)
    s += ARR(910, 380, 910, 310, OK, 2, marker="arrG")
    s += ARR(910, 310, 780, 220, OK, 2, marker="arrG")
    s += R(690, 150, 120, 56, rx=10, fill=GREEN, stroke=OK)
    s += T(750, 178, "有源隐性", 12.5, "#0b4b37", "bold")
    s += T(750, 196, "≈100 Ω", 11.5, "#0b4b37")
    s += T(900, 200, "反射进入低阻支路被吸收", 13, OK, "bold")
    # 底部波形对比
    s += T(290, 540, "总线波形", 14, RED, "bold")
    s += hline(90, 510, 630, RED, 1.1, "4 4")
    s += hline(90, 510, 670, MUTED, 1.1, "4 4")
    s += L(90, 500, 210, 500, RED, 2)
    s += damped(210, 510, 500, 680, freq=2.4, decay=2.6, amp=0.55, color=RED, sw=2)
    s += T(300, 720, "振铃长时间越阈 → RXD 毛刺", 13, RED)
    s += T(890, 540, "总线波形", 14, OK, "bold")
    s += hline(690, 1110, 630, RED, 1.1, "4 4")
    s += hline(690, 1110, 670, MUTED, 1.1, "4 4")
    s += L(690, 500, 810, 500, OK, 2)
    s += damped(810, 1050, 500, 650, freq=1.8, decay=7.0, amp=0.28, color=OK, sw=2)
    s += T(900, 720, "采样点前回到 0.5 V 以下", 13, OK)
    return s + close_svg()


def fig26():
    h = 880
    s = open_svg(h, "图 26 显性→隐性转换:采样点与振铃抑制窗口",
                 "SIC 窗口必须让总线在最早采样点前回到 0.5 V 以下;无 SIC 时振铃越阈导致 RXD 毛刺")

    def tx(t):
        return 120 + t * 1.2

    # 总线波形
    s += T(60, 210, "总线 Vdiff", 15, INK, "bold", "start")
    s += hline(tx(0), tx(700), 375, RED, 1.2, "5 4")
    s += T(tx(700) - 8, 367, "0.9 V", 12, RED, "end")
    s += hline(tx(0), tx(700), 394, MUTED, 1.2, "5 4")
    s += T(tx(700) - 8, 386, "0.5 V", 12, MUTED, "end")
    s += L(tx(0), 326, tx(60), 326, MUTED, 2.0, "6 4")
    s += damped(tx(60), tx(520), 326, 405, freq=2.6, decay=2.8, amp=0.5, color=RED, sw=2.0)
    s += L(tx(60), 326, tx(60), 405, MUTED, 1.2)
    s += T(210, 300, "无 SIC:振铃越阈", 13, RED, "bold")
    s += L(tx(0), 430, tx(60), 430, BRAND, 2.4)
    s += damped(tx(60), tx(360), 430, 520, freq=1.8, decay=6.5, amp=0.3, color=BRAND, sw=2.2)
    s += L(tx(360), 520, tx(700), 520, BRAND, 2.4)
    s += T(240, 416, "有 SIC:快速回到 0.5 V 以下", 13, BRAND, "bold")
    # 采样点
    sx = tx(220)
    s += L(sx, 120, sx, 660, BRAND, 1.5, "4 4")
    s += T(sx, 108, "最早采样点", 13, BRAND, "bold")
    s += T(sx, 676, "▼", 15, BRAND)
    # SIC 窗口条
    y = 570
    s += R(tx(0), y, tx(60) - tx(0), 40, rx=8, fill=AMBER, stroke=ACCENT)
    s += T(tx(30), y + 25, "显性", 12.5, "#5b3a12", "bold")
    s += R(tx(60), y, tx(430) - tx(60), 40, rx=8, fill=LIGHT, stroke=BRAND)
    s += T(tx(245), y + 25, "有源隐性 ≤120 / ≥355 ns", 12.5, BRAND2, "bold")
    s += R(tx(430), y, tx(700) - tx(430), 40, rx=8, fill="#f1f5f9", stroke=MUTED)
    s += T(tx(560), y + 25, "被动 ≤530 ns", 12.5, MUTED, "bold")
    # RXD 对比
    s += T(60, 700, "RXD(无 SIC)", 14, RED, "bold", "start")
    s += wave([(tx(60) - tx(0), 0), (tx(130) - tx(60), 1), (tx(160) - tx(130), 0), (tx(190) - tx(160), 1), (tx(700) - tx(190), 0)], tx(0), 720, 40, RED, 2.0)
    s += T(60, 800, "RXD(有 SIC)", 14, BRAND, "bold", "start")
    s += wave([(tx(60) - tx(0), 0), (tx(700) - tx(60), 1)], tx(0), 820, 40, BRAND, 2.2)
    return s + close_svg()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    default_out = os.path.abspath(os.path.join(here, "..", "public", "files", "sic-design", "images"))
    out_dir = sys.argv[1] if len(sys.argv) > 1 else default_out
    os.makedirs(out_dir, exist_ok=True)
    figures = {
        "fig1_ringing_compare.svg": fig1,
        "fig2_sic_timing.svg": fig2,
        "fig3_transceiver_arch.svg": fig3,
        "fig4_star_topology.svg": fig4,
        "fig5_safe_area.svg": fig5,
        "fig6_standard_evolution.svg": fig6,
        "fig7_can_fd_frames.svg": fig7,
        "fig8_bit_timing.svg": fig8,
        "fig9_arbitration.svg": fig9,
        "fig10_error_states.svg": fig10,
        "fig11_tdc.svg": fig11,
        "fig12_levels.svg": fig12,
        "fig13_test_circuit.svg": fig13,
        "fig14_wakeup.svg": fig14,
        "fig15_ring_suppress_circuit.svg": fig15,
        "fig16_topologies.svg": fig16,
        "fig17_can_mindmap.svg": fig17,
        "fig18_sic_mindmap.svg": fig18,
        "fig19_frame_mindmap.svg": fig19,
        "fig20_phys_mindmap.svg": fig20,
        "fig21_design_mindmap.svg": fig21,
        "fig22_test_mindmap.svg": fig22,
        "fig23_dr_overview.svg": fig23,
        "fig24_dr_impedance.svg": fig24,
        "fig25_dr_reflection.svg": fig25,
        "fig26_dr_sampling.svg": fig26,
    }
    for name, fn in figures.items():
        with open(os.path.join(out_dir, name), "w", encoding="utf-8") as f:
            f.write(fn())
        print("generated", name)
    print(f"\n共生成 {len(figures)} 张 SVG → {out_dir}")


if __name__ == "__main__":
    main()
