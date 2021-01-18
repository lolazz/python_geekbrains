counter = 0
with open("part1.txt", "r") as my_file:
    while my_file.readline():
        counter = counter + 1
print(counter)
