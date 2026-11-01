import sys

def main():
    numbers = list(map(float, input().split()))
    if not numbers:
        print('Ошибка: пустой список', file=sys.stderr)
        return 1
    zero_count = 0
    minimum = 0
    for i, number in enumerate(numbers):
        if number == 0:
            zero_count += 1
        if number < numbers[minimum]:
            minimum = i
    total = 0.0
    for number in numbers[minimum + 1:]:
        total += number
    ordered = sorted(numbers, key=abs)
    print('Исходный:', numbers)
    print(f'Нулей: {zero_count}')
    print(f'Первый минимум: {minimum}')
    print(f'Сумма после: {total:.6f}')
    print('По модулю:', ordered)
    return 0

if __name__ == '__main__':
    sys.exit(main())
