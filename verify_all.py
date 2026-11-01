from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
codes = []
for number in range(1, 6):
    folder = root / f'python-lab-{number:02}'
    print(f'Lab {number}', flush=True)
    result = subprocess.run([sys.executable, 'verify.py'], cwd=folder)
    codes.append(result.returncode)
sys.exit(0 if not any(codes) else 1)
