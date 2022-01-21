import heapq as hq
import sys

n = int(sys.stdin.readline())

# 메모리 초과 때문에 리스트에 미리 받아놓지 않고, 한 번에 한 줄씩만 입력받음
maxheap = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    maxheap += list(map(int, sys.stdin.readline().split()))  # 힙에 다음 row 하나 더 추가함
    hq.heapify(maxheap)  # maxheapify
    maxheap.sort(reverse=True)
    for _ in range(n):
        maxheap.pop()  # 작은 순으로 n개 pop

maxheap.sort(reverse=True)
print(maxheap.pop())  # 현재 maxheap 의 마지막노드가 n번째 큰 수
