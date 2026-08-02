#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 CAN FD 学习资料库各分类 README.md 提取资源元数据,输出 7 个 JSON。

用法:
    python scripts/extract_metadata.py <资料库根目录> <输出目录>

输出(文件名与分类 slug 对应,均为 ASCII):
    standards.json / patents.json / papers.json / journals.json
    books.json / vendors.json / tools-community.json

字段遵循项目设计文档 5.2 资源条目模板:
    title / type / organization / year / version / access / status
    / download / priority / audience / tags / source / local_file(可选)

纪律:
- 解析不了的字段留空并打印 WARNING 到 stderr,禁止猜测/编造。
- download 由各分类 PDF/ 目录是否存在对应文件推导(按 README 提及的文件名匹配)。
- priority 由资料库总 README 的"必读 TOP 10"表、各分类详细说明中的"必读/最关键/
  权威规范"等字样推导,默认 1。
- 仅使用标准库。
"""

import json
import os
import re
import sys
from collections import Counter

# --------------------------------------------------------------------------
# 分类目录与输出文件名
# --------------------------------------------------------------------------
CATALOG_DIRS = {
    "standards":     ("01_标准规范", "标准规范"),
    "patents":       ("02_专利", "专利"),
    "papers":        ("03_论文", "论文"),
    "journals":      ("04_期刊", "期刊"),
    "books":         ("05_教材书籍", "教材"),
    "vendors":       ("06_厂商资料", "厂商资料"),
    "tools-community": ("07_工具与社区", "工具"),
}
OUTPUT_FILES = {
    "standards": "standards.json",
    "patents": "patents.json",
    "papers": "papers.json",
    "journals": "journals.json",
    "books": "books.json",
    "vendors": "vendors.json",
    "tools-community": "tools-community.json",
}

# --------------------------------------------------------------------------
# 通用工具
# --------------------------------------------------------------------------

def warn(msg):
    print("WARNING: " + msg, file=sys.stderr)


def extract_tables(text):
    """把 markdown 中连续的 `|` 行分组为表格块,返回 list[list[str]]。"""
    tables, cur = [], []
    for ln in text.splitlines():
        s = ln.strip()
        if s.startswith("|"):
            cur.append(s)
        else:
            if cur:
                tables.append(cur)
                cur = []
    if cur:
        tables.append(cur)
    return tables


def parse_md_table(block):
    """解析一个 markdown 表格块为单元格列表,跳过分隔行。"""
    rows = []
    for s in block:
        cells = [c.strip() for c in s.strip().strip("|").split("|")]
        # 分隔行(全是 --- / :---: 之类)跳过
        if cells and all(re.fullmatch(r":?-{2,}:?", c) or c == "" for c in cells):
            continue
        rows.append(cells)
    return rows


def first_data_rows(table):
    """返回首列为数字的数据行(跳过表头与分隔行)。"""
    out = []
    for cells in parse_md_table(table):
        if cells and cells[0].isdigit():
            out.append(cells)
    return out


def extract_url(cell):
    """从单元格提取第一个 URL;支持 markdown 链接与纯 URL。"""
    if not cell:
        return None
    m = re.search(r"\[[^\]]*\]\((https?://[^)\s]+)\)", cell)
    if m:
        return m.group(1)
    m = re.search(r"https?://[^\s\u4e00-\u9fff)(]+", cell)
    if m:
        return m.group(0).rstrip("。)")  # 去掉尾部可能残留的标点
    return None


def extract_year(cell):
    """提取 4 位公历年份(第一个);无则 None。"""
    m = re.search(r"\b(19|20)\d{2}\b", cell or "")
    return int(m.group(0)) if m else None


def extract_version(cell):
    """提取 vX.Y(.Z) 形式版本号;无则 None。"""
    m = re.search(r"v\d+(\.\d+)*", cell or "")
    return m.group(0) if m else None


def map_access(cell):
    """免费/付费 列 → free|paid|member。"""
    if not cell:
        return None
    if "免费" in cell:
        return "free"
    if "成员" in cell and "付费" not in cell:
        return "member"
    if "付费" in cell:
        return "paid"
    return None


def map_status(cell):
    """验证状态列 → verified|unverified|withdrawn。"""
    if not cell:
        return None
    if any(k in cell for k in ("已撤销", "已撤回", "已下架", "withdrawn")):
        return "withdrawn"
    if "未验证" in cell or "无法验证" in cell:
        return "unverified"
    if "验证" in cell:
        return "verified"
    return None


def extract_detail_sections(text):
    """提取 `### N. ...` 详细说明节,返回 {序号: 节文本}。"""
    sections, cur = {}, None
    in_detail = False
    for ln in text.splitlines():
        if ln.startswith("## "):
            in_detail = ("详细说明" in ln or "说明" in ln)
            cur = None
            continue
        if not in_detail:
            continue
        m = re.match(r"^###\s+(\d+)\.", ln)
        if m:
            cur = int(m.group(1))
            sections[cur] = []
        elif cur is not None:
            sections[cur].append(ln)
    return {k: "\n".join(v) for k, v in sections.items()}


# --- priority 推导(详细说明中的显式字面标记) ---
PRIORITY_3_WORDS = ["必读", "最关键", "最重要", "权威规范", "金标准",
                    "最值得精读", "强烈推荐", "强烈建议"]
PRIORITY_2_WORDS = ["关键", "核心", "奠基", "直接依据", "事实标准", "重点"]


def infer_priority(text):
    """基于显式字面标记推导 priority(3/2/1)。"""
    if not text:
        return 1
    for w in PRIORITY_3_WORDS:
        if w in text:
            return 3
    for w in PRIORITY_2_WORDS:
        if w in text:
            return 2
    return 1


# --- 资料库总 README 的"必读 TOP 10"表 ---
def parse_top10(root_dir):
    """解析 `README.md` 的"快速入口:必读 TOP 10"表。

    返回 [(level, 资料名, 位置目录号), ...],level: 3/2/1。
    """
    path = os.path.join(root_dir, "README.md")
    if not os.path.exists(path):
        warn("资料库根 README 不存在: %s(TOP 10 优先级无法应用)" % path)
        return []
    with open(path, encoding="utf-8") as f:
        text = f.read()
    tables = extract_tables(text)
    top10 = []
    for t in tables:
        for cells in parse_md_table(t):
            if len(cells) >= 3 and "★" in cells[0] and not cells[0].strip().startswith("优先级"):
                star, name, loc = cells[0], cells[1], cells[2]
                if "★★★" in star:
                    level = 3
                elif "★★" in star:
                    level = 2
                else:
                    level = 1
                top10.append((level, name, loc.strip()))
    return top10


def _expand_tokens(text):
    """从 TOP10 资料名中提取匹配 token(编号/型号/专名)。

    覆盖:
      "ISO 16845-1/-2"      -> ISO 16845-1 / ISO 16845-2 / 16845-1 / 16845-2
      "CiA 601-1 / 601-3"   -> CiA 601-1 / CiA 601-3 / 601-1 / 601-3
      "ISO 11898-2:2024"    -> ISO 11898-2 / 11898-2
      "CiA 140"             -> CiA 140
      "TJA1463 / TCAN1463"  -> TJA1463 / TCAN1463
      "US9606948B2"         -> US9606948B2
      "Bosch / Adamson / Lawrenz / 饶运涛" -> 专名
    """
    tokens = set()
    # 复合编号族(含 "/" 展开)
    for m in re.finditer(
        r"\b((?:ISO|CiA|SAE|IEC)\s*)?(\d{2,5})-(\d+)\s*/\s*-?(\d+)(?:-(\d+))?",
        text,
    ):
        pre = (m.group(1) or "").strip()
        base = m.group(2)
        if m.group(5):  # "CiA 601-1 / 601-3" -> 601-3
            tokens.add(pre + " " + base + "-" + m.group(5))
            tokens.add(base + "-" + m.group(5))
        else:  # "ISO 16845-1/-2" -> 16845-2
            tokens.add(pre + " " + base + "-" + m.group(4))
            tokens.add(base + "-" + m.group(4))
    # 完整复合编号: ISO 11898-1、ISO 11898-2、CiA 601-1、ISO 16845-1
    for m in re.finditer(r"\b(ISO|CiA|SAE|IEC)\s*(\d{2,5})-(\d+)\b", text):
        tokens.add(m.group(1) + " " + m.group(2) + "-" + m.group(3))
        tokens.add(m.group(2) + "-" + m.group(3))
    # 单编号: CiA 140、SAE J2284、IEC 62228-3
    for m in re.finditer(r"\b(ISO|CiA|SAE|IEC)\s*[0-9][0-9A-Z.\-]*", text):
        tokens.add(m.group(0).replace(" ", ""))
    # 型号: TJA1463、TCAN1463、SLLA581、US9606948B2、TLE9371V
    for m in re.finditer(r"\b[A-Z]{2,}[0-9][A-Z0-9]*(?:-[A-Z0-9]+)?\b", text):
        tokens.add(m.group(0))
    # 专名
    for name in ("Bosch", "Adamson", "Lawrenz", "饶运涛"):
        if name in text:
            tokens.add(name)
    return tokens


LOC_TO_SLUG = {
    "01": "standards", "02": "patents", "03": "papers",
    "04": "journals", "05": "books", "06": "vendors", "07": "tools-community",
}


def apply_top10(items, top10, cat):
    """把 TOP10 优先级应用到分类条目(覆盖详细说明关键词结果)。"""
    for level, name, loc in top10:
        if LOC_TO_SLUG.get(loc.strip()) != cat:
            continue
        tokens = _expand_tokens(name)
        if not tokens:
            continue
        year_hint = extract_year(name)
        for it in items:
            if year_hint is not None and it.get("year") not in (None, year_hint):
                continue
            hay = (it.get("_text") or it["title"]).replace(" ", "")
            if any(tok.replace(" ", "") in hay for tok in tokens):
                it["priority"] = level


# --------------------------------------------------------------------------
# PDF 匹配(本地下载推导)
# --------------------------------------------------------------------------

def pdf_files_of(cat_dir):
    p = os.path.join(cat_dir, "PDF")
    if not os.path.isdir(p):
        return []
    return sorted(f for f in os.listdir(p) if f.lower().endswith(".pdf"))


def match_pdf_generic(pdf_files, item):
    """通用打分匹配(用于 01 标准)。"""
    text = (item.get("_text") or item["title"]).lower()
    best, best_score = None, 0
    stop = {"pdf", "can", "fd", "sic", "datasheet", "series", "with", "for",
            "the", "and", "app", "hints", "v10"}
    for f in pdf_files:
        stem = f[:-4] if f.lower().endswith(".pdf") else f
        toks = [t.lower() for t in re.split(r"[_\-.\s]+", stem) if len(t) >= 3]
        score = sum(1 for t in toks if t not in stop and t in text)
        if score > best_score:
            best, best_score = f, score
    return best if best_score >= 2 else None


def match_pdf_by_patent(pdf_files, patent_no):
    for f in pdf_files:
        if f[:-4] == patent_no:
            return f
    return None


def match_pdf_by_year_surname(pdf_files, item):
    """03 论文:文件名 `YYYY_姓氏_标题.pdf`。"""
    for f in pdf_files:
        stem = f[:-4]
        parts = stem.split("_")
        if len(parts) >= 2 and parts[0].isdigit() and parts[1]:
            if item.get("year") == int(parts[0]) and \
               parts[1].lower() in item.get("_authors", "").lower():
                return f
    return None


def match_pdf_by_year_journal(pdf_files, item):
    """04 期刊:文件名 `JYYYY_期刊关键词_标题.pdf`。"""
    for f in pdf_files:
        stem = f[:-4]
        parts = stem.split("_")
        if len(parts) >= 2 and parts[0].startswith("J") and parts[0][1:].isdigit():
            if item.get("year") == int(parts[0][1:]) and \
               parts[1].lower() in item.get("_journal", "").lower():
                return f
    return None


def match_pdf_by_model(pdf_files, title):
    """06 厂商:标题中的型号 token 出现在 PDF 文件名中。"""
    cands = re.findall(r"\b[A-Z]{2,}[0-9][A-Z0-9]*(?:-[A-Z0-9]+)?\b", title)
    cands = sorted(set(cands), key=len, reverse=True)
    for f in pdf_files:
        stem = f[:-4].upper()
        for c in cands:
            if c.upper() in stem:
                return f
    return None


# --------------------------------------------------------------------------
# 标签 / 受众
# --------------------------------------------------------------------------

def topic_keywords(title):
    """从标题提取主题标签。"""
    out = []
    pairs = [
        ("SIC", r"SIC|Signal Improvement|信号改善"),
        ("CAN FD", r"CAN ?FD|CAN-FD"),
        ("收发器", r"[Tt]ransceiver|收发器"),
        ("EMC", r"\bEMC\b|Electromagnetic|电磁|EMI|Noise"),
        ("物理层", r"physical layer|物理层"),
        ("信号完整性", r"signal integrity|Eye Diagram|眼图|overshoot|过冲"),
        ("振铃抑制", r"ringing|ring suppression|振铃|oscillation"),
        ("网络", r"[Nn]etwork|网络|bus system|总线"),
        ("协议", r"[Pp]rotocol|协议"),
        ("安全", r"Auth|Secure|Intrusion|安全|认证|IDS"),
    ]
    for tag, pat in pairs:
        if re.search(pat, title):
            out.append(tag)
    return out


def std_tags(name):
    tags = ["标准规范"]
    m = re.match(r"^(ISO|CiA|SAE|IEC)\s*[0-9][0-9A-Z/ .-]*", name)
    if m:
        tags.append(m.group(0).strip())
    else:
        tags.append(name)
    return tags


def make_local_file(slug, fname):
    return "files/%s/%s" % (slug, fname)


def clean_item(it):
    return {k: v for k, v in it.items() if not k.startswith("_")}


# --------------------------------------------------------------------------
# 各分类解析器
# --------------------------------------------------------------------------

def parse_standards(readme_text, pdf_files):
    tables = extract_tables(readme_text)
    if not tables:
        warn("[01 标准规范] 未找到表格,条目数为 0")
        return []
    rows = first_data_rows(tables[0])
    detail = extract_detail_sections(readme_text)
    items, prev_source, name_counts = [], None, Counter()
    raw = []
    for r in rows:
        # # | 名称 | 发布机构 | 版本/年份 | 免费/付费 | 链接 | 验证状态
        name, org, vercol, acc, link, stcell = r[1], r[2], r[3], r[4], r[5], r[6]
        year = extract_year(vercol)
        if not year:
            warn("[01 标准规范] %s 无年份可解析" % name)
        version = extract_version(vercol)
        access = map_access(acc)
        if access is None:
            # "—" / "已撤回" 等无法直接映射:按发布机构规则推导(详见 README 获取渠道)
            if org in ("ISO", "IEC", "SAE International"):
                access = "paid"
            elif org == "CiA":
                access = "free"
            else:
                access = ""
                warn("[01 标准规范] %s access 无法推导: %r" % (name, acc))
        status = map_status(stcell)
        if status is None:
            status = "unverified"
            warn("[01 标准规范] %s status 无法解析: %r" % (name, stcell))
        source = extract_url(link)
        if link.strip() in ("同上", "同上。"):
            source = prev_source
        if source:
            prev_source = source
        elif not source:
            warn("[01 标准规范] %s 无链接" % name)
        raw.append({
            "_name": name, "title": name, "organization": org,
            "year": year if year else "", "version": version or "",
            "access": access, "status": status, "source": source or "",
            "_version_col": vercol, "_text": name + " " + org + " " +
                        (version or "") + " " + (str(year) if year else ""),
        })
        name_counts[name] += 1
    # 同名条目 title 追加年份以区分(如 ISO 11898-1 2015 / 2024)
    for it in raw:
        if name_counts[it["_name"]] > 1:
            it["title"] = "%s (%s)" % (it["_name"],
                                       it["year"] if it["year"] else "?")
    # 组装完整条目
    for idx, it in enumerate(raw, start=1):
        dtext = detail.get(idx, "")
        priority = infer_priority(it["_version_col"] + " " + dtext)
        local = match_pdf_generic(pdf_files, it)
        items.append({
            "title": it["title"],
            "type": "标准规范",
            "organization": it["organization"],
            "year": it["year"],
            "version": it["version"],
            "access": it["access"],
            "status": it["status"],
            "download": "local" if local else "link",
            "priority": priority,
            "audience": ["模拟IC"],
            "tags": std_tags(it["_name"]),
            "source": it["source"],
            "_text": it["_text"],
        })
        if local:
            items[-1]["local_file"] = make_local_file("standards", local)
    return items


def parse_patents(readme_text, pdf_files):
    tables = extract_tables(readme_text)
    if not tables:
        warn("[02 专利] 未找到表格,条目数为 0")
        return []
    rows = first_data_rows(tables[0])
    detail = extract_detail_sections(readme_text)
    items = []
    for idx, r in enumerate(rows, start=1):
        # # | 专利号 | 标题 | 申请人 | 年份 | 技术方向 | 验证状态
        pno, title, org, yearcell, tech, stcell = r[1], r[2], r[3], r[4], r[5], r[6]
        years = re.findall(r"\b(?:19|20)\d{2}\b", yearcell)
        # 取公开年(表格中最后一个年份)
        year = int(years[-1]) if years else ""
        if not years:
            warn("[02 专利] %s 无年份" % pno)
        source = "https://patents.google.com/patent/%s/zh" % pno
        status = map_status(stcell) or "verified"
        local = match_pdf_by_patent(pdf_files, pno)
        tags = ["专利"] + [p.strip() for p in re.split(r"[/、]", tech) if p.strip()]
        dtext = detail.get(idx, "")
        priority = infer_priority(title + " " + tech + " " + dtext)
        items.append({
            "title": title,
            "type": "专利",
            "organization": org,
            "year": year,
            "version": "",
            "access": "free",
            "status": status,
            "download": "local" if local else "link",
            "priority": priority,
            "audience": ["模拟IC"],
            "tags": tags,
            "source": source,
            "_text": title + " " + org + " " + pno,
        })
        if local:
            items[-1]["local_file"] = make_local_file("patents", local)
    return items


def parse_papers(readme_text, pdf_files):
    tables = extract_tables(readme_text)
    if not tables:
        warn("[03 论文] 未找到表格,条目数为 0")
        return []
    rows = first_data_rows(tables[0])
    detail = extract_detail_sections(readme_text)
    items = []
    for idx, r in enumerate(rows, start=1):
        # # | 标题 | 作者 | 年份 | 会议/来源 | DOI/链接 | 开放获取
        title, authors, ycell, venue, link, oa = r[1], r[2], r[3], r[4], r[5], r[6]
        year = extract_year(ycell)
        if not year:
            warn("[03 论文] %s 无年份" % title)
        # 作者机构:取最后一个括号内容
        br = re.findall(r"\(([^()]*)\)", authors)
        org = br[-1].strip() if br else ""
        if not org:
            # 无机构标注:按会议发布方推导(DOI 前缀)
            if "10.1109" in link:
                org = "IEEE"
            elif "10.4271" in link:
                org = "SAE International"
            else:
                org = ""
                warn("[03 论文] %s 无机构信息" % title)
        source = extract_url(link) or ""
        if not source:
            warn("[03 论文] %s 无链接" % title)
        access = "free" if oa.startswith("✅") else "paid"
        local = match_pdf_by_year_surname(pdf_files, {
            "year": year, "_authors": authors})
        dtext = detail.get(idx, "")
        priority = infer_priority(title + " " + venue + " " + dtext)
        items.append({
            "title": title,
            "type": "论文",
            "organization": org,
            "year": year if year else "",
            "version": "",
            "access": access,
            "status": "verified",
            "download": "local" if local else "link",
            "priority": priority,
            "audience": ["模拟IC"],
            "tags": ["学术论文"] + topic_keywords(title),
            "source": source,
            "_text": title + " " + org + " " + venue +
                     " " + authors + (" " + str(year) if year else ""),
            "_authors": authors,
        })
        if local:
            items[-1]["local_file"] = make_local_file("papers", local)
    return items


def _journal_publisher(journal):
    if "IEEE" in journal:
        return "IEEE"
    if "IEICE" in journal:
        return "IEICE"
    if "EURASIP" in journal:
        return "Springer"
    if "Advanced Materials Research" in journal:
        return "Trans Tech Publications"
    if "Chips" in journal or "MDPI" in journal:
        return "MDPI"
    return ""


def parse_journals(readme_text, pdf_files):
    tables = extract_tables(readme_text)
    if not tables:
        warn("[04 期刊] 未找到表格,条目数为 0")
        return []
    rows = first_data_rows(tables[0])
    detail = extract_detail_sections(readme_text)
    # 阅读优先级建议:"先读 3→7→6→2→1→5;8、9、10 按需补充"
    pri_map = {}
    m = re.search(r"阅读优先级建议[^:：]*[:：]*(.*)", readme_text)
    if m:
        head = re.search(r"先读(.*?)(?:;|网络层|按需)", m.group(1), re.S)
        if head:
            seq = re.findall(r"(\d+)", head.group(1))[:6]
            for i, no in enumerate(seq):
                pri_map[int(no)] = 3 if i < 3 else 2
    items = []
    for idx, r in enumerate(rows, start=1):
        # # | 标题 | 作者 | 期刊 | 年份 | DOI/链接 | 开放获取 | 综述?
        title, authors, journal, ycell, doi, oa, review = (
            r[1], r[2], r[3], r[4], r[5], r[6],
            r[7] if len(r) > 7 else "")
        year = extract_year(ycell)
        if not year:
            warn("[04 期刊] %s 无年份" % title)
        # 机构:详细说明"作者 / 机构:"行的括号内容;缺失则按期刊发布方
        org = ""
        dtext = detail.get(idx, "")
        m = re.search(r"作者\s*/\s*机构[:：](.*)", dtext)
        if m:
            br = [b.strip() for b in re.findall(r"\(([^()]*)\)", m.group(1))]
            cands = [b for b in br if "未标注" not in b and "Crossref" not in b
                     and not b.startswith("机构未")]
            if cands:
                org = cands[0]
        if not org:
            org = _journal_publisher(journal)
        if not org:
            warn("[04 期刊] %s 无法确定机构" % title)
        source = (doi.strip() if doi.strip().startswith("http")
                  else "https://doi.org/" + doi.strip())
        access = "free" if (oa.startswith("是") or "CC-BY" in oa) else "paid"
        local = match_pdf_by_year_journal(pdf_files, {
            "year": year, "_journal": journal})
        priority = pri_map.get(idx, infer_priority(title + " " + journal + " " + dtext))
        tags = ["期刊论文"] + topic_keywords(title)
        if "是" in review:
            tags.append("综述")
        items.append({
            "title": title,
            "type": "期刊",
            "organization": org,
            "year": year if year else "",
            "version": "",
            "access": access,
            "status": "verified",
            "download": "local" if local else "link",
            "priority": priority,
            "audience": ["模拟IC"],
            "tags": tags,
            "source": source,
            "_text": title + " " + org + " " + journal +
                     (" " + str(year) if year else ""),
            "_journal": journal,
        })
        if local:
            items[-1]["local_file"] = make_local_file("journals", local)
    return items


def parse_books(readme_text):
    tables = extract_tables(readme_text)
    if not tables:
        warn("[05 教材书籍] 未找到表格,条目数为 0")
        return []
    rows = first_data_rows(tables[0])
    detail = extract_detail_sections(readme_text)
    items = []
    for idx, r in enumerate(rows, start=1):
        # # | 书名 | 作者 | 出版社 | 年份 | 语言 | ISBN | 获取渠道
        title, authors, pub, ycell, lang, isbn, channel = (
            r[1], r[2], r[3], r[4], r[5], r[6], r[7])
        year = extract_year(ycell)
        if not year:
            warn("[05 教材书籍] %s 无年份" % title)
        isbn_m = re.search(r"\d[0-9-]{11,}", isbn)
        isbn_first = isbn_m.group(0).rstrip("-") if isbn_m else ""
        # 优先 README 详细说明中的 Open Library 链接,否则按 ISBN 构建
        dtext = detail.get(idx, "")
        m = re.search(r"https://openlibrary\.org/isbn/\S+", dtext)
        if m:
            source = m.group(0).rstrip("。)")
        elif isbn_first:
            source = "https://openlibrary.org/isbn/" + isbn_first
        else:
            source = ""
            warn("[05 教材书籍] %s 无 ISBN 与链接" % title)
        org = re.sub(r"\([^)]*\)", "", pub).strip()
        # 受众:类型含"入门" → 加学生
        audience = ["模拟IC"]
        mtype = re.search(r"类型[:：](.*)", dtext)
        if mtype and "入门" in mtype.group(1):
            audience = ["模拟IC", "学生"]
        priority = infer_priority(title + " " + dtext)
        items.append({
            "title": title,
            "type": "教材",
            "organization": org,
            "year": year if year else "",
            "version": "",
            "access": "paid",
            "status": "verified",
            "download": "none",
            "priority": priority,
            "audience": audience,
            "tags": ["教材", lang],
            "source": source,
            "_text": title + " " + org + " " + authors +
                     (" " + str(year) if year else ""),
        })
    return items


def parse_vendors(readme_text, pdf_files):
    tables = extract_tables(readme_text)
    if not tables:
        warn("[06 厂商资料] 未找到表格,条目数为 0")
        return []
    rows = first_data_rows(tables[0])
    detail = extract_detail_sections(readme_text)
    items = []
    for idx, r in enumerate(rows, start=1):
        # # | 产品/文档 | 厂商 | 类型 | 年份 | 链接 | 验证状态
        title, org, vtype, ycell, link, stcell = r[1], r[2], r[3], r[4], r[5], r[6]
        year = extract_year(ycell)
        if not year:
            warn("[06 厂商资料] %s 无年份" % title)
        source = extract_url(link) or ""
        if not source:
            warn("[06 厂商资料] %s 无链接" % title)
        status = "verified" if ("验证" in stcell or "✅" in stcell
                                or "⚠️" in stcell) else "unverified"
        local = match_pdf_by_model(pdf_files, title)
        dtext = detail.get(idx, "")
        priority = infer_priority(title + " " + dtext)
        items.append({
            "title": title,
            "type": "厂商资料",
            "organization": org,
            "year": year if year else "",
            "version": "",
            "access": "free",
            "status": status,
            "download": "local" if local else "link",
            "priority": priority,
            "audience": ["模拟IC"],
            "tags": [org, vtype],
            "source": source,
            "_text": title + " " + org + " " + vtype +
                     (" " + str(year) if year else ""),
        })
        if local:
            items[-1]["local_file"] = make_local_file("vendors", local)
    return items


# --- 07 工具与社区 ---
OFFICIAL_SITES = {
    "Keysight": "https://www.keysight.com",
    "Tektronix": "https://www.tek.com",
    "R&S": "https://www.rohde-schwarz.com",
    "PEAK": "https://www.peak-system.com",
    "Vector": "https://www.vector.com",
    "Kvaser": "https://www.kvaser.com",
    "周立功": "https://www.zlg.cn",
    "CiA": "https://www.can-cia.org",
    "ISO": "https://www.iso.org",
    "TÜV": "https://www.tuv.com",
}


def _site_of(org_text):
    if not org_text:
        return None
    for k, url in OFFICIAL_SITES.items():
        if k in org_text:
            return url
    return None


def parse_tools_community(readme_text):
    tables = extract_tables(readme_text)
    year_m = re.search(r"更新日期[:：]\s*(\d{4})", readme_text)
    items = []
    # ---- 一、软件工具 ----
    if tables:
        for r in first_data_rows(tables[0]):
            # # | 工具 | 厂商/项目 | 类型 | 链接 | 说明
            title, org, vtype, link, desc = r[1], r[2], r[3], r[4], r[5]
            source = extract_url(link) or ""
            if not source:
                warn("[07 工具与社区] 软件工具 %s 无链接" % title)
            access = "free" if ("开源" in vtype or "内核" in vtype) else "paid"
            items.append({
                "title": title,
                "type": "工具",
                "organization": org,
                "year": "",
                "version": "",
                "access": access,
                "status": "verified",
                "download": "link" if source else "none",
                "priority": infer_priority(desc),
                "audience": ["模拟IC", "嵌入式", "学生"],
                "tags": ["软件工具", vtype],
                "description": desc,
                "source": source,
                "_text": title + " " + org + " " + vtype,
            })
    # ---- 二、硬件测试设备 ----
    if len(tables) > 1:
        for r in first_data_rows(tables[1]):
            # # | 设备 | 厂商 | 说明
            title, org, desc = r[1], r[2], r[3]
            source = _site_of(org) or ""
            if not source:
                warn("[07 工具与社区] 硬件设备 %s 无法确定官网链接" % title)
            items.append({
                "title": title,
                "type": "工具",
                "organization": org,
                "year": "",
                "version": "",
                "access": "paid",
                "status": "verified",
                "download": "link" if source else "none",
                "priority": infer_priority(desc),
                "audience": ["模拟IC"],
                "tags": ["硬件设备"],
                "description": desc,
                "source": source,
                "_text": title + " " + org,
            })
    # ---- 三、测试与认证渠道(bullet 列表) ----
    m3 = re.search(r"##\s*三[、.].*?(?=\n##|\Z)", readme_text, re.S)
    if m3:
        for ln in m3.group(0).splitlines():
            s = ln.strip()
            if not s.startswith("- **"):
                continue
            t = re.match(r"- \*\*(.*?)\*\*", s)
            if not t:
                continue
            title = t.group(1).strip()
            body = s[len("- **" + title + "**"):]
            url = extract_url(body) or ""
            if "plugfest" in title or "CiA" in title:
                org = "CiA"
                access = "member"
            elif "一致性" in title:
                org = "ISO / IEC"
                access = "paid"
            else:
                org = "TÜV / SGS / 广电计量 / 赛宝"
                access = "paid"
            source = url or _site_of(org) or ""
            if not source:
                warn("[07 工具与社区] 认证渠道 %s 无链接" % title)
            items.append({
                "title": title,
                "type": "工具",
                "organization": org,
                "year": "",
                "version": "",
                "access": access,
                "status": "verified",
                "download": "link" if source else "none",
                "priority": infer_priority(body),
                "audience": ["模拟IC"],
                "tags": ["认证渠道"],
                "description": body.strip(" :"),
                "source": source,
                "_text": title + " " + org,
            })
    # ---- 四、社区与学习平台 ----
    if len(tables) > 2:
        for r in first_data_rows(tables[2]):
            # # | 平台 | 类型 | 链接 | 说明
            title, vtype, link, desc = r[1], r[2], r[3], r[4]
            source = extract_url(link) or ""
            if not source:
                warn("[07 工具与社区] 社区平台 %s 无链接" % title)
            org = re.sub(r"\([^)]*\)", "", title).strip()
            items.append({
                "title": title,
                "type": "工具",
                "organization": org,
                "year": "",
                "version": "",
                "access": "free",
                "status": "verified",
                "download": "link" if source else "none",
                "priority": infer_priority(desc),
                "audience": ["模拟IC", "嵌入式", "学生"],
                "tags": ["社区平台", vtype],
                "description": desc,
                "source": source,
                "_text": title + " " + org + " " + vtype,
            })
    return items


# --------------------------------------------------------------------------
# 主流程
# --------------------------------------------------------------------------

def main():
    if len(sys.argv) != 3:
        print("用法: python scripts/extract_metadata.py <资料库根目录> <输出目录>",
              file=sys.stderr)
        sys.exit(1)
    root = sys.argv[1].rstrip('\\/')
    out_dir = sys.argv[2]
    os.makedirs(out_dir, exist_ok=True)

    top10 = parse_top10(root)
    summaries = []
    for slug, (dir_name, _ctype) in CATALOG_DIRS.items():
        cat_dir = os.path.join(root, dir_name)
        readme_path = os.path.join(cat_dir, "README.md")
        if not os.path.exists(readme_path):
            warn("缺少 %s,跳过 %s" % (readme_path, slug))
            continue
        with open(readme_path, encoding="utf-8") as f:
            text = f.read()
        pdf_files = pdf_files_of(cat_dir)
        if slug == "standards":
            items = parse_standards(text, pdf_files)
        elif slug == "patents":
            items = parse_patents(text, pdf_files)
        elif slug == "papers":
            items = parse_papers(text, pdf_files)
        elif slug == "journals":
            items = parse_journals(text, pdf_files)
        elif slug == "books":
            items = parse_books(text)
        elif slug == "vendors":
            items = parse_vendors(text, pdf_files)
        else:
            items = parse_tools_community(text)
        apply_top10(items, top10, slug)
        clean = [clean_item(it) for it in items]
        out_path = os.path.join(out_dir, OUTPUT_FILES[slug])
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(clean, f, ensure_ascii=False, indent=2)
        summaries.append("%-16s %3d 条 -> %s" % (slug, len(clean),
                                                 OUTPUT_FILES[slug]))
    print("=== 元数据提取完成 ===")
    for s in summaries:
        print(s)
    print("输出目录: %s" % out_dir)


if __name__ == "__main__":
    main()
