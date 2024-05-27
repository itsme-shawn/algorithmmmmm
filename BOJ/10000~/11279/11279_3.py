import heapq as hq
import sys

read = sys.stdin.readline

lst = []

hq.heapify(lst)

n = int(read())

for _ in range(n):
    x = int(read())

    if x:
        hq.heappush(lst, -x)
    else:
        if not lst:
            print(0)
        else:
            print(-hq.heappop(lst))
