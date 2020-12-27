list = list(input("введите список"))

print(list)
i = 0
while i < (len(list) - 1):
    list[i], list[i + 1] = list[i + 1], list[i]
    i = i + 2

print(list)
