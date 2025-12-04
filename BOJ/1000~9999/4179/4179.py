import sys
from collections import deque

# sys.stdin = open("in.txt", "r")
read = sys.stdin.readline

r, c = map(int, read().split())
board = [list(read().rstrip()) for _ in range(r)]

def pprint(arr):
    print("===")
    for row in arr:
        print(row)
    print("===")


dx = [-1,0,1,0]
dy = [0,1,0,-1]

# pprint(board)

fire_q = deque()
fire_visited = [[float('INF')]*c for _ in range(r)]

human_q = deque()
human_visited = [[float('INF')]*c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if board[i][j] == "J":
            human_q.append((i,j))
            human_visited[i][j] = 0
            # 끝지점 예외처리 종료
            if i ==0 or i == r-1 or j == 0 or j == c-1:
                print(1)
                exit(0)
        elif board[i][j] == "F":
            fire_q.append((i,j)) # 다중 시작점 처리
            fire_visited[i][j] = 0

# print("init fire")
# pprint(fire_visited)

# print("init human")
# pprint(human_visited)

while fire_q:
    (x,y) = fire_q.popleft()
    # print("+++")
    # print("x: ", x, "y : ", y)
    # pprint(fire_visited)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<r and 0<=ny<c and fire_visited[nx][ny] == float('inf') and board[nx][ny] == ".":
            fire_visited[nx][ny] = fire_visited[x][y] + 1
            fire_q.append((nx,ny))

while human_q:
    (x,y) = human_q.popleft()
    # print("---")
    # print("x: ", x, "y : ", y)
    # pprint(human_visited)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<r and 0<=ny<c and human_visited[nx][ny] == float('inf') and board[nx][ny] == "." and human_visited[x][y]+1<fire_visited[nx][ny]:
            human_visited[nx][ny] = human_visited[x][y] + 1
            if nx == 0 or nx == r-1 or ny == 0 or ny == c-1: # 종료
                result = human_visited[nx][ny] + 1
                print(result)
                exit(0)
            human_q.append((nx,ny))


# print("after fire")
# pprint(fire_visited)

# print("after human")
# pprint(human_visited)

print("IMPOSSIBLE")