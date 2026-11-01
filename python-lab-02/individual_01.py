import sys

def main():
    x = float(input())
    if not 0 <= x <= 1000:
        print('Ошибка: масса вне [0, 1000]', file=sys.stderr)
        return 1
    if x <= 50:
        payment = 0.30 * x
    elif x <= 75:
        payment = 0.50 * x
    elif x <= 90:
        payment = 0.65 * x
    else:
        payment = 0.70 * x + 20
    print(f'Оплата: {payment:.2f} руб.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
