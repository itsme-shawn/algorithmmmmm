import sys
from collections import deque

read = sys.stdin.readline

n, m, v = map(int, read().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    i, j = map(int, read().split())
    graph[i][j] = 1
    graph[j][i] = 1


def dfs(v):
    visited[v] = 1  # 현재노드 방문처리
    res.append(v)
    for i in range(1, n + 1):
        if graph[v][i] == 1:  # 인접노드일때만
            if visited[i] == 0:  # 미방문노드일때만
                dfs(i)


def bfs(v):
    q = deque([v])  # 시작노드 큐에 추가
    visited[v] = 1  # 방문처리
    res.append(v)
    while q:
        x = q.popleft()  # 노드하나 pop
        for i in range(1, n + 1):
            if graph[x][i] == 1:  # 인접노드일때만
                if visited[i] == 0:  # 미방문노드일때만
                    visited[i] = 1
                    res.append(i)
                    q.append(i)


visited = [0] * (n + 1)
res = []
dfs(v)
print(" ".join(map(str, res)))

visited = [0] * (n + 1)
res = []
bfs(v)
print(" ".join(map(str, res)))
