from datetime import date
import sys

def parse_birth(text, reference_year):
    parts = text.split('.')
    if (len(parts) != 3 or [len(part) for part in parts] != [2, 2, 4]
            or not all(part.isascii() and part.isdigit() for part in parts)):
        raise ValueError
    day, month, year = map(int, parts)
    date(year, month, day)
    if year > reference_year:
        raise ValueError
    return [day, month, year]

def show(records):
    if not records:
        print('Нет записей')
    for i, item in enumerate(records, start=1):
        day, month, year = item['birth']
        print(f"{i}. Имя: {item['name']} | Телефон: {item['phone']} | "
              f'Дата рождения: {day:02d}.{month:02d}.{year:04d}')

def main():
    try:
        reference_year = int(input())
    except ValueError:
        print('Ошибка: опорный год', file=sys.stderr)
        return 1
    if not 1 <= reference_year <= 9999:
        print('Ошибка: опорный год', file=sys.stderr)
        return 1
    people = []
    while True:
        line = input().strip()
        if not line:
            continue
        parts = line.split(maxsplit=1)
        command = parts[0].casefold()
        argument = parts[1].strip() if len(parts) == 2 else ''
        if command == 'exit' and not argument:
            break
        if command == 'add' and not argument:
            name, phone, birth_text = input().strip(), input().strip(), input().strip()
            try:
                if (len(name.split()) < 2 or len(phone) < 3
                        or not phone.isascii() or not phone.isdigit()):
                    raise ValueError
                birth = parse_birth(birth_text, reference_year)
            except ValueError:
                print('Ошибка: запись отклонена')
                continue
            people.append({'name': name, 'phone': phone, 'birth': birth})
            people.sort(key=lambda item: item['phone'][:3])
            print('Добавлено')
        elif command == 'list' and not argument:
            show(people)
        elif command == 'select' and argument:
            selected = [item for item in people
                        if item['name'].split()[0].casefold() == argument.casefold()]
            show(selected)
        elif command == 'help' and not argument:
            print('add, list, select ФАМИЛИЯ, help, exit')
        else:
            print('Ошибка: неизвестная команда')
    return 0

if __name__ == '__main__':
    sys.exit(main())
