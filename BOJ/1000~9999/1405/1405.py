import sys
read = sys.stdin.readline

N, pe, pw, ps, pn = map(int, read().split())

def printt():
    for row in board:
        print(row)
    print()

P = [p*0.01 for p in [pe,pw,ps,pn]]

board = [[0]*(2*N+1) for _ in range(2*N+1)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
# E, W, S, N (동,서,남,북)

res = 0

def dfs(x,y,L,cur_p):
    # printt()
    global res, cnt
    if L == N:
        res += cur_p
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 2*N+1 and 0 <= ny < 2*N + 1:
            if P[i] and board[nx][ny] == 0:
                board[nx][ny] = 1
                dfs(nx,ny,L+1,cur_p*P[i])
                board[nx][ny] = 0

board[N][N] = 1      
dfs(N,N,0,1)
        
print(res)
    
