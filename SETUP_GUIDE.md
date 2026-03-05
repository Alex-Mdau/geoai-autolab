# 🚀 Setup Guide — GeoAI AutoLab

Get your autonomous lab running in under 10 minutes.

---

## Step 1 — Create a GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. Name it: `geoai-autolab` (or anything you like)
3. Set to **Public** (so your portfolio is visible)
4. **Do NOT** initialize with README (we provide one)
5. Click **Create repository**

---

## Step 2 — Push This Code

```bash
# In this folder:
git init
git add -A
git commit -m "🌍 Initialize GeoAI AutoLab"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/geoai-autolab.git
git push -u origin main
```

---

## Step 3 — Enable GitHub Actions

1. Go to your repo on GitHub
2. Click the **Actions** tab
3. If prompted, click **"I understand my workflows, go ahead and enable them"**

---

## Step 4 — Test It Right Now (Optional but Recommended)

Don't wait until Monday — trigger it manually:

1. Go to **Actions** tab
2. Click **"Lint"**
3. Click **"Run workflow"** → **"Run workflow"**
4. Watch it generate your first project in ~60 seconds!

---

## Step 5 — Add Claude API Key (When Ready)

This unlocks full AI-written, production-grade code:

1. Get your API key at [console.anthropic.com](https://console.anthropic.com)
2. In your repo: **Settings → Secrets and variables → Actions**
3. Click **"New repository secret"**
4. Name: `CLAUDE_API_KEY`
5. Value: your API key
6. Click **"Add secret"**

The system detects the key automatically — no other changes needed.

---

## What Happens Automatically

| Schedule              | Action                              |
| --------------------- | ----------------------------------- |
| Every Monday 9 AM UTC | New project generated and committed |
| Tue–Sat 2 PM UTC      | Daily progress update committed     |
| Always                | README updates with latest stats    |

---

## Folder Structure After First Project

```
geoai-autolab/
├── .github/workflows/
│   ├── lint.yml                ← runs Mondays
│   └── ci.yml                  ← runs Tue–Sat
├── orchestrator/
│   ├── orchestrator.py         ← main brain
│   ├── generator.py            ← code generator
│   ├── project_queue.py        ← 52 projects
│   └── readme_updater.py       ← auto README
├── projects/
│   └── week_01_osm_road_analyzer/   ← Week 1 project
│       ├── main.py
│       ├── config.py
│       ├── utils.py
│       ├── requirements.txt
│       ├── README.md
│       └── tests/
│           └── test_main.py
├── public_feed/
│   ├── status.json
│   ├── projects.json
│   └── activity.json
├── state.json
├── projects_queue.json
└── README.md                   ← auto-updated each week
```

---

## Troubleshooting

**Workflow fails on pip install?**
The workflow installs all needed packages automatically. Check the Actions log for the specific error.

**Nothing committed?**
Make sure the workflow has `contents: write` permission. Check **Settings → Actions → General → Workflow permissions** → set to "Read and write permissions".

**Want to change which project runs next?**
Edit `projects_queue.json` and change `"current_index"` to any number 0–51.

---

_Questions? Open an issue on GitHub._
