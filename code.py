print("Введите трехзначеное число")
n = int(input())

total = 0
mult = 1

while n > 0:
    digit = n % 10
    if digit != 0:
        total += digit
        mult *= digit
    n = n // 10

print("Сумма:", total)
print("Произведение:", mult)