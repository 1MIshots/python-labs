import sys

def money(kopecks):
    rubles, remainder = divmod(kopecks, 100)
    return f'{rubles}.{remainder:02d} руб.'

def main():
    try:
        n = int(input())
    except ValueError:
        print('Ошибка: число заказов', file=sys.stderr)
        return 1
    if n < 0:
        print('Ошибка: отрицательное число заказов', file=sys.stderr)
        return 1
    revenue = {}
    for _ in range(n):
        cafe, amount_text = input().strip(), input()
        try:
            amount = int(amount_text)
            if not cafe or amount < 0:
                raise ValueError
        except ValueError:
            print('Ошибка: заказ отклонён')
            continue
        revenue[cafe] = revenue.get(cafe, 0) + amount
    try:
        threshold = int(input())
    except ValueError:
        print('Ошибка: формат порога', file=sys.stderr)
        return 1
    if threshold < 0:
        print('Ошибка: отрицательный порог', file=sys.stderr)
        return 1
    selected = {cafe: total for cafe, total in revenue.items()
                if total > threshold}
    print('Выручка:')
    for cafe in sorted(revenue):
        print(f'{cafe}: {money(revenue[cafe])}')
    print('Выше порога:')
    if not selected:
        print('Совпадений нет')
    for cafe in sorted(selected):
        print(f'{cafe}: {money(selected[cafe])}')
    if revenue:
        maximum = max(revenue.values())
        leaders = sorted(cafe for cafe, total in revenue.items()
                         if total == maximum)
        print('Максимум:', ', '.join(leaders), '|', money(maximum))
    else:
        print('Максимум: Нет данных')
    return 0

if __name__ == '__main__':
    sys.exit(main())
