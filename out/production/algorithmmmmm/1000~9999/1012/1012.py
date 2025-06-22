import sys

sys.setrecursionlimit(10 ** 6)

read = sys.stdin.readline

t = int(read())
for _ in range(t):
    m, n, k = map(int, read().split())
    board = [[0] * m for _ in range(n)]
    for _ in range(k):
        i, j = map(int, read().split())
        board[j][i] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def dfs(x, y):
        board[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
                dfs(nx, ny)

    cnt = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                cnt += 1
                dfs(i, j)

    print(cnt)
