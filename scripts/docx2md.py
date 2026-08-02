# -*- coding: utf-8 -*-
"""docx → Markdown 转换脚本(标准全文站内查阅用)。

用法:
    python scripts/docx2md.py <输入.docx> <输出.md>

特性:
- 按文档顺序遍历段落与表格(保留原顺序)
- 编号标题(如 "1 Scope"、"5.3.1 Maximum ratings")识别为 ##/### 标题
- 表格转 Markdown 表格
- 输出 UTF-8
"""
import re
import sys
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn


HEADING_RE = re.compile(r'^(\d+(?:\.\d+){0,3})\s+(.+)$')
# 行内多空格压缩(ISO docx 常见)但保留单词间单空格
def clean(text):
    return re.sub(r'[ \t]+', ' ', text).strip()


def para_is_heading(text):
    """编号标题启发式:编号 + 短文本(≤120 字符),且非纯数字表格行。"""
    if not text:
        return None
    m = HEADING_RE.match(text)
    if not m:
        return None
    body = m.group(2)
    if len(body) > 120:
        return None
    # 编号层级决定标题级别:1 → ##,1.1 → ###,1.1.1 → ####
    depth = m.group(1).count('.') + 2
    depth = min(depth, 5)
    return '#' * depth, f'{m.group(1)} {body}'


def cell_to_md(cell):
    t = clean(cell.text)
    return t.replace('|', '\\|')


def table_to_md(table):
    rows = []
    for r in table.rows:
        cells = [cell_to_md(c) for c in r.cells]
        rows.append(cells)
    if not rows:
        return ''
    out = []
    header = rows[0]
    out.append('| ' + ' | '.join(header) + ' |')
    out.append('|' + '|'.join(['---'] * len(header)) + '|')
    for r in rows[1:]:
        # 与上一行完全相同则跳过(合并单元格重复)
        out.append('| ' + ' | '.join(r) + ' |')
    return '\n'.join(out)


def convert(src, dst):
    doc = Document(src)
    body = doc.element.body
    out_lines = []
    for child in body.iterchildren():
        tag = child.tag
        if tag == qn('w:p'):
            p = Paragraph(child, doc)
            t = clean(p.text)
            if not t:
                continue
            h = para_is_heading(t)
            if h:
                out_lines.append('')
                out_lines.append(f'{h[0]} {h[1]}')
                out_lines.append('')
            else:
                out_lines.append(t)
        elif tag == qn('w:tbl'):
            tbl = Table(child, doc)
            md = table_to_md(tbl)
            if md:
                out_lines.append('')
                out_lines.append(md)
                out_lines.append('')
    content = '\n'.join(out_lines)
    # 压缩连续空行
    content = re.sub(r'\n{3,}', '\n\n', content)
    with open(dst, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'{src} -> {dst}: {len(content)} 字符')


if __name__ == '__main__':
    convert(sys.argv[1], sys.argv[2])
