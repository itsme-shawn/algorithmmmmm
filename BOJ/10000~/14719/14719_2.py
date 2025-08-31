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
        # print("\n===")
        # print("row",row)
        # print(f"start, {i=}, {flag=}, {row[i]=}, {cur=}, {res=}")
        if not flag and row[i] == 1:
            flag = True
        elif flag and row[i] == 0:
            cur += 1
        elif flag and cur and row[i] == 1:
            res += cur
            cur = 0
            
        # print(f"end, {i=}, {flag=}, {row[i]=}, {cur=}, {res=}")
        # print("===\n")
            
print(res)
            
            
        