# bfs
import sys
from collections import deque

read = sys.stdin.readline

n = int(read())
board = [list(map(int, read().rstrip())) for _ in range(n)]
res = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    global cnt
    q = deque([(x, y)])
    board[x][y] = 0
    cnt += 1
    while q:
        v = q.popleft()
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    q.append((nx, ny))
                    cnt += 1


for i in range(n):
    for j in range(n):
        if board[i][j] == 1:  # 노드 값이 1일때만 dfs
            cnt = 0
            bfs(i, j)
            res.append(cnt)  # cnt : dfs 종료 후 한 단지내에 있는 집 개수

res.sort()

print(len(res))
print("\n".join(map(str, res)))
