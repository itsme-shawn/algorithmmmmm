import sys
read = sys.stdin.readline

h,w = map(int, read().split())

heights = list(map(int, read().split()))

board = [[0]*w for _ in range(h)]

    
for i,height in enumerate(heights):
    for j in range(height): # j : 0,1,2
        board[h-j-1][i] = 1
    
res = 0
    
for row in board:
    flag = False
    cur = 0
    stack = []
    for i in range(len(row)):
        if row[i] == 1:
            if not stack:
                stack.append(i)
            else:
                res += i - stack.pop() - 1
                stack.append(i)

print(res)