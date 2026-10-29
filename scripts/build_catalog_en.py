#!/usr/bin/env python3
"""Build catalog_cn.csv, progress_cn.csv, download_failures_cn.csv, README_cn.md."""
import csv
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common_en import (ACCESS_DATE, CATS, ITEMS, ROOT, SCRIPTS, SEARCH_DATE, SLUGS,  # noqa: E402
                       TYPES, WINDOW_START, item_state, load_json)

SEEDS = SCRIPTS / "seeds"
META = ROOT / "state" / "arxiv_meta_en.json"


def load_seeds():
    rows = []
    for f in sorted(SEEDS.glob("*.json")):
        for s in json.loads(f.read_text(encoding="utf-8")):
            s["_seedfile"] = f.name
            rows.append(s)
    return rows


def st_ok(s):
    return item_state(s["id"]).get("status") == "ok"


def window_of(s, meta):
    m = meta.get(s["id"], {})
    aid = (s.get("arxiv") or "").split("v")[0]
    meta_aid = (m.get("arxiv") or "").split("v")[0]
    if s["type"] == "paper" and m.get("published") and m.get("ok") and aid and meta_aid.startswith(aid):
        if WINDOW_START <= m["published"][:10] <= "2026-10-30":
            return "近三年"
        return "三年前经典"
    if s.get("window"):
        return s["window"]
    return "近三年" if s["type"] == "paper" else "教材/课程/软件（不适用论文窗口）"


def catalog_row(s, st, meta):
    m = meta.get(s["id"], {})
    path = s.get("out", "")
    exists = (ROOT / path).exists() if path else False
    status = st.get("status", "todo")
    complete = "完整（已核验）" if status == "ok" else ("失败" if status == "failed" else "待核验/未下载")
    year = m.get("published", s.get("year", ""))[:10] if m.get("published") else s.get("year", "")
    authors = s.get("authors", "")
    if m.get("authors"):
        authors = "; ".join(m["authors"][:12])
    title = m.get("title") or s.get("title", "")
    src = st.get("download_url") or s.get("source", "")
    p = s.get("paper") or {}
    reuse = "已有复用" if s.get("reuse") or (s.get("get") or {}).get("kind") == "reuse" else "新下载"
    if status != "ok":
        reuse = ""
    return {
        "编号": s["id"],
        "主题": CATS.get(s["cat"], s["cat"]),
        "资料类型": TYPES.get(s["type"], s.get("material", "")),
        "标题": title,
        "作者或机构": authors,
        "学校": s.get("school", ""),
        "年份": year,
        "版本": s.get("version", ""),
        "语言": "英文" if s.get("lang") == "en" else s.get("lang", ""),
        "学位层次": s.get("level", ""),
        "先修要求": s.get("prereq", ""),
        "原始来源": s.get("source", ""),
        "本地路径": path if exists else "",
        "完整性": complete,
        "许可证": s.get("license", ""),
        "阅读优先级": s.get("use", ""),
        "核验说明": (st.get("verify") or st.get("error") or "")[:400],
        "来源性质": reuse,
        "下载日期": st.get("access_date", ""),
        "提交号": st.get("commit", ""),
        "交叉主题": ",".join(CATS.get(c, c) for c in s.get("cross", [])),
        "时间窗口": window_of(s, meta),
        "三年前保留理由": s.get("classic_reason", ""),
        "课程代码": s.get("course_code", ""),
        "学期": s.get("term", ""),
        "工具": s.get("tool", ""),
        "范围说明": s.get("scope", ""),
        "机器人类型": p.get("robot_type", ""),
        "任务": p.get("task", ""),
        "传感器": p.get("sensors", ""),
        "是否使用真实机器人": p.get("real_robot", ""),
        "仿真或实机评测": p.get("eval", ""),
        "代码可用性": p.get("code", ""),
        "数据可用性": p.get("data", ""),
        "arXiv": m.get("arxiv") or s.get("arxiv", ""),
        "备注": s.get("note", ""),
    }


FIELDS = list(catalog_row({"id": "", "cat": "01", "type": "book", "title": "", "get": {}}, {}, {}).keys())


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow(r)


