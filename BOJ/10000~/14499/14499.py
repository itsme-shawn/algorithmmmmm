import copy
import sys

read = sys.stdin.readline
n, m, x, y, k = map(int, read().split())
board = [list(map(int, read().split())) for _ in range(n)]
command = list(map(int, read().split()))
dice = [0] * 6
dice[5] = board[x][y]


for cmd in command:
    tmp = copy.copy(dice)
    if cmd == 1 and y + 1 < m:
        tmp[0] = dice[3]
        tmp[2] = dice[0]
        tmp[3] = dice[5]
        tmp[5] = dice[2]
        y = y + 1
        if board[x][y] == 0:
            board[x][y] = tmp[5]
        else:
            tmp[5] = board[x][y]
            board[x][y] = 0
        print(tmp[0])
    elif cmd == 2 and y - 1 >= 0:
        tmp[0] = dice[2]
        tmp[2] = dice[5]
        tmp[3] = dice[0]
        tmp[5] = dice[3]
        y = y - 1
        if board[x][y] == 0:
            board[x][y] = tmp[5]
        else:
            tmp[5] = board[x][y]
            board[x][y] = 0
        print(tmp[0])

    elif cmd == 3 and x - 1 >= 0:
        tmp[0] = dice[4]
        tmp[1] = dice[0]
        tmp[4] = dice[5]
        tmp[5] = dice[1]
        x = x - 1
        if board[x][y] == 0:
            board[x][y] = tmp[5]
        else:
            tmp[5] = board[x][y]
            board[x][y] = 0
        print(tmp[0])

    elif cmd == 4 and x + 1 < n:
        tmp[0] = dice[1]
        tmp[1] = dice[5]
        tmp[4] = dice[0]
        tmp[5] = dice[4]
        x = x + 1
        if board[x][y] == 0:
            board[x][y] = tmp[5]
        else:
            tmp[5] = board[x][y]
            board[x][y] = 0
        print(tmp[0])
    dice = tmp
