import math
import sys

def main():
    a = float(input())
    if not 0 <= a <= 1e6:
        print('Ошибка: a вне [0, 1000000]', file=sys.stderr)
        return 1
    x = max(1.0, a)
    iterations = 0
    if a == 0:
        x = 0.0
    else:
        while iterations < 1000:
            previous = x
            x = (previous + a / previous) / 2
            iterations += 1
            if abs(x - previous) <= 1e-10:
                break
        else:
            print('Ошибка: предел итераций', file=sys.stderr)
            return 1
    print(f'Корень: {x:.12f}')
    print(f'Итераций: {iterations}')
    print(f'Расхождение: {abs(x - math.sqrt(a)):.3e}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
