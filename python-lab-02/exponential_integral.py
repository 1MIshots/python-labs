import math
import sys

def main():
    x = float(input())
    if not 0.1 <= x <= 1:
        print('Ошибка: x вне [0.1, 1]', file=sys.stderr)
        return 1
    eps = 1e-10
    term = x
    total = term
    k = 1
    while abs(term) / 3 > eps:
        if k >= 1000:
            print('Ошибка: предел членов', file=sys.stderr)
            return 1
        term *= x * k / (k + 1) ** 2
        k += 1
        total += term
    result = 0.5772156649015329 + math.log(x) + total
    print(f'Ei = {result:.10f}')
    print(f'Членов: {k}')
    print(f'Оценка остатка: {abs(term) / 3:.3e}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
