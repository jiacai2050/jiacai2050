#!/usr/bin/env python3
import tomllib

with open("project.toml", "rb") as f:
    data = tomllib.load(f)

rows = []
for p in data.get("project", []):
    repo = p["repo"]
    name = repo.split('/')[-1]
    repo_md = f"[{name}](https://github.com/{repo})"
    lang = ", ".join(p.get("lang", []))
    desc = p.get("description", "").strip()
    # Use main as default branch; could be extended to support other branches
    badge = f"![](https://img.shields.io/github/last-commit/{repo}/main)"
    rows.append((repo_md, lang, desc, badge))

header = "| Repo | Lang | Description | Last Commit |"
sep    = "| --- | --- | --- | --- |"
lines = [header, sep]
for repo, lang, desc, badge in rows:
    lines.append(f"| {repo} | {lang} | {desc} | {badge} |")

print("\n".join(lines))
