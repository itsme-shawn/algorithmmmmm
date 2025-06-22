import sys

read = sys.stdin.readline

v, e = map(int, read().split())
k = int(read())

MAX = 1e9
dist = [[MAX] * (v + 1) for _ in range(v + 1)]

for _ in range(e):
    a, b, w = map(int, read().split())
    if dist[a][b] == MAX:  # 처음 들어오는 간선일 때
        dist[a][b] = w
    else:  # 기존에 간선이 존재할 때
        dist[a][b] = min(dist[a][b], w)

for x in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            dist[i][j] = min(dist[i][j], dist[i][x] + dist[x][j])

for i in range(1, v + 1):
    if i == k:
        print(0)
    elif dist[k][i] == MAX:
        print("INF")
    else:
        print(dist[k][i])
