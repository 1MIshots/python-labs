import sys

def main():
    text = input()
    length = int(input())
    if (not text or text.startswith(' ') or text.endswith(' ')
            or any(c.isspace() and c != ' ' for c in text)):
        print('Ошибка: формат строки', file=sys.stderr)
        return 1
    words = text.split()
    if len(words) < 2 or not len(text) <= length <= 10000:
        print('Ошибка: слова или длина', file=sys.stderr)
        return 1
    letters = 0
    for word in words:
        letters += len(word)
    gap_count = len(words) - 1
    base, extra = divmod(length - letters, gap_count)
    parts = []
    for i, word in enumerate(words):
        parts.append(word)
        if i < gap_count:
            parts.append(' ' * (base + (i < extra)))
    result = ''.join(parts)
    print(repr(result))
    print(f'Длина: {len(result)}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
