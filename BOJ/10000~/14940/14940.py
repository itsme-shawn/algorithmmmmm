import sys
from collections import deque

# sys.stdin = open("in.txt", "r")

read = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

n, m = map(int, read().split())

board = [list(map(int, read().split())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)] # dist 최초 처리는 -1
visited = [[False] * m for _ in range(n)]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    dist[x][y] = 0

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and board[nx][ny] != 0: # 방문하지 않았고, 갈 수 있는 곳이면
                    dist[nx][ny] = dist[cx][cy] + 1
                    visited[nx][ny] = True
                    q.append((nx,ny))
        
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            bfs(i,j)
            break

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            dist[i][j] = 0 # 원래 갈 수 없는 곳에 대해 dist 보정처리
        print(dist[i][j], end=" ")
    print()
    
            
'''
각 지점에서의 목표지점까지의 거리

현재 0 => 결과 0

'2'인 지점에서 bfs 실행
dist 값이 결과

'''