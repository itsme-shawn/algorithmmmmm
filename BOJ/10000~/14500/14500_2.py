import sys
from collections import deque

read = sys.stdin.readline

n,m = map(int,read().split())
board = [list(map(int, read().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
maxx = -1

# def bfs(x,y):
#     global maxx
#     q = deque()
#     q.append((x,y,1,board[x][y]))
#     visited = [[0]*m for _ in range(n)]
#     visited[x][y] = 1
    
#     while q:
#         cx,cy,cnt,summ = q.popleft()
#         if cnt == 4:
#             maxx = max(maxx, summ)
#         else:
#             for i in range(4):
#                 nx = cx + dx[i]
#                 ny = cy + dy[i]
#                 if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
#                     visited[nx][ny] = 1
#                     q.append((nx,ny,cnt+1,summ+board[nx][ny]))

def dfs(x, y, cnt, summ):
    global maxx
    if cnt == 4:
        maxx = max(maxx, summ)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, cnt + 1, summ + board[nx][ny])
            visited[nx][ny] = False  # 백트래킹

# 'T' 자
def get_T(x,y):
    global maxx
    temp = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            temp.append(board[nx][ny])
    if len(temp) == 4:
        maxx = max(maxx, sum(temp)-min(temp)+board[x][y])
    elif len(temp) == 3:
        maxx = max(maxx, sum(temp)+board[x][y])
            
        
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,1,board[i][j])
        visited[i][j] = False
        get_T(i,j)
        
print(maxx)
                    