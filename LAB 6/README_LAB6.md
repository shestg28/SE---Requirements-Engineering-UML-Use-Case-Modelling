# Lab 6 — Code and Branch Coverage

## Contents
- `shopping_cart.py`: assigned application module (unchanged)
- `CodeCoverageTest_PES1UG24AM261_application.py`: line/code coverage tests
- `BranchCoverageTest_PES1UG24AM261_application.py`: branch-focused tests
- `coverage_evidence/`: text reports from the verified test runs

## Run locally
Install dependencies:
```bash
python -m pip install pytest coverage
```

Run code coverage:
```bash
coverage erase
coverage run --source=shopping_cart -m pytest -q CodeCoverageTest_PES1UG24AM261_application.py
coverage report -m
```

Run branch coverage:
```bash
coverage erase
coverage run --branch --source=shopping_cart -m pytest -q BranchCoverageTest_PES1UG24AM261_application.py
coverage report -m
```

The test files are separate to match the Lab 6 deliverables. The assigned application file is included unchanged.
