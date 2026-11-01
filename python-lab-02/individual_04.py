import math
import sys

def main():
    x = float(input())
    if not -1 <= x <= 1:
        print('Ошибка: x вне [-1, 1]', file=sys.stderr)
        return 1
    eps = 1e-10
    k = 0
    term = x
    total = term
    while abs(term) > eps:
        if k + 1 >= 1000:
            print('Ошибка: предел членов', file=sys.stderr)
            return 1
        term *= x * x / ((2 * k + 2) * (2 * k + 3))
        k += 1
        total += term
    reference = math.fsum(
        x ** (2 * j + 1) / math.factorial(2 * j + 1)
        for j in range(50)
    )
    print(f'sinh = {total:.10f}')
    print(f'Членов: {k + 1}')
    print(f'Оценка остатка: {abs(term):.3e}')
    print(f'Проверка 50 членов: {reference:.12f}')
    print(f'Расхождение: {abs(total - reference):.3e}')
    print(f'Расхождение с math.sinh: {abs(total - math.sinh(x)):.3e}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
