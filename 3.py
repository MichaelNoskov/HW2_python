amount = 0
summa = 0
# Пока вводимое пользователем число не равняется нулю, мы прибавляем его к общей сумме, а счётчик количества итераций
# увеличивается на 1
while (n := int(input())) != 0:
    summa += n
    amount += 1
# Выводим высчитанное по формуле среднее арифметическое
print(summa/amount)