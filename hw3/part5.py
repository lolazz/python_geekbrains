Sum = 0
while True:
    nums = input("enter space separated nums")
    int_nums = list(map(str, nums.split()))
    cleaned = [int(x) for x in int_nums if x.isdigit()]
    Sum = Sum + sum(cleaned)
    print(Sum)
    if '~' in nums:
        break
