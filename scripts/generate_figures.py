#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CAN FD 知识库 22 张原创 SVG 技术图生成器。

用法:
    python scripts/generate_figures.py [输出目录]

默认输出到 docs/files/sic-design/images/。所有图均采用统一设计语言:
品牌蓝 #0f4c81、强调橙 #d97706、正文 #1f2933、辅助 #64748b。
重新生成后请人工抽查 2~3 张图的排版。
"""

from __future__ import annotations

import html
import math
import os
import sys

W = 1000

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


def esc(s: str) -> str:
    return html.escape(str(s), quote=False)


def T(
    x: float,
    y: float,
    s: str,
    size: float = 15,
    fill: str = INK,
    weight: str = "normal",
    anchor: str = "middle",
    family: str = FONT,
    style: str = "",
) -> str:
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="{family}" font-size="{size}" '
        f'fill="{fill}" font-weight="{weight}" text-anchor="{anchor}"{style}>{esc(s)}</text>'
    )


def TL(
    x: float,
    y: float,
    lines: list[str],
    size: float = 14,
    lh: float = 1.4,
    fill: str = INK,
    weight: str = "normal",
    anchor: str = "middle",
) -> str:
    """多行文本,以首行基线 y 为基准向下排。"""
    out = []
    for i, ln in enumerate(lines):
        out.append(T(x, y + i * size * lh, ln, size, fill, weight, anchor))
    return "\n".join(out)


def R(
    x: float,
    y: float,
    w: float,
    h: float,
    rx: float = 8,
    fill: str = WHITE,
    stroke: str = LINE,
    sw: float = 1.3,
    dash: str | None = None,
) -> str:
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
    )


def box(
    x: float,
    y: float,
    w: float,
    h: float,
    title: str = "",
    lines: list[str] | None = None,
    fill: str = WHITE,
    stroke: str = LINE,
    title_size: float = 15,
    line_size: float = 12.5,
    title_fill: str = INK,
    weight: str = "bold",
) -> str:
    parts = [R(x, y, w, h, fill=fill, stroke=stroke)]
    cx = x + w / 2
    if title:
        parts.append(T(cx, y + 24, title, title_size, title_fill, weight))
    if lines:
        parts.append(TL(cx, y + h / 2 + (6 if title else 0), lines, line_size))
    return "\n".join(parts)


def L(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    stroke: str = MUTED,
    sw: float = 1.5,
    dash: str | None = None,
) -> str:
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="{stroke}" stroke-width="{sw}"{d}/>'
    )


def ARR(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    color: str = BRAND,
    sw: float = 1.8,
    dash: str | None = None,
    marker: str = "arr",
) -> str:
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="{color}" stroke-width="{sw}" marker-end="url(#{marker})"{d}/>'
    )


def PATH(d: str, stroke: str = BRAND, sw: float = 1.8, fill: str = "none") -> str:
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def DEFS() -> str:
    return f"""<defs>
<marker id="arr" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
  <path d="M0,0 L8,3 L0,6 Z" fill="{BRAND}"/>
</marker>
<marker id="arrA" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
  <path d="M0,0 L8,3 L0,6 Z" fill="{ACCENT}"/>
</marker>
<marker id="arrG" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
  <path d="M0,0 L8,3 L0,6 Z" fill="{OK}"/>
</marker>
<marker id="dot" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
  <circle cx="4" cy="4" r="3" fill="{MUTED}"/>
</marker>
</defs>"""


def open_svg(h: float, title: str, subtitle: str = "") -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" font-family="{FONT}">
<rect x="0" y="0" width="{W}" height="{h}" fill="{WHITE}"/>
<rect x="0" y="0" width="{W}" height="62" fill="{BRAND2}"/>
<text x="36" y="30" font-size="22" font-weight="bold" fill="#ffffff">{esc(title)}</text>
<text x="36" y="51" font-size="13" fill="#c7d6ea">{esc(subtitle)}</text>
{DEFS()}
"""


def close_svg() -> str:
    return "</svg>\n"


