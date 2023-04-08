import sys

sys.stdin = open("in2.txt", "r")

read = sys.stdin.readline

n, m = map(int, read().split())  # 노드개수, 간선개수
# graph = [list(map(int, read().split())) for _ in range(m)]

INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0 으로 초기화
for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, read().split())
    # 양방향 연결
    graph[a][b] = 1
    graph[b][a] = 1


for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


x, k = map(int, read().split())  # 도착지, 경유지

if graph[1][k] != INF and graph[k][x] != INF:
    print(graph[1][k] + graph[k][x])
else:
    print(-1)
