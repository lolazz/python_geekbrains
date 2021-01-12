List = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
dedup = list(dict.fromkeys(List))
print(dedup)
uniqueList = set()
dedup = [x for x in List if x not in uniqueList and (uniqueList.add(x) or True)]
print(dedup)
