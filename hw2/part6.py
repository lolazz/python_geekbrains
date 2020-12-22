from collections import defaultdict

a = ((1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
     (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
     (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."}))

analyticsDictionary = defaultdict(list)
for k1,v1 in a:
    for k, v in v1.items():
        if v not in analyticsDictionary[k]:
            analyticsDictionary[k].append(v)
print(analyticsDictionary)


# для ручного ввода тоже сделал, но смысла не оч понял, если честно
num = int(input("Введите количество товаров"))
goods = []
for i in range(0, num):
    newLine = input("введите название, цену, количество и единицу измерения через пробел")
    stringList = list(newLine.split(' '))
    goods.append({"название": stringList[0], "цена": int(stringList[1]), "количество": int(stringList[2]),
                  "eд": stringList[3]})
analyticsDictionary = defaultdict(list)
for k1 in goods:
    for k, v in k1.items():
        if v not in analyticsDictionary[k]:
            analyticsDictionary[k].append(v)

print(analyticsDictionary)
