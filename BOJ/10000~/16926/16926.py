import copy
import sys
from collections import deque

# sys.stdin = open("in1.txt")
read = sys.stdin.readline

n, m, r = map(int, read().split())

board = [read().split() for _ in range(n)]


def pr_board(board):
    for b in board:
        print(b)


new_board = [["0"] * m for _ in range(n)]

# pr_board(board)

loops = min(n, m) // 2
for i in range(loops):
    deq = deque()

    # 위쪽
    deq.extend(board[i][i : m - i])

    # 오른쪽
    for j in range(i + 1, n - i - 1):
        deq.extend([board[j][m - (i + 1)]])

    # 아래쪽
    deq.extend(board[n - (i + 1)][i : m - i][::-1])

    # 왼쪽
    for j in range(n - i - 2, i, -1):
        deq.extend([board[j][i]])

    deq.rotate(-r)

    for j in range(i, m - i):
        new_board[i][j] = deq.popleft()
    for j in range(i + 1, n - i - 1):
        new_board[j][m - i - 1] = deq.popleft()
    for j in range(m - i - 1, i - 1, -1):
        new_board[n - i - 1][j] = deq.popleft()
    for j in range(n - i - 2, i, -1):
        new_board[j][i] = deq.popleft()


# pr_board(new_board)

for b in new_board:
    print(" ".join(b))
