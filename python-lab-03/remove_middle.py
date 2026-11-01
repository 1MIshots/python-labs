import sys

def main():
    word = input()
    if not word:
        print('Ошибка: пустое слово', file=sys.stderr)
        return 1
    middle = len(word) // 2
    left = middle if len(word) % 2 else middle - 1
    result = word[:left] + word[middle + 1:]
    print(repr(result))
    return 0

if __name__ == '__main__':
    sys.exit(main())
