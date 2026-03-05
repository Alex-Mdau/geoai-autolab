"""
README Updater
==============
Auto-generates the main repository README.md with live project stats,
progress badges, and a table of completed projects.
"""

import json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent


class ReadmeUpdater:

    def update(self, state: dict, current_project: dict):
        """Rebuild the root README.md with current state"""
        projects_file = BASE_DIR / "public_feed" / "projects.json"
        completed = []
        if projects_file.exists():
            with open(projects_file) as f:
                completed = json.load(f)

        readme = self._build(state, current_project, completed)

        with open(BASE_DIR / "README.md", "w") as f:
            f.write(readme)

    def _build(self, state: dict, project: dict, completed: list) -> str:
        week = state.get("week", 1)
        total = len(completed)
        status = state.get("status", "active")
        mode = state.get("mode", "template")
        started = completed[0]["completed_at"][:10] if completed else datetime.now().strftime("%Y-%m-%d")

        # Category breakdown
        by_category = {}
        for p in completed:
            cat = p.get("category", "Other")
            by_category[cat] = by_category.get(cat, 0) + 1
        category_badges = "  ".join(
            f"![{cat}](https://img.shields.io/badge/{cat}-{count}%20projects-informational)"
            for cat, count in by_category.items()
        )

        # Completed projects table (last 10)
        table_rows = []
        for p in reversed(completed[-15:]):
            w = p["week"]
            name = p["name"]
            slug = p.get("slug", "")
            cat = p.get("category", "")
            diff = p.get("difficulty", "")
            link = f"projects/week_{w:02d}_{slug}"
            table_rows.append(f"| Week {w:02d} | [{name}]({link}) | `{cat}` | {diff.title()} | Done |")

        table = "\n".join(table_rows) if table_rows else "| — | *First project generating...* | — | — | ... |"

        tech_used = set()
        for p in completed:
            tech_used.update(p.get("tech_stack", []))
        tech_list = " ".join(f"`{t}`" for t in sorted(tech_used)[:12])

        return f'''# GeoAI Lab

> **AI Engineering Lab** — One production-ready GIS, GeoAI, or ML project per week. Every week. Forever.

![Status](https://img.shields.io/badge/status-{status}-{"brightgreen" if status == "active" else "yellow"})
![Week](https://img.shields.io/badge/current_week-{week}-blue)
![Projects](https://img.shields.io/badge/projects_delivered-{total}-orange)
![Powered By](https://img.shields.io/badge/powered_by-Claude_AI-purple)
![Activity](https://img.shields.io/badge/automation-GitHub_Actions-2088FF)

{category_badges}

---

## Live Now — Week {week}

### [{project.get("name", "Initializing...")}](projects/week_{week:02d}_{project.get("slug", "")})

> {project.get("description", "Starting first project...")}

**Category:** `{project.get("category", "GeoAI")}` | **Difficulty:** `{project.get("difficulty", "intermediate").title()}`  
**Stack:** {" ".join(f"`{t}`" for t in project.get("tech_stack", []))}  
**Datasets:** {", ".join(project.get("datasets", []))}

---

## Completed Projects

| Week | Project | Category | Difficulty | Status |
|------|---------|----------|------------|--------|
{table}

---

## How It Works

```
Every Monday — GitHub Actions triggers
         ↓
  orchestrator.py runs
         ↓
  Next project pulled from 52-project queue
         ↓
  Claude API writes complete production code (activates with API key)
  OR scaffolding is generated (works without API key)
         ↓
  Full project committed: main.py, config.py,
  utils.py, tests/, README.md, requirements.txt
         ↓
  Root README updates with new stats
         ↓
  Daily commits keep GitHub contribution graph green
```

## Technologies Used

{tech_list if tech_list else "`geopandas` `folium` `scikit-learn` `rasterio` `numpy` `pandas` `matplotlib` `fastapi` `plotly` `networkx`"}

## Lab Stats

| Metric | Value |
|--------|-------|
| Total Projects Delivered | {total} |
| Active Since | {started} |
| Current Week | {week} |
| Generation Mode | {"Claude API" if mode == "claude_api" else "Template"} |
| Last Updated | {datetime.now().strftime("%Y-%m-%d %H:%M")} UTC |

## Repository Structure

```
geoai-lab/
├── .github/workflows/
│   ├── ci.yml               # Weekly construction and checks
│   └── lint-and-format.yml  # Daily checks and updates
├── orchestrator/
│   ├── orchestrator.py      # Main brain
│   ├── generator.py         # Code construction (template + Claude API)
│   ├── project_queue.py     # 52 projects, auto-rotates
│   └── readme_updater.py    # This file's builder
├── projects/
│   └── week_XX_*/           # Each week's project
├── public_feed/
│   ├── status.json          # Current status
│   ├── projects.json        # All completed projects
│   └── activity.json        # Activity log
├── state.json               # Orchestrator state
└── README.md                # This file (auto-generated)
```

## Upgrade to Full AI Generation

Add your Claude API key as a GitHub Secret to get fully AI-written, production-grade code:

1. Go to **Settings → Secrets → Actions**
2. Add secret: `CLAUDE_API_KEY` = your key from [console.anthropic.com](https://console.anthropic.com)
3. Re-run the weekly workflow

The system detects the key automatically and switches to Claude API mode.

---

*Maintained by [Claude AI](https://anthropic.com) + [GitHub Actions](https://github.com/features/actions)*  
*New project every Monday | Daily activity maintained*
'''
