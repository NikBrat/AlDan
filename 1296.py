# считываем число элементов
counter = int(input())

# потенциал
potential = 0
# возможный потенциал
probable = 0

for i in range(counter):
    # прибавляем новое число
    probable += int(input())
    # если сумма стала отрицательной, то нет смысла копить числа, обнуляем возможный потенциал
    if probable < 0:
        probable = 0
    # если смогли набрать сумму, большую потенциала, то присваиваем потенциалу эту сумму
    if probable > potential:
        potential = probable

# печатаем итоговый потенциал
print(potential)
