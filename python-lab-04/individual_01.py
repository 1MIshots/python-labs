import sys

def main():
    numbers = list(map(int, input().split()))
    if len(numbers) != 10:
        print('Ошибка: требуется 10 чисел', file=sys.stderr)
        return 1
    total = count = 0
    for number in numbers:
        if abs(number) < 3 or number % 9 == 0:
            total += number
            count += 1
    selected = [x for x in numbers if abs(x) < 3 or x % 9 == 0]
    print(f'Сумма: {total}')
    print(f'Количество: {count}')
    print(f'Проверка: {sum(selected)}, {len(selected)}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
