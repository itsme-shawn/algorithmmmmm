import sys

read = sys.stdin.readline

N, M = map(int, input().split())

board = [[0] * (M + 1) for _ in range(N + 1)]
count = 0

def dfs(depth):
    global count
    if depth == N * M:
        count += 1
        return
    
    x = depth // M + 1
    y = depth % M + 1

    # Case 1: 넴모를 놓는 경우 => 세 방향 중 하나라도 0이면 가능
    if board[x-1][y] == 0 or board[x-1][y-1] == 0 or board[x][y-1] == 0:
        board[x][y] = 1
        dfs(depth + 1)
        board[x][y] = 0  # 백트래킹

    # Case 2: 넴모를 놓지 않는 경우 (항상 가능)
    dfs(depth + 1)

dfs(0)
print(count)