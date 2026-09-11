from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
metrics = pd.read_csv(ROOT / "data" / "release_metrics.csv")
defects = pd.read_csv(ROOT / "data" / "defects.csv")

critical_open = len(defects[(defects.severity == "Critical") & (defects.status == "Open")])
high_open = len(defects[(defects.severity == "High") & (defects.status == "Open")])

print("=== END-TO-END RELEASE QUALITY GATE ===")

checks = {
    "Critical requirements coverage": float(metrics.loc[metrics.metric == "requirements_critical_coverage", "value"].iloc[0]) >= 100,
    "API pass rate": float(metrics.loc[metrics.metric == "api_pass_rate", "value"].iloc[0]) >= 95,
    "Critical UI path": float(metrics.loc[metrics.metric == "ui_critical_path_pass_rate", "value"].iloc[0]) >= 100,
    "No open critical defects": critical_open == 0,
    "No unresolved high defects": high_open == 0,
    "Production readiness": float(metrics.loc[metrics.metric == "production_readiness", "value"].iloc[0]) >= 100,
}

for name, passed in checks.items():
    print(f"[{'PASS' if passed else 'REVIEW'}] {name}")

if all(checks.values()):
    print("\nRELEASE DECISION: GO")
elif checks["No open critical defects"]:
    print("\nRELEASE DECISION: CONDITIONAL GO / REVIEW")
else:
    print("\nRELEASE DECISION: NO-GO")

print("\nNote: a failed gate is intentionally visible so release sign-off is evidence-based.")
