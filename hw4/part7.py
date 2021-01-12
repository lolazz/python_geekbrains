def fact(n):
    val = 1
    for x in range(1, n + 1):
        yield val
        val = val * (x + 1)


for el in fact(10):
    print(el)
