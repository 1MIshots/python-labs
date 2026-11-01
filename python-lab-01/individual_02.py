n = int(input())

first_sum = n // 100000 + n // 10000 % 10 + n // 1000 % 10
last_sum = n // 100 % 10 + n // 10 % 10 + n % 10
difference = abs(first_sum - last_sum)

print(f"Модуль разности сумм: {difference}")
