my_file = open('part1.txt', 'w+')

while True:
    strings = input("ВВодите строки")
    if strings != "":
        my_file.write(strings + '\n')
    else:
        my_file.close()
        break
