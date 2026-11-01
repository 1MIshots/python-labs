import sys

def main():
    n = int(input())
    if not 1 <= n <= 100000:
        print('Ошибка: n вне [1, 100000]', file=sys.stderr)
        return 1
    divisors = []
    for k in range(1, n + 1):
        if n % k == 0:
            divisors.append(k)
    print('Делители:', *divisors)
    return 0

if __name__ == '__main__':
    sys.exit(main())
