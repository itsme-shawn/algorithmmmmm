import math
import sys

sys.setrecursionlimit(10**8)

read = sys.stdin.readline

T = int(read())


for _ in range(T):
    x, y = map(int, read().split())
    end = y - x
    sqrt = math.sqrt(end)
    if sqrt == int(sqrt):
        print(int(sqrt) + (int(sqrt) - 1))
    elif end - (int(sqrt) ** 2) <= int(sqrt):
        print(2 * int(sqrt))
    else:
        print(2 * int(sqrt) + 1)
