import sys
from collections import deque

sys.stdin = open("in.txt", "rt")
read = sys.stdin.readline

n, m = map(int, read().split())

board = [list(map(int, read().rstrip())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[0] * m for _ in range(n)]


def bfs(x, y):
    deq = deque([(x, y)])
    visited[x][y] = 1

    while deq:
        _x, _y = deq.popleft()

        for i in range(4):
            nx = _x + dx[i]
            ny = _y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and board[nx][ny] == 0:
                    visited[nx][ny] = 1
                    deq.append((nx, ny))


cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0 and visited[i][j] == 0:
            bfs(i, j)
            cnt += 1

print(cnt)
