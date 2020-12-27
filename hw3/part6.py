def int_func(line):
    return str(line).capitalize()


print(int_func("text"))
line = "we are the champignons"
words = line.split()
result = [int_func(x) for x in words]
print(result)
