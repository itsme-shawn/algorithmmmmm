import copy
import sys
from collections import deque
from itertools import combinations

read = sys.stdin.readline

n, m = map(int, read().split())
board = [list(map(int, read().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

blank = []
q = deque()
visited = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:  # 빈 칸
            blank.append((i, j))
        elif board[i][j] == 2:  # 바이러스
            q.append((i, j))
            visited[i][j] = 1


max_cnt = float("-inf")

for combi in combinations(blank, 3):
    temp_board = copy.deepcopy(board)
    temp_q = copy.deepcopy(q)
    visited = [[0] * m for _ in range(n)]
    for i in range(3):
        temp_board[combi[i][0]][combi[i][1]] = 1
    while temp_q:
        (x, y) = temp_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < m
                and visited[nx][ny] == 0
                and temp_board[nx][ny] == 0
            ):
                visited[nx][ny] = 1
                temp_board[nx][ny] = 2
                temp_q.append((nx, ny))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp_board[i][j] == 0:
                cnt += 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)
