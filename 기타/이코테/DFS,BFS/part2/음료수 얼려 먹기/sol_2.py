import sys
from collections import deque

sys.stdin = open("in.txt", "rt")
read = sys.stdin.readline

n, m = map(int, read().split())

board = [list(map(int, read().rstrip())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[0] * m for _ in range(n)]


def dfs(x, y):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                dfs(nx, ny)


res = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0 and visited[i][j] == 0:
            cnt = 0
            dfs(i, j)
            res.append(cnt)

print(res)
print(len(res))
