#!/usr/bin/env python3
"""
README_sync.md 생성 스크립트.

역할:
- 레포 내 복기 md(BOJ/**/<num>/<num>.md) 목록과 README.md 표의 문제 링크를 비교.
- 아래 두 가지를 분리해 보여준다.
  1) README에 누락된 복기 md (레포엔 md 존재, README엔 없음)
  2) README에는 있지만 복기 md가 없는 것
- 전체 비교 표를 README_sync.md로 출력.

사용법:
    python generate_readme_sync.py
"""

import re
from pathlib import Path


def collect_readme_entries(readme_path: Path):
    text = readme_path.read_text(encoding="utf-8")
    pattern = re.compile(r"\[(\d+)\. [^\]]+\]\(([^)]+)\)")
    return {m.group(1): {"path": m.group(2)} for m in pattern.finditer(text)}


def collect_repo_md():
    repo = {}
    for path in Path("BOJ").rglob("*.md"):
        if path.stem.isdigit():
            repo[path.stem] = path.as_posix()
    return repo


def build_table(repo, readme, missing=None, extra=None):
    missing = set(missing or [])
    extra = set(extra or [])

    def sort_key(pid):
        if pid in missing:
            return (0, int(pid))
        if pid in extra:
            return (1, int(pid))
        return (2, int(pid))

    ids = sorted(set(repo) | set(readme), key=sort_key)
    lines = []
    lines.append("| 문제번호 | 레포 md 경로 | README 포함? | README 링크 |")
    lines.append("| --- | --- | --- | --- |")
    for pid in ids:
        repo_path = repo.get(pid, "")
        rd_path = readme.get(pid, {}).get("path", "")
        repo_link = f"[{Path(repo_path).name}]({repo_path})" if repo_path else "-"
        rd_link = f"[링크]({rd_path})" if rd_path else "-"
        in_readme = "Y" if pid in readme else "N"
        lines.append(f"| {pid} | {repo_link} | {in_readme} | {rd_link} |")
    return "\n".join(lines)


def main():
    repo = collect_repo_md()
    readme = collect_readme_entries(Path("README.md"))

    missing = sorted(set(repo) - set(readme), key=int)  # md 있음, README 없음
    extra = sorted(set(readme) - set(repo), key=int)    # README 있음, md 없음

    header = [
        "# README Sync Check",
        "",
        "README의 문제 분류 표와 레포 내 복기용 md 목록을 비교한 결과입니다.",
        "",
        "(generate_readme_sync.py 로부터 생성)",
        "",
        "## README에 누락된 복기 md (레포에는 md 존재)",
    ]
    if missing:
        for pid in missing:
            header.append(f"- {pid} — 경로: `{repo[pid]}`")
    else:
        header.append("- 없음")

    header.append("")
    header.append("## README에는 있지만 복기 md가 없는 것")
    if extra:
        for pid in extra:
            header.append(f"- {pid} — README 링크: `{readme[pid]['path']}`")
    else:
        header.append("- 없음")

    table = build_table(repo, readme, missing=missing, extra=extra)
    out = "\n".join(header + ["", "## 전체 내역", "", table])
    Path("README_sync.md").write_text(out, encoding="utf-8")
    print("Generated README_sync.md")


if __name__ == "__main__":
    main()
