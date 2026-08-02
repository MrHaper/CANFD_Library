# -*- coding: utf-8 -*-
"""validate_resources.py 的 pytest 测试。

运行方式(在仓库根 canfd-learning/ 下):
    python -m pytest scripts/test_validate_resources.py -v

测试策略:
    * 用 pytest tmp_path 构造小型 JSON 夹具,不依赖真实 _data;
    * 另含一个集成测试:指向真实 docs/ 跑全量校验,断言退出码为 0
      (真实数据当前有 4 条 source 空 + 35 条 local_file 缺失,均为
      WARNING 级不阻塞;ERROR 应为 0)。
"""

import json
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate_resources import validate_file, main

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 各分类文件名 -> 期望 type(与脚本 CATEGORIES 一致)
CATEGORY_TYPES = {
    "standards": "标准规范",
    "patents": "专利",
    "papers": "论文",
    "journals": "期刊",
    "books": "教材",
    "vendors": "厂商资料",
    "tools-community": "工具",
}

# 测试用宽松分类配置:type 与真实一致,条数下限降为 1
LOOSE_CATEGORIES = {name: {"type": t, "min_items": 1}
                    for name, t in CATEGORY_TYPES.items()}


def write_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False)


def base_item(**overrides):
    """构造一条合法资源,可按需覆盖字段。"""
    item = {
        "title": "示例资源",
        "type": "标准规范",
        "organization": "示例机构",
        "year": 2020,
        "access": "free",
        "status": "verified",
        "download": "link",
        "priority": 1,
        "audience": ["模拟IC"],
        "source": "https://example.org",
    }
    item.update(overrides)
    return item


def run(tmp_path, filename, items, categories=None, repo_root=None):
    """写入临时 JSON 并校验,返回 (errors, warnings)。"""
    path = os.path.join(str(tmp_path), filename)
    write_json(path, items)
    return validate_file(path, filename, repo_root or str(tmp_path),
                         categories or LOOSE_CATEGORIES)


# ---------------------------------------------------------------------------
# 1) 必填字段缺失 -> ERROR
# ---------------------------------------------------------------------------

def test_required_field_missing_is_error(tmp_path):
    item = base_item(title="缺 organization")
    del item["organization"]
    errors, warnings = run(tmp_path, "standards.json", [item])
    assert len(errors) == 1
    assert errors[0]["severity"] == "ERROR"
    assert errors[0]["title"] == "缺 organization"
    assert "organization" in errors[0]["message"]

    # audience 为空数组 -> ERROR(必填且非空)
    item2 = base_item(title="空 audience", audience=[])
    errors2, _ = run(tmp_path, "standards.json", [item2])
    assert len(errors2) == 1
    assert "audience" in errors2[0]["message"]

    # 非空字段为空串 -> ERROR
    item3 = base_item(title="")
    errors3, _ = run(tmp_path, "standards.json", [item3])
    assert len(errors3) == 1
    assert "title" in errors3[0]["message"]


def test_year_missing_is_error(tmp_path):
    item = base_item(title="缺 year")
    del item["year"]
    errors, warnings = run(tmp_path, "standards.json", [item])
    assert len(errors) == 1
    assert "year" in errors[0]["message"]


# ---------------------------------------------------------------------------
# 2) 非法枚举 -> ERROR
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("field,bad", [
    ("access", "free-to-all"),
    ("status", "unknown"),
    ("download", "url"),
    ("priority", 9),
    ("priority", "高"),
])
def test_invalid_enum_is_error(tmp_path, field, bad):
    item = base_item(title=f"非法 {field}", **{field: bad})
    errors, warnings = run(tmp_path, "standards.json", [item])
    assert len(errors) == 1
    assert errors[0]["severity"] == "ERROR"
    assert field in errors[0]["message"]


# ---------------------------------------------------------------------------
# 3) type 与分类不匹配 -> ERROR
# ---------------------------------------------------------------------------

def test_type_mismatch_is_error(tmp_path):
    item = base_item(title="type 不匹配", type="专利")
    errors, warnings = run(tmp_path, "standards.json", [item])
    assert len(errors) == 1
    assert "type 与分类不匹配" in errors[0]["message"]
    assert "标准规范" in errors[0]["message"]


# ---------------------------------------------------------------------------
# 4) download 与 local_file 一致性
# ---------------------------------------------------------------------------

def test_local_file_missing_is_warning(tmp_path):
    """download=local 但没有 local_file 字段 -> WARNING,不阻塞。"""
    item = base_item(title="local 缺字段", download="local")
    errors, warnings = run(tmp_path, "standards.json", [item])
    assert errors == []
    assert len(warnings) == 1
    assert warnings[0]["severity"] == "WARNING"
    assert "local_file 缺失" in warnings[0]["message"]


