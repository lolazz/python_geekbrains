part5_nums = open('part5_nums.txt', 'w+')
for i in range(0, 10):
    part5_nums.write(str(i) + ' ')
part5_nums.close()

with open('part5_nums.txt', "r") as f:
    nums = sum(map(int, f.readline().split()))

print(nums)
