import subprocess
import sys

result = subprocess.run(
    [sys.executable, "-m", "pytest", "api/test_transactions.py", "-v"],
    check=False
)
raise SystemExit(result.returncode)
