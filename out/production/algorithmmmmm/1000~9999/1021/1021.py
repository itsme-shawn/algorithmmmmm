import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
pop_list = list(map(int, sys.stdin.readline().split()))

deq = deque(range(1, n + 1))
cnt = 0

for num in pop_list:
    # 찾는 수 인덱스 찾기
    idx = deq.index(num)
    if idx <= len(deq) // 2:  # 왼쪽으로 rotate
        for _ in range(idx):
            deq.rotate(-1)
            cnt += 1
        deq.popleft()
    else:  # 오른쪽으로 rotate
        for _ in range(len(deq) - idx):
            deq.rotate(1)
            cnt += 1
        deq.popleft()

print(cnt)
