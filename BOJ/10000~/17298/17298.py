import sys
from collections import deque

n = int(sys.stdin.readline())
deq = deque(map(int, sys.stdin.readline().split()))
res = []

for i in range(len(deq) - 1):
    cur = deq[i]
    for j in range(i + 1, len(deq)):
        if cur < deq[j]:
            res.append(deq[j])
            break
    else:
        res.append(-1)
res.append(-1)

print(" ".join(map(str, res)))
