import subprocess
import sys

result = subprocess.run(
    [sys.executable, "-m", "pytest", "ui/test_ui.py", "-v"],
    check=False
)
raise SystemExit(result.returncode)
