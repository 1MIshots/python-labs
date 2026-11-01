"""Проверка полного вывода программ на заранее рассчитанных примерах."""

import json
from pathlib import Path
import subprocess
import sys


CASES = [
    ("hello.py", "", "Hello, Python!\n"),
    ("zed_example.py", "3\n25.5\n", "Стоимость покупки: 76.50 руб.\n"),
    ("user.py", "Анна\n18\nКазань\n", "Имя: Анна\nВозраст: 18\nГород: Казань\n"),
    ("user.py", "Иван\n0\nОмск\n", "Имя: Иван\nВозраст: 0\nГород: Омск\n"),
    ("user.py", "Елена\n120\nТула\n", "Имя: Елена\nВозраст: 120\nГород: Тула\n"),
    ("arithmetic.py", "350\n", "Правильный ответ: 346\nВаш ответ: 350\n"),
    ("arithmetic.py", "346\n", "Правильный ответ: 346\nВаш ответ: 346\n"),
    ("arithmetic.py", "не знаю\n", "Правильный ответ: 346\nВаш ответ: не знаю\n"),
    ("numbers.py", "1\n2\n3\n5\n", "Результат: 0.38\n"),
    ("numbers.py", "-2.5\n1\n2\n1\n", "Результат: -0.50\n"),
    ("numbers.py", "-3\n3\n1\n1\n", "Результат: 0.00\n"),
    ("individual_01.py", "10\n14\n", "Средний возраст: 12.00\nОтклонение первого возраста: 2.00\nОтклонение второго возраста: 2.00\n"),
    ("individual_01.py", "0\n120\n", "Средний возраст: 60.00\nОтклонение первого возраста: 60.00\nОтклонение второго возраста: 60.00\n"),
    ("individual_01.py", "17\n20\n", "Средний возраст: 18.50\nОтклонение первого возраста: 1.50\nОтклонение второго возраста: 1.50\n"),
    ("individual_01.py", "20\n20\n", "Средний возраст: 20.00\nОтклонение первого возраста: 0.00\nОтклонение второго возраста: 0.00\n"),
    ("individual_02.py", "123321\n", "Модуль разности сумм: 0\n"),
    ("individual_02.py", "100999\n", "Модуль разности сумм: 26\n"),
    ("individual_02.py", "100000\n", "Модуль разности сумм: 1\n"),
    ("individual_02.py", "999999\n", "Модуль разности сумм: 0\n"),
]


def main():
    base = Path(__file__).resolve().parent
    records = []
    for filename, stdin, expected in CASES:
        run = subprocess.run(
            [sys.executable, "-X", "utf8", str(base / filename)],
            input=stdin,
            text=True,
            capture_output=True,
            encoding="utf-8",
            timeout=10,
        )
        passed = run.returncode == 0 and run.stdout == expected and not run.stderr
        records.append({
            "file": filename, "input": stdin, "expected": expected,
            "actual": run.stdout, "stderr": run.stderr,
            "returncode": run.returncode, "passed": passed,
        })
    target = base / "results"
    target.mkdir(exist_ok=True)
    data = {"python": sys.version.split()[0], "checks": records}
    (target / "checks.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    lines = [f"Python {data['python']}"]
    for item in records:
        lines.append(f"{item['file']} | {item['input'].strip()!r} | {'OK' if item['passed'] else 'FAIL'}")
    lines.append(f"Успешно: {sum(item['passed'] for item in records)} из {len(records)}")
    (target / "checks.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(lines[-1])
    if not all(item["passed"] for item in records):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
