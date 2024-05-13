import sys

sys.stdin = open("in.txt", "rt")
read = sys.stdin.readline

n, m = map(int, read().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = []

for _ in range(n):
    board.append(list(map(int, list(read().rstrip()))))


def dfs(x, y):
    board[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            dfs(nx, ny)


cnt = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            dfs(i, j)
            cnt += 1

print(cnt)
