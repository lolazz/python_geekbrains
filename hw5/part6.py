from collections import defaultdict

dict = defaultdict(list)
b = []
with open("part6.txt", encoding='utf-8', mode="r") as f:
    for line in f:
        a, b = line.split(':')
        b = b.split()
        summ = 0
        for v in b:
            v = ''.join(c for c in v if c.isdigit())
            if v !='':
                summ = summ + int(v)
        dict[a].append(summ)
print(dict)
