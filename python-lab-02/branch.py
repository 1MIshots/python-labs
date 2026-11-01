import math
import sys

def main():
    x = float(input())
    if not -100 <= x <= 100:
        print('Ошибка: x вне [-100, 100]', file=sys.stderr)
        return 1
    if x <= 0:
        y = 2 * x ** 2 + math.cos(x)
    elif x < 5:
        y = x + 1
    else:
        y = math.sin(2 * x) - x ** 2
    print(f'y = {y:.6f}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
