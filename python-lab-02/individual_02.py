import sys

def main():
    x = int(input())
    y = int(input())
    if x < 1 or y < 1:
        print('Ошибка: нужны натуральные числа', file=sys.stderr)
        return 1
    if x % y == 0:
        print('Делится')
    else:
        print('Не делится')
    return 0

if __name__ == '__main__':
    sys.exit(main())
