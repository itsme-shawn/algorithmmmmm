import sys
from collections import deque

read = sys.stdin.readline

n, m = map(int, read().split())
graph = dict()
in_degree = [0] * (n + 1)  # 각 노드의 진입차수

for _ in range(m):
    a, b = map(int, read().split())
    graph[a] = graph.get(a, []) + [b]
    in_degree[b] += 1

start_node = [i for i in range(1, len(in_degree)) if in_degree[i] == 0]


q = deque(start_node)

while q:
    x = q.popleft()
    print(x, end=" ")
    if x in graph.keys():
        for node in graph[x]:
            in_degree[node] -= 1
            if in_degree[node] == 0:
                q.append(node)
