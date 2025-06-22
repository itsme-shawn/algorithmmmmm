# 2차원배열로 그래프구현 시 메모리초과남

import sys
from collections import deque

read = sys.stdin.readline

n, m = map(int, read().split())  # n : 학생수(노드수), m : 비교횟수(간선 수)

graph = [[0] * (n + 1) for _ in range(n + 1)]  # 그래프
in_degree = [0] * (n + 1)  # 각 노드들의 진입차수

# 그래프와 진입차수 생성
for _ in range(m):
    a, b = map(int, read().split())
    graph[a][b] = 1
    in_degree[b] += 1

q = deque()
res = []

# 초기 큐 세팅 (진입차수가 0인 노드들 큐에 삽입)
for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append(i)


while q:
    node = q.popleft()
    res.append(node)
    for i in range(1, n + 1):
        if graph[node][i] == 1:  # 완료한 노드와 인접한 노드 찾기
            in_degree[i] -= 1  # 인접한 노드들 진입차수 감소
            if in_degree[i] == 0:  # 진입차수가 0 이라면(=작업해도 되는 노드라면) 큐에 append
                q.append(i)

print(" ".join(map(str, res)))
