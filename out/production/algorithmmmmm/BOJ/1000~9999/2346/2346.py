import sys
from collections import deque

read = sys.stdin.readline

n = int(read())
nums = list(map(int, read().split()))

balloon = deque()
res = []

for i in range(0, n):
    balloon.append((i + 1, nums[i]))

while balloon:
    # print(balloon)
    cur, diff = balloon.popleft()
    res.append(cur)
    if diff > 0:
        balloon.rotate(1 - diff)
    else:
        balloon.rotate(-diff)

print(" ".join(map(str, res)))
