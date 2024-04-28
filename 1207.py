# считываем количество точек
n = int(input())
# создаем массивы для точек, значений тангенса
points = []
tg = []
# значения координат, а также индекс ближайшей к (0,0) точки
minx = 1000000
miny = 1000000
min_i = 0

for i in range(n):
    # считываем данные
    x, y = ([int(s) for s in input().split(" ")])
    points.append([x, y])
    # находим координаты и индекс ближайшей к началу отсчёта точки
    if x < minx or x == minx and y < miny:
        minx = x
        miny = y
        min_i = i

for i in range(n):
    # вычисляем значения тангенса
    if i == min_i:
        # случай начальной точки
        continue
    elif points[i][0] == minx:
        # случай 90 градусов
        tg.append([10000000, i + 1])
    else:
        # остальные случаи
        tg.append([(points[i][1] - miny) / (points[i][0] - minx), i + 1])

# сортируем список по значениям тангенса угла наклона
tg.sort(key=lambda j: j[0])
# выводим номер начальной и медианной точек
print(min_i + 1, tg[(n - 1) // 2][1])
