import sys
from collections import deque

read = sys.stdin.readline

n, k = map(int, read().split())
visited = [0] * 100001  # visited 사용안하면 메모리 초과 뜸


def bfs(v):
    deq = deque()
    deq.append(v)
    visited[v] = 1
    cnt = 0
    while deq:
        for _ in range(len(deq)):
            x = deq.popleft()
            if x == k:
                print(cnt)
                sys.exit()
            for nxt in (x - 1, x + 1, x * 2):
                if 0 <= nxt < 100001:  # 범위 설정안하면 반례 생김
                    if visited[nxt] == 0:
                        visited[nxt] = 1
                        deq.append(nxt)
        cnt += 1


bfs(n)