def main():
    seeds = load_seeds()
    meta = load_json(META, {})
    rows, fails = [], []
    for s in seeds:
        st = item_state(s["id"])
        rec = catalog_row(s, st, meta)
        if st.get("status") == "ok":
            rows.append(rec)
        else:
            fails.append(rec)

    write_csv(ROOT / "catalog_cn.csv", rows)
    write_csv(ROOT / "download_failures_cn.csv", fails)

    def n(typ, pred=lambda s: True):
        return sum(1 for s in seeds if s["type"] == typ and st_ok(s) and pred(s))

    books = n("book")
    courses = n("course")
    papers = n("paper")
    docs = n("docs")
    prac = n("practice")
    reuse = sum(1 for s in seeds if st_ok(s) and ((s.get("get") or {}).get("kind") == "reuse" or s.get("reuse")))
    new = sum(1 for s in seeds if st_ok(s)) - reuse
    recent = sum(1 for s in seeds if s["type"] == "paper" and st_ok(s) and window_of(s, meta) == "近三年")
    classic = papers - recent
    quota_p = n("paper", lambda s: s.get("quota", True))
    quota_recent = sum(1 for s in seeds if s["type"] == "paper" and st_ok(s) and s.get("quota", True) and window_of(s, meta) == "近三年")
    pct = f"{100 * quota_recent / quota_p:.1f}%" if quota_p else "n/a"

    prog_fields = ["类型", "已核验", "目标", "新下载", "已有复用", "失败", "待办", "近三年", "三年前经典", "近三年占比", "状态"]
    targets = {"book": "15–25", "course": "10–15", "paper": "约 50", "docs": "8–12", "practice": "10–15"}
    names = {"book": "教材/专著", "course": "大学课程", "paper": "论文/综述/教程", "docs": "官方工具文档", "practice": "实践项目"}
    with open(ROOT / "progress_cn.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=prog_fields)
        w.writeheader()
        for typ in ["book", "course", "paper", "docs", "practice"]:
            ok = n(typ)
            failed = sum(1 for s in seeds if s["type"] == typ and item_state(s["id"]).get("status") == "failed")
            todo = sum(1 for s in seeds if s["type"] == typ and item_state(s["id"]).get("status") not in ("ok", "failed"))
            ru = sum(1 for s in seeds if s["type"] == typ and st_ok(s) and ((s.get("get") or {}).get("kind") == "reuse" or s.get("reuse")))
            rec = sum(1 for s in seeds if s["type"] == typ and st_ok(s) and window_of(s, meta) == "近三年") if typ == "paper" else ""
            cla = (ok - rec) if typ == "paper" and rec != "" else ""
            paper_pct = pct if typ == "paper" else ""
            w.writerow({
                "类型": names[typ], "已核验": ok, "目标": targets[typ],
                "新下载": ok - ru, "已有复用": ru, "失败": failed, "待办": todo,
                "近三年": rec, "三年前经典": cla,
                "近三年占比": paper_pct,
                "状态": "进行中" if todo or (typ == "paper" and quota_recent < 43) or (typ == "docs" and ok < 8) else "达标或接近",
            })

    # README progress table
    readme = ROOT / "README_cn.md"
    table = f"""<!-- PROGRESS:START -->
检索执行日：{SEARCH_DATE}。论文近三年窗口：{WINDOW_START} 至 {SEARCH_DATE}。只计已完整保存且核验通过的资料。

| 类型 | 已核验 | 目标 | 新下载 | 已有复用 | 失败 | 说明 |
|---|---|---|---|---|---|---|
| 教材/专著 | {books} | 15–25 | {n("book", lambda s: (s.get("get") or {{}}).get("kind") != "reuse" and not s.get("reuse"))} | {n("book", lambda s: (s.get("get") or {{}}).get("kind") == "reuse" or s.get("reuse"))} | {sum(1 for s in seeds if s["type"]=="book" and item_state(s["id"]).get("status")=="failed")} | 经典教材允许旧版 |
| 大学课程 | {courses} | 10–15 | {n("course", lambda s: (s.get("get") or {{}}).get("kind") != "reuse" and not s.get("reuse"))} | {n("course", lambda s: (s.get("get") or {{}}).get("kind") == "reuse" or s.get("reuse"))} | {sum(1 for s in seeds if s["type"]=="course" and item_state(s["id"]).get("status")=="failed")} | 完整讲义/课件包计一次 |
| 论文/综述/教程 | {papers} | 约 50 | {papers} | 0 | {sum(1 for s in seeds if s["type"]=="paper" and item_state(s["id"]).get("status")=="failed")} | 近三年 {recent}；必要经典计入配额后占比 {pct}（配额 {quota_p}）；其余经典单列 {classic - (quota_p - quota_recent)} |
| 官方工具文档 | {docs} | 8–12 | {n("docs", lambda s: (s.get("get") or {{}}).get("kind") != "reuse" and not s.get("reuse"))} | {n("docs", lambda s: (s.get("get") or {{}}).get("kind") == "reuse" or s.get("reuse"))} | {sum(1 for s in seeds if s["type"]=="docs" and item_state(s["id"]).get("status")=="failed")} | HTML 离线包，记录范围 |
| 实践项目 | {prac} | 10–15 | {n("practice", lambda s: (s.get("get") or {{}}).get("kind") != "reuse" and not s.get("reuse"))} | {n("practice", lambda s: (s.get("get") or {{}}).get("kind") == "reuse" or s.get("reuse"))} | {sum(1 for s in seeds if s["type"]=="practice" and item_state(s["id"]).get("status")=="failed")} | 含许可证；不执行代码 |

全库去重已核验：{books + courses + papers + docs + prac}；其中新下载 {new}，已有复用 {reuse}。
<!-- PROGRESS:END -->
"""
    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        if "<!-- PROGRESS:START -->" in text:
            import re
            text = re.sub(r"<!-- PROGRESS:START -->.*?<!-- PROGRESS:END -->", table.strip(), text, flags=re.S)
            readme.write_text(text, encoding="utf-8")
        else:
            readme.write_text(table + "\n" + text, encoding="utf-8")
    print(f"catalog {len(rows)} ok, failures {len(fails)}")
    print(f"books {books} courses {courses} papers {papers} ({pct} recent) docs {docs} practice {prac}")
    print(f"reuse {reuse} new {new}")


if __name__ == "__main__":
    main()
