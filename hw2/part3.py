month = (input("Введите месяц"))

cleverList = [
    "нет такого", "зима", "зима", "весна", "весна", "весна", "лето", "лето", "лето", "осень", "осень", "осень", "зима",
    "зима", "зима"]

print(cleverList[int(month)])

dictionary = {"зима": [1, 2, 12], "весна": [3, 4, 5], "лето": [6, 7, 8], "осень": [9, 10, 11]}

for k, v in dictionary.items():
    if int(month) in v:
        print(k)