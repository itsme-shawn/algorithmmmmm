import sys
read = sys.stdin.readline

K,L = map(int, read().split())
nums = []
for _ in range(L):
    nums.append(read().rstrip())

dic = dict()
cnt = 1

for num in nums:
    dic[num] = cnt
    cnt += 1

items = list(dic.items())
items.sort(key=lambda x : x[1])

if len(items) < K:
    for key,val in items:
        print(key)
else:
    for i in range(K):
        print(items[i][0])
