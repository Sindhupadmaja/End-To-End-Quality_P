from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
metrics = pd.read_csv(ROOT / "data" / "release_metrics.csv")

print("=== Release Quality Dashboard ===")
for _, row in metrics.iterrows():
    state = "PASS" if bool(row["pass"]) else "FAIL"
    print(f"{row['metric']}: {row['value']} (target {row['target']}) [{state}]")

failed = metrics[metrics["pass"] == False]
print()
if failed.empty:
    print("Overall release gate: GO")
else:
    print("Overall release gate: CONDITIONAL GO / REVIEW")
    print("Failed or exception metrics:")
    for metric in failed["metric"]:
        print(f" - {metric}")
