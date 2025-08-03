import sys

from collections import deque

read = sys.stdin.readline

N,M = map(int, read().split())

board = [i for i in range(101)] # 매핑테이블 역할

for _ in range(N+M):
    n1, n2 = map(int, read().split())
    board[n1] = n2
    
q = deque([[1,0]]) # [최초위치, 주사위 횟수]
visited = [0] * 101
visited[1] = 1


while q:
    pos, cnt = q.popleft() # 위치, 주사위 던진 횟수
    if pos == 100:
        print(cnt)
        break
        
    for step in range(1,7):
        n_pos = pos + step
        if n_pos > 100:
            continue
        
        final_pos = board[n_pos]
        
        if visited[final_pos] == 0:
            q.append([final_pos, cnt+1])
            visited[final_pos] = 1