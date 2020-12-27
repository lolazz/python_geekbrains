def mu_func(a):
    return sorted(a, reverse=True)[0:2]


a, b = mu_func((0, 20, 4, 34, 55, 23, 123, 234, 123, 12, 3))

print(a, b)
