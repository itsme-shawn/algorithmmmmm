import sys

read = sys.stdin.readline

N, M = map(int, input().split())
board = [[0] * M for _ in range(N)]
count = 0

def is_valid(r, c):
    # 2*2 사각형이 만들어지는지 확인
    if r > 0 and c > 0:
        if board[r-1][c-1] == 1 and board[r-1][c] == 1 and board[r][c-1] == 1: # 2*2 사각형이 만들어지므로 현재칸에 놓으면 안 됨
            return False
    return True

def dfs(r, c):
    global count
    
    # 탈출 조건 : 모든 칸을 다 채웠을 때
    if r == N:
        count += 1
        return
    
    # 다음 칸 진행
    next_r, next_c = r, c + 1
    if next_c == M:
        next_r, next_c = r + 1, 0

    # Case 1: 현재 칸 (r, c)에 넴모를 놓지 않는 경우
    board[r][c] = 0
    dfs(next_r, next_c)

    # Case 2: 현재 칸 (r, c)에 넴모를 놓는 경우 (왼위, 위, 왼 모두에 넴모가 있으면 안 된다 )
    if is_valid(r, c):
        board[r][c] = 1
        dfs(next_r, next_c)

dfs(0, 0)
print(count)
