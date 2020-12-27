def simple_pow(a, b):
    return a ** b


def cycle_pow(a, b):
    multiplicator = a
    for i in range(1, b):
        a = a * multiplicator
    return a


print(5 ** 5)
print(cycle_pow(5, 5))
print(simple_pow(5, 5))
