import sys

def main():
    try:
        n = int(input())
    except ValueError:
        print('Ошибка: число записей', file=sys.stderr)
        return 1
    if n < 0:
        print('Ошибка: отрицательное число записей', file=sys.stderr)
        return 1
    mapping = {}
    used_values = set()
    for _ in range(n):
        key_text, value = input(), input().strip()
        try:
            key = int(key_text)
            if not value or key in mapping or value in used_values:
                raise ValueError
        except ValueError:
            print('Ошибка: пара отклонена')
            continue
        mapping[key] = value
        used_values.add(value)
    inverse = {value: key for key, value in mapping.items()}
    print('Исходный:', mapping)
    print('Обратный:', inverse)
    return 0

if __name__ == '__main__':
    sys.exit(main())
