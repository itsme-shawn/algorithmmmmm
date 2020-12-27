import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(input()) for _ in range(N)]

min_count = 1000000
count = 0

for i in range(0, N-7):
  for j in range(0, M-7):
    if(board[i][j] == 'W'):
      for y in range(0, 8):
        for x in range(0, 8):
          if((x+y) % 2 == 0 and board[i+y][j+x] != 'W'): count += 1
          if((x+y) % 2 != 0 and board[i+y][j+x] != 'B'): count += 1
    else:   # board[i][j] == 'B'
      for y in range(0, 8):
        for x in range(0, 8):
          if((x+y) % 2 == 0 and board[i+y][j+x] != 'B'): count += 1
          if((x+y) % 2 != 0 and board[i+y][j+x] != 'W'): count += 1
    min_count = min(min_count, count, 64-count)
    count = 0

print(min_count)