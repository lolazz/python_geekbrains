import datetime

str1 = input("Введите ваше Имя: ")
print(f'Прекрасно выглядите, {str1}')

nums = input("Введите пару-тройку целых чисел через пробел")
numbers = list(map(int, nums.split()))
print(f'Вы ввели {numbers}, вы такой молодец')

timeInSeconds = int(input("Давайте я преведу ваши секудны куда-нибудь?"))
seconds = timeInSeconds % 60
minutes = ((timeInSeconds) // 60) % 60
hours = timeInSeconds // 3600
print(
    f'В ваших секундах вот столько по версии timedelta {datetime.timedelta(seconds=float(timeInSeconds))},\n'
    f' а по моей вот столько : {hours:02}:{minutes:02}:{seconds:02}')

multiplicator = input("Введите множитель от 0 до 9")
multiplicator = int(multiplicator)
print(multiplicator + multiplicator * 11 + multiplicator * 111)

num = (input("Введите целое положительно число и мы найдем вам в нём самую большую цифру:"))
intNum = int(num)
a = len(num)
biggestNum = 0
while a > 0:
    a = a - 1
    qwe = (intNum // (10 ** a))
    biggestNum = max(qwe, biggestNum)
    intNum = intNum % (10 ** a)

print(f"Самая большая цифра в числе была{biggestNum}")

profit = float(input("Введите выручку вашей конторы"))
costs = float(input("Введите издержки вашей конторы"))

if profit > costs:
    print(
        f"А выручка то у вас больше издержек, вы в плюсе! "
        f"Рентабельность: {((profit - costs) / profit) * 100:10.4f} процентов")
    employeesCount = int(input("Сколько человек работает?"))
    print(f"один человек вам приносит {((profit - costs) / employeesCount)}")

elif costs > profit:
    print("Да у вас издержки больше выручки!")
else:
    print("Вы или в ноль работаете или не то чёто ввели")

aims = input("Введите сколько пробегаете км и сколько ходите пробегать через пробел")
numbers = list(map(float, aims.split()))
result = numbers[0]
day = 1
while result < (numbers[1]):
    result = result * 1.1
    day = day + 1
print(f'Вы добежите на {day} день')
