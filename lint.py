"""wiki 的程式檢查（AGENTS.md §10.1）。「通過」以本腳本為準。

用法：python lint.py [--fix] [--root 路徑]

  --fix   自動修正機械性問題：has_inference、status、sources、index 缺項、
          可以唯一對應的 [[ ]] 連結。內容問題只回報，不修改。
  --root  指定專案根目錄（預設是本檔所在目錄；測試用）

結束代碼：0 = 通過（沒有 ERROR），1 = 有 ERROR。WARN 和 INFO 不影響通過。

檢查代號：
  (a) 引用鍵存在於對照表，頁碼在 1..總頁數 之間
  (b) 英文引文逐字出現在原文中，而且只有一句
  (d) frontmatter 必填欄位、列舉值、has_inference、sources
  (e) 一級標題「中文 (English)」、與 title 一致；檔名是 kebab-case
  (g) 相對連結有效，沒有 [[ ]]
  (h) 沒有孤兒頁
  (i) index.md 列出所有頁面
  (k) 列出〔待檢視〕，並確認 status 是 needs-review
  (s) 句子既沒有出處、也沒有〔推論〕；白話摘要中不得有〔推論〕
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

import yaml

sys.stdout.reconfigure(encoding="utf-8")

INFER = "〔推論〕"
PENDING = "〔待檢視〕"
TODO = "〔待補〕"

TYPES = {"paper", "concept", "paradigm", "synthesis", "town", "glossary"}
STATUSES = {"draft", "stable", "needs-review"}
TOWN_STATUSES = {"idea", "adopted", "rejected"}
COMMON_FIELDS = ["title", "type", "summary", "sources", "related", "tags",
                 "status", "has_inference", "created", "updated"]
PAPER_FIELDS = ["citekey", "authors", "year", "venue", "version",
                "raw_file", "pdf_pages", "page_offset"]
INDEX_SECTIONS = {
    "paper": "## 論文 (Papers)",
    "concept": "## 概念 (Concepts)",
    "paradigm": "## 實驗範式 (Paradigms)",
    "synthesis": "## 綜合 (Syntheses)",
    "town": "## 小鎮應用 (Town)",
    "glossary": "## 術語表 (Glossary)",
}
EXEMPT_SECTIONS = ("白話摘要", "相關頁面")

CITEKEY = r"[A-Z][A-Za-z]+\d{4}[a-z]?"
CITE_ITEM = rf"({CITEKEY}), p\.(\d+)(?:[–-](\d+))?"
CITE_GROUP = re.compile(rf"\[({CITE_ITEM}(?:; {CITE_ITEM})*)\](?!\()")
CITE_ITEM_RE = re.compile(CITE_ITEM)
LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)\s]+)\)")
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
QUOTE_RE = re.compile(r'^>\s*"(.+)"\s*(\[[^\]]+\])\s*$')
H1_RE = re.compile(r"^# (.+) \(([^()]+)\)$")
KEBAB_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
CJK_RE = re.compile(r"[一-鿿]")


# ---------------------------------------------------------------- 回報

class Report:
    def __init__(self):
        self.items: list[tuple[str, str, str, str]] = []  # (level, code, where, msg)
        self.fixes: list[str] = []

    def add(self, level, code, where, msg):
        self.items.append((level, code, where, msg))

    def error(self, code, where, msg):
        self.add("ERROR", code, where, msg)

    def warn(self, code, where, msg):
        self.add("WARN", code, where, msg)

    def info(self, code, where, msg):
        self.add("INFO", code, where, msg)

    def print(self) -> int:
        by_code = defaultdict(list)
        for it in self.items:
            by_code[it[1]].append(it)
        for code in sorted(by_code):
            print(f"\n--- ({code}) ---")
            for level, _, where, msg in by_code[code]:
                print(f"{level:<5} {where}  {msg}")
        if self.fixes:
            print("\n--- 已自動修正 ---")
            for f in self.fixes:
                print(f"FIXED {f}")
        n_err = sum(1 for i in self.items if i[0] == "ERROR")
        n_warn = sum(1 for i in self.items if i[0] == "WARN")
        print(f"\n結果：{'通過' if n_err == 0 else '未通過'}"
              f"（ERROR {n_err}、WARN {n_warn}、已修正 {len(self.fixes)}）")
        return 0 if n_err == 0 else 1


# ---------------------------------------------------------------- 讀取

def load_citekeys(root: Path) -> dict[str, str]:
    text = (root / "AGENTS.md").read_text(encoding="utf-8")
    return dict(re.findall(
        r"^\|\s*`([A-Za-z]+\d{4}[a-z]?)`\s*\|\s*`([^`]+\.pdf)`\s*\|", text, re.M))


class Source:
    """cache/text/<citekey>.txt 的內容。"""

    def __init__(self, path: Path):
        text = path.read_text(encoding="utf-8")
        self.header = dict(re.findall(r"^# (\w[\w-]*): (.*)$", text.split("=== p.")[0], re.M))
        parts = re.split(r"^=== p\.(\d+) ===$", text, flags=re.M)[1:]
        self.pages = {int(n): body for n, body in zip(parts[0::2], parts[1::2])}
        self.n_pages = int(self.header.get("pages", len(self.pages)))
        self.vision = self.header.get("source") == "vision-transcribed"
        self.untranscribed = parse_ranges(self.header.get("untranscribed", ""))
        self.partial = parse_ranges(self.header.get("partial", ""))  # 只轉錄部分段落的頁
        self._compact = {n: compact(b) for n, b in self.pages.items()
                         if n not in self.untranscribed}

    def find(self, quote: str) -> list[int]:
        q = compact(quote)
        return [n for n, body in self._compact.items() if q in body]


def parse_ranges(s: str) -> set[int]:
    """'18-21, 5' → {5, 18, 19, 20, 21}"""
    out = set()
    for part in re.split(r"[,\s]+", s.strip()):
        if m := re.fullmatch(r"(\d+)[-–](\d+)", part):
            out.update(range(int(m.group(1)), int(m.group(2)) + 1))
        elif part.isdigit():
            out.add(int(part))
    return out


def normalize(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)  # 連字 ﬁ → fi 等
    s = s.translate(str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"',
                                   "–": "-", "—": "-", "­": ""}))
    s = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", s)  # 去除斷行連字號
    return re.sub(r"\s+", " ", s).strip()


def compact(s: str) -> str:
    """比對用：正規化之後再去掉所有空白和連字號。

    PDF 的斷行連字號有時是真的連字號（self-\\ninterest），去掉全部連字號
    可以讓兩種情況都對得上，又不至於讓不同句子誤判相同。
    """
    return re.sub(r"[\s\-]", "", normalize(s))


class Page:
    def __init__(self, path: Path, wiki: Path):
        self.path = path
        self.rel = path.relative_to(wiki).as_posix()
        self.raw = path.read_text(encoding="utf-8")
        self.fm: dict = {}
        self.fm_text = ""
        self.fm_error = None
        self.body_start = 0  # 內文第一行的行號（0 起算）
        lines = self.raw.split("\n")
        if lines and lines[0].strip() == "---":
            try:
                end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
                self.fm_text = "\n".join(lines[1:end])
                self.fm = yaml.safe_load(self.fm_text) or {}
                self.body_start = end + 1
            except StopIteration:
                self.fm_error = "frontmatter 沒有結束的 ---"
            except yaml.YAMLError as e:
                self.fm_error = f"YAML 解析失敗：{e}"
        else:
            self.fm_error = "缺少 frontmatter"
        self.lines = lines
        self.body = lines[self.body_start:]

    def where(self, body_idx: int) -> str:
        return f"wiki/{self.rel}:{self.body_start + body_idx + 1}"

    def iter_body(self):
        """產生 (行索引, 行內容, 所在 H2 標題, 是否在程式碼區塊)。

        行內程式碼 `...` 會先移除，不參與連結、引用、句子檢查。
        """
        h2, fence = "", False
        for i, line in enumerate(self.body):
            line = re.sub(r"`[^`]*`", "", line)
            if line.lstrip().startswith("```"):
                fence = not fence
                yield i, line, h2, True
                continue
            if not fence and line.startswith("## "):
                h2 = line[3:].strip()
            yield i, line, h2, fence


# ---------------------------------------------------------------- 檢查

def check_frontmatter(p: Page, keys: dict, r: Report, fix: bool):
    """(d)：回傳要套用的 frontmatter 修正 {欄位: 新值字串}。"""
    w = f"wiki/{p.rel}"
    if p.fm_error:
        r.error("d", w, p.fm_error)
        return {}
    fm = p.fm
    for f in COMMON_FIELDS:
        if f not in fm:
            r.error("d", w, f"缺少必填欄位 {f}")
    t = fm.get("type")
    if t is not None and t not in TYPES:
        r.error("d", w, f"type 不合法：{t}")
    if "status" in fm and fm["status"] not in STATUSES:
        r.error("d", w, f"status 不合法：{fm['status']}")
    for f in ("sources", "related", "tags"):
        if f in fm and not isinstance(fm[f], list):
            r.error("d", w, f"{f} 必須是清單")
    for f in ("created", "updated"):
        if f in fm and not isinstance(fm[f], dt.date):
            r.error("d", w, f"{f} 必須是 YYYY-MM-DD 日期")
    if "summary" in fm and (not isinstance(fm["summary"], str) or not fm["summary"].strip()):
        r.error("d", w, "summary 不得為空")
    if isinstance(fm.get("summary"), str) and INFER in fm["summary"]:
        r.error("d", w, "summary 不得含〔推論〕")
    for tag in fm.get("tags") or []:
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", str(tag)):
            r.error("d", w, f"tag 必須是英文 kebab-case：{tag}")
    for rel in fm.get("related") or []:
        if not (p.path.parents[len(Path(p.rel).parts) - 1] / str(rel)).exists():
            r.error("d", w, f"related 指向不存在的頁面：{rel}")

    if t == "paper":
        for f in PAPER_FIELDS:
            if f not in fm:
                r.error("d", w, f"論文頁缺少欄位 {f}")
        ck = fm.get("citekey")
        if ck and ck not in keys:
            r.error("d", w, f"citekey {ck} 不在 AGENTS.md §3 對照表")
        elif ck and fm.get("raw_file") and keys.get(ck) != fm["raw_file"]:
            r.error("d", w, f"raw_file 與對照表不符（應為 {keys.get(ck)}）")
        if ck and p.path.name != f"{str(ck).lower()}.md":
            r.error("e", w, f"論文頁檔名應為 {str(ck).lower()}.md")
    if t == "town" and fm.get("town_status") not in TOWN_STATUSES:
        r.error("d", w, f"town_status 必須是 {'/'.join(sorted(TOWN_STATUSES))}")

    fixes = {}
    body = "\n".join(p.body)
    # has_inference 與內文一致
    has = INFER in body
    if fm.get("has_inference") is not has:
        msg = f"has_inference 應為 {str(has).lower()}（目前 {fm.get('has_inference')}）"
        (r.fixes.append(f"{w}  {msg}") if fix else r.error("d", w, msg))
        fixes["has_inference"] = str(has).lower()
    # 含〔待檢視〕就必須是 needs-review
    if PENDING in body and fm.get("status") != "needs-review":
        msg = f"含〔待檢視〕，status 應為 needs-review（目前 {fm.get('status')}）"
        (r.fixes.append(f"{w}  {msg}") if fix else r.error("k", w, msg))
        fixes["status"] = "needs-review"
    # sources 涵蓋內文所有引用鍵
    cited = []
    for m in CITE_GROUP.finditer(body):
        for it in CITE_ITEM_RE.finditer(m.group(1)):
            if it.group(1) not in cited:
                cited.append(it.group(1))
    declared = list(fm.get("sources") or [])
    missing = [k for k in cited if k not in declared]
    if missing:
        msg = f"sources 缺少內文用到的引用鍵：{missing}"
        (r.fixes.append(f"{w}  {msg}") if fix else r.error("d", w, msg))
        fixes["sources"] = "[" + ", ".join(declared + missing) + "]"
    for k in declared:
        if k not in keys:
            r.error("a", w, f"sources 中的 {k} 不在對照表")
    return fixes


def check_title(p: Page, r: Report):
    """(e)"""
    w = f"wiki/{p.rel}"
    if not KEBAB_RE.match(p.path.name):
        r.error("e", w, "檔名必須是英文 kebab-case（小寫英數與 -）")
    h1 = [(i, l) for i, l in enumerate(p.body) if l.startswith("# ")]
    if not h1:
        r.error("e", w, "缺少一級標題")
        return
    if len(h1) > 1:
        r.error("e", p.where(h1[1][0]), "一級標題只能有一個")
    i, line = h1[0]
    m = H1_RE.match(line)
    if not m or not CJK_RE.search(m.group(1)) or CJK_RE.search(m.group(2)):
        r.error("e", p.where(i), f"一級標題須為「中文 (English)」：{line}")
    title = p.fm.get("title")
    if title and line[2:].strip() != str(title).strip():
        r.error("e", p.where(i), f"一級標題與 title 不一致（title：{title}）")


def check_citations(p: Page, keys: dict, sources: dict, r: Report):
    """(a)"""
    for i, line, _, fence in p.iter_body():
        if fence:
            continue
        for m in CITE_GROUP.finditer(line):
            for it in CITE_ITEM_RE.finditer(m.group(1)):
                key, a, b = it.group(1), int(it.group(2)), it.group(3)
                if key not in keys:
                    r.error("a", p.where(i), f"引用鍵 {key} 不在 AGENTS.md §3 對照表")
                    continue
                src = sources.get(key)
                if src is None:
                    r.warn("a", p.where(i), f"cache/text/{key}.txt 不存在，無法核對頁碼")
                    continue
                if b and int(b) <= a:
                    r.error("a", p.where(i), f"[{key}, p.{a}–{b}] 頁碼範圍的起始頁必須小於結束頁")
                    continue
                ends = [a, int(b)] if b else [a]  # 起訖頁
                bad = [n for n in ends if not 1 <= n <= src.n_pages]
                for n in bad:
                    r.error("a", p.where(i), f"[{key}, p.{n}] 超出範圍（PDF 共 {src.n_pages} 頁）")
                if bad:
                    continue
                for n in range(ends[0], ends[-1] + 1):  # 範圍內每一頁
                    if n in src.untranscribed:
                        r.warn("a", p.where(i), f"[{key}, p.{n}] 這頁未轉錄，請對照 PDF 人工核對")
        # 看起來像引用、但格式不對的
        for m in re.finditer(rf"\[({CITEKEY})[^\]]*\](?!\()", line):
            if not CITE_GROUP.fullmatch(m.group(0)) and not fence:
                r.error("a", p.where(i), f"引用格式錯誤：{m.group(0)}（應為 [Key, p.N]）")
    if p.fm.get("type") == "paper":
        ck, n = p.fm.get("citekey"), p.fm.get("pdf_pages")
        if ck in sources and n is not None and n != sources[ck].n_pages:
            r.error("a", f"wiki/{p.rel}", f"pdf_pages={n} 與 PDF 實際頁數 {sources[ck].n_pages} 不符")


def check_quotes(p: Page, sources: dict, r: Report):
    """(b)"""
    for i, line, _, fence in p.iter_body():
        if fence or not line.startswith(">"):
            continue
        m = QUOTE_RE.match(line)
        if not m:
            continue
        quote, cite = m.group(1), m.group(2)
        items = CITE_ITEM_RE.findall(cite)
        if len(items) != 1:
            r.error("b", p.where(i), "英文引文必須恰好標一個出處")
            continue
        key, page = items[0][0], int(items[0][1])
        # 只能一句：句中出現「句點/問號/驚嘆號＋空白＋大寫或引號」就視為多句
        inner = re.sub(r"\b(e\.g|i\.e|et al|cf|vs|Fig|Eq|No|pp?|Dr|Mr|Ms)\.", "", quote)
        if re.search(r"[.!?]\s+[\"'A-Z(]", inner):
            r.error("b", p.where(i), "英文引文超過一句")
        nxt = p.body[i + 1] if i + 1 < len(p.body) else ""
        if not re.match(r"^>\s*中譯：\S", nxt):
            r.error("b", p.where(i), "英文引文下一行必須是「> 中譯：……」")
        src = sources.get(key)
        if src is None:
            r.warn("b", p.where(i), f"cache/text/{key}.txt 不存在，無法比對引文")
            continue
        if page in src.untranscribed:
            r.warn("b", p.where(i), f"[{key}, p.{page}] 這頁未轉錄，引文無法自動比對，請對照 PDF 人工核對")
            continue
        hits = src.find(quote)
        tag = "（原文為人工轉錄，可信度較低）" if src.vision else ""
        if page in hits:
            if src.vision:
                r.info("b", p.where(i), f"引文比對成功{tag}")
            continue
        # 跨頁的句子：和下一頁接起來再找
        joined = compact(src.pages.get(page, "") + " " + src.pages.get(page + 1, ""))
        if compact(quote) in joined:
            continue
        if hits:
            r.error("b", p.where(i), f"引文出現在 p.{hits}，不是標註的 p.{page}{tag}")
        elif page in src.partial:
            r.warn("b", p.where(i), f"[{key}, p.{page}] 只有部分轉錄，引文不在已轉錄的段落，請對照 PDF 人工核對")
        else:
            r.error("b", p.where(i), f"引文在 {key} 原文中找不到（逐字比對失敗）{tag}")


INLINE_QUOTE_RE = re.compile(r'["“]([^"“”\n]*[A-Za-z][^"“”\n]*)["”]')


def check_inline_quotes(p: Page, sources: dict, r: Report):
    """(b) 內文裡用雙引號括起來的英文片段，也要逐字出現在所引頁面。

    - 出處取同一句（以。！？切句）裡的引用；同句有多個出處時，任一頁找到就算通過
    - 比對前的正規化和整句引文相同：合併斷行連字號、統一空白和引號（見 compact）
    - 片段不一定是完整的一句，所以不檢查「只能一句」
    """
    for i, line, h2, fence in p.iter_body():
        if fence or QUOTE_RE.match(line):
            continue
        for sent in re.split(r"(?<=[。！？])", line):
            for m in INLINE_QUOTE_RE.finditer(sent):
                frag = m.group(1).strip()
                cites = [(k, int(a)) for g in CITE_GROUP.finditer(sent)
                         for k, a, _ in CITE_ITEM_RE.findall(g.group(1))]
                if not cites:
                    r.error("b", p.where(i), f"英文片段沒有出處，無法比對：\"{frag[:40]}\"")
                    continue
                ok, notes = False, []
                for key, page in cites:
                    src = sources.get(key)
                    if src is None:
                        notes.append(f"cache/text/{key}.txt 不存在")
                        continue
                    if page in src.untranscribed:
                        notes.append(f"{key} p.{page} 未轉錄")
                        continue
                    joined = compact(src.pages.get(page, "") + " " + src.pages.get(page + 1, ""))
                    if compact(frag) in joined:
                        ok = True
                        break
                    hits = src.find(frag)
                    if hits:
                        notes.append(f"{key} 在 p.{hits} 找到，不是 p.{page}")
                    elif page in src.partial:
                        notes.append(f"{key} p.{page} 只有部分轉錄，不在已轉錄段落")
                    else:
                        notes.append(f"{key} p.{page} 找不到")
                if ok:
                    continue
                if all("未轉錄" in n or "不存在" in n or "部分轉錄" in n for n in notes):
                    r.warn("b", p.where(i), f"英文片段無法自動比對（{'；'.join(notes)}），請人工核對：\"{frag[:40]}\"")
                else:
                    r.error("b", p.where(i), f"英文片段逐字比對失敗（{'；'.join(notes)}）：\"{frag[:40]}\"")


def resolve(p: Page, target: str, wiki: Path) -> Path:
    return (p.path.parent / target.split("#")[0]).resolve()


def check_links(pages: list[Page], extra: list[Page], wiki: Path, r: Report, fix: bool):
    """(g) 回傳 {頁面: 修正後內容}，以及連入關係。"""
    by_stem = defaultdict(list)
    for q in pages:
        by_stem[q.path.stem].append(q)
    inbound: dict[str, set[str]] = defaultdict(set)
    rewrites = {}
    for p in pages + extra:
        new_lines = list(p.lines)
        for i, line, _, fence in p.iter_body():
            if fence:
                continue
            for m in LINK_RE.finditer(line):
                target = m.group(2)
                if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                    continue
                dest = resolve(p, target, wiki)
                if not dest.exists():
                    r.error("g", p.where(i), f"連結失效：{target}")
                elif dest.suffix == ".md" and wiki in dest.parents and p.rel != "index.md":
                    inbound[dest.relative_to(wiki).as_posix()].add(p.rel)
            for m in WIKILINK_RE.finditer(line):
                name = m.group(1).split("|")[0].strip()
                cands = by_stem.get(Path(name).stem, [])
                if fix and len(cands) == 1:
                    q = cands[0]
                    rel = Path(os.path.relpath(q.path, p.path.parent)).as_posix()
                    label = q.fm.get("title", name)
                    new_lines[p.body_start + i] = new_lines[p.body_start + i].replace(
                        m.group(0), f"[{label}]({rel})")
                    r.fixes.append(f"{p.where(i)}  [[{name}]] → 相對連結")
                    inbound[q.rel].add(p.rel)
                else:
                    r.error("g", p.where(i), f"禁止使用 [[ ]]：{m.group(0)}"
                            + ("" if cands else "（找不到對應頁面）"))
        if new_lines != p.lines:
            rewrites[p] = new_lines
    for p in pages:  # related 欄位也算連入
        for rel in p.fm.get("related") or []:
            inbound[str(rel)].add(p.rel)
    return rewrites, inbound


INDEX_LINE_RE = re.compile(r"^- \[(.+?)\]\(([^)]+\.md)\)(?: — (.*))?$")


def index_line(p: Page) -> str:
    """index.md 中一頁應有的那一行：- [title](路徑) — summary"""
    return f"- [{p.fm.get('title', p.rel)}]({p.rel}) — {p.fm.get('summary', '')}".rstrip(" —")


def check_index(pages: list[Page], index: Page | None, wiki: Path, r: Report, fix: bool):
    """(i) 每頁都要列在 index.md，而且標題、摘要和頁面 frontmatter 一致（--fix 自動同步）。"""
    if index is None:
        r.error("i", "wiki/index.md", "index.md 不存在")
        return None
    listed = set()
    for m in LINK_RE.finditer(re.sub(r"`[^`]*`", "", index.raw)):
        dest = (wiki / m.group(2).split("#")[0]).resolve()
        if dest.exists() and wiki in dest.parents:
            listed.add(dest.relative_to(wiki).as_posix())
    lines = index.raw.split("\n")
    changed = False
    # 已列出的頁面：標題和摘要要和該頁 frontmatter 一致
    by_rel = {p.rel: p for p in pages}
    for j, l in enumerate(lines):
        m = INDEX_LINE_RE.match(l)
        if not m or m.group(2) not in by_rel:
            continue
        p = by_rel[m.group(2)]
        expected = index_line(p)
        if l != expected:
            what = "、".join(x for x, a, b in (("標題", m.group(1), p.fm.get("title")),
                                                ("摘要", m.group(3), p.fm.get("summary"))) if a != b) or "格式"
            if fix:
                lines[j] = expected
                changed = True
                r.fixes.append(f"wiki/index.md:{j + 1}  同步 {p.rel} 的{what}")
            else:
                r.error("i", f"wiki/index.md:{j + 1}", f"{p.rel} 的{what}和頁面 frontmatter 不一致")
    missing = [p for p in pages if p.rel not in listed]
    if not missing:
        return lines if changed else None
    if not fix:
        for p in missing:
            r.error("i", "wiki/index.md", f"沒有列出 {p.rel}")
        return None
    for p in missing:
        head = INDEX_SECTIONS.get(p.fm.get("type"))
        if head is None or head not in lines:
            r.error("i", "wiki/index.md", f"沒有列出 {p.rel}，且找不到對應的分節，無法自動補上")
            continue
        start = lines.index(head)
        end = next((j for j in range(start + 1, len(lines)) if lines[j].startswith("## ")), len(lines))
        section = lines[start + 1:end]
        section = [l for l in section if l.strip() != "（尚無頁面）"]
        while section and not section[-1].strip():
            section.pop()
        if not section or section[0].strip():
            section.insert(0, "")
        section.append(index_line(p))
        section.append("")
        lines[start + 1:end] = section
        r.fixes.append(f"wiki/index.md  補上 {p.rel}")
    return lines


def check_orphans(pages: list[Page], inbound: dict, r: Report):
    """(h)：index.md 的連結不算。"""
    for p in pages:
        if not (inbound.get(p.rel, set()) - {p.rel}):
            r.error("h", f"wiki/{p.rel}", "孤兒頁：除了 index.md 之外，沒有任何頁面連到這裡")


def check_pending(p: Page, r: Report):
    """(k) 列出〔待檢視〕和〔待補〕。"""
    for i, line, _, fence in p.iter_body():
        if fence:
            continue
        if PENDING in line:
            r.info("k", p.where(i), "〔待檢視〕等使用者決定：" + line.strip()[:60])
        if TODO in line:
            r.info("k", p.where(i), "〔待補〕尚無資料：" + line.strip()[:60])


def check_sentences(p: Page, r: Report):
    """(s) 沒有出處也沒有〔推論〕的句子。豁免範圍見 AGENTS.md §4.5。"""
    body = p.body
    for i, line, h2, fence in p.iter_body():
        s = line.strip()
        if fence or not s or s.startswith("#"):
            continue
        in_summary = h2.startswith("白話摘要")
        if in_summary and INFER in s:
            r.error("s", p.where(i), "白話摘要中不得出現〔推論〕")
        if h2.startswith(EXEMPT_SECTIONS):
            continue
        if s.lstrip("-*+> ").startswith(TODO):
            continue  # 〔待補〕佔位行，改由 (k) 列出
        if s.startswith("|"):
            if re.fullmatch(r"\|[\s:|-]+\|?", s):
                continue  # 分隔列
            nxt = body[i + 1].strip() if i + 1 < len(body) else ""
            if re.fullmatch(r"\|[\s:|-]+\|?", nxt):
                continue  # 標題列
            if not (CITE_GROUP.search(s) or INFER in s):
                r.error("s", p.where(i), f"表格列沒有出處也沒有〔推論〕：{s[:50]}")
            continue
        if re.match(r"^>\s*中譯：", s):
            continue
        text = re.sub(r"^(>\s*)?([-*+]|\d+\.)\s+", "", s)
        if re.fullmatch(r"(\[[^\]]*\]\([^)]*\)[\s，、]*)+", text):
            continue  # 純連結行
        for sent in re.split(r"(?<=[。！？])", text):
            sent = sent.strip()
            if not sent or re.search(r"[：:]$", sent):
                continue  # 引導句，例如「三種策略如下：」
            if CITE_GROUP.search(sent) or INFER in sent:
                continue
            r.error("s", p.where(i), f"沒有出處也沒有〔推論〕：{sent[:50]}")


# ---------------------------------------------------------------- 主程式

def set_fm_field(lines: list[str], start: int, end: int, field: str, value: str):
    for j in range(start, end):
        if re.match(rf"^{field}:", lines[j]):
            lines[j] = f"{field}: {value}"
            return
    lines.insert(end, f"{field}: {value}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true")
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent))
    args = ap.parse_args()
    root = Path(args.root).resolve()
    wiki = root / "wiki"
    r = Report()

    keys = load_citekeys(root)
    if not keys:
        r.error("a", "AGENTS.md", "§3 找不到引用鍵對照表")
    sources = {}
    for key in keys:
        f = root / "cache" / "text" / f"{key}.txt"
        if f.exists():
            sources[key] = Source(f)
            if not sources[key].vision and sum(
                    1 for b in sources[key].pages.values() if len(re.sub(r"\s", "", b)) >= 50) == 0:
                r.warn("b", f"cache/text/{key}.txt", "沒有可比對的文字（掃描檔？），該篇引文無法核對")
        else:
            r.warn("a", f"cache/text/{key}.txt", "不存在，請先執行 extract.py")

    special = {"index.md", "log.md"}
    files = sorted(f for f in wiki.rglob("*.md") if f.relative_to(wiki).as_posix() not in special)
    pages = [Page(f, wiki) for f in files]
    extra = [Page(wiki / n, wiki) for n in sorted(special) if (wiki / n).exists()]
    for e in extra:  # index/log 沒有 frontmatter
        e.fm_error, e.body_start, e.body = None, 0, e.lines
    index = next((e for e in extra if e.rel == "index.md"), None)

    fm_fixes = {}
    for p in pages:
        fm_fixes[p] = check_frontmatter(p, keys, r, args.fix)
        if p.fm_error:
            continue
        check_title(p, r)
        check_citations(p, keys, sources, r)
        check_quotes(p, sources, r)
        check_inline_quotes(p, sources, r)
        check_pending(p, r)
        check_sentences(p, r)

    rewrites, inbound = check_links(pages, extra, wiki, r, args.fix)
    check_orphans(pages, inbound, r)
    index_lines = check_index(pages, index, wiki, r, args.fix)

    if args.fix:
        for p in pages + extra:
            lines = rewrites.get(p, list(p.lines))
            fx = fm_fixes.get(p) or {}
            if fx:
                end = p.body_start - 1
                for field, value in fx.items():
                    set_fm_field(lines, 1, end, field, value)
            if lines != p.lines:
                p.path.write_text("\n".join(lines), encoding="utf-8", newline="\n")
        if index_lines is not None:
            index.path.write_text("\n".join(index_lines), encoding="utf-8", newline="\n")

    print(f"lint：檢查 {len(pages)} 個頁面（另含 index.md、log.md 的連結）")
    return r.print()


if __name__ == "__main__":
    sys.exit(main())
