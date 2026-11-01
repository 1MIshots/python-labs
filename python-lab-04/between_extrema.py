import sys

def main():
    numbers = list(map(int, input().split()))
    if not numbers:
        print('Ошибка: пустой список', file=sys.stderr)
        return 1
    minimum = maximum = 0
    for i, number in enumerate(numbers):
        if number < numbers[minimum]:
            minimum = i
        if number > numbers[maximum]:
            maximum = i
    left, right = sorted((minimum, maximum))
    count = 0
    for i in range(left + 1, right):
        if numbers[i] > 0:
            count += 1
    print(f'Индекс минимума: {minimum}')
    print(f'Индекс максимума: {maximum}')
    print(f'Положительных между: {count}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
