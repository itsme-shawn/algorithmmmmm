import sys

n = int(input())

for i in range(10000001):
    res = i + sum(map(int, list(str(i))))
    if res == n:
        print(i)
        break
    elif i >= n:
        print(0)
        break
else:
    print(0)
