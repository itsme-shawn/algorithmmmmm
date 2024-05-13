import sys
from collections import deque

read = sys.stdin.readline

n, m, t = map(int, read().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = [list(map(int, read().split())) for _ in range(n)]
dis = [[0] * m for _ in range(n)]
cnt = 0

minn = float("inf")

sword_x, sword_y = 0, 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            sword_x, sword_y = i, j


def bfs(option, _x, _y):
    deq = deque()
    deq.append((_x, _y))
    dis[_x][_y] = 1

    while deq:
        x, y = deq.popleft()

        if option in ("A", "C") and (x, y) == (n - 1, m - 1):
            return dis[n - 1][m - 1] - 1

        if option == "B" and (x, y) == (sword_x, sword_y):
            return dis[sword_x][sword_y] - 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and dis[nx][ny] == 0:

                if option == "A" or option == "B":
                    if board[nx][ny] != 1:
                        dis[nx][ny] = dis[x][y] + 1
                        deq.append((nx, ny))

                if option == "C":
                    dis[nx][ny] = dis[x][y] + 1
                    deq.append((nx, ny))
    return float("inf")


# 검을 사용 안 하는 경우
# print(bfs("A", 0, 0))
A = bfs("A", 0, 0)

# 검을 사용하는 경우
dis = [[0] * m for _ in range(n)]
# print(bfs("B", 0, 0))  # 시작점 ~ 검 까지 최단경로 (벽 존재)
B = bfs("B", 0, 0)

dis = [[0] * m for _ in range(n)]
# print(bfs("C", sword_x, sword_y))  # 검 ~ 도착점 까지 최단경로 (벽 무시)
C = bfs("C", sword_x, sword_y)

if min(A, (B + C)) > t:
    print("Fail")
else:
    print(min(A, (B + C)))
