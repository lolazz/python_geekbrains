lines = input("Введите строки")
stringList = list(lines.split(' '))

num = 0
for x in stringList:
    print(f'{num}:', x[:10])
    num = num + 1
