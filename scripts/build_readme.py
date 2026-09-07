#!/usr/bin/env python3
"""Render README.md = header template + auto TOC + full body of the reference catalog."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "OT_DEEP_REFERENCE_CATALOG_2026.md"
HEADER = ROOT / "scripts" / "readme_header.md"
README = ROOT / "README.md"


def github_slug(heading: str) -> str:
    # Port of github-slugger: lowercase, drop punctuation/symbols, spaces -> hyphens.
    text = re.sub(r"[^\w\- ]+", "", heading.strip().lower())
    return text.replace(" ", "-")


def main() -> None:
    catalog = CATALOG.read_text("utf-8")
    lines = catalog.splitlines()
    assert lines[0].startswith("# "), "catalog must start with an H1"
    body_lines = lines[1:]
    body = "\n".join(body_lines).strip("\n") + "\n"

    m_p = re.search(r"\*\*(\d+) 篇正式", catalog)
    m_r = re.search(r"\*\*(\d+) 篇需继续跟踪", catalog)
    m_d = re.search(r"最近复检：(\d{4}-\d{2}-\d{2})", catalog)
    assert m_p and m_r and m_d, "catalog intro/recheck line format changed"
    deep_reads = len(list(ROOT.glob("*/report.md")))

    toc = []
    for line in body_lines:
        m = re.match(r"^(##|###) (.+)$", line)
        if not m:
            continue
        level, title = m.group(1), m.group(2).strip()
        indent = "" if level == "##" else "  "
        label = title.replace("[", "\\[").replace("]", "\\]")
        toc.append(f"{indent}- [{label}](#{github_slug(title)})")

    header = HEADER.read_text("utf-8").format(
        proceedings=m_p.group(1),
        preprints=m_r.group(1),
        deep_reads=deep_reads,
        recheck=m_d.group(1).replace("-", "--"),  # shields.io escapes '-' as '--'
        toc="\n".join(toc),
    )
    README.write_text(header + body, "utf-8")

    # Every TOC anchor must resolve to a heading in the rendered file.
    slugs = {github_slug(h) for h in re.findall(r"^#{2,3} (.+)$", body, re.M)}
    for anchor in re.findall(r"\]\(#([^)]+)\)", header):
        assert anchor in slugs, f"dangling anchor: #{anchor}"
    print(f"README.md written: {README.stat().st_size} bytes, {len(toc)} TOC entries, "
          f"{m_p.group(1)} proceedings / {m_r.group(1)} preprints / {deep_reads} deep reads, "
          f"recheck {m_d.group(1)}")


if __name__ == "__main__":
    main()
