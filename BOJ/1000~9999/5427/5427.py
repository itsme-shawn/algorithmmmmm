import sys
from collections import deque

# sys.stdin = open('in.txt', 'r') 

read = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def printt(map):
    for m in map:
        print(m)
    print()
        

def fire_bfs(q: deque, visited):
    # print("fire")
    while q:
        # printt(visited)
        cx, cy ,time = q.popleft()  
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            # print("nx,ny", nx,ny)

            if 0 <= nx < h and 0 <= ny < w:
                if visited[nx][ny] == -1 and (board[nx][ny] == '.' or board[nx][ny] == '@'):
                    visited[nx][ny] = visited[cx][cy] + 1
                    q.append([nx,ny,visited[nx][ny]])
    
def sang_bfs(q: deque, visited):
    # print("sang")
    while q:
        # printt(visited)
        cx, cy ,time = q.popleft()  
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            # print("nx,ny", nx,ny)

            # 이동 가능
            if 0 <= nx < h and 0 <= ny < w:
                if visited[nx][ny] == -1 and board[nx][ny] == '.' and ((visited[cx][cy] + 1 < fire_visited[nx][ny]) or fire_visited[nx][ny] == -1):
                    visited[nx][ny] = visited[cx][cy] + 1
                    q.append([nx,ny,visited[nx][ny]])
            else: # 탈출
                return visited[cx][cy]+1
    return False
    

t = int(read())

for _ in range(t):
    # print("\n^^^^^^^^^^")
    w, h = map(int, read().split())
    board = [list(read().rstrip()) for _ in range(h)]
    sang_visited = [[-1] * w for _ in range(h)]
    fire_visited = [[-1] * w for _ in range(h)]
    
    sang_q = deque([]) # 상근 위치 queue
    fire_q = deque([]) # 불 위치 queue
    
    # 상근, 불 시작위치 queue 에 삽입
    for i in range(h):
        for j in range(w):
            if board[i][j] == '@': # 상근
                sang_q.append([i,j,0]) # x,y,time
                sang_visited[i][j] = 0
            elif board[i][j] == '*': # 불
                fire_q.append([i,j,0]) # x,y,time    
                fire_visited[i][j] = 0
                
    fire_bfs(fire_q, fire_visited)
    res = sang_bfs(sang_q,sang_visited)
    
    if res:
        print(res)
    else:
        print("IMPOSSIBLE")
                


                    
                
        
        
    
