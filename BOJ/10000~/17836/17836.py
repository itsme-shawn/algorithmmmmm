# 재귀횟수 초과

import sys

read = sys.stdin.readline

n, m, t = map(int, read().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = [list(map(int, read().split())) for _ in range(n)]
dis = [[0] * m for _ in range(n)]
cnt = 0

minn = float("inf")


def dfs(x, y, sword):
    global cnt, minn
    if (x, y) == (n - 1, m - 1):
        cnt += 1
        # for d in dis:
        #     print(d)
        # print()
        if dis[n - 1][m - 1] < minn:
            minn = dis[n - 1][m - 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and dis[nx][ny] == 0:

            if sword:
                dis[nx][ny] = dis[x][y] + 1
                dfs(nx, ny, 1)
                dis[nx][ny] = 0

            else:
                if board[nx][ny] == 0:
                    dis[nx][ny] = dis[x][y] + 1
                    dfs(nx, ny, 0)
                    dis[nx][ny] = 0

                elif board[nx][ny] == 2:
                    dis[nx][ny] = dis[x][y] + 1
                    dfs(nx, ny, 1)
                    dis[nx][ny] = 0


dis[0][0] = 1

if board[0][0] == 2:  # 첫 위치에 검이 있을 때
    dfs(0, 0, 1)
else:  # 첫 위치에 검 없을 때
    dfs(0, 0, 0)

if cnt:
    print(minn - 1)
else:
    print("Fail")
