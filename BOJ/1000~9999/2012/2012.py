import sys

N = int(sys.stdin.readline())
sum = 0

lst = [int(sys.stdin.readline()) for _ in range(N)]

lst.sort()

for i in range(len(lst)):
    sum += abs(i + 1 - lst[i])

print(sum)
