import sys
from collections import deque

read = sys.stdin.readline

n, k = map(int, read().split())
dist = [0] * 100001  # 시작노드부터의 거리 ( bfs 레벨)


def bfs(v):
    deq = deque()
    deq.append(v)
    while deq:
        x = deq.popleft()
        if x == k:
            print(dist[k])
            sys.exit()
        for nxt in (x - 1, x + 1, x * 2):
            if 0 <= nxt < 100001:  # 범위 설정안하면 반례 생김
                if dist[nxt] == 0:
                    dist[nxt] = dist[x] + 1
                    deq.append(nxt)


bfs(n)
