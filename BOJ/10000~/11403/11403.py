import sys

read = sys.stdin.readline

n = int(read())
MAX = int(1e9)
dist = [list(map(int, read().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if dist[i][j] == 0:
            dist[i][j] = MAX

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])

for i in range(n):
    for j in range(n):
        if dist[i][j] == MAX:
            dist[i][j] = 0
        else:
            dist[i][j] = 1

for row in dist:
    print(" ".join(map(str, row)))
