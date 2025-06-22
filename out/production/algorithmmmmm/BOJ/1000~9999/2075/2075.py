import heapq as hq
import sys

n = int(sys.stdin.readline())

# 메모리 초과 때문에 리스트에 미리 받아놓지 않고, 한 번에 한 줄씩만 입력받음
minheap = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    minheap += list(map(int, sys.stdin.readline().split()))  # 힙에 다음 row 하나 더 추가함
    hq.heapify(minheap)  # minheapify
    for _ in range(n):
        hq.heappop(minheap)  # 작은 순으로 n개 pop

print(hq.heappop(minheap))  # 현재 minheap 의 root 가 n번째큰수
