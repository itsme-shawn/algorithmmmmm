# 16236. 아기상어

import sys
from collections import deque

read = sys.stdin.readline

n = int(read())
board = [list(map(int, read().split())) for _ in range(n)]

# 상어 위치, 사이즈 초기화
shark = [0, 0]
shark_size = 2  # 상어 크기
shark_eat = 0  # 먹은 물고기 수
time = 0

# 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            shark = [i, j]
            board[i][j] = 0


# bfs()
def bfs(x, y):
    deq = deque()
    deq.append((x, y))
    visited[x][y] = True

    while deq:
        v = deq.popleft()

        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 상어 < 물고기크기 : 못 지나감
                if shark_size < board[nx][ny]:
                    continue
                visited[nx][ny] = True  # 방문처리
                dist[nx][ny] = dist[v[0]][v[1]] + 1  # 거리계산
                # 상어 > 물고기 인 물고기만 먹을 수 있음
                if board[nx][ny] and shark_size > board[nx][ny]:
                    eatable.append((dist[nx][ny], nx, ny))  # (거리,x,y)
                deq.append((nx, ny))


# 먹을 수 있는 물고기에서 같은 거리인 것이 여러 개라면, 위->왼쪽 우선순위
def find_eatable_fish():
    if eatable:
        eatable.sort(key=lambda x: (x[0], x[1], x[2]))
        return eatable
    else:
        return []


# eat()
# 상어 위치 갱신
# 물고기 빈 칸 처리
# 물고기 먹은 횟수 계산
# 자신의 크기와 같다면 크기 1 증가 후 먹은 횟수 초기화
def eat(fish):
    global shark_eat, shark_size, time, shark
    dist, x, y = fish
    shark = [x, y]  # 상어 위치 갱신 (통으로 갱신하는 것이기 때문에 global 처리해야함)
    board[x][y] = 0  # 물고기 먹음
    shark_eat += 1
    time += dist

    if shark_size == shark_eat:
        shark_size += 1
        shark_eat = 0


while True:
    visited = [[False] * n for _ in range(n)]
    dist = [[0] * n for _ in range(n)]
    eatable = []
    bfs(shark[0], shark[1])
    eatable = find_eatable_fish()
    # print(f"{eatable = }")
    if eatable:
        eat(eatable[0])
    else:
        print(time)
        break
