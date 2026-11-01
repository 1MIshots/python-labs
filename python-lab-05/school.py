import sys

def read_record():
    label, count_text = input().strip(), input()
    count = int(count_text)
    if not label or count < 0:
        raise ValueError
    return label, count

def main():
    try:
        n = int(input())
    except ValueError:
        print('Ошибка: число записей', file=sys.stderr)
        return 1
    if n < 0:
        print('Ошибка: отрицательное число записей', file=sys.stderr)
        return 1
    school = {}
    for _ in range(n):
        try:
            label, count = read_record()
            if label in school:
                raise ValueError
            school[label] = count
        except ValueError:
            print('Ошибка: начальная запись отклонена')
    try:
        label, count = read_record()
        if label not in school:
            raise ValueError
        school[label] = count
    except ValueError:
        print('Ошибка: изменение отклонено')
    try:
        label, count = read_record()
        if label in school:
            raise ValueError
        school[label] = count
    except ValueError:
        print('Ошибка: добавление отклонено')
    label = input().strip()
    if label in school:
        del school[label]
    else:
        print('Ошибка: удаление отклонено')
    for label in sorted(school):
        print(f'{label}: {school[label]}')
    print(f'Всего учеников: {sum(school.values())}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
