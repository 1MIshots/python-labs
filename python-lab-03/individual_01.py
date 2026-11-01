def main():
    text = input()
    positions = []
    for position, character in enumerate(text, start=1):
        if position % 2 == 0 and character == 'и':
            positions.append(position)
    if positions:
        for position in positions:
            print(position)
    else:
        print('Не найдено')

if __name__ == '__main__':
    main()
