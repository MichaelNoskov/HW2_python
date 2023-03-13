n = int(input())
s = 1
z = 1
for i in range(1, n + 1):
    # Факториал числа - это факториал предыдущего числа, умноженный на само это число. Факториал 1 = 1, поэтому с него и начинаем.
    # Альтернативным, но более объёмозатратным вариантом является:
    # z *= i
    # s += 1/z
    # P.S. это я просто объяснил принцип работы строчки ниже. Она выполняет два действия выше за одно.
    z = z / i
    s += z
print(round(s, 5))
