x = 0
y = 0
d = False
# Получаем первое значение
previous_n = int(input())
while (n := int(input())) != 0:
    # Если следующее значение отличается от предыдущего, то счётчик x фиксирует это (увеличивает длину на 1)
    if (n > previous_n and d == True) or (n < previous_n and d == False):
        x += 1
    # Если значение отличается, но до этого уменьшались числа, а сейчас увеличиваются (или наоборот), то последовательность = 1
    elif n > previous_n and x > y:
        d = True
        y = x
        x = 1
    elif n > previous_n:
        d = True
        x = 1
    elif n < previous_n and x > y:
        d = False
        y = x
        x = 1
    elif n < previous_n:
        d = False
        x = 1
    # Если значение сохраняется, то просто сравниваем длину монотонности с максимальной до этого
    elif n == previous_n and x > y:
        y = x
        x = 0
    elif n == previous_n:
        x = 0
    
    previous_n = n
if x > y:
    y = x
print(y+1)
