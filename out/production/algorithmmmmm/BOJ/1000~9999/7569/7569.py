import sys
from collections import deque

read = sys.stdin.readline

m, n, h = map(int, read().split())
board = [[] for _ in range(h)]
for i in range(h):
    board[i] = [list(map(int, read().split())) for _ in range(n)]

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

deq = deque()

flag = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 1:
                deq.append((i, j, k))
            if board[i][j][k] == 0:  # 익지 않은 토마토 있는지 확인 -> 없으면 다 이미 다 익었다는 뜻이므로 바로 종료함
                flag = 1

if flag == 0:
    print(0)
    sys.exit()

level = 0

while deq:
    for _ in range(len(deq)):
        v = deq.popleft()
        for i in range(6):
            nz = v[0] + dz[i]
            nx = v[1] + dx[i]
            ny = v[2] + dy[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if board[nz][nx][ny] == 0:
                    board[nz][nx][ny] = 1
                    deq.append((nz, nx, ny))
    level += 1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 0:
                print(-1)
                sys.exit()
else:
    print(level - 1)
