from collections import defaultdict
import json
List = []
dict = defaultdict(list)
average_profit = 0
num_of_pofits = 0
with open("part7.txt", encoding='utf-8', mode="r") as f:
    for line in f:
        a, b, c, d = line.split()
        profit = int(c) - int(d)
        if profit > 0:
            average_profit = average_profit + profit
            num_of_pofits = num_of_pofits + 1
        dict[a].append(profit)

print(dict)
List.append(dict)
List.append({"average_profit": average_profit / num_of_pofits})


print(List)

jsonObj = json.dumps(List)

with open("part7_json.txt","w+") as f:
    f.writelines(jsonObj)