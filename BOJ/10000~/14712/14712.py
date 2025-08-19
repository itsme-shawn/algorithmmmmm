import sys

read = sys.stdin.readline

n,m = map(int, read().split())

board = [[0]*m for _ in range(n)]

count = 0

def dfs(x,y):
    # 종료 조건
    if x == n:
        global count
        count += 1
        return
    
    # 오른쪽으로 진행 (행은 유지, 열만 증가)
    nx, ny = x, y+1
    if ny == m:
        nx += 1
        ny = 0
        
    
    
    
