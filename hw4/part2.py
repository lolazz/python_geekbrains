List = (100, 2, 3, 4, 5, 6, 7, 4, 234, 234, 234, 23, 42, 35, 67, 5687, 456, 23)
result = [x for index, x in enumerate(List) if index > 0 and x > List[index - 1]]
print(result)
List = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([x for index, x in enumerate(List) if index > 0 and x > List[index - 1]])