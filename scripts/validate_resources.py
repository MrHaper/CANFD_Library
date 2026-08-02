#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""资源条目元数据校验脚本(设计文档 5.2 / 9 节)。

用法:
    python scripts/validate_resources.py <docs目录>   # 例如 docs/
    python scripts/validate_resources.py              # 默认 docs

扫描 <docs>/resources/_data/*.json(standards / patents / papers / journals /
books / vendors / tools-community),逐条校验元数据。

退出码:
    0 = 全部通过(可含 WARNING,WARNING 不阻塞)
    1 = 存在 ERROR

输出格式:
    ERROR: <文件名> <title> <问题描述>
    WARNING: <文件名> <title> <问题描述>

校验规则(WARNING 不阻塞退出码):
  ERROR:
    * JSON 无法解析 / 未知分类文件 / JSON 顶层非数组 / 条目非对象
    * 必填字段缺失或为空:title / type / organization / year / access /
      status / download / priority / audience(source 例外,见 WARNING)
    * 枚举非法:access ∈ {free, paid, member};status ∈ {verified, unverified,
      withdrawn};download ∈ {local, link, none};priority ∈ {1, 2, 3}
    * type 与所在 JSON 分类不匹配(如 standards.json 必须全部为"标准规范")
    * download = link / none 却填写了 local_file
    * year 非空但非 1980~2027 的整数(year 允许空串)
    * 条目数低于该分类数量下限
  WARNING(不阻塞):
    * source 缺失或为空
    * download = local 但 local_file 缺失
    * download = local 但 local_file 指向的文件不存在
      (PDF 入库属于 M2 阶段任务,故此处不阻塞退出码)
"""

import json
import os
import sys

# 分类文件名 -> {期望 type, 条目数下限}(设计文档 5.2 / 9 节)
CATEGORIES = {
    "standards":       {"type": "标准规范", "min_items": 16},
    "patents":         {"type": "专利",     "min_items": 12},
    "papers":          {"type": "论文",     "min_items": 15},
    "journals":        {"type": "期刊",     "min_items": 10},
    "books":           {"type": "教材",     "min_items": 11},
    "vendors":         {"type": "厂商资料", "min_items": 17},
    "tools-community": {"type": "工具",     "min_items": 20},
}

REQUIRED_FIELDS = (
    "title", "type", "organization", "year", "access",
    "status", "download", "priority", "audience", "source",
)

ACCESS_VALUES = ("free", "paid", "member")
STATUS_VALUES = ("verified", "unverified", "withdrawn")
DOWNLOAD_VALUES = ("local", "link", "none")
PRIORITY_VALUES = (1, 2, 3)
YEAR_MIN, YEAR_MAX = 1980, 2027


def _category_name(filename):
    """由文件名提取分类名,如 'standards.json' -> 'standards'。"""
    base = os.path.basename(filename)
    if base.endswith(".json"):
        return base[: -len(".json")]
    return None


def _resolve_local_path(repo_root, local_file):
    """把 local_file(相对仓库根,如 files/standards/x.pdf)解析为绝对路径。

    剥离前导 '/'、'./' 与 '..' 段,防路径逃逸;统一 '/' 分隔跨平台拼接。
    """
    rel = local_file.strip().replace("\\", "/").lstrip("/")
    parts = [p for p in rel.split("/") if p and p != "." and p != ".."]
    return os.path.join(repo_root, *parts)


def _record(severity, filename, title, message):
    return {"severity": severity, "file": filename,
            "title": title, "message": message}


def validate_file(path, filename, repo_root, categories=None):
    """校验单个 JSON 数据文件。

    参数:
        path:        JSON 文件路径
        filename:    数据文件名(仅用于输出,如 standards.json)
        repo_root:   仓库根目录(local_file 相对此路径解析)
        categories:  分类配置覆盖项(主要供测试使用);默认全局 CATEGORIES

    返回:
        (errors, warnings);每个元素为 dict:
        {"severity": "ERROR"/"WARNING", "file", "title", "message"}
    """
    if categories is None:
        categories = CATEGORIES

    errors, warnings = [], []

    try:
        with open(path, "r", encoding="utf-8") as fh:
            items = json.load(fh)
    except (OSError, ValueError) as exc:
        errors.append(_record("ERROR", filename, "<无标题>",
                              f"JSON 解析失败: {exc}"))
        return errors, warnings

    cat = _category_name(filename)
    if cat is None or cat not in categories:
        errors.append(_record("ERROR", filename, "<无标题>",
                              "未知分类文件(不在 categories 中)"))
        return errors, warnings
    spec = categories[cat]

    if not isinstance(items, list):
        errors.append(_record("ERROR", filename, "<无标题>",
                              "JSON 顶层必须是数组"))
        return errors, warnings

    if len(items) < spec["min_items"]:
        errors.append(_record(
            "ERROR", filename, "<无标题>",
            f"条目数 {len(items)} 低于分类 {cat} 的下限 {spec['min_items']}"))

    for item in items:
        if not isinstance(item, dict):
            errors.append(_record("ERROR", filename, "<无标题>",
                                  "条目必须是 JSON 对象"))
            continue
        title = item.get("title") or "<无标题>"

        _check_required(item, filename, title, errors, warnings)
        _check_enums(item, filename, title, errors)
        _check_type(item, spec, filename, title, errors)
        _check_local_file(item, filename, title, repo_root, errors, warnings)

    return errors, warnings


def _check_required(item, filename, title, errors, warnings):
    """必填字段存在且非空;source 为空记 WARNING,其余记 ERROR。"""
    for field in REQUIRED_FIELDS:
        if field not in item:
            if field == "source":
                warnings.append(_record("WARNING", filename, title,
                                        "source 缺失"))
            else:
                errors.append(_record("ERROR", filename, title,
                                      f"必填字段缺失: {field}"))
            continue

        value = item[field]
        if field == "source":
            if value is None or value == "":
                warnings.append(_record("WARNING", filename, title,
                                        "source 为空"))
        elif field == "year":
            if value is None or value == "":
                continue  # 年份允许为空串
            _check_year(item, filename, title, errors)
        elif field == "audience":
            if not isinstance(value, list) or len(value) == 0:
                errors.append(_record("ERROR", filename, title,
                                      "audience 必须为非空数组"))
        elif value is None or value == "":
            errors.append(_record("ERROR", filename, title,
                                  f"必填字段为空: {field}"))


def _check_year(item, filename, title, errors):
    """year 若非空必须为 1980~2027 的整数(兼容字符串数字)。"""
    value = item.get("year")
    if value is None or value == "":
        return
    if isinstance(value, bool) or not isinstance(value, (int, str)):
        errors.append(_record("ERROR", filename, title,
                              "year 必须为 1980~2027 的整数或空"))
        return
    if isinstance(value, str):
        text = value.strip()
        if text == "":
            return
        if not text.isdigit():
            errors.append(_record("ERROR", filename, title,
                                  "year 必须为 1980~2027 的整数或空"))
            return
        value = int(text)
    if not (YEAR_MIN <= value <= YEAR_MAX):
        errors.append(_record("ERROR", filename, title,
                              f"year 越界: {value}(允许 {YEAR_MIN}~{YEAR_MAX})"))


def _check_enums(item, filename, title, errors):
    """枚举字段合法性。空值已在必填检查中报告,此处跳过避免重复。"""
    checks = (
        ("access", ACCESS_VALUES),
        ("status", STATUS_VALUES),
        ("download", DOWNLOAD_VALUES),
        ("priority", PRIORITY_VALUES),
    )
    for field, allowed in checks:
        value = item.get(field)
        if value is None or value == "":
            continue
        if value not in allowed:
            errors.append(_record(
                "ERROR", filename, title,
                f"非法 {field} 值: {value!r}(合法值: {list(allowed)})"))


def _check_type(item, spec, filename, title, errors):
    """type 必须与所在 JSON 分类一致。"""
    actual = item.get("type")
    if not actual:
        return  # 缺失已由必填检查报告
    if actual != spec["type"]:
        errors.append(_record(
            "ERROR", filename, title,
            f"type 与分类不匹配: 应为 {spec['type']!r},实际 {actual!r}"))


def _check_local_file(item, filename, title, repo_root, errors, warnings):
    """local_file 与 download 的一致性。

    download=local 且文件缺失/不存在 -> WARNING(PDF 入库属 M2 阶段);
    download=link/none 却填了 local_file -> ERROR。
    """
    download = item.get("download")
    local_file = item.get("local_file")

    if download == "local":
        if not local_file or str(local_file).strip() == "":
            warnings.append(_record("WARNING", filename, title,
                                    "download=local 但 local_file 缺失"))
            return
        abs_path = _resolve_local_path(repo_root, str(local_file))
        if not os.path.isfile(abs_path):
            warnings.append(_record(
                "WARNING", filename, title,
                f"download=local 但 local_file 指向的文件不存在: {local_file}"))
    elif download in ("link", "none"):
        if local_file and str(local_file).strip() != "":
            errors.append(_record(
                "ERROR", filename, title,
                f"download={download} 时不得有 local_file"))


def main(argv=None):
    """CLI 入口。返回退出码:0=无 ERROR;1=有 ERROR。"""
    args = list(sys.argv[1:] if argv is None else argv)
    docs_dir = args[0] if args else "docs"
    data_dir = os.path.join(docs_dir, "resources", "_data")

    if not os.path.isdir(data_dir):
        print(f"ERROR: 找不到资源数据目录: {data_dir}")
        return 1

    # 仓库根 = docs 目录的父目录(files/ 与 docs/ 平级)
    repo_root = os.path.dirname(os.path.abspath(docs_dir))

    errors, warnings = [], []
    file_count = item_count = 0

    for filename in sorted(os.listdir(data_dir)):
        if not filename.endswith(".json"):
            continue
        path = os.path.join(data_dir, filename)
        file_errors, file_warnings = validate_file(path, filename, repo_root)

        try:
            with open(path, "r", encoding="utf-8") as fh:
                items = json.load(fh)
            if isinstance(items, list):
                item_count += len(items)
        except (OSError, ValueError):
            pass  # 解析错误已由 validate_file 报告

        file_count += 1
        errors.extend(file_errors)
        warnings.extend(file_warnings)

    for record in errors + warnings:
        print(f"{record['severity']}: {record['file']} "
              f"{record['title']} {record['message']}")

    print(f"校验完成: {file_count} 个文件, {item_count} 条资源, "
          f"ERROR={len(errors)}, WARNING={len(warnings)}")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
