def main():
    first, second = input(), input()
    print('Общие:', sorted(set(first) & set(second)))

if __name__ == '__main__':
    main()
