# число товарищей
comrades = int(input())

# списки с абсциссами и ординатами, а также суммарная длина между домами
x, y = [], []
dist = 0

# считываем данные
for i in range(comrades):
    a, b = [int(s) for s in input().split()]
    x.append(a)
    y.append(b)

# сортируем списки
x.sort(reverse=True)
y.sort(reverse=True)

# вычисляем суммы длин маршрутов между каждым домом
# умножаем её на 2, так как по одному маршруту проходит два человека (от А до В/от В до А и т.п.)
for j in range(len(x)-1):
    dist += 2*(comrades - 1 - j)*(x[j] + y[j])
    dist -= 2*(j+1)*(x[j+1]+y[j+1])

# итоговую дистанцию делим на число прогулок всех товарищей
print(int(dist//(comrades**2-comrades)))

