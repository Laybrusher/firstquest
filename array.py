mass_1 = []
volley = input("Введите число ")
volley2 = int(volley)
zero = 0

for volley in range(volley2):
    string = ""
    if volley % 2:
        mass_1.insert(0, volley)
for zero in range(volley2):
    if zero % 2:
        zero = zero * 0
        mass_1.append(zero)

print(mass_1)