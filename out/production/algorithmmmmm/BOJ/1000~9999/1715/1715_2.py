import heapq as hq
import sys

read = sys.stdin.readline

n = int(read())
q = []
for _ in range(n):
    card = int(read())
    hq.heappush(q, card)

res = 0

while len(q) > 1:
    a = hq.heappop(q)
    b = hq.heappop(q)
    total = a + b
    hq.heappush(q, total)
    res += total

print(res)
