import sys

def main():
    numbers = list(map(int, input().split()))
    if len(numbers) != 10:
        print('Ошибка: требуется 10 чисел', file=sys.stderr)
        return 1
    total = 0
    for number in numbers:
        if abs(number) < 5:
            total += number
    check = sum(number for number in numbers if abs(number) < 5)
    print(f'Сумма: {total}')
    print(f'Проверка: {check}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
