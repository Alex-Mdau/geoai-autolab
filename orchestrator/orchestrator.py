"""
GeoAI AutoLab — Main Orchestrator
===================================
Routes tasks, manages project state, coordinates generation.
Works in template mode (no API) or Claude API mode (full generation).
"""

import json
import os
import sys
import argparse
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from project_queue import ProjectQueue
from generator import ProjectGenerator
from readme_updater import ReadmeUpdater

BASE_DIR = Path(__file__).parent.parent


class Orchestrator:
    def __init__(self):
        self.state_file = BASE_DIR / "state.json"
        self.state = self.load_state()
        self.queue = ProjectQueue()
        self.generator = ProjectGenerator()
        self.readme_updater = ReadmeUpdater()

    def load_state(self):
        if self.state_file.exists():
            with open(self.state_file) as f:
                return json.load(f)
        return {
            "week": 0,
            "total_projects": 0,
            "current_project": None,
            "status": "initialized",
            "last_run": None,
            "mode": "template"
        }

    def save_state(self):
        self.state["last_run"] = datetime.now().isoformat()
        self.state["mode"] = "claude_api" if os.environ.get("CLAUDE_API_KEY") else "template"
        with open(self.state_file, "w") as f:
            json.dump(self.state, f, indent=2)

    def run_weekly(self):
        """Generate a new project for the week"""
        self.state["week"] += 1
        week_num = self.state["week"]
        mode = "Claude API" if os.environ.get("CLAUDE_API_KEY") else "Template"

        print(f"\n{'='*50}")
        print(f"🚀 Week {week_num} — GeoAI AutoLab [{mode} Mode]")
        print(f"{'='*50}")

        project = self.queue.get_next_project()
        print(f"📋 Project selected: {project['name']}")
        print(f"🏷  Category: {project['category']} | Difficulty: {project['difficulty']}")

        project_dir = BASE_DIR / "projects" / f"week_{week_num:02d}_{project['slug']}"
        project_dir.mkdir(parents=True, exist_ok=True)

        print(f"⚙️  Generating project files...")
        self.generator.generate(project, project_dir, week_num)

        self.state["current_project"] = project["name"]
        self.state["current_project_data"] = project
        self.state["total_projects"] = week_num
        self.state["status"] = "active"

        self.update_public_feed(project, week_num)
        self.readme_updater.update(self.state, project)
        self.save_state()

        print(f"\n✅ Week {week_num}: '{project['name']}' generated!")
        print(f"📁 Location: {project_dir.relative_to(BASE_DIR)}")

    def run_daily(self):
        """Daily activity update — keeps GitHub green"""
        if not self.state.get("current_project"):
            print("No active project. Skipping daily update.")
            return

        print(f"📊 Daily update: {self.state['current_project']}")
        self.update_activity_feed()
        self.save_state()
        print("✅ Daily activity recorded")

    def update_public_feed(self, project, week_num):
        feed_dir = BASE_DIR / "public_feed"
        feed_dir.mkdir(exist_ok=True)

        # status.json
        with open(feed_dir / "status.json", "w") as f:
            json.dump({
                "current_project": project["name"],
                "week": week_num,
                "status": "active",
                "active_model": "Claude API" if os.environ.get("CLAUDE_API_KEY") else "AutoLab Template",
                "last_updated": datetime.now().isoformat(),
                "progress": 100,
                "category": project["category"]
            }, f, indent=2)

        # projects.json — append completed project
        projects_file = feed_dir / "projects.json"
        projects = []
        if projects_file.exists():
            with open(projects_file) as f:
                projects = json.load(f)

        projects.append({
            "week": week_num,
            "name": project["name"],
            "slug": project["slug"],
            "category": project["category"],
            "difficulty": project["difficulty"],
            "tech_stack": project["tech_stack"],
            "description": project["description"],
            "completed_at": datetime.now().isoformat(),
            "dir": f"projects/week_{week_num:02d}_{project['slug']}"
        })

        with open(projects_file, "w") as f:
            json.dump(projects, f, indent=2)

    def update_activity_feed(self):
        feed_dir = BASE_DIR / "public_feed"
        activity_file = feed_dir / "activity.json"

        activity = []
        if activity_file.exists():
            with open(activity_file) as f:
                activity = json.load(f)

        activity.append({
            "timestamp": datetime.now().isoformat(),
            "action": "daily_progress",
            "project": self.state.get("current_project"),
            "week": self.state.get("week", 1),
            "model": "Claude API" if os.environ.get("CLAUDE_API_KEY") else "AutoLab"
        })

        # Keep last 60 entries
        activity = activity[-60:]
        with open(activity_file, "w") as f:
            json.dump(activity, f, indent=2)


def main():
    parser = argparse.ArgumentParser(description="GeoAI AutoLab Orchestrator")
    parser.add_argument("--mode", choices=["weekly", "daily"], required=True,
                        help="weekly: new project | daily: activity update")
    args = parser.parse_args()

    orchestrator = Orchestrator()

    if args.mode == "weekly":
        orchestrator.run_weekly()
    elif args.mode == "daily":
        orchestrator.run_daily()


if __name__ == "__main__":
    main()
