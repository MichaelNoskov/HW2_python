# Самое первое число вне конкуренции - оно в самом начале будет максимальным
max_ = int(input())
amount = 1
while (n := int(input())) != 0:
    # Если мы нашли ещё одно число, равное максимальному, то увеличиваем количество максимальных чисел на 1
    if n == max_:
        amount += 1
    # Если введённое число является больше всех предыдущих, то количество максимальных стаёт равно 1,
    # а максимальное число перезаписывается
    elif n > max_:
        amount = 1
        max_ = n
print(amount)
