"""把 raw/ 的 PDF 抽成 cache/text/<citekey>.txt。

用法：python extract.py [--force] [citekey ...]

- 引用鍵和檔名的對照，從 AGENTS.md §3 的表格讀取（唯一來源）
- 輸出格式：檔頭幾行以 # 開頭的中繼資料，接著每頁一段 `=== p.N ===`
- PDF 的 sha256 沒變就不重抽；檔頭有 `# source: vision-transcribed` 的檔案永不覆寫
- 抽完列出每篇的頁數和空白頁。結束代碼：0 = 全部有文字，1 = 有空白頁或錯誤
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "raw"
OUT = ROOT / "cache" / "text"
MIN_CHARS = 50  # 一頁少於這個字數視為「沒抽到文字」

sys.stdout.reconfigure(encoding="utf-8")


def load_citekeys() -> dict[str, str]:
    """從 AGENTS.md 讀出 {引用鍵: raw 檔名}。"""
    text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    rows = re.findall(r"^\|\s*`([A-Za-z]+\d{4}[a-z]?)`\s*\|\s*`([^`]+\.pdf)`\s*\|", text, re.M)
    return dict(rows)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read_header(path: Path) -> dict[str, str]:
    header = {}
    if not path.exists():
        return header
    with path.open(encoding="utf-8") as f:
        for line in f:
            m = re.match(r"^# (\w[\w-]*): (.*)$", line.rstrip("\n"))
            if not m:
                break
            header[m.group(1)] = m.group(2)
    return header


def extract(citekey: str, pdf: Path, force: bool) -> tuple[int, list[int]]:
    from pypdf import PdfReader

    out = OUT / f"{citekey}.txt"
    digest = sha256(pdf)
    header = read_header(out)
    if header.get("source") == "vision-transcribed":
        print(f"[skip] {citekey}: 人工轉錄檔，不覆寫")
        return check(out)
    if not force and header.get("sha256") == digest:
        print(f"[skip] {citekey}: PDF 沒有變動")
        return check(out)

    reader = PdfReader(str(pdf))
    parts = [
        f"# citekey: {citekey}",
        f"# raw_file: {pdf.name}",
        f"# sha256: {digest}",
        "# source: pypdf",
        f"# pages: {len(reader.pages)}",
        "",
    ]
    for i, page in enumerate(reader.pages, start=1):
        try:
            txt = page.extract_text() or ""
        except Exception as e:  # 單頁壞掉不影響其他頁
            txt = ""
            print(f"  ! {citekey} p.{i} 抽取失敗：{e}")
        parts.append(f"=== p.{i} ===")
        parts.append(txt.strip())
        parts.append("")
    OUT.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(parts), encoding="utf-8")
    print(f"[done] {citekey}: {len(reader.pages)} 頁 → {out.relative_to(ROOT)}")
    return check(out)


def check(out: Path) -> tuple[int, list[int]]:
    """回傳 (總頁數, 空白頁清單)。"""
    text = out.read_text(encoding="utf-8")
    pages = re.split(r"^=== p\.(\d+) ===$", text, flags=re.M)[1:]
    empty = []
    for num, body in zip(pages[0::2], pages[1::2]):
        if len(re.sub(r"\s", "", body)) < MIN_CHARS:
            empty.append(int(num))
    return len(pages) // 2, empty


def main() -> int:
    args = sys.argv[1:]
    force = "--force" in args
    wanted = [a for a in args if not a.startswith("--")]
    keys = load_citekeys()
    if not keys:
        print("錯誤：AGENTS.md §3 找不到引用鍵對照表")
        return 1

    ok = True
    print(f"{'引用鍵':<12}{'頁數':>5}  空白頁")
    results = []
    for key, fname in keys.items():
        if wanted and key not in wanted:
            continue
        pdf = RAW / fname
        if not pdf.exists():
            print(f"[miss] {key}: 找不到 raw/{fname}")
            ok = False
            continue
        n, empty = extract(key, pdf, force)
        results.append((key, n, empty))
        ok &= not empty

    print("\n=== 抽取檢查 ===")
    for key, n, empty in results:
        status = "OK" if not empty else f"{len(empty)}/{n} 頁沒有文字：{empty}"
        print(f"{key:<12}{n:>4} 頁  {status}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
