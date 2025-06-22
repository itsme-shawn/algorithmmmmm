# dist(거리) 이용

import sys
from collections import deque

read = sys.stdin.readline

m, n = map(int, read().split())
board = [list(map(int, read().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = 0
dist = [[0] * m for _ in range(n)]

deq = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            deq.append((i, j))  # bfs 시작점 여러개 세팅

while deq:
    v = deq.popleft()
    for i in range(4):
        nx = v[0] + dx[i]
        ny = v[1] + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 0 and dist[nx][ny] == 0:
                board[nx][ny] = 1
                dist[nx][ny] = dist[v[0]][v[1]] + 1
                # 거리의 최댓값(bfs 최대레벨 수) 구하는 로직
                if dist[nx][ny] > res:
                    res = dist[nx][ny]
                deq.append((nx, ny))


flag = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:  # 남아있는 익지않은 토마토가 있을 때
            print(-1)
            flag = 1
            break
    if flag == 1:
        break
else:
    print(res)
