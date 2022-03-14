import sys
from collections import deque

read = sys.stdin.readline

n, m = map(int, read().split())
graph = {}

for i in range(1, n + 1):
    graph[i] = []

for _ in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)
cnt = 0

# 모든 노드돌면서 bfs 시작점 찾기
for i in range(1, n + 1):
    q = deque()
    # 방문하지 않은 노드만 bfs의 시작점(연결요소의 시작점)이 될 수 있음
    if visited[i] == 0:
        visited[i] = 1
        q.append(i)
        cnt += 1
        # bfs 로 연결요소의 모든 노드 찾기
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                if visited[nxt] == 0:
                    visited[nxt] = 1
                    q.append(nxt)

print(cnt)
