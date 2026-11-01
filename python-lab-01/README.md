# Лабораторная работа 1

Основы Python и работа в VS Code и Zed.

## Запуск в Windows

Требуется Python 3.14.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe hello.py
.\.venv\Scripts\python.exe individual_01.py
.\.venv\Scripts\python.exe individual_02.py
```

Вводите каждое значение на отдельной строке. Дробная часть отделяется точкой.

| Файл | Входные данные |
| --- | --- |
| hello.py | Нет |
| zed_example.py | Количество тетрадей, цена одной тетради |
| user.py | Непустое имя, целый возраст 0–120, непустой город |
| arithmetic.py | Непустая строка с ответом |
| numbers.py | a, b, c, d; c + d не равно 0 |
| individual_01.py | Целые x, y от 0 до 120 |
| individual_02.py | Положительное шестизначное целое n |

## VS Code и Zed

Откройте одну и ту же папку проекта в обоих редакторах. В VS Code выполните
`Python: Select Interpreter`, в Zed — `toolchain: select` и выберите
`.venv/Scripts/python.exe`. Для проверки выполните в терминале:

```powershell
.\.venv\Scripts\python.exe -c "import sys; print(sys.executable)"
```

Для отладки `individual_02.py` установите точку останова на строке 5 перед
вычислением `difference`. При вводе `100999` перед этой строкой должны быть
`first_sum = 1`, `last_sum = 27`; после шага — `difference = 26`.
Запустите команду `debugger: start` и выберите текущий файл Python.

## Проверка в VS Code

Проверено в VS Code 1.144.0 и Python.Все проверки verify.py успешно запущены из
VS Code.
