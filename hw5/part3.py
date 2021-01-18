rich = []
with open("part3.txt", "r") as f:
    for line in f:
        a, b = line.split()
        if int(b) > 20:
            rich.append(a)
print(rich)
