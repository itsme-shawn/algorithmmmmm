import sys
import heapq as hq
# sys.stdin = open("in.txt", "r")
read = sys.stdin.readline

heap = []

n = int(read())
nums = []
for _ in range(n):
    nums.append(int(read()))

for num in nums:
    if num:
        hq.heappush(heap, (abs(num),num))
    else:
        if heap:
            print(hq.heappop(heap)[1])
        else:
            print(0)

# 파이썬 우선순위 큐 커스텀하는내용도 추가
