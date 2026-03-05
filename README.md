# GeoAI Lab

> **AI Engineering Lab** — One production-ready GIS, GeoAI, or ML project per week. Every week. Forever.

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Week](https://img.shields.io/badge/current_week-1-blue)
![Projects](https://img.shields.io/badge/projects_delivered-1-orange)
![Powered By](https://img.shields.io/badge/powered_by-Claude_AI-purple)
![Activity](https://img.shields.io/badge/activity-GitHub_Actions-2088FF)

![GeoAI](https://img.shields.io/badge/GeoAI-1%20projects-informational)

---

## Live Now — Week 1

### [Urban Heat Island Detector](projects/week_01_urban_heat_island)

> Detect and visualize urban heat islands using satellite LST data and land cover classification. Compare urban vs rural temperature differentials.

**Category:** `GeoAI` | **Difficulty:** `Intermediate`  
**Stack:** `rasterio` `numpy` `matplotlib` `scikit-learn` `geopandas`  
**Datasets:** NASA MODIS, USGS Landsat

---

## Completed Projects

| Week    | Project                                                          | Category | Difficulty   | Status |
| ------- | ---------------------------------------------------------------- | -------- | ------------ | ------ |
| Week 01 | [Urban Heat Island Detector](projects/week_01_urban_heat_island) | `GeoAI`  | Intermediate | Done   |

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

`geopandas` `matplotlib` `numpy` `rasterio` `scikit-learn`

## Lab Stats

| Metric                   | Value                |
| ------------------------ | -------------------- |
| Total Projects Delivered | 1                    |
| Active Since             | 2026-03-05           |
| Current Week             | 1                    |
| Generation Mode          | Template             |
| Last Updated             | 2026-03-05 15:36 UTC |

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

_Maintained by [Claude AI](https://anthropic.com) + [GitHub Actions](https://github.com/features/actions)_  
_New project every Monday | Daily activity maintained_
