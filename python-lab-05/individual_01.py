import string

U = set(string.ascii_lowercase)

def calculate(a, b, c, d):
    if not (a | b | c | d) <= U:
        raise ValueError('Элемент вне универсума')
    x = (a - b) & (c | d)
    y = ((U - a) & (U - b)) - (c | d)
    return x, y

def format_set(values):
    return str(sorted(values)) if values else '∅'


def main():
    a, b = set('abgkmp'), set('beflr')
    c, d = set('klwx'), set('ejopquv')
    x, y = calculate(a, b, c, d)
    print('X:', format_set(x))
    print('Y:', format_set(y))

if __name__ == '__main__':
    main()
