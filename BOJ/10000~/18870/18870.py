import sys
# sys.stdin = open("in.txt", "r")
read = sys.stdin.readline

n = int(read())
nums = list(map(int, read().split()))

sorted_nums = sorted(set(nums))

dic = dict()

for i,sn in enumerate(sorted_nums):
    if sn not in dic:
        dic[sn] = i

for num in nums:
    print(dic[num], end=" ")

