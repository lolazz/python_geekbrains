import itertools


def nums(a):
    return itertools.count(a)


def repeatEl(a):
    return itertools.cycle(a)


q = 3
num = nums(q)
while q < 10:
    print(next(num))
    q += 1

List = [1, 3, 5]
q = 10
rep = repeatEl(List)
while q < 20:
    print(next(rep))
    q += 1
