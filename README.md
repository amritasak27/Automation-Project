# Automation Exercise – Test Automation Portfolio

Two independent Playwright + Python frameworks testing [automationexercise.com](https://automationexercise.com),
built to demonstrate two different automation architectures against the same application under test.

| Framework | Approach | Purpose |
|---|---|---|
| [`bdd-framework/`](./bdd-framework) | BDD with `pytest-bdd` + Gherkin | Stakeholder-readable specs, acceptance-style scenarios |
| [`data-driven-framework/`](./data-driven-framework) | Page Object Model + external data files (JSON/CSV) | Fast, code-first regression suite driven by data sets |

Both frameworks test the same core flows — login, signup, cart & checkout — so you can compare the two
approaches directly. See [`docs/ARCHITECTURE.md`](./docs/ARCHITECTURE.md) for the design patterns used
and why.

## Quick start

```bash
# BDD framework
cd bdd-framework
pip install -r requirements.txt
playwright install
pytest

# Data-driven framework
cd data-driven-framework
pip install -r requirements.txt
playwright install
pytest
```

## CI

GitHub Actions (`.github/workflows/ci.yml`) runs both suites headlessly on every push.

## Why two frameworks?

In real projects the right architecture depends on the audience and the goal:
- **BDD** is chosen when business/QA stakeholders need to read and approve scenarios (Gherkin `Given/When/Then`).
- **Data-driven POM** is chosen for lean, fast regression suites maintained purely by engineers, parameterized
  across many data combinations without duplicating test code.

This repo shows I can build, and choose between, both — and explain the trade-offs.
