import sys
from collections import deque

read = sys.stdin.readline

n, m = map(int, read().split())
board = [list(map(int, read().rstrip())) for _ in range(n)]
dist = [[0] * m for _ in range(n)]  # (0,0)로부터의 거리를 저장할 이차원리스트

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque([(x, y)])
    dist[x][y] = 1  # (0,0) 거리 == 1
    while q:
        v = q.popleft()
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1 and dist[nx][ny] == 0:  # dist 로 미방문노드 체크
                    dist[nx][ny] = dist[v[0]][v[1]] + 1  # 부모노드거리 + 1
                    q.append((nx, ny))


bfs(0, 0)
print(dist[n - 1][m - 1])
