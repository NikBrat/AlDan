# количество типов знаков
type_amount = int(input())

# ассортимент и количество промежутков
sign_assortment = [int(s) for s in input().split()]
gap = max(sign_assortment)

mx_id = 0

# последовательность
order = []

for i in range(type_amount):
    # для случая, когда мы расставили все знаки между промежутками или для первой расстановка
    if i == 0 or sign_assortment[mx_id] == 0:
        mx_id = sign_assortment.index(max(sign_assortment))
    gp = gap
    # ставим знаки одного типа через 1, 2, 3 ... знаков
    j = i + 1
    # начальный индекс для постановки знаков
    index = i
    # расставляем знаки в промежутках
    while gp and sum(sign_assortment):
        # постановка знака
        sign_assortment[mx_id] -= 1
        order.insert(index, mx_id+1)
        # уменьшаем оставшиеся промежутки и переходим к следующему индексу
        gp -= 1
        index += j
        # если знаки одного типа закончились, но не все промежутки закончились, то берем новые знаки
        if not sign_assortment[mx_id]:
            mx_id = sign_assortment.index(max(sign_assortment))

# выводим результат
print(*order)
