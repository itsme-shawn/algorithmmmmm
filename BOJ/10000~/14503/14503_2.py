import sys

read = sys.stdin.readline

N, M = map(int, read().split())
r, c, d = map(int,read().split())

board = [list(map(int, read().split())) for _ in range(N)]
# 0 : 청소 X, 1 : 벽

# 반시계(북,서,남,동)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 방향 : (4-d) % 4
dir = (4-d) % 4

# 주변 4칸 중에 청소 안 된 칸이 있으면 True
def check_around(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M:
            if board[nx][ny] == 0: # 청소 필요
                return True
    return False

# 바라보는 방향 유지한채로 한 칸 후진 가능한 지
def check_back(x,y):
    nx = x - dx[dir]
    ny = y - dy[dir]
    if 0<=nx<N and 0<=ny<M:
        if board[nx][ny] != 1: # 뒷칸이 벽이 아니라면 True
            return True
    return False

# 바라보는 방향 기준 앞 쪽이 청소 안 됐으면 True
def check_front(x,y,dir):
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0<=nx<N and 0<=ny<M:
        if board[nx][ny] == 0:
            return True
    return False

cnt = 0


while True:
    print("cnt", cnt)
    # 1
    if board[r][c] == 0:
        board[r][c] = -1 # 청소수행 : -1
        cnt += 1
    # 2
    elif check_around(r,c) == False:
        # 2-1
        if check_back(r,c) == True:
            r = r + dx[dir]
            c = c + dy[dir]
            continue
        # 2-2
        else:
            break
    # 3
    else:
        d = (d+2) % 4 # 3-1. 반시계 90도 회전
        dir = (4-d) % 4
        if check_front(r,c,dir) == True: # 3-2
            r = r + dx[dir]
            c = c + dy[dir]
            continue
        
print(cnt)
        