def test_local_file_not_found_is_warning(tmp_path):
    """download=local 但 local_file 指向的文件不存在 -> WARNING,不阻塞。"""
    item = base_item(title="文件不存在",
                     download="local",
                     local_file="files/standards/missing.pdf")
    errors, warnings = run(tmp_path, "standards.json", [item])
    assert errors == []
    assert len(warnings) == 1
    assert "文件不存在" in warnings[0]["message"]


def test_local_file_exists_passes(tmp_path):
    """download=local 且文件真实存在 -> 无 ERROR 无 WARNING。"""
    write_json(os.path.join(str(tmp_path), "files", "standards", "ok.pdf"), {})
    item = base_item(title="文件存在",
                     download="local",
                     local_file="files/standards/ok.pdf")
    errors, warnings = run(tmp_path, "standards.json", [item])
    assert errors == [] and warnings == []


def test_link_with_local_file_is_error(tmp_path):
    """download=link/none 却带 local_file -> ERROR。"""
    item = base_item(title="link 带文件",
                     download="link",
                     local_file="files/standards/x.pdf")
    errors, warnings = run(tmp_path, "standards.json", [item])
    assert len(errors) == 1
    assert "不得有 local_file" in errors[0]["message"]


# ---------------------------------------------------------------------------
# 5) year 校验
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("year,ok", [
    (1980, True),
    (2027, True),
    (1979, False),
    (2028, False),
    ("", True),
    ("2015", True),
    ("abc", False),
    (None, True),
])
def test_year_validation(tmp_path, year, ok):
    item = base_item(title=f"year={year!r}", year=year)
    errors, warnings = run(tmp_path, "standards.json", [item])
    assert (len(errors) == 0) == ok, f"year={year!r} 预期 ok={ok}"


# ---------------------------------------------------------------------------
# 6) source 为空 -> WARNING 不阻塞
# ---------------------------------------------------------------------------

def test_source_empty_is_warning_not_error(tmp_path):
    item = base_item(title="source 空", source="")
    errors, warnings = run(tmp_path, "standards.json", [item])
    assert errors == []
    assert len(warnings) == 1
    assert warnings[0]["severity"] == "WARNING"
    assert "source" in warnings[0]["message"]


def test_source_missing_is_warning_not_error(tmp_path):
    item = base_item(title="source 缺失")
    del item["source"]
    errors, warnings = run(tmp_path, "standards.json", [item])
    assert errors == []
    assert len(warnings) == 1
    assert "source" in warnings[0]["message"]


# ---------------------------------------------------------------------------
# 7) 条数下限
# ---------------------------------------------------------------------------

def test_item_count_below_minimum_is_error(tmp_path):
    categories = {"standards": {"type": "标准规范", "min_items": 5}}
    items = [base_item(title=f"第 {i} 条") for i in range(4)]
    errors, warnings = run(tmp_path, "standards.json", items,
                           categories=categories)
    assert len(errors) == 1
    assert "低于分类" in errors[0]["message"]


# ---------------------------------------------------------------------------
# 8) 边界/健壮性
# ---------------------------------------------------------------------------

def test_invalid_json_is_error(tmp_path):
    path = os.path.join(str(tmp_path), "standards.json")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("{{{ not valid json")
    errors, warnings = validate_file(path, "standards.json", str(tmp_path),
                                     LOOSE_CATEGORIES)
    assert len(errors) == 1
    assert "JSON 解析失败" in errors[0]["message"]


def test_item_not_object_is_error(tmp_path):
    errors, warnings = run(tmp_path, "standards.json", [["不是对象"]])
    assert len(errors) == 1
    assert "必须是 JSON 对象" in errors[0]["message"]


# ---------------------------------------------------------------------------
# 9) 集成测试:真实 docs/ 全量校验应通过(退出码 0)
# ---------------------------------------------------------------------------

def test_real_docs_validation_passes():
    data_dir = os.path.join(REPO_ROOT, "docs", "resources", "_data")
    if not os.path.isdir(data_dir):
        pytest.skip("docs/resources/_data 不存在,跳过集成测试")
    code = main([os.path.join(REPO_ROOT, "docs")])
    assert code == 0, "真实资源数据存在 ERROR,退出码应为 0"


def test_main_missing_data_dir_returns_error(tmp_path):
    code = main([os.path.join(str(tmp_path), "不存在的目录")])
    assert code == 1
