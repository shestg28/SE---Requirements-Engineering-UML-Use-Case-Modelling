# Lab 5 — Bike-Share Station Manager

## Files
- `bike_share_stations.py`: revised Python program.
- `issues.md`: issue table based on the original repository source.
- `reflection.md`: draft answers to the four reflection questions.
- `run_analysis.sh`: helper script to save before/after tool reports when run in the repository.

## Run locally
From the cloned repository folder, create a virtual environment and install the tools:

```bash
python -m venv venv
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# macOS/Linux:
source venv/bin/activate
python -m pip install pylint bandit flake8
```

Before replacing the original Python file, save the original reports:

```bash
pylint bike_share_stations.py > pylint_before.txt
bandit -r bike_share_stations.py > bandit_before.txt
flake8 bike_share_stations.py > flake8_before.txt
```

Then replace `bike_share_stations.py` with the revised file and run:

```bash
python bike_share_stations.py
pylint bike_share_stations.py
bandit -r bike_share_stations.py
flake8 bike_share_stations.py
```

Save the final reports as `pylint_after.txt`, `bandit_after.txt`, and `flake8_after.txt`. The reports must be generated on your computer; they are not fabricated in this package.

## Required three commits
After copying the fixed Python file and supporting documents into your cloned repo, commit in three separate steps:

```bash
git add bike_share_stations.py
git commit -m "Fix SQL safety and secure PIN generation"

git add bike_share_stations.py
git commit -m "Fix station validation and missing-row handling"

git add bike_share_stations.py issues.md reflection.md
git commit -m "Improve Python style and document static analysis"
```

For an authentic before/after comparison, create the `*_before.txt` reports before replacing the original script. Then generate the `*_after.txt` reports after fixing it.
