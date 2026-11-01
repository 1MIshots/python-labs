import sys

def show(records):
    if not records:
        print('Нет записей')
    for i, item in enumerate(records, start=1):
        print(f"{i}. {item['name']} | {item['post']} | {item['year']}")

def main():
    try:
        reference_year = int(input())
    except ValueError:
        print('Ошибка: опорный год', file=sys.stderr)
        return 1
    if not 1 <= reference_year <= 9999:
        print('Ошибка: опорный год', file=sys.stderr)
        return 1
    workers = []
    while True:
        line = input().strip()
        if not line:
            continue
        parts = line.split(maxsplit=1)
        command = parts[0].casefold()
        argument = parts[1] if len(parts) == 2 else ''
        if command == 'exit' and not argument:
            break
        if command == 'add' and not argument:
            name, post, year_text = input().strip(), input().strip(), input()
            try:
                year = int(year_text)
                if not name or not post or not 1 <= year <= reference_year:
                    raise ValueError
            except ValueError:
                print('Ошибка: запись отклонена')
                continue
            workers.append({'name': name, 'post': post, 'year': year})
            workers.sort(key=lambda item: item['name'].casefold())
            print('Добавлено')
        elif command == 'list' and not argument:
            show(workers)
        elif command == 'select':
            try:
                experience = int(argument)
                if experience < 0:
                    raise ValueError
            except ValueError:
                print('Ошибка: нужен неотрицательный стаж')
                continue
            selected = [item for item in workers
                        if reference_year - item['year'] > experience]
            show(selected)
        elif command == 'help' and not argument:
            print('add, list, select N, help, exit')
        else:
            print('Ошибка: неизвестная команда')
    return 0

if __name__ == '__main__':
    sys.exit(main())
