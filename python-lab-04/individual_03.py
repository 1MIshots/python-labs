import sys

def main():
    grades = tuple(map(int, input().split()))
    if any(grade not in (2, 3, 4, 5) for grade in grades):
        print('Ошибка: оценки должны быть от 2 до 5', file=sys.stderr)
        return 1
    frequencies = tuple(grades.count(grade) for grade in (2, 3, 4, 5))
    twos, threes, fours, fives = frequencies
    print('Оценки:', grades)
    print('Частоты:', frequencies)
    print(f'Двоек: {twos}; троек: {threes}; четвёрок: {fours}; пятёрок: {fives}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
