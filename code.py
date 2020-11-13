n = int(input())

total = 0
mult = 1

while n > 0:
    digit = n % 10
    total = total + digit
    mult = mult * digit
    n = n // 10

print("Сумма:", total)
print("Произведение:", mult)