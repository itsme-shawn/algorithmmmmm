import sys
from collections import deque

read = sys.stdin.readline

n, k = map(int, read().split())
visited = [0] * 100001


def bfs(v):
    deq = deque([(v, 0)])  # (node번호, 루트노드부터의 거리)
    cnt = 0
    flag = 0

    while deq:
        for _ in range(len(deq)):  # 레벨 단위 실행을 위한 for문
            x, dist = deq.popleft()
            visited[x] = 1  # 여기서 방문처리를 함! 정석적인 bfs 보다 늦게 방문처리를 함.

            if x == k:  # 원하는 노드를 발견했지만 이번 레벨 끝까지 돌아야하므로 바로 끝내지는 않는다.
                flag = 1  # 이번 레벨 끝나고 탈출하기 위해서
                cnt += 1  # 개수 증가

            for nxt in (x - 1, x + 1, x * 2):
                if 0 <= nxt < 100001:  # 범위 설정안하면 반례 생김
                    if visited[nxt] == 0:  # 방문하지 않은 노드이면
                        deq.append((nxt, dist + 1))  # 거리증가시켜서 큐에 추가
        # 탈출
        if flag == 1:
            print(dist)
            print(cnt)
            break


bfs(n)
