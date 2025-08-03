# 틀린 풀이

import sys

from collections import deque

read = sys.stdin.readline

N,M = map(int, read().split())

edge = []

for _ in range(N+M):
    n1, n2 = map(int, read().split())
    edge.append([n1,n2])
    
q = deque([[1,0]]) # [최초위치, 주사위 횟수]
visited = [0] * 101
visited[1] = 1


while q:

    # print(f"{q=}")
    pos, cnt = q.popleft() # 위치, 주사위 던진 횟수
    if pos == 100:
        print(cnt)
        break
        
    for step in range(1,7):
        flag = False
        n_pos = pos + step
        # print(f"{n_pos=}, {q=}")
        if n_pos > 100:
            continue
        
        for start, end in edge:
            if n_pos == start:
                if visited[end]==0: # end 를 일반방문으로 도착했을때 처리가 안 되고
                    q.append([end, cnt+1])
                    visited[end] = 1
                    flag = True
                    break
        if flag == False and visited[n_pos]==0: # 여기로 내려와서 사다리/뱀을 안 타고 n_pos 로 처리 되버리는 오류 발생
            q.append([n_pos, cnt+1])
            visited[n_pos] = 1