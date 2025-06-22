import sys
from collections import deque

read = sys.stdin.readline

m, n = map(int, read().split())
board = [list(map(int, read().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
level = 0

deq = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            deq.append((i, j))  # bfs 시작점 여러개 세팅

while deq:
    size = len(deq)
    for _ in range(size):  # 레벨 계산을 위한 for문
        v = deq.popleft()
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                board[nx][ny] = 1
                deq.append((nx, ny))
    level += 1  # 한 레벨(너비) 에서 bfs 끝나면 레벨 1 증가

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
    print(level - 1)  # 마지막에 모두 안 되는 경우 한 번을 더 도므로 -1을 해줘야함
