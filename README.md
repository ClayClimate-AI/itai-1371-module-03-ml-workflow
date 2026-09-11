# Wine Classification — ML Workflow (ITAI 1371, Module 3)

<p>
  <img alt="Course" src="https://img.shields.io/badge/Course-ITAI%201371-0A66C2">
  <img alt="Module" src="https://img.shields.io/badge/Module-03-1F6FEB">
  <img alt="Task" src="https://img.shields.io/badge/Task-Wine%20Classification-8E44AD">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.12%20%7C%203.14-3776AB?logo=python&logoColor=white">
  <img alt="CI" src="https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white">
  <img alt="License" src="https://img.shields.io/badge/License-Educational-lightgrey">
</p>

An end-to-end machine-learning workflow on the classic **Wine** dataset: load and explore the data,
run exploratory analysis, train and compare classifiers, and evaluate the results. The work is
organized as a single Jupyter notebook backed by a reproducible environment, contract tests, and
continuous integration.

## Overview

The notebook walks through the full supervised-learning pipeline end to end:

1. Load the Wine dataset (178 samples, 13 chemical features, 3 cultivar classes).
2. Explore structure and class distribution.
3. Prepare features, split into train/test, and standardize (scaler fit on the training set only).
4. Train two models — Logistic Regression and a Decision Tree — and compare them.
5. Evaluate with accuracy, a classification report, and a confusion matrix, then interpret the results.

## Dataset

The [Wine recognition dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#wine-recognition-dataset)
ships with scikit-learn (`sklearn.datasets.load_wine`). It contains 178 samples described by 13
continuous chemical-analysis features, labeled across 3 classes. No external download is required.

## Project structure

```
.
├── Module_03_Lab_Exercise.ipynb   # main notebook (analysis + models)
├── requirements.txt               # Python dependencies
├── scripts/setup_gate.py          # environment / dependency check
├── src/                           # supporting implementation code
├── tests/                         # contract tests
├── specs/                         # product & technical specifications
├── docs/adr/                      # architecture decision records
└── .github/workflows/ci.yml       # CI pipeline
```

## Getting started

Requires Python 3.12+ (developed on 3.14; CI runs on 3.12).

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. (Optional) verify the environment is set up correctly
python scripts/setup_gate.py

# 4. Launch the notebook
jupyter notebook Module_03_Lab_Exercise.ipynb
```

Run the notebook top to bottom (Kernel → Restart & Run All) so cells execute in order.

## Testing & CI

```bash
pytest -q tests
```

Every push and pull request runs the [CI pipeline](.github/workflows/ci.yml) on a clean runner, which
installs dependencies, runs the environment check and tests, and executes the notebook end to end to
confirm it reproduces without errors. A local pre-commit hook can run the same fast checks before each
commit — enable it once per clone with:

```bash
git config core.hooksPath .githooks
```

## Development

Development happens on feature branches and is merged into `main` via pull request after CI passes.
Notable technical decisions are recorded as [architecture decision records](docs/adr/), and
requirements are captured under [`specs/`](specs/).

## Deliverables

| # | Deliverable | Format |
| --- | --- | --- |
| 1 | Executed notebook with all outputs | PDF |
| 2 | Reflective journal | PDF (1–2 pages) |
| 3 | Contribution journal | PDF (1–2 pages) |

## License

Coursework for ITAI 1371 (Module 3). Provided for educational purposes.
