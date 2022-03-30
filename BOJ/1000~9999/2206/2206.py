import sys
from collections import deque

read = sys.stdin.readline

n, m = map(int, read().split())
board = [list(map(int, read().rstrip())) for _ in range(n)]
dist = [[[0] * 2 for _ in range(m)] for _ in range(n)]
# dist[x][y][check]
# check=0 : 지금까지 벽 안 깸
# check=1 : 벽 깼음


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


q = deque()
q.append((0, 0, 0))
dist[0][0][0] = 1
exit_flag = 0
while q:
    x, y, check = q.popleft()
    if (x, y) == (n - 1, m - 1):
        print(dist[x][y][check])
        exit_flag = 1
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            # 다음 위치== 벽 and 현재 안 깬 상황 => 깨고 지나감
            if board[nx][ny] == 1 and check == 0:  # 벽,안깬상황이면 방문체크 필요없음
                dist[nx][ny][1] = dist[x][y][0] + 1
                q.append((nx, ny, 1))
            # 다음 위치 == 길 and 미방문한 위치, 벽 깼든안깼든 상관없음
            elif board[nx][ny] == 0 and dist[nx][ny][check] == 0:
                dist[nx][ny][check] = dist[x][y][check] + 1
                q.append((nx, ny, check))

if exit_flag == 0:
    print(-1)
