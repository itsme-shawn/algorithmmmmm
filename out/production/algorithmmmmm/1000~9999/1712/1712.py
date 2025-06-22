import sys

a, b, c = map(int, sys.stdin.readline().split())
res = -1
if c - b != 0:
    res = int(a / (c - b)) + 1

if res < 0:
    res = -1

print(res)
