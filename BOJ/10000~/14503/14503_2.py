import sys

read = sys.stdin.readline

N, M = map(int, read().split())
r, c, d = map(int,read().split())

board = [list(map(int, read().split())) for _ in range(N)]
# 0 : 청소 X, 1 : 벽

# 반시계(북,동,남,서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def print_board():
    for row in board:
        print(row)

# 주변 4칸이 모두 청소가 됐으면 True, 청소되지 않은 칸이 있으면 False
def is_all_clean(x,y):
    #print("x,y", x, y)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M:
            #print("nx,ny,board[nx][ny]", nx,ny,board[nx][ny])
            if board[nx][ny] == 0: # 청소 안 된 칸
                return False
    return True
            
# 바라보는 방향 유지한채로 한 칸 후진 가능한 지
def check_back(x,y,d):
    nx = x - dx[d]
    ny = y - dy[d]
    if 0<=nx<N and 0<=ny<M:
        if board[nx][ny] != 1: # 뒷칸이 벽이 아니라면 True
            return True
    return False

# 바라보는 방향 기준 앞 쪽이 청소 안 됐으면 True
def check_front(x,y,d):
    nx = x + dx[d]
    ny = y + dy[d]
    if 0<=nx<N and 0<=ny<M:
        if board[nx][ny] == 0:
            return True
    return False

cnt = 0


while True:
    #print("====")
    #print("cnt", cnt)
    #print("r,c", r,c)

    # print_board()
    # 1
    if board[r][c] == 0:
        #print("111")
        board[r][c] = -1 # 청소수행 : -1
        cnt += 1
    # 2
    elif is_all_clean(r,c) == True:
        # 2-1. 방향 유지하면서 한 칸 후진 시도
        if check_back(r,c,d) == True:
            #print("2-1")
            r = r - dx[d]
            c = c - dy[d]
            continue
        # 2-2
        else:
            #print("2-2")
            break
    # 3
    else:
        #print("3-1")
        d = (d-1) % 4 # 3-1. 반시계 90도 회전
        #print(f"{d=}")
        if check_front(r,c,d) == True: # 3-2
            #print("3-2")
            r = r + dx[d]
            c = c + dy[d]
            continue
        
print(cnt)
        