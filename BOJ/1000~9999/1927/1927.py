import sys

import heapq as hq

read = sys.stdin.readline

N = int(read())

heap = []

for _ in range(N):
    x = int(read())
    
    if x > 0:
        hq.heappush(heap, x)
    elif x == 0:
        if heap:
            print(hq.heappop(heap))
        else:
            print(0)