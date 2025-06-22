import sys
from collections import deque

sys.stdin = open("in.txt", "r")

read = sys.stdin.readline

n, m = map(int, read().split())

board = [list(map(int, list(read().rstrip()))) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dist = [[0] * m for _ in range(n)]


def bfs(x, y):
    q = deque([(x, y)])
    dist[x][y] = 1

    while q:
        print("q : ", q)
        cur = q.popleft()
        for i in range(4):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1 and dist[nx][ny] == 0:
                    dist[nx][ny] = dist[cur[0]][cur[1]] + 1
                    q.append((nx, ny))


bfs(0, 0)
for i in range(n):
    print(dist[i])

print(dist[n - 1][m - 1])
