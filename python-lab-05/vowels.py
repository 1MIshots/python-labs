def main():
    text = input().casefold()
    vowels = set('аеёиоуыэюя')
    found = [character for character in text if character in vowels]
    print(f'Гласных: {len(found)}')
    print('Различные:', sorted(set(found)))

if __name__ == '__main__':
    main()
