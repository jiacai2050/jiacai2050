#!/usr/bin/env python3
import tomllib

with open("project.toml", "rb") as f:
    data = tomllib.load(f)

cache_seconds = 60 * 60 * 24 # 1 day
rows = []
for p in data.get("project", []):
    repo = p["repo"]
    name = repo.split('/')[-1]
    repo_link = f"https://github.com/{repo}"
    repo_md = f"[{name}]({repo_link})"
    lang = ", ".join(p.get("lang", []))
    desc = p.get("description", "").strip()
    badge = f"![](https://img.shields.io/github/last-commit/{repo}?cacheSeconds={cache_seconds}&label={name}&style=flat-square)"
    rows.append((repo_md, lang, desc, badge))

header = "| Repo | Lang | Description | Last Commit |"
sep    = "| --- | --- | --- | --- |"
lines = [header, sep]
for repo, lang, desc, badge in rows:
    lines.append(f"| {repo} | {lang} | {desc} | {badge} |")

print("\n".join(lines))
