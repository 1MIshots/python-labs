def main():
    total = 0
    while True:
        number = int(input())
        if number == 0:
            break
        if number < 0:
            continue
        total += number
    print(f'Сумма: {total}')

if __name__ == '__main__':
    main()
