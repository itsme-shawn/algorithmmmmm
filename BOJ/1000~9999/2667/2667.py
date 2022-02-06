# dfs
import sys

read = sys.stdin.readline

n = int(read())
board = [list(map(int, read().rstrip())) for _ in range(n)]
res = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    global cnt
    board[x][y] = 0  # 노드 값을 0 으로 만든다는 것 == 방문처리
    cnt += 1  # 단지내 집 개수증가
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 1:  # 미방문노드
                dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if board[i][j] == 1:  # 노드 값이 1일때만 dfs
            cnt = 0
            dfs(i, j)
            res.append(cnt)  # cnt : dfs 종료 후 한 단지내에 있는 집 개수

res.sort()

print(len(res))
print("\n".join(map(str, res)))
