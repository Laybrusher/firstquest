print ("Введите трехзначное число")
n = input()

suma = 0
mult = 1

for digit in n:
    if digit.isdigit():
        suma += int(digit)
        mult *= int(digit)

print("Сумма:", suma)
print("Произведение:", mult)