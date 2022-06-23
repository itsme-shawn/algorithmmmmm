import sys
from collections import deque

read = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(read())
board = [list(read().rstrip()) for _ in range(n)]


def bfs(x, y, color):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        v = q.popleft()
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and board[nx][ny] == color:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


visited = [[0] * n for _ in range(n)]
cnt_1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j, board[i][j])
            cnt_1 += 1

for i in range(n):
    for j in range(n):
        if board[i][j] == "G":
            board[i][j] = "R"

visited = [[0] * n for _ in range(n)]
cnt_2 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j, board[i][j])
            cnt_2 += 1

print(cnt_1, cnt_2)
