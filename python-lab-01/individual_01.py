x = int(input())
y = int(input())

average_age = (x + y) / 2
deviation_x = abs(x - average_age)
deviation_y = abs(y - average_age)

print(f"Средний возраст: {average_age:.2f}")
print(f"Отклонение первого возраста: {deviation_x:.2f}")
print(f"Отклонение второго возраста: {deviation_y:.2f}")
