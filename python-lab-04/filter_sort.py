def main():
    numbers = list(map(int, input().split()))
    nonnegative = [number for number in numbers if number >= 0]
    ordered = sorted(nonnegative, reverse=True)
    print('Исходный:', numbers)
    print('Неотрицательные:', nonnegative)
    print('По убыванию:', ordered)

if __name__ == '__main__':
    main()
