# End-to-End Release Quality Program

A portfolio-ready QA operating model demonstrating end-to-end release quality ownership:
requirements traceability → risk-based planning → API/UI validation → regression → defect analytics → release sign-off → production readiness.

> **Portfolio project / simulation:** This repository is intentionally built as a realistic end-to-end QA program using a sample banking-style transaction platform. It demonstrates the workflow, artifacts, automation, analytics, and release decision-making expected from a QA/Quality Engineering role.

## Project goals

- Build requirements traceability from business requirements to tests.
- Score release risk using impact, likelihood, change surface, and detectability.
- Create a risk-based test plan and regression strategy.
- Validate REST APIs with automated tests.
- Validate critical UI flows with Playwright.
- Track defects and calculate release-quality metrics.
- Produce a release-readiness dashboard.
- Make a transparent GO / CONDITIONAL GO / NO-GO release decision.

## Repository structure

```text
End-to-End-Release-Quality-Program/
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── docs/
│   ├── 01_QA_Strategy.md
│   ├── 02_Requirements_Traceability.md
│   ├── 03_Risk_Register.md
│   ├── 04_Test_Plan.md
│   ├── 05_Regression_Strategy.md
│   ├── 06_Release_Readiness.md
│   └── 07_Production_Readiness.md
├── data/
│   ├── requirements.csv
│   ├── test_cases.csv
│   ├── defects.csv
│   └── release_metrics.csv
├── api/
│   ├── app.py
│   └── test_transactions.py
├── ui/
│   ├── app.py
│   └── test_ui.py
├── analytics/
│   ├── defect_analytics.py
│   └── release_dashboard.py
├── reports/
│   └── release_signoff.md
├── scripts/
│   ├── run_api_tests.py
│   ├── run_ui_tests.py
│   └── run_quality_gate.py
└── .github/
    └── workflows/
        └── quality-gate.yml
```

## Quick start

### 1. Create a virtual environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the sample API

```bash
uvicorn api.app:app --reload
```

The API runs at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

### 4. Run API tests

```bash
pytest api/test_transactions.py -v
```

### 5. Run UI

In another terminal:

```bash
streamlit run ui/app.py
```

### 6. Run UI automation

With the Streamlit application running:

```bash
python scripts/run_ui_tests.py
```

The first Playwright run may require:

```bash
playwright install chromium
```

### 7. Run analytics

```bash
python analytics/defect_analytics.py
python analytics/release_dashboard.py
```

### 8. Run the release quality gate

```bash
python scripts/run_quality_gate.py
```

The gate evaluates:

- critical/high severity open defects
- critical requirement coverage
- API pass rate
- UI pass rate
- regression status
- production readiness

## Quality model

The project uses five release gates:

| Gate | Example threshold |
|---|---:|
| Critical requirements covered | 100% |
| Critical/high open defects | 0 critical; high defects require disposition |
| API validation | ≥ 95% |
| UI critical-path validation | 100% |
| Production readiness | All mandatory checks complete |

The final release decision is documented in `reports/release_signoff.md`.

## Suggested GitHub presentation

Use the repository to demonstrate:

1. **QA strategy** — how testing is planned rather than simply executed.
2. **Traceability** — every critical requirement maps to test coverage.
3. **Risk management** — testing effort follows business risk.
4. **Automation** — API and UI checks run through repeatable scripts.
5. **Defect analytics** — defect severity, status, leakage, and aging are measurable.
6. **Release governance** — release decisions are based on explicit quality gates.
7. **Production thinking** — observability, rollback, smoke validation, and incident readiness are considered.

## Important honesty note

Do not describe this as testing a real banking production system unless you actually did so. On a resume, position it as a **portfolio/simulated end-to-end release quality program** if it was built for demonstration.
