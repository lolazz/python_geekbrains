def divide(a, b):
    try:
        return int(a) / int(b)
    except ZeroDivisionError:
        print("ну зачем на ноль тооооооооо")


a, b = input("Введите два числа через пробел").split()
print(divide(a, b))
