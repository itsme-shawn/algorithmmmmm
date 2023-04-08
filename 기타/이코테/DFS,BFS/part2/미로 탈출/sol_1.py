import sys
from collections import deque

sys.stdin = open("in.txt", "r")
read = sys.stdin.readline

n, m = map(int, read().split())
board = [list(map(int, read().rstrip())) for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[0] * m for _ in range(n)]


def bfs(x, y):
    # 시작위치 deq에 저장하고 방문처리
    deq = deque([(x, y)])
    visited[x][y] = 1

    while deq:
        _x, _y = deq.popleft()
        for i in range(4):
            nx = _x + dx[i]
            ny = _y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and board[nx][ny] == 1:
                    visited[nx][ny] = visited[_x][_y] + 1  # 거리계산 겸 방문처리
                    deq.append((nx, ny))


bfs(0, 0)

# for row in visited:
#     print(row)

print(visited[n - 1][m - 1])
