import heapq as hq
import sys

mh = []
n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if not mh:
            print(0)
        else:
            print(hq.heappop(mh)[1])
    else:
        hq.heappush(mh, [-num, num])
