import math
import sys

def main():
    n = int(input())
    x = float(input())
    if not (0 <= n <= 10000 and 0 < x <= 100):
        print('Ошибка: недопустимые n или x', file=sys.stderr)
        return 1
    total = 0.0
    for k in range(1, n + 1):
        total += math.log(k * x) / k ** 2
    print(f'S = {total:.10f}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
