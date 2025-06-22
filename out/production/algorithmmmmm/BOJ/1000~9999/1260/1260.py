import sys
from collections import deque

read = sys.stdin.readline

n, m, v = map(int, read().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    i, j = map(int, read().split())
    graph[i].append(j)
    graph[j].append(i)

# 정렬(작은 정점부터 방문하기위함)
for k in range(n + 1):  # n+1 로 해야함!
    graph[k].sort()


def dfs(v):
    visited[v] = 1  # 현재노드 방문처리
    res.append(v)
    for node in graph[v]:  # 현재노드의 인접노드들 확인
        if visited[node] == 0:  # 인접노드가 방문하지 않은 노드일때만 dfs
            dfs(node)


def bfs(v):
    q = deque([v])  # 시작노드 큐에 추가
    visited[v] = 1  # 방문처리
    res.append(v)
    while q:
        x = q.popleft()  # 노드하나 pop
        for node in graph[x]:  # pop한 노드의 인접노드들 확인
            if visited[node] == 0:  # 인접노드가 방문하지 않은 노드일때만 큐에 추가
                visited[node] = 1  # 인접노드 방문처리
                res.append(node)
                q.append(node)  # 큐 추가


visited = [0] * (n + 1)
res = []
dfs(v)
print(" ".join(map(str, res)))

visited = [0] * (n + 1)
res = []
bfs(v)
print(" ".join(map(str, res)))
