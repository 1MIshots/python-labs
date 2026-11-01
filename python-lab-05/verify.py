from pathlib import Path
import importlib.util
import json
import os
import re
import subprocess
import sys

BASE = Path(__file__).resolve().parent

def main():
    fixtures = json.loads((BASE / 'fixtures.json').read_text(encoding='utf-8'))
    checks = []
    for case in fixtures:
        if 'sets' in case:
            spec = importlib.util.spec_from_file_location('tested', BASE / case['file'])
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            x, y = module.calculate(*(set(s) for s in case['sets']))
            result = subprocess.CompletedProcess([], 0, f'X: {module.format_set(x)}\nY: {module.format_set(y)}\n', '')
        else:
            result = subprocess.run([sys.executable, str(BASE / case['file'])],
                input=case['input'], text=True, encoding='utf-8', capture_output=True,
                env={**os.environ, 'PYTHONIOENCODING': 'utf-8', 'PYTHONUTF8': '1'}, timeout=10)
        actual = result.stderr if case['error'] else result.stdout
        expected = case['expected']
        match = (all(line in actual.splitlines() for line in expected)
                 if case['contains'] else actual == expected)
        if 'numeric' in case:
            value = float(actual.splitlines()[0].split('=')[1])
            match = abs(value - case['numeric']['target']) <= case['numeric']['tolerance']
        passed = (match and result.returncode == (1 if case['error'] else 0)
                  and not (result.stdout if case['error'] else result.stderr))
        checks.append({**case, 'actual': actual, 'returncode': result.returncode,
                       'stdout': result.stdout, 'stderr': result.stderr, 'passed': passed})
    results = BASE / 'results'
    results.mkdir(exist_ok=True)
    report = {'python': sys.version.split()[0], 'checks': checks,
              'passed': sum(c['passed'] for c in checks), 'total': len(checks)}
    (results / 'checks.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    lines = [f"Python {report['python']}; {report['passed']}/{report['total']}"]
    for case in checks:
        lines.extend([case['file'] + ' | ' + case['label'], 'INPUT: ' + repr(case['input']),
                      'EXPECTED: ' + repr(case['expected']), 'STDOUT: ' + repr(case['stdout']),
                      'STDERR: ' + repr(case['stderr']), 'EXIT: ' + str(case['returncode']),
                      'PASS' if case['passed'] else 'FAIL', ''])
    (results / 'checks.txt').write_text('\n'.join(lines), encoding='utf-8')
    print(lines[0])
    for case in checks:
        if not case['passed']:
            print('FAIL', case['file'], case['label'], repr(case['actual']))
    return 0 if report['passed'] == report['total'] else 1

if __name__ == '__main__':
    sys.exit(main())
