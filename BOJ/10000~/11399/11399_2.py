import sys

n = int(input())
time = list(map(int, input().split()))
time.sort()
result = 0
for i in range(n):
    total = 0
    for j in range(i + 1):
        total += time[j]
    result += total

print(result)
