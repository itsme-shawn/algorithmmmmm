import copy
import sys

sys.setrecursionlimit(10**5)

read = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = 0

n = int(read())
board = [list(map(int, read().split())) for _ in range(n)]

max_height = -1
for i in range(n):
    for j in range(n):
        max_height = max(max_height, board[i][j])


def dfs(board, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] != 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dfs(board, nx, ny)


for height in range(0, max_height + 1):
    new_board = copy.deepcopy(board)
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if new_board[i][j] <= height:
                new_board[i][j] = 0

    for i in range(n):
        for j in range(n):
            if new_board[i][j] > height and visited[i][j] == 0:
                dfs(new_board, i, j)
                cnt += 1
    res = max(res, cnt)

print(res)
