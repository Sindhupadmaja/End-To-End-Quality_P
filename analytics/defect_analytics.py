from pathlib import Path
import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "data" / "defects.csv"
df = pd.read_csv(DATA)

print("=== Defect Analytics ===")
print(f"Total defects: {len(df)}")
print(f"Open defects: {(df.status == 'Open').sum()}")
print(f"Critical defects: {(df.severity == 'Critical').sum()}")
print(f"High defects: {(df.severity == 'High').sum()}")
print(f"Production leakage: {(df.release_leakage == 'Yes').sum()}")

print("\nDefects by severity:")
print(df.groupby("severity").size().sort_values(ascending=False))

print("\nDefects by area:")
print(df.groupby("area").size().sort_values(ascending=False))

print("\nAverage defect age by severity:")
print(df.groupby("severity")["age_days"].mean().round(1))
