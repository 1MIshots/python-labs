import sys

def main():
    n = int(input())
    if n <= 0:
        print('Ошибка: n должно быть положительным', file=sys.stderr)
        return 1
    readings = []
    for _ in range(n):
        name = input().strip()
        temperature = float(input())
        readings.append((name, temperature))
    average = sum(item[1] for item in readings) / n
    selected = [item for item in readings if item[1] > average]
    ordered = sorted(selected, key=lambda item: item[1], reverse=True)
    print(f'Средняя: {average:.2f}')
    if not ordered:
        print('Нет показаний выше средней')
    for name, temperature in ordered:
        print(f'{name}: {temperature:.2f}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
