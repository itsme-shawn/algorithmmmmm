import sys
from collections import deque

read = sys.stdin.readline

n, m = map(int, read().split())
graph = dict()
for i in range(1, n + 1):
    graph[i] = []

for _ in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)
ans = 1

# 연결요소 구하기 (visited 초기화하면 안됨)
for i in range(1, n + 1):  # bfs 시작점 세팅
    # 연결요소의 출발점 찾기
    if visited[i] == 0:
        q = deque()
        q.append(i)
        visited[i] = 1
        num = 0
        # 연결요소들의 모든 노드를 bfs 로 찾기
        while q:
            cur = q.popleft()
            num += 1
            for nxt in graph[cur]:
                if visited[nxt] == 0:
                    visited[nxt] = 1
                    q.append(nxt)
        ans *= num
        ans %= 1000000007

print(ans)