def write_svg(name: str, content: str, out_dir: str) -> str:
    path = os.path.join(out_dir, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path


# ---------------------------------------------------------------- 波形工具

def step_path(points: list[tuple[float, float]]) -> str:
    """points: [(x, y), ...],绘制阶梯波形(第一段竖线起点)。"""
    if not points:
        return ""
    d = f"M {points[0][0]:.1f} {points[0][1]:.1f}"
    for i in range(1, len(points)):
        x, y = points[i]
        px, py = points[i - 1]
        d += f" L {x:.1f} {py:.1f} L {x:.1f} {y:.1f}"
    return d


def wave_step(
    segs: list[tuple[float, float, float]],  # (起始x, 宽度, 电平[0..1])
    y0: float,
    amp: float,
    color: str = BRAND,
    sw: float = 2.0,
) -> str:
    """画数字波形。y0=电平0的y坐标,amp=电平1与0的y距离。"""
    pts = [(segs[0][0], y0 + segs[0][2] * amp)]
    x = segs[0][0]
    for w_, _, lv in segs:
        x2 = x + w_
        pts.append((x2, y0 + lv * amp))
        x = x2
    d = f"M {pts[0][0]:.1f} {pts[0][1]:.1f}"
    for i in range(1, len(pts)):
        d += f" L {pts[i][0]:.1f} {pts[i - 1][1]:.1f} L {pts[i][0]:.1f} {pts[i][1]:.1f}"
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linejoin="round"/>'


def damped_path(
    x0: float,
    x1: float,
    y_start: float,
    y_end: float,
    freq: float = 3.2,
    decay: float = 5.5,
    amp: float = 0.5,
    color: str = BRAND,
    sw: float = 2.2,
) -> str:
    """阻尼振荡曲线:从 y_start 衰减到 y_end。"""
    n = 120
    pts = []
    for i in range(n + 1):
        t = i / n
        xx = x0 + (x1 - x0) * t
        yy = y_end + (y_start - y_end) * math.exp(-decay * t) * math.cos(2 * math.pi * freq * t)
        pts.append((xx, yy))
    d = "M " + " L ".join(f"{px:.1f} {py:.1f}" for px, py in pts)
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linejoin="round"/>'


def axis(
    x0: float,
    y0: float,
    x1: float,
    y1: float,
    label_x: str = "",
    label_y: str = "",
) -> str:
    parts = [L(x0, y0, x1, y0, INK, 1.6), L(x0, y0, x0, y1, INK, 1.6)]
    if label_x:
        parts.append(T((x0 + x1) / 2, y0 + 30, label_x, 13, MUTED))
    if label_y:
        parts.append(T(x0 - 38, (y0 + y1) / 2, label_y, 13, MUTED))
    return "\n".join(parts)


def hline_dashed(x0: float, x1: float, y: float, color: str = MUTED, dash: str = "6 4") -> str:
    return L(x0, y, x1, y, color, 1.3, dash)


# ---------------------------------------------------------------- 树布局(思维导图)

class Node:
    def __init__(
        self,
        label: str,
        children: list["Node"] | None = None,
        sub: str = "",
        fill: str = WHITE,
        stroke: str = LINE,
        label_size: float = 14,
    ):
        self.label = label
        self.sub = sub
        self.children = children or []
        self.fill = fill
        self.stroke = stroke
        self.label_size = label_size
        self.x = 0.0
        self.y = 0.0


def node_h(n: Node, base: float = 40.0, sub_extra: float = 12.0) -> float:
    if n.sub:
        return base + sub_extra
    return base


def tree_h(n: Node, gap: float = 14.0) -> float:
    if not n.children:
        return node_h(n)
    return sum(tree_h(c, gap) for c in n.children) + gap * (len(n.children) - 1)


def layout_tree(n: Node, x: float, y_top: float, col_w: float, gap: float = 14.0) -> None:
    h = tree_h(n, gap)
    n.x = x
    n.y = y_top + h / 2
    cy = y_top
    for c in n.children:
        ch_h = tree_h(c, gap)
        layout_tree(c, x + col_w, cy, col_w, gap)
        cy += ch_h + gap


def draw_tree(n: Node, col_w: float, node_w: float) -> str:
    parts = []
    for c in n.children:
        px = n.x + node_w / 2
        py = n.y
        cx = c.x - node_w / 2
        cy = c.y
        mx = (px + cx) / 2
        parts.append(PATH(f"M {px:.1f} {py:.1f} C {mx:.1f} {py:.1f} {mx:.1f} {cy:.1f} {cx:.1f} {cy:.1f}", MUTED, 1.5))
        parts.append(draw_tree(c, col_w, node_w))
    h = node_h(n)
    x = n.x - node_w / 2
    y = n.y - h / 2
    parts.append(R(x, y, node_w, h, rx=10, fill=n.fill, stroke=n.stroke, sw=1.4))
    if n.sub:
        parts.append(T(n.x, n.y - 1, n.label, n.label_size, INK, "bold"))
        parts.append(T(n.x, n.y + 15, n.sub, 11.5, MUTED))
    else:
        parts.append(T(n.x, n.y + 4, n.label, n.label_size, INK, "bold"))
    return "\n".join(parts)


def mindmap_svg(
    title: str,
    subtitle: str,
    root: Node,
    height: float,
    col_w: float = 230,
    node_w: float = 218,
    gap: float = 14,
) -> str:
    del height  # 高度按内容自动计算
    h = tree_h(root, gap) + 190
    layout_tree(root, 150, 96, col_w, gap)
    body = draw_tree(root, col_w, node_w)
    return open_svg(h, title, subtitle) + body + close_svg()


# ================================================================ 图 1

def fig1() -> str:
    h = 560
    s = open_svg(h, "图 1 总线振铃现象对比", "常规 CAN FD 显性→隐性转换后振铃越阈;CAN SIC 有源隐性快速压振铃")
    x0, x1 = 90, 940
    # 阈值线
    s += hline_dashed(x0, x1, 190, RED, "5 4")
    s += T(x1 - 8, 185, "0.9 V 显性阈值", 12, RED, anchor="end")
    s += hline_dashed(x0, x1, 265, MUTED, "5 4")
    s += T(x1 - 8, 260, "0.5 V 隐性阈值", 12, MUTED, anchor="end")
    # 上波形:常规 CAN FD
    s += T(60, 120, "常规 CAN FD(无 SIC)", 14, INK, "bold", anchor="start")
    s += damped_path(300, 620, 140, 290, freq=2.8, decay=4.2, amp=0.45, color=BRAND, sw=2.2)
    s += L(90, 140, 300, 140, BRAND, 2.2)
    s += L(620, 290, 940, 290, BRAND, 2.2)
    s += T(600, 330, "振铃越过 0.9 V/0.5 V → RXD 出现伪毛刺", 13, RED)
    # 下波形:CAN SIC
    s += T(60, 390, "CAN SIC(有源隐性)", 14, OK, "bold", anchor="start")
    s += L(90, 410, 300, 410, OK, 2.2)
    s += damped_path(300, 560, 410, 470, freq=2.2, decay=7.5, amp=0.35, color=OK, sw=2.2)
    s += L(560, 470, 940, 470, OK, 2.2)
    s += T(600, 505, "有源隐性快速拉低并阻尼反射 → 采样前已低于 0.5 V", 13, OK)
    # 位时间标注
    s += L(300, 545, 300, 560, MUTED, 1.2)
    s += L(500, 545, 500, 560, MUTED, 1.2)
    s += T(400, 555, "5 Mbit/s 数据相位位时间 = 200 ns", 12.5, MUTED)
    s += T(940, 560, "", 10, MUTED)
    return s + close_svg()


# ================================================================ 图 2

def fig2() -> str:
    h = 620
    s = open_svg(h, "图 2 SIC 事件时序", "显性 → 有源隐性 → 被动隐性三相位,参数取 ISO 11898-2:2024 Set C")
    x0, x1 = 90, 940
    # 时间轴刻度
    for xx, lbl in [(190, "0 ns"), (440, "200 ns"), (690, "400 ns"), (940, "600 ns")]:
        s += L(xx, 540, xx, 550, MUTED, 1.2)
        s += T(xx, 565, lbl, 12, MUTED)
    # TXD 波形
    s += T(50, 92, "TXD", 14, INK, "bold", anchor="start")
    s += wave_step([(90, 210, 0), (210, 0.5, 1)], 120, 60, BRAND, 2.2)
    # 电平标注
    s += T(300, 95, "显性", 13, BRAND)
    s += T(300, 155, "隐性", 13, MUTED)
    # 总线输出阻抗相位
    s += T(50, 232, "总线", 14, INK, "bold", anchor="start")
    s += wave_step([(90, 210, 0), (210, 0.5, 1)], 260, 60, BRAND2, 2.2)
    # 相位条
    y = 360
    s += R(90, y, 210, 34, rx=6, fill=AMBER, stroke=ACCENT)
    s += T(195, y + 21, "显性 R≈50 Ω", 13, "#5b3a12", "bold")
    s += R(300, y, 390, 34, rx=6, fill=LIGHT, stroke=BRAND)
    s += T(495, y + 21, "有源隐性 R≈100 Ω(RDIFF_act_rec 75~133 Ω)", 13, BRAND2, "bold")
    s += R(690, y, 250, 34, rx=6, fill="#f1f5f9", stroke=MUTED)
    s += T(815, y + 21, "被动隐性 R≈60 kΩ", 13, MUTED, "bold")
    # 时序箭头
    s += ARR(90, 330, 300, 330, ACCENT, 1.6)
    s += T(195, 322, "tact_rec_start ≤ 120 ns", 12, ACCENT)
    s += ARR(300, 440, 690, 440, BRAND, 1.6)
    s += T(495, 432, "tact_rec_end ≥ 355 ns", 12, BRAND)
    s += ARR(690, 330, 940, 330, MUTED, 1.6)
    s += T(815, 322, "tpas_rec_start ≤ 530 ns", 12, MUTED)
    # 底部说明
    s += T(515, 500, "tSIC_TX_base(+300~+530 ns,自 TXD 上升沿 50% 阈值起测)覆盖整个数据相位隐性位", 13, MUTED)
    return s + close_svg()


# ================================================================ 图 3

def fig3() -> str:
    h = 620
    s = open_svg(h, "图 3 收发器芯片架构", "CAN SIC 收发器内部模块:驱动、SIC 控制、接收器、电源与保护")
    # 外围引脚
    s += T(80, 95, "TXD", 15, INK, "bold")
    s += ARR(120, 90, 210, 90, BRAND, 2)
    s += T(80, 560, "RXD", 15, INK, "bold")
    s += ARR(210, 560, 120, 560, BRAND, 2)
    s += T(920, 95, "CANH", 15, INK, "bold")
    s += ARR(790, 180, 880, 180, BRAND, 2)
    s += T(920, 130, "CANL", 15, INK, "bold")
    s += ARR(790, 230, 880, 230, BRAND, 2)
    # 主芯片框
    s += R(200, 60, 600, 500, rx=16, fill="#fbfdff", stroke=BRAND, sw=2)
    s += T(500, 88, "CAN SIC 收发器芯片", 18, BRAND2, "bold")
    # 内部模块
    s += box(240, 120, 240, 90, "驱动控制逻辑", ["边沿检测 / 模式控制 / 斜率控制"], fill=LIGHT, stroke=BRAND)
    s += box(520, 120, 250, 90, "输出级(驱动器)", ["显性 50 Ω / 有源隐性 100 Ω / 被动 60 kΩ"], fill=AMBER, stroke=ACCENT)
    s += box(240, 400, 240, 90, "接收器(比较器)", ["迟滞 / 共模范围 / 输入阻抗"], fill=GREEN, stroke=OK)
    s += box(520, 400, 250, 90, "SIC 控制逻辑", ["时序窗口 ≤120 / ≥355 / ≤530 ns,阻抗切换"], fill=LIGHT, stroke=BRAND)
    s += box(240, 250, 530, 90, "电源管理与保护", ["VCC / VIO / VBAT · ESD · 总线容错 · TXD 超时 · 唤醒"], fill="#f1f5f9", stroke=MUTED)
    # 连接
    s += ARR(480, 165, 520, 165, BRAND, 1.8)
    s += ARR(360, 165, 360, 250, MUTED, 1.5)
    s += ARR(360, 250, 360, 400, MUTED, 1.5)
    s += ARR(645, 250, 645, 400, MUTED, 1.5)
    s += ARR(240, 445, 180, 445, MUTED, 1.5)
    s += L(180, 445, 180, 90, MUTED, 1.5)
    s += ARR(180, 90, 240, 90, MUTED, 1.5)
    # 总线连接
    s += L(770, 180, 790, 180, BRAND, 2)
    s += L(770, 230, 790, 230, BRAND, 2)
    s += L(770, 180, 770, 205, BRAND, 2)
    s += L(770, 205, 770, 230, BRAND, 2)
    s += T(515, 565, "三大设计域:输出级(对称性/斜率/SIC 阻抗)· SIC 控制(时序窗口)· 接收器(tREC/抗扰度)", 13, MUTED)
    return s + close_svg()


# ================================================================ 图 4

def fig4() -> str:
    h = 560
    s = open_svg(h, "图 4 星型拓扑与 stub 反射", "未端接 stub 末端产生反射,反射波在网络中来回振荡形成振铃")
    # 主干
    y = 250
    s += L(120, y, 880, y, BRAND, 3)
    s += T(500, y - 18, "总线主干 CANH / CANL(双绞线)", 14, INK, "bold")
    # 终端
    s += R(70, y - 16, 70, 32, rx=6, fill=AMBER, stroke=ACCENT)
    s += T(105, y + 7, "60 Ω", 13, "#5b3a12", "bold")
    s += R(860, y - 16, 70, 32, rx=6, fill=AMBER, stroke=ACCENT)
    s += T(895, y + 7, "60 Ω", 13, "#5b3a12", "bold")
    # stub
    for sx, label in [(280, "stub 1(短,已端接)"), (500, "stub 2(中)"), (720, "stub 3(长,未端接)")]:
        s += L(sx, y, sx, 360, MUTED, 2)
        s += R(sx - 70, 360, 140, 40, rx=8, fill=LIGHT, stroke=BRAND)
        s += T(sx, 383, label, 13, BRAND2)
    # 反射
    s += ARR(720, 400, 720, 330, ACCENT, 1.8)
    s += T(720, 430, "阻抗突变 → 反射", 13, ACCENT)
    s += damped_path(560, 760, 300, 300, freq=3.4, decay=3.0, amp=36, color=RED, sw=1.8)
    s += T(660, 210, "反射波沿 stub 返回总线,来回振荡 → 叠加在有用信号上", 13.5, RED)
    s += T(500, 490, "stub 越长、数量越多,等效电容越大,振荡越持久,采样点前难以衰减干净", 13.5, MUTED)
    return s + close_svg()


# ================================================================ 图 5

def fig5() -> str:
    h = 600
    s = open_svg(h, "图 5 安全操作区与采样点", "信号可在安全操作区内自由振荡,但必须在最早隐性采样点前回到 0.5 V 以下")
    x0, x1 = 90, 940
    s += hline_dashed(x0, x1, 200, RED, "5 4")
    s += T(x1 - 8, 195, "0.9 V(显性阈值)", 12, RED, anchor="end")
    s += hline_dashed(x0, x1, 275, MUTED, "5 4")
    s += T(x1 - 8, 270, "0.5 V(隐性阈值)", 12, MUTED, anchor="end")
    # 安全操作区(带色带)
    s += R(470, 285, 430, 90, rx=6, fill="rgba(22,163,74,0.12)", stroke=OK, dash="5 4")
    s += T(685, 315, "安全操作区", 14, OK, "bold")
    s += T(685, 340, "信号可自由振荡,只要在最早采样点前", 12, MUTED)
    s += T(685, 358, "回到 0.5 V 以下(Allowable Ringing Time)", 12, MUTED)
    # 波形
    s += L(x0, 170, 300, 170, BRAND, 2.2)
    s += damped_path(300, 940, 170, 330, freq=2.6, decay=3.6, amp=0.5, color=BRAND, sw=2.2)
    # 采样点
    for sx, lbl in [(620, "最早采样点"), (840, "最晚采样点")]:
        s += L(sx, 130, sx, 560, BRAND, 1.4, "4 4")
        s += T(sx, 120, lbl, 12.5, BRAND)
        s += T(sx, 545, "▼", 14, BRAND)
    s += ARR(300, 420, 620, 420, OK, 1.8, marker="arrG")
    s += T(460, 410, "允许振铃时间(Allowable Ringing Time)", 13, OK)
    s += T(515, 580, "SIC 价值:① 收紧对称性 → 扩大安全区;② 快速压振铃 → 尽早进入安全区", 13.5, MUTED)
    return s + close_svg()


# ================================================================ 图 6

def fig6() -> str:
    h = 560
    s = open_svg(h, "图 6 SIC 标准演进", "CAN FD → CAN SIC → CAN XL:参数集 Set A/B/C 与 Annex A")
    nodes = [
        (120, "2012", "Bosch CAN FD Spec v1.0", "CAN FD 协议源头(免费 PDF)", LIGHT, BRAND),
        (300, "2016", "ISO 11898-2:2016", "常规 CAN FD 收发器参数", LIGHT, BRAND),
        (480, "2019", "CiA 601-4", "SIC 原始规范 v2.0.0", AMBER, ACCENT),
        (660, "2023", "CiA 601-4 撤回", "内容并入 ISO 11898-2", "#f1f5f9", MUTED),
        (840, "2024", "ISO 11898-2:2024 第三版", "Set A(≤2M) / Set B(≤5M) / Set C(≤8M, SIC)", LIGHT, BRAND),
    ]
    y = 250
    for x, yr, name, desc, fill, stroke in nodes:
        s += R(x - 90, y - 58, 180, 116, rx=12, fill=fill, stroke=stroke, sw=1.6)
        s += T(x, y - 34, yr, 15, BRAND2, "bold")
        s += T(x, y - 10, name, 14, INK, "bold")
        s += TL(x, y + 12, [desc], 11.5, fill=MUTED)
    # 时间线
    s += L(120, y + 95, 840, y + 95, BRAND, 2)
    for x in [120, 300, 480, 660, 840]:
        s += L(x, y + 88, x, y + 102, BRAND, 2)
    s += ARR(480, y + 150, 660, y + 150, ACCENT, 1.8, marker="arrA")
    s += T(570, y + 140, "并入(2023)", 13, ACCENT)
    s += ARR(660, y + 180, 840, y + 180, BRAND, 1.8)
    s += T(750, y + 170, "发布", 13, BRAND)
    # Annex A
    s += R(720, 430, 240, 80, rx=12, fill=GREEN, stroke=OK, sw=1.6)
    s += T(840, 460, "Annex A / FAST 模式", 14, "#0b4b37", "bold")
    s += T(840, 482, "≤20 Mbit/s · CAN XL 兼容 · SIC 向后兼容", 12, "#0b4b37")
    s += ARR(840, 370, 840, 430, OK, 1.8, marker="arrG")
    return s + close_svg()


# ================================================================ 图 7

def fig7() -> str:
    h = 600
    s = open_svg(h, "图 7 经典 CAN vs CAN FD 帧格式", "CAN FD 的秘密在控制场:EDL / BRS / ESI 三个标志位")
    # 经典 CAN
    s += T(90, 100, "经典 CAN 数据帧", 16, INK, "bold", anchor="start")
    cls = [
        (90, "SOF", "1 位", "显性"),
        (170, "仲裁场", "11/29 位 ID + RTR", ""),
        (330, "控制场", "IDE · r1 + DLC", ""),
        (450, "数据场", "0~8 字节", ""),
        (540, "CRC", "15 位 + delimiter", ""),
        (660, "ACK", "slot + delimiter", ""),
        (740, "EOF", "7 位隐性", ""),
    ]
    for x, name, sub, note in cls:
        w = 90 if name in ("SOF", "ACK") else 120 if name != "EOF" else 100
        s += R(x, 118, w, 52, rx=6, fill=LIGHT, stroke=BRAND)
        s += T(x + w / 2, 138, name, 14, BRAND2, "bold")
        s += T(x + w / 2, 158, sub, 11.5, MUTED)
    # CAN FD
    s += T(90, 280, "CAN FD 数据帧", 16, INK, "bold", anchor="start")
    fd = [
        (90, "SOF", "1 位", "显性", LIGHT, BRAND),
        (170, "仲裁场", "11/29 位 ID + RRS", "", LIGHT, BRAND),
        (330, "控制场", "IDE·EDL·res·BRS·ESI·DLC", "", AMBER, ACCENT),
        (460, "数据场", "0~64 字节", "", LIGHT, BRAND),
        (560, "CRC", "17/21 位 + 填充", "", LIGHT, BRAND),
        (680, "ACK", "slot + delimiter", "", LIGHT, BRAND),
        (760, "EOF", "7 位隐性", "", LIGHT, BRAND),
    ]
    for x, name, sub, note, fill, stroke in fd:
        w = 90 if name in ("SOF", "ACK") else 130 if name == "控制场" else 100
        s += R(x, 298, w, 56, rx=6, fill=fill, stroke=stroke, sw=1.6 if name == "控制场" else 1.3)
        s += T(x + w / 2, 320, name, 14, BRAND2 if name != "控制场" else "#5b3a12", "bold")
        s += T(x + w / 2, 341, sub, 11.5, MUTED)
    # BRS 速率切换标注
    s += ARR(410, 230, 410, 298, ACCENT, 1.8, marker="arrA")
    s += T(505, 242, "BRS 隐性 → 数据相位高速率(如 2/5 Mbit/s)", 13, ACCENT)
    s += ARR(620, 230, 620, 298, MUTED, 1.8)
    s += T(700, 242, "CRC delimiter 切回仲裁速率", 12.5, MUTED)
    s += T(515, 395, "一句话记忆:EDL 决定「这是什么帧」,BRS 决定「数据段跑多快」,ESI 报告「发送方状态」", 14, INK, "bold")
    # 仲裁/数据相位条
    s += R(90, 440, 320, 34, rx=6, fill="#f1f5f9", stroke=MUTED)
    s += T(250, 462, "仲裁相位(经典速率,如 500 kbit/s)", 13, MUTED)
    s += R(410, 440, 210, 34, rx=6, fill=GREEN, stroke=OK)
    s += T(515, 462, "数据相位(高速率)", 13, "#0b4b37", "bold")
    s += R(620, 440, 280, 34, rx=6, fill="#f1f5f9", stroke=MUTED)
    s += T(760, 462, "仲裁速率(ACK/EOF)", 13, MUTED)
    return s + close_svg()


# ================================================================ 图 8

def fig8() -> str:
    h = 600
    s = open_svg(h, "图 8 位时间结构与采样点", "一位时间 = Sync_Seg + Prop_Seg + Phase_Seg1 + Phase_Seg2,采样点在 PS1/PS2 边界")
    y0, y1 = 220, 260
    segs = [
        (110, 100, "Sync_Seg", "1 tq", "同步段", LIGHT, BRAND),
        (210, 260, "Prop_Seg", "1~8 tq", "传播段", "#f1f5f9", MUTED),
        (470, 260, "Phase_Seg1", "1~8 tq", "相位段 1", AMBER, ACCENT),
        (730, 180, "Phase_Seg2", "2~8 tq", "相位段 2", LIGHT, BRAND),
    ]
    for x, w, name, tq, cn, fill, stroke in segs:
        s += R(x, y0, w, 40, rx=6, fill=fill, stroke=stroke, sw=1.5)
        s += T(x + w / 2, y0 + 18, name, 14, INK, "bold")
        s += T(x + w / 2, y0 + 33, tq, 11.5, MUTED)
    # 采样点
    sx = 730
    s += L(sx, 150, sx, 420, BRAND, 1.8, "5 4")
    s += T(sx, 138, "采样点", 13.5, BRAND)
    s += T(sx + 30, 330, "PS1/PS2 边界", 12, BRAND)
    # 下方标注
    s += L(110, 310, 910, 310, MUTED, 1.2)
    s += T(510, 340, "一位时间 tBit = m × tq(tq = 节点时钟周期 × 预分频)", 13.5, INK)
    # SJW
    s += ARR(660, 400, 560, 400, ACCENT, 1.6, marker="arrA")
    s += ARR(560, 430, 660, 430, ACCENT, 1.6, marker="arrA")
    s += T(610, 415, "SJW 调整", 12.5, ACCENT)
    s += T(610, 470, "再同步:相位误差超过容差时,PS1/PS2 可伸缩 ≤ SJW(1~4 tq)", 13, MUTED)
    s += T(510, 530, "配置范围示例(ISO 11898-1:2024 Table 12,支持 FD 的实现)", 13, MUTED)
    return s + close_svg()


# ================================================================ 图 9

def fig9() -> str:
    h = 600
    s = open_svg(h, "图 9 非破坏性位仲裁", "显性(0)覆盖隐性(1):ID 数值小者优先,仲裁失败节点自动转为接收")
    # 节点 A
    s += T(70, 110, "节点 A(TxD)", 14, INK, "bold", anchor="start")
    s += wave_step([(130, 90, 0), (220, 0.5, 1), (270, 0.5, 1), (320, 0.5, 1)], 140, 55, BRAND, 2.2)
    # 节点 B
    s += T(70, 240, "节点 B(TxD)", 14, INK, "bold", anchor="start")
    s += wave_step([(130, 90, 0), (220, 0.5, 1), (270, 0.5, 0), (320, 0.5, 0)], 270, 55, "#8b9bb4", 2.2)
    # 总线
    s += T(70, 370, "总线结果", 14, INK, "bold", anchor="start")
    s += wave_step([(130, 90, 0), (220, 0.5, 1), (270, 0.5, 0), (320, 0.5, 0)], 400, 55, BRAND2, 2.6)
    # 位编号
    for xx, lbl in [(175, "ID10"), (265, "ID9"), (315, "ID8")]:
        s += L(xx, 470, xx, 480, MUTED, 1.1)
        s += T(xx, 495, lbl, 12, MUTED)
    # 仲裁点标注
    s += L(265, 120, 265, 470, ACCENT, 1.4, "4 4")
    s += T(265, 108, "A 发隐性,B 发显性 → B 胜出", 13, ACCENT)
    s += T(515, 540, "非破坏性:胜者继续发送,无需重发;仲裁失败节点在帧间空间后自动重发", 13.5, MUTED)
    return s + close_svg()


# ================================================================ 图 10

def fig10() -> str:
    h = 620
    s = open_svg(h, "图 10 故障遏制状态机", "error-active → error-passive → bus-off,恢复请求 + 128 次空闲回到 active")
    # 三个状态
    s += box(120, 180, 220, 90, "error-active", ["TEC≤127 且 REC≤127", "正常收发,主动错误帧"], fill=GREEN, stroke=OK)
    s += box(390, 180, 220, 90, "error-passive", ["REC>127 或 TEC>127", "被动错误帧 + suspend 8 位"], fill=AMBER, stroke=ACCENT)
    s += box(660, 180, 220, 90, "bus-off", ["TEC>255", "不发送 / 不应答 / 不拉显性"], fill="#fde8e8", stroke=RED)
    # 转移
    s += ARR(340, 225, 390, 225, ACCENT, 1.8, marker="arrA")
    s += T(365, 210, "T2", 13, ACCENT, "bold")
    s += ARR(390, 290, 340, 290, MUTED, 1.6)
    s += T(365, 305, "T3", 12, MUTED, "bold")
    s += ARR(610, 225, 660, 225, RED, 1.8)
    s += T(635, 210, "T4", 13, RED, "bold")
    # 恢复
    s += PATH("M 770 270 C 770 380 220 380 220 270", BRAND, 1.6)
    s += T(495, 395, "T5:恢复请求 + 监测到 128 次空闲(11 连续隐性位)→ 计数清零", 13, BRAND)
    s += ARR(220, 270, 220, 250, BRAND, 1.8)
    # 说明表
    s += T(515, 470, "计数增减(§8.1.4):成功收发递减,错误递增;主动/被动节点规则不同", 13.5, MUTED)
    s += T(515, 500, "故障遏制保证单个故障节点不会拖垮总线", 13.5, INK, "bold")
    return s + close_svg()


# ================================================================ 图 11

def fig11() -> str:
    h = 640
    s = open_svg(h, "图 11 TDC 发射器延迟补偿原理", "SSP = 测得环回延迟 + 可编程 TDC 偏移(以 tq 为单位)")
    x0, x1 = 100, 940
    # 控制器 TXD
    s += T(70, 120, "控制器 TXD", 14, INK, "bold", anchor="start")
    s += wave_step([(x0, 260, 0), (260, 0.5, 1), (520, 0.5, 1), (780, 0.5, 0)], 150, 55, BRAND, 2.2)
    # 总线
    s += T(70, 260, "总线", 14, INK, "bold", anchor="start")
    s += wave_step([(x0 + 90, 260, 0), (350, 0.5, 1), (610, 0.5, 1), (870, 0.5, 0)], 290, 55, BRAND2, 2.2)
    # 回读 RXD
    s += T(70, 400, "收发器 RXD(回读)", 14, INK, "bold", anchor="start")
    s += wave_step([(x0 + 170, 260, 0), (430, 0.5, 1), (690, 0.5, 1), (950, 0.5, 0)], 430, 55, OK, 2.2)
    # 延迟箭头
    s += ARR(360, 205, 450, 345, MUTED, 1.5)
    s += T(355, 235, "td(TXD→bus)", 12, MUTED)
    s += ARR(450, 345, 540, 485, MUTED, 1.5)
    s += T(545, 420, "td(bus→RXD)", 12, MUTED)
    s += ARR(360, 160, 540, 450, ACCENT, 1.5, marker="arrA", dash="5 4")
    s += T(600, 265, "环回延迟 tLoop ≤ 190 ns", 13.5, ACCENT)
    # 采样点
    s += L(520, 90, 520, 560, BRAND, 1.4, "4 4")
    s += T(520, 80, "正常采样点", 12, BRAND)
    s += L(780, 90, 780, 560, OK, 1.4, "4 4")
    s += T(780, 80, "SSP 二次采样点", 12, OK)
    s += ARR(520, 530, 780, 530, OK, 1.8, marker="arrG")
    s += T(650, 545, "TDC 偏移(可编程,tq 为单位)", 12.5, OK)
    s += T(515, 600, "数据相位位时间 ≤1000 ns 时应使用 TDC;环回延迟越小、对称性越好,SSP 裕量越大", 13.5, MUTED)
    return s + close_svg()


# ================================================================ 图 12

def fig12() -> str:
    h = 620
    s = open_svg(h, "图 12 物理层电平与接收判定", "显性/隐性电平、接收阈值与迟滞判定区")
    # 坐标轴
    x0, x1 = 150, 900
    y0, y1 = 500, 120
    s += L(x0, y0, x1, y0, INK, 1.6)
    s += L(x0, y0, x0, y1, INK, 1.6)
    s += T(x0 - 40, 320, "V / mV", 13, MUTED)
    # 刻度
    for val, y in [(0, 500), (500, 370), (900, 290), (1500, 190), (3000, 40)]:
        s += L(x0 - 6, y, x0, y, INK, 1.2)
        s += T(x0 - 14, y + 4, str(val), 12, MUTED, anchor="end")
    # 区域
    s += R(x0 + 40, 40, 700, 150, rx=8, fill="rgba(15,76,129,0.10)", stroke=BRAND, dash="5 4")
    s += T(820, 150, "显性区:差分 1.5~3 V", 13.5, BRAND2, "bold", anchor="end")
    s += R(x0 + 40, 290, 700, 80, rx=8, fill="rgba(100,116,139,0.10)", stroke=MUTED, dash="5 4")
    s += T(820, 340, "隐性区:差分 −0.5~+0.05 V", 13.5, MUTED, "bold", anchor="end")
    # 阈值线
    s += hline_dashed(x0 + 40, x1 - 20, 370, RED, "5 4")
    s += T(x1 - 24, 364, "0.5 V:隐性判定阈值", 12.5, RED, anchor="end")
    s += hline_dashed(x0 + 40, x1 - 20, 290, MUTED, "5 4")
    s += T(x1 - 24, 284, "0.9 V:显性判定阈值", 12.5, MUTED, anchor="end")
    s += hline_dashed(x0 + 40, x1 - 20, 330, ACCENT, "6 5")
    s += T(x1 - 24, 324, "~0.7 V:实际比较器翻转点", 12.5, ACCENT, anchor="end")
    # 迟滞示意
    s += T(515, 580, "判据:隐性位必须在最早采样点前降到 0.5 V 以下,振荡时间即为 Allowable Ringing Time", 13.5, MUTED)
    return s + close_svg()


# ================================================================ 图 13

def fig13() -> str:
    h = 620
    s = open_svg(h, "图 13 HS-PMA 标准测试电路", "DUT + 固定负载 RL=60 Ω 与测试电容,测量点 TXD/RXD/总线")
    # DUT
    s += box(160, 180, 260, 180, "DUT 收发器", ["驱动 + 接收 + SIC", "VCC / VIO"], fill=LIGHT, stroke=BRAND)
    # 引脚
    s += T(90, 230, "TXD", 14, INK, "bold")
    s += ARR(130, 225, 160, 225, BRAND, 2)
    s += T(90, 310, "RXD", 14, INK, "bold")
    s += ARR(160, 310, 130, 310, BRAND, 2)
    # CANH / CANL
    s += ARR(420, 210, 520, 210, BRAND, 2)
    s += ARR(420, 260, 520, 260, BRAND, 2)
    s += T(470, 192, "CANH", 13, BRAND2, "bold")
    s += T(470, 242, "CANL", 13, BRAND2, "bold")
    # 负载
    s += R(520, 180, 220, 110, rx=8, fill="#f1f5f9", stroke=MUTED)
    s += T(630, 225, "RL = 60 Ω ±1%", 14, INK, "bold")
    s += T(630, 248, "(固定差分负载)", 12, MUTED)
    # 电容
    s += box(790, 170, 150, 60, "C2 = 100 pF", ["CANH 对地"], fill=AMBER, stroke=ACCENT)
    s += box(790, 250, 150, 60, "C1 = 0", ["CANL 对地"], fill=AMBER, stroke=ACCENT)
    s += L(740, 200, 790, 200, MUTED, 1.5)
    s += L(740, 280, 790, 280, MUTED, 1.5)
    s += L(790, 230, 790, 250, MUTED, 1.2)
    s += T(865, 320, "GND", 13, MUTED)
    # CRXD
    s += box(200, 440, 220, 60, "CRXD = 15 pF", ["RXD 测试点负载"], fill=GREEN, stroke=OK)
    s += L(270, 360, 270, 440, OK, 1.5)
    # 测量点
    s += T(110, 430, "测量点:示波器探头 → 总线差分 / RXD 边沿", 13, MUTED)
    s += T(515, 570, "时序测量条件(Table 17 脚注):RL=60 Ω、C1=0、C2=100 pF、CRXD=15 pF,TXD 沿 <10 ns", 13, MUTED)
    return s + close_svg()


# ================================================================ 图 14

def fig14() -> str:
    h = 600
    s = open_svg(h, "图 14 总线唤醒时序", "基本唤醒(单显性 ≥ tFilter)、WUP(双显性)与 WUF(帧 ID 过滤)")
    # 总线波形
    s += T(70, 110, "总线", 14, INK, "bold", anchor="start")
    s += wave_step([(110, 180, 0), (290, 0.5, 1), (330, 0.5, 1), (430, 0.5, 0), (470, 0.5, 1), (570, 0.5, 0), (610, 0.5, 1), (720, 0.5, 0)], 140, 55, BRAND, 2.2)
    # 标注
    s += T(200, 120, "显性 ≥ tFilter", 12.5, ACCENT)
    s += T(380, 120, "隐性 ≥ tFilter", 12.5, MUTED)
    s += T(520, 120, "显性 ≥ tFilter", 12.5, ACCENT)
    s += ARR(290, 170, 330, 170, ACCENT, 1.5, marker="arrA")
    s += ARR(430, 170, 470, 170, ACCENT, 1.5, marker="arrA")
    # WUP 窗口
    s += R(290, 230, 280, 40, rx=6, fill=AMBER, stroke=ACCENT)
    s += T(430, 256, "唤醒模式 WUP:两个显性脉冲", 13, "#5b3a12", "bold")
    # RXD 输出
    s += T(70, 340, "RXD(唤醒输出)", 14, INK, "bold", anchor="start")
    s += wave_step([(110, 180, 1), (290, 0.5, 0), (610, 0.5, 1), (720, 0.5, 0)], 370, 55, OK, 2.2)
    # 参数框
    s += R(110, 440, 380, 90, rx=10, fill=LIGHT, stroke=BRAND)
    s += T(300, 470, "tFilter:长 0.5~5.0 µs / 短 0.15~1.8 µs", 13, BRAND2, "bold")
    s += T(300, 495, "tWake:800 µs ~ 10 ms(可选)", 13, MUTED)
    s += R(530, 440, 380, 90, rx=10, fill=GREEN, stroke=OK)
    s += T(720, 470, "选择性唤醒 WUF:按帧 ID 过滤", 13, "#0b4b37", "bold")
    s += T(720, 495, "Standby/Sleep 模式均依赖唤醒机制", 12.5, "#0b4b37")
    s += T(515, 570, "设计关联:唤醒滤波器决定抗毛刺与唤醒延迟的折衷", 13, MUTED)
    return s + close_svg()


# ================================================================ 图 15

def fig15() -> str:
    h = 620
    s = open_svg(h, "图 15 振铃抑制电路原理", "显性→隐性转换瞬间的低阻泄放通路 + 振铃检测阻尼(各厂商专利思路)")
    # 驱动器
    s += box(110, 150, 220, 120, "驱动器输出级", ["M1~M6(含高压/负压保护)", "显性驱动 / 高阻"], fill=LIGHT, stroke=BRAND)
    # 总线
    s += L(330, 190, 430, 190, BRAND, 2)
    s += L(330, 230, 430, 230, BRAND, 2)
    s += T(380, 172, "CANH", 12, BRAND2)
    s += T(380, 212, "CANL", 12, BRAND2)
    s += L(430, 190, 430, 230, MUTED, 1.2)
    s += T(470, 215, "总线", 13, MUTED)
    # recessive nulling
    s += box(110, 330, 220, 100, "Recessive Nulling", ["并联低阻通路加速放电", "LRN / HRN 可编程"], fill=AMBER, stroke=ACCENT)
    s += L(220, 270, 220, 330, ACCENT, 1.8)
    s += ARR(330, 380, 430, 380, ACCENT, 1.8, marker="arrA")
    # 脉冲发生器
    s += box(420, 330, 240, 100, "脉冲发生器(~200 ns)", ["驱动 nulling 将内部节点", "拉到 VCM"], fill=AMBER, stroke=ACCENT)
    s += ARR(420, 380, 330, 380, ACCENT, 1.8)
    # 振铃检测
    s += box(420, 140, 240, 100, "振铃检测 / 阻尼", ["电容耦合 → 幅度超阈值", "导通 NMOS 泄放振铃能量"], fill=GREEN, stroke=OK)
    s += ARR(430, 190, 420, 190, OK, 1.8, marker="arrG")
    s += L(540, 190, 540, 240, MUTED, 1.5)
    s += ARR(540, 240, 540, 330, MUTED, 1.5)
    # VCM
    s += box(720, 330, 200, 100, "VCM 参考", ["内部共模电平"], fill="#f1f5f9", stroke=MUTED)
    s += ARR(660, 380, 720, 380, MUTED, 1.6)
    # 设计要点
    s += T(515, 500, "设计要点:nulling 时长可寄存器编程;终止时刻必须与采样点错开;额外低阻通路增加转换瞬间电流,需评估 EMC", 13, MUTED)
    s += T(515, 530, "对应专利:TI US9606948B2(recessive nulling)、US11310072B2(瞬态触发)、Microchip US11539548B2(阻抗匹配)", 13, MUTED)
    return s + close_svg()


# ================================================================ 图 16

def fig16() -> str:
    h = 620
    s = open_svg(h, "图 16 网络拓扑类型与端接", "总线型 / 星型 / 菊花链:两端 60 Ω 端接,stub 越短越好")
    # 三面板
    panels = [
        (60, "总线型(推荐)", [
            ("line", 90, 180, 350, 180),
            ("node", 220, 180, "节点 1"),
            ("node", 300, 180, "节点 2"),
            ("term", 60, 165, "60 Ω"),
            ("term", 380, 165, "60 Ω"),
        ]),
        (390, "星型(注意 stub)", [
            ("hub", 500, 180, "集线点"),
            ("line", 500, 180, 500, 260),
            ("line", 430, 220, 500, 220),
            ("line", 570, 220, 500, 220),
            ("node", 430, 260, "节点 A"),
            ("node", 500, 260, "节点 B"),
            ("node", 570, 260, "节点 C"),
            ("term", 390, 205, "60 Ω"),
        ]),
        (720, "菊花链(较长)", [
            ("line", 750, 180, 950, 180),
            ("node", 790, 180, "节点 1"),
            ("node", 870, 180, "节点 2"),
            ("node", 940, 180, "节点 3"),
            ("term", 720, 165, "60 Ω"),
            ("term", 970, 165, "60 Ω"),
        ]),
    ]
    for px, title, items in panels:
        s += T(px + 145, 120, title, 15, INK, "bold")
        for it in items:
            if it[0] == "line":
                s += L(it[1], it[2], it[3], it[4], BRAND, 2.4)
            elif it[0] == "node":
                s += R(it[1] - 45, it[2] - 18, 90, 36, rx=8, fill=LIGHT, stroke=BRAND)
                s += T(it[1], it[2] + 5, it[3], 12.5, BRAND2)
            elif it[0] == "term":
                s += R(it[1], it[2], 56, 30, rx=6, fill=AMBER, stroke=ACCENT)
                s += T(it[1] + 28, it[2] + 19, it[3], 12, "#5b3a12", "bold")
            elif it[0] == "hub":
                s += R(it[1] - 38, it[2] - 18, 76, 36, rx=18, fill=BRAND, stroke=BRAND)
                s += T(it[1], it[2] + 5, it[3], 12, "#fff", "bold")
    s += T(515, 350, "经验法则:HS-CAN 500 kbps 能工作的网络 → CAN SIC 2 Mbps 也能工作;", 13, INK)
    s += T(515, 378, "HS-CAN 2 Mbps 能工作的网络 → CAN SIC 5 Mbps 也能工作(Adamson 2020)", 13, INK)
    s += T(515, 430, "端接:总线两端各 60 Ω(等效 120 Ω);stub 越短越好;线缆阻抗 110~140 Ω(CiA 601-6)", 13, MUTED)
    s += T(515, 470, "PVC 绝缘线缆阻抗温度敏感、传播延迟大,会放大振铃,SIC 仅部分补偿", 13, MUTED)
    return s + close_svg()


# ================================================================ 图 17~22 思维导图

def fig17() -> str:
    root = Node(
        "CAN 知识体系",
        [
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
                Node("ESD / 保护", sub="80V 耐压"),
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
        ],
    )
    return mindmap_svg("图 17 CAN 知识体系总览", "协议 → 物理层 → 收发器 → 工具测试 → 标准资料", root, 780, col_w=216, node_w=204, gap=12)


def fig18() -> str:
    root = Node(
        "CAN SIC 全流程",
        [
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
        ],
    )
    return mindmap_svg("图 18 CAN SIC 全流程知识体系", "原理 → 设计 → 测试 完整知识链", root, 720, col_w=220, node_w=208, gap=12)


def fig19() -> str:
    root = Node(
        "CAN FD 帧",
        [
            Node("仲裁场", [
                Node("11/29 位 ID"),
                Node("RRS(恒显性)"),
            ], fill=LIGHT, stroke=BRAND),
            Node("控制场", [
                Node("EDL = 1 → FD 帧"),
                Node("BRS = 1 → 数据相位提速"),
                Node("ESI = 发送方错误状态"),
                Node("DLC:0~8 直映,9~15 → 12/16/20/24/32/48/64"),
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
        ],
    )
    return mindmap_svg("图 19 CAN FD 帧结构思维导图", "SOF → 仲裁 → 控制 → 数据 → CRC → ACK → EOF", root, 700, col_w=216, node_w=204, gap=12)


def fig20() -> str:
    root = Node(
        "物理层指标体系",
        [
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
                Node("ESD / 80V 耐压"),
            ], fill="#fde8e8", stroke=RED),
            Node("测量条件", [
                Node("RL=60 Ω · C2=100 pF"),
                Node("CRXD=15 pF · 激励沿 <10 ns"),
            ], fill="#f1f5f9", stroke=MUTED),
        ],
    )
    return mindmap_svg("图 20 物理层指标体系思维导图", "ISO 11898-2:2024 Set C 关键参数速查", root, 820, col_w=222, node_w=210, gap=12)


def fig21() -> str:
    root = Node(
        "收发器设计要点",
        [
            Node("输出级", [
                Node("三态阻抗:50 Ω / 100 Ω / 60 kΩ"),
                Node("边沿斜率与对称性"),
                Node("大电流灌/拉能力"),
            ], fill=LIGHT, stroke=BRAND),
            Node("SIC 控制逻辑", [
                Node("显性→隐性边沿检测"),
                Node("时序窗口 ≤120 / ≥355 / ≤530 ns"),
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
        ],
    )
    return mindmap_svg("图 21 收发器芯片设计要点思维导图", "输出级 → SIC 控制 → 振铃抑制 → 接收器 → 电源保护 → 检查清单", root, 880, col_w=224, node_w=212, gap=13)


def fig22() -> str:
    root = Node(
        "验证测试体系",
        [
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
        ],
    )
    return mindmap_svg("图 22 验证测试体系思维导图", "芯片级 → 一致性 → EMC → 网络级 → 测试计划", root, 820, col_w=224, node_w=212, gap=13)


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    default_out = os.path.abspath(os.path.join(here, "..", "docs", "files", "sic-design", "images"))
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
    }
    for name, fn in figures.items():
        write_svg(name, fn(), out_dir)
        print(f"generated {name}")
    print(f"\n共生成 {len(figures)} 张 SVG → {out_dir}")


if __name__ == "__main__":
    main()
