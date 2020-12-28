from functools import reduce

List = [x for x in range(100, 1001) if x % 2 == 0]
res = 1
for x in List:
    res = res * x

print(res)
print(reduce(lambda x, y: x * y, List))
