"""
Project Generator
==================
Generates complete project files.
- Template Mode: Works right now, no API key needed. Creates real, structured code.
- Claude API Mode: Activates automatically when CLAUDE_API_KEY secret is set.
"""

import os
import json
import re
import logging
from pathlib import Path
from datetime import datetime

logger = logging.getLogger(__name__)


class ProjectGenerator:
    def __init__(self):
        self.api_key = os.environ.get("CLAUDE_API_KEY")
        self.mode = "claude_api" if self.api_key else "template"
        logger.info(f"Generator mode: {self.mode}")

    def generate(self, project: dict, project_dir: Path, week_num: int):
        """Entry point — routes to Claude API or template based on key availability"""
        if self.api_key:
            try:
                logger.info("Generating with Claude API...")
                self._generate_with_claude(project, project_dir, week_num)
                return
            except Exception as e:
                logger.warning(f"Claude API failed ({e}), falling back to template mode")

        logger.info("Generating from template...")
        self._generate_from_template(project, project_dir, week_num)

    # ─── Claude API Mode ───────────────────────────────────────────────────────

    def _generate_with_claude(self, project: dict, project_dir: Path, week_num: int):
        """Generate a complete, AI-written production project via Claude API"""
        import requests

        system_prompt = """You are a senior GeoAI engineer generating production-ready Python projects.
        
Return ONLY a valid JSON object with this exact structure:
{
  "files": {
    "main.py": "...full file content...",
    "config.py": "...full file content...",
    "utils.py": "...full file content...",
    "requirements.txt": "...content...",
    "README.md": "...content...",
    "tests/test_main.py": "...content..."
  }
}

Rules:
- Write real, working Python code (not pseudocode)
- Include proper error handling, logging, docstrings
- Make main.py fully runnable with `python main.py`
- Include data loading that works with public/free datasets
- No API keys required in the generated code
- Tests must actually test the logic"""

        user_prompt = f"""Generate a complete production-ready Python project:

Project: {project['name']}
Description: {project['description']}
Category: {project['category']}
Tech Stack: {', '.join(project['tech_stack'])}
Datasets: {', '.join(project['datasets'])}
Week: {week_num}
Difficulty: {project['difficulty']}
Expected Outputs: {', '.join(project.get('outputs', ['results.json']))}

Generate all 6 files. The code should be real and functional."""

        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json"
            },
            json={
                "model": "claude-opus-4-5",
                "max_tokens": 8000,
                "system": system_prompt,
                "messages": [{"role": "user", "content": user_prompt}]
            },
            timeout=120
        )

        response.raise_for_status()
        content = response.json()["content"][0]["text"]

        # Extract JSON (handle markdown code blocks)
        content = re.sub(r'```json\s*', '', content)
        content = re.sub(r'```\s*', '', content)
        content = content.strip()

        data = json.loads(content)
        files = data.get("files", {})

        for filename, file_content in files.items():
            filepath = project_dir / filename
            filepath.parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, "w") as f:
                f.write(file_content)
            logger.info(f"  ✓ {filename}")

    # ─── Template Mode ─────────────────────────────────────────────────────────

    def _generate_from_template(self, project: dict, project_dir: Path, week_num: int):
        """Generate a real, well-structured project without API"""

        files = {
            "main.py": self._build_main(project, week_num),
            "config.py": self._build_config(project),
            "utils.py": self._build_utils(project),
            "requirements.txt": self._build_requirements(project),
            "README.md": self._build_readme(project, week_num),
            "tests/__init__.py": "",
            "tests/test_main.py": self._build_tests(project),
            "outputs/.gitkeep": "",
            "data/.gitkeep": "",
        }

        for filename, content in files.items():
            filepath = project_dir / filename
            filepath.parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, "w") as f:
                f.write(content)
            logger.info(f"  ✓ {filename}")

    def _build_main(self, project: dict, week_num: int) -> str:
        tech = project["tech_stack"]
        cls = self._class_name(project["name"])
        name = project["name"]
        desc = project["description"]
        category = project["category"]
        datasets = project["datasets"]
        slug = project["slug"]

        imports = self._build_imports(tech)
        sample_data_fn = self._build_sample_data(tech)
        viz_fn = self._build_viz(tech)

        return f'''"""
{name}
{"=" * len(name)}

{desc}

Week:       {week_num}
Category:   {category}
Tech Stack: {", ".join(tech)}
Datasets:   {", ".join(datasets)}
Author:     GeoAI AutoLab — https://github.com/geoai-autolab
Generated:  {datetime.now().strftime("%Y-%m-%d")}
"""

import logging
import json
from pathlib import Path
from datetime import datetime

{imports}

from config import Config
from utils import setup_logging, timer, save_json

logger = logging.getLogger(__name__)


class {cls}:
    """
    {name}

    {desc}

    Usage:
        pipeline = {cls}()
        pipeline.run()
    """

    def __init__(self, config: Config = None):
        self.config = config or Config()
        self.data = None
        self.results = {{}}
        setup_logging(self.config.log_level)
        logger.info(f"Initialized: {name}")

    @timer
    def load_data(self):
        """Load and validate input data from configured sources."""
        logger.info("Loading data...")
        try:
            self.data = self._fetch_data()
            logger.info(f"Loaded {{len(self.data) if hasattr(self.data, '__len__') else 1}} records")
            return self.data
        except Exception as e:
            logger.error(f"Data loading failed: {{e}}")
            raise

    def _fetch_data(self):
        """
        Fetch data from: {", ".join(datasets)}

        TODO: Connect to real data source.
              Currently returns sample data for demonstration.
        """
        logger.info("Using sample data (replace with real data source)")
        return {sample_data_fn}

    @timer
    def process(self):
        """Run the full analysis pipeline."""
        if self.data is None:
            self.load_data()

        logger.info("Processing...")
        try:
            self.results = {{
                "project": "{name}",
                "category": "{category}",
                "week": {week_num},
                "timestamp": datetime.now().isoformat(),
                "input_records": len(self.data) if hasattr(self.data, "__len__") else 1,
                "analysis": self._run_analysis(),
                "summary": self._compute_summary(),
                "status": "completed"
            }}
            logger.info("Processing complete")
            return self.results
        except Exception as e:
            logger.error(f"Processing failed: {{e}}")
            raise

    def _run_analysis(self) -> dict:
        """Core {category} analysis — extend with domain-specific logic."""
        import numpy as np

        # ── Step 1: Preprocessing ──────────────────────────
        logger.info("Step 1: Preprocessing...")
        processed = self._preprocess(self.data)

        # ── Step 2: Core Computation ───────────────────────
        logger.info("Step 2: Running core analysis...")
        computed = self._compute(processed)

        # ── Step 3: Post-processing ────────────────────────
        logger.info("Step 3: Post-processing...")
        return self._postprocess(computed)

    def _preprocess(self, data):
        """Preprocess and clean input data."""
        return data

    def _compute(self, data):
        """Domain-specific computation for {name}."""
        import numpy as np
        return {{
            "record_count": len(data) if hasattr(data, "__len__") else 1,
            "computation": "complete"
        }}

    def _postprocess(self, computed: dict) -> dict:
        """Format and enrich computed results."""
        return computed

    def _compute_summary(self) -> dict:
        """Generate summary statistics."""
        return {{
            "status": "success",
            "outputs": {json.dumps(project.get("outputs", ["results.json"]))},
            "datasets_used": {json.dumps(datasets)}
        }}

    @timer
    def visualize(self, output_dir: Path = None):
        """Generate visualizations and save to output directory."""
        output_dir = output_dir or self.config.output_dir
        output_dir.mkdir(parents=True, exist_ok=True)

        logger.info(f"Generating visualizations → {{output_dir}}")
        {viz_fn}
        logger.info("Visualizations saved")

    @timer
    def export(self, output_dir: Path = None):
        """Export results to JSON."""
        output_dir = output_dir or self.config.output_dir
        output_dir.mkdir(parents=True, exist_ok=True)

        results_path = output_dir / "results.json"
        save_json(self.results, results_path)
        logger.info(f"Results exported → {{results_path}}")
        return results_path

    def run(self):
        """Run full pipeline: load → process → visualize → export."""
        logger.info("=" * 50)
        logger.info(f"Starting: {name}")
        logger.info("=" * 50)

        self.load_data()
        self.process()
        self.visualize()
        self.export()

        logger.info("=" * 50)
        logger.info("Pipeline completed successfully!")
        logger.info(f"Results in: {{self.config.output_dir}}")
        logger.info("=" * 50)

        return self.results


def main():
    config = Config()
    pipeline = {cls}(config)
    results = pipeline.run()
    print(f"\\n✅ Done! Status: {{results.get('status')}}")


if __name__ == "__main__":
    main()
'''

    def _build_config(self, project: dict) -> str:
        return f'''"""Configuration for {project["name"]}"""
from dataclasses import dataclass, field
from pathlib import Path
import os


@dataclass
class Config:
    # ── Paths ──────────────────────────────────────────────────────
    base_dir: Path = field(default_factory=lambda: Path(__file__).parent)
    data_dir: Path = field(default_factory=lambda: Path(__file__).parent / "data")
    output_dir: Path = field(default_factory=lambda: Path(__file__).parent / "outputs")
    cache_dir: Path = field(default_factory=lambda: Path(__file__).parent / ".cache")

    # ── Runtime ────────────────────────────────────────────────────
    random_seed: int = 42
    n_workers: int = int(os.environ.get("N_WORKERS", 4))
    log_level: str = os.environ.get("LOG_LEVEL", "INFO")
    debug: bool = os.environ.get("DEBUG", "false").lower() == "true"

    # ── Model / Processing ─────────────────────────────────────────
    batch_size: int = 64
    max_iterations: int = 200
    tolerance: float = 1e-4

    # ── Data Sources ───────────────────────────────────────────────
    datasets: list = field(default_factory=lambda: {json.dumps(project["datasets"])})

    def __post_init__(self):
        for d in [self.data_dir, self.output_dir, self.cache_dir]:
            d.mkdir(parents=True, exist_ok=True)

    def to_dict(self) -> dict:
        return {{
            "base_dir": str(self.base_dir),
            "output_dir": str(self.output_dir),
            "random_seed": self.random_seed,
            "log_level": self.log_level,
        }}
'''

    def _build_utils(self, project: dict) -> str:
        return f'''"""Utility functions for {project["name"]}"""
import logging
import json
import time
import functools
from pathlib import Path
from datetime import datetime


def setup_logging(level: str = "INFO"):
    """Configure logging format and level."""
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )


def timer(func):
    """Decorator: log function execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        logging.getLogger(func.__module__).info(
            f"{{func.__name__}} completed in {{elapsed:.2f}}s"
        )
        return result
    return wrapper


def save_json(data: dict, path: Path, indent: int = 2):
    """Save dict as formatted JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=indent, default=str)


def load_json(path: Path) -> dict:
    """Load JSON file safely."""
    if not path.exists():
        return {{}}
    with open(path) as f:
        return json.load(f)


def validate_data(data, required_fields: list = None) -> bool:
    """Basic data validation."""
    if data is None:
        raise ValueError("Data is None")
    if required_fields:
        for field in required_fields:
            if hasattr(data, "columns") and field not in data.columns:
                raise ValueError(f"Missing required field: {{field}}")
    return True


def chunk_list(lst: list, chunk_size: int):
    """Split list into chunks."""
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]


def format_bytes(size_bytes: int) -> str:
    """Human-readable file size."""
    for unit in ["B", "KB", "MB", "GB"]:
        if size_bytes < 1024:
            return f"{{size_bytes:.1f}} {{unit}}"
        size_bytes /= 1024
    return f"{{size_bytes:.1f}} TB"
'''

    def _build_requirements(self, project: dict) -> str:
        base = ["pytest>=7.0", "python-dotenv"]
        return "\n".join(sorted(set(project["tech_stack"] + base)))

    def _build_readme(self, project: dict, week_num: int) -> str:
        badges = " ".join([
            f"![{t}](https://img.shields.io/badge/{t.replace('-','--')}-blue)"
            for t in project["tech_stack"][:4]
        ])
        outputs_list = "\n".join(f"- `{o}`" for o in project.get("outputs", ["results.json"]))
        datasets_list = "\n".join(f"- {d}" for d in project["datasets"])

        return f'''# {project["name"]}

> **Week {week_num}** | GeoAI AutoLab | {datetime.now().strftime("%B %Y")}

{badges}
![Category](https://img.shields.io/badge/category-{project["category"]}-green)
![Difficulty](https://img.shields.io/badge/difficulty-{project["difficulty"]}-{"red" if project["difficulty"] == "advanced" else "yellow" if project["difficulty"] == "intermediate" else "brightgreen"})

---

## Overview

{project["description"]}

## Datasets

{datasets_list}

## Tech Stack

{chr(10).join(f"- `{t}`" for t in project["tech_stack"])}

## Outputs

{outputs_list}

---

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run the pipeline
python main.py
```

## Project Structure

```
{project["slug"]}/
├── main.py           # Main pipeline
├── config.py         # Configuration
├── utils.py          # Utilities
├── requirements.txt
├── tests/
│   └── test_main.py
├── data/             # Input data
└── outputs/          # Generated outputs
```

## Usage

```python
from main import {self._class_name(project["name"])}
from config import Config

pipeline = {self._class_name(project["name"])}(Config())
results = pipeline.run()
```

## Running Tests

```bash
pytest tests/ -v
```

---

*🤖 Generated by [GeoAI AutoLab](https://github.com/geoai-autolab) — Week {week_num}*
'''

    def _build_tests(self, project: dict) -> str:
        cls = self._class_name(project["name"])
        return f'''"""Tests for {project["name"]}"""
import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from main import {cls}
from config import Config


@pytest.fixture
def config(tmp_path):
    cfg = Config()
    cfg.output_dir = tmp_path / "outputs"
    cfg.data_dir = tmp_path / "data"
    cfg.cache_dir = tmp_path / ".cache"
    return cfg


@pytest.fixture
def pipeline(config):
    return {cls}(config)


class TestInitialization:
    def test_creates_instance(self, pipeline):
        assert pipeline is not None

    def test_has_config(self, pipeline):
        assert pipeline.config is not None

    def test_data_initially_none(self, pipeline):
        assert pipeline.data is None


class TestDataLoading:
    def test_loads_data(self, pipeline):
        data = pipeline.load_data()
        assert data is not None

    def test_data_not_empty(self, pipeline):
        data = pipeline.load_data()
        assert len(data) > 0 if hasattr(data, "__len__") else True

    def test_data_stored_on_instance(self, pipeline):
        pipeline.load_data()
        assert pipeline.data is not None


class TestProcessing:
    def test_runs_without_error(self, pipeline):
        pipeline.load_data()
        results = pipeline.process()
        assert results is not None

    def test_results_have_status(self, pipeline):
        pipeline.load_data()
        results = pipeline.process()
        assert "status" in results
        assert results["status"] == "completed"

    def test_results_have_project_name(self, pipeline):
        pipeline.load_data()
        results = pipeline.process()
        assert "project" in results


class TestExport:
    def test_exports_json(self, pipeline, tmp_path):
        pipeline.load_data()
        pipeline.process()
        output = pipeline.export(tmp_path)
        assert output.exists()

    def test_json_is_valid(self, pipeline, tmp_path):
        import json
        pipeline.load_data()
        pipeline.process()
        output = pipeline.export(tmp_path)
        with open(output) as f:
            data = json.load(f)
        assert isinstance(data, dict)


class TestFullPipeline:
    def test_run_completes(self, pipeline):
        results = pipeline.run()
        assert results is not None
        assert results.get("status") == "completed"
'''

    # ─── Helpers ───────────────────────────────────────────────────────────────

    def _class_name(self, name: str) -> str:
        return "".join(w.title() for w in re.sub(r"[^a-zA-Z0-9 ]", " ", name).split())

    def _build_imports(self, tech: list) -> str:
        lines = []
        if "geopandas" in tech:
            lines.append("import geopandas as gpd")
            lines.append("from shapely.geometry import Point, Polygon")
        if "pandas" in tech or not lines:
            lines.append("import pandas as pd")
        if "numpy" in tech:
            lines.append("import numpy as np")
        if "folium" in tech:
            lines.append("import folium")
        if "matplotlib" in tech:
            lines.append("import matplotlib.pyplot as plt")
            lines.append("import matplotlib.cm as cm")
        if "scikit-learn" in tech:
            lines.append("from sklearn.preprocessing import StandardScaler")
            lines.append("from sklearn.cluster import KMeans, DBSCAN")
            lines.append("from sklearn.ensemble import RandomForestClassifier")
            lines.append("from sklearn.model_selection import train_test_split")
            lines.append("from sklearn.metrics import classification_report")
        if "rasterio" in tech:
            lines.append("import rasterio")
            lines.append("from rasterio.transform import from_bounds")
        if "scipy" in tech:
            lines.append("from scipy import stats, spatial")
        if "requests" in tech:
            lines.append("import requests")
        if "networkx" in tech:
            lines.append("import networkx as nx")
        return "\n".join(lines)

    def _build_sample_data(self, tech: list) -> str:
        if "geopandas" in tech:
            return """gpd.GeoDataFrame(
            {
                "id": range(150),
                "value": __import__("numpy").random.RandomState(42).randn(150).tolist(),
                "category": (["A", "B", "C"] * 50),
                "geometry": gpd.points_from_xy(
                    __import__("numpy").random.RandomState(1).uniform(-120, -70, 150),
                    __import__("numpy").random.RandomState(2).uniform(25, 50, 150)
                )
            },
            crs="EPSG:4326"
        )"""
        elif "pandas" in tech:
            return """pd.DataFrame({
            "timestamp": pd.date_range("2024-01-01", periods=365, freq="D"),
            "value": __import__("numpy").random.RandomState(42).randn(365).cumsum(),
            "category": (["A", "B", "C", "D"] * 92)[:365],
            "location": ["site_" + str(i % 10) for i in range(365)]
        })"""
        else:
            return """list(range(100))"""

    def _build_viz(self, tech: list) -> str:
        if "folium" in tech:
            return """try:
            m = folium.Map(location=[39.5, -98.35], zoom_start=4)
            if self.data is not None and hasattr(self.data, "geometry"):
                for _, row in self.data.iterrows():
                    folium.CircleMarker(
                        [row.geometry.y, row.geometry.x],
                        radius=5,
                        color="steelblue",
                        fill=True,
                        popup=str(row.get("value", ""))
                    ).add_to(m)
            map_path = output_dir / "map.html"
            m.save(str(map_path))
            logger.info(f"Map saved → {map_path}")
        except Exception as e:
            logger.warning(f"Map generation skipped: {e}")"""
        elif "matplotlib" in tech:
            return """try:
            fig, axes = plt.subplots(1, 2, figsize=(14, 5))
            if self.data is not None and hasattr(self.data, "value"):
                self.data["value"].plot(ax=axes[0], title="Value Distribution")
                self.data["value"].hist(bins=30, ax=axes[1], color="steelblue", edgecolor="white")
                axes[1].set_title("Histogram")
            fig.suptitle(f"{project['name']}", fontsize=14, fontweight="bold")
            plt.tight_layout()
            plot_path = output_dir / "analysis.png"
            plt.savefig(plot_path, dpi=150, bbox_inches="tight")
            plt.close()
            logger.info(f"Plot saved → {plot_path}")
        except Exception as e:
            logger.warning(f"Plot generation skipped: {e}")""".replace("{project['name']}", project["name"] if hasattr(self, '_current_project') else "Analysis")
        else:
            return """logger.info("Visualization step complete (no viz libraries configured)")"""
