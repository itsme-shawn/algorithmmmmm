# DFS 시간초과 오답

from pprint import pprint
from collections import deque
import sys

sys.setrecursionlimit(10000) 

# sys.stdin = open("in.txt", "r")
read = sys.stdin.readline

# dfs 로는 될 것 같은데
# bfs 로도 될지?

n = int(read())
board = [list(map(int, read().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

milk = {"STRAWBERRY":0, "CHOCO":1, "BANANA":2}

dx = [0, 1]
dy = [1, 0]
# 동,남

maxx = -1

def dfs(x,y,cnt,last):
    global maxx
    if maxx < cnt:
        maxx = cnt
    if (x,y) == (n-1,n-1):
        if board[x][y] == (last+1) % 3:
            cnt += 1
            if maxx < cnt:
                maxx = cnt
        return
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
            visited[nx][ny] = 1

            # 조건에 따라 우유개수 증감
            if cnt == 0: # 우유 하나도 안 마셨을때
                if board[nx][ny] == milk["STRAWBERRY"]: # 딸기 마셔야함
                    cnt += 1
                    last = milk["STRAWBERRY"]
                    
            elif board[nx][ny] == (last+1) % 3:
                cnt += 1
                last = (last+1) % 3
            
            dfs(nx,ny,cnt,last)
            visited[nx][ny] = 0

if board[0][0] == milk["STRAWBERRY"]:
    cnt = 1
else:
    cnt = 0

dfs(0,0,cnt,board[0][0])

print(maxx)
