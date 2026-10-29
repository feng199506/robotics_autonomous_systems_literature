#!/usr/bin/env python3
"""Verify paper titles against arXiv and record v1 dates. Resume-safe cache."""
import json
import sys
import time
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common_en import STATE, SCRIPTS, WINDOW_START, http, load_json, save_json, norm_words  # noqa: E402

NS = {"a": "http://www.arxiv.org/oai2", "atom": "http://www.w3.org/2005/Atom",
      "arxiv": "http://arxiv.org/schemas/atom"}
CACHE = STATE / "arxiv_meta_en.json"


def parse_atom(body):
    root = ET.fromstring(body)
    out = []
    for e in root.findall("atom:entry", NS):
        aid = (e.findtext("atom:id", default="", namespaces=NS) or "").split("/abs/")[-1]
        title = " ".join((e.findtext("atom:title", default="", namespaces=NS) or "").split())
        published = (e.findtext("atom:published", default="", namespaces=NS) or "")[:10]
        updated = (e.findtext("atom:updated", default="", namespaces=NS) or "")[:10]
        authors = [a.findtext("atom:name", default="", namespaces=NS)
                   for a in e.findall("atom:author", NS)]
        summary = " ".join((e.findtext("atom:summary", default="", namespaces=NS) or "").split())
        doi = e.findtext("arxiv:doi", default="", namespaces=NS) or ""
        comment = e.findtext("arxiv:comment", default="", namespaces=NS) or ""
        out.append({"arxiv": aid, "title": title, "published": published, "updated": updated,
                    "authors": authors, "summary": summary, "doi": doi, "comment": comment})
    return out


def query_id(arxiv_id):
    url = "https://export.arxiv.org/api/query?id_list=" + urllib.parse.quote(arxiv_id) + "&max_results=1"
    r = http(url, timeout=60)
    if r["status"] != 200 or not r["body"]:
        return None, f"arxiv http {r['status']} {r.get('err')}"
    rows = parse_atom(r["body"])
    return (rows[0] if rows else None), ""


def query_title(title):
    q = "ti:\"" + title.split(":")[0][:90].replace('"', "") + "\""
    url = "https://export.arxiv.org/api/query?search_query=" + urllib.parse.quote(q) + "&max_results=5"
    r = http(url, timeout=60)
    if r["status"] != 200 or not r["body"]:
        return [], f"arxiv http {r['status']} {r.get('err')}"
    return parse_atom(r["body"]), ""


def ratio(a, b):
    wa, wb = set(norm_words(a)), set(norm_words(b))
    if not wa or not wb:
        return 0.0
    return len(wa & wb) / len(wa)


def main():
    seeds = json.loads((SCRIPTS / "seeds" / "P_papers_en.json").read_text(encoding="utf-8"))
    cache = load_json(CACHE, {})
    for s in seeds:
        sid = s["id"]
        if sid in cache and cache[sid].get("ok"):
            print(f"{sid:<10} cached {cache[sid].get('arxiv')} {cache[sid].get('published')}")
            continue
        rec = {"id": sid, "seed_arxiv": s.get("arxiv", ""), "seed_title": s["title"]}
        meta, err = query_id(s.get("arxiv", "")) if s.get("arxiv") else (None, "no arxiv")
        if meta and ratio(s["title"], meta["title"]) >= 0.55:
            rec.update(ok=True, match="id", **{k: meta[k] for k in
                       ("arxiv", "title", "published", "updated", "authors", "summary", "doi", "comment")})
        else:
            alts, err2 = query_title(s["title"])
            best = max(alts, key=lambda m: ratio(s["title"], m["title"]), default=None)
            if best and ratio(s["title"], best["title"]) >= 0.7:
                rec.update(ok=True, match="title-search", **{k: best[k] for k in
                           ("arxiv", "title", "published", "updated", "authors", "summary", "doi", "comment")})
                rec["seed_arxiv_mismatch"] = s.get("arxiv", "")
            else:
                rec.update(ok=False, error=err or err2 or "title mismatch",
                           id_meta_title=(meta or {}).get("title", ""),
                           id_ratio=round(ratio(s["title"], (meta or {}).get("title", "")), 2))
        if rec.get("published"):
            rec["in_window"] = WINDOW_START <= rec["published"] <= "2026-10-30"
        cache[sid] = rec
        save_json(CACHE, cache)
        print(f"{sid:<10} {'OK' if rec.get('ok') else 'FAIL':<5} {rec.get('arxiv','')} "
              f"{rec.get('published','')} {(rec.get('error') or rec.get('title') or '')[:80]}", flush=True)
        time.sleep(0.2)
    ok = sum(1 for v in cache.values() if v.get("ok"))
    print(f"metadata ok {ok}/{len(seeds)}")


if __name__ == "__main__":
    main()
