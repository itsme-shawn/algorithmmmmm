import sys
from collections import deque

read = sys.stdin.readline

n, k = map(int, read().split())
dist = [-1] * 100001  # 시작노드부터의 거리(시간) ( bfs 레벨)
cnt = [0] * 100001  # 경우의 수


def bfs(v):
    deq = deque([v])
    dist[v] = 0  # 시작노드 자기자신은 거리 0
    cnt[v] = 1  # 시작노드 자기자신 경우의수 1 기본세팅
    flag = 0

    while deq:
        for _ in range(len(deq)):
            x = deq.popleft()
            # 이번 레벨에 찾는 노드가 있으므로 이번 레벨 탐색끝나면 탈출
            # 이번 레벨에 동일 노드 있을 수 있으므로 바로 탈출하면은 안 됨
            if x == k:
                flag = 1

            for nxt in (x - 1, x + 1, x * 2):
                if 0 <= nxt < 100001:  # 범위 설정안하면 반례 생김
                    if dist[nxt] == -1:  # 방문하지 않은 노드
                        # 시작노드로부터 현재노드의 거리 = 부모노드의 거리 + 1
                        dist[nxt] = dist[x] + 1
                        # 경우의 수는 부모에게서 그대로 물려받음
                        cnt[nxt] = cnt[x]
                        # 큐에 추가
                        deq.append(nxt)
                    # 방문한 노드이고, 같은 레벨에 존재하는 노드라면
                    elif dist[nxt] == dist[x] + 1:
                        # 마찬가지로 부모의 경우의 수를 더해줌
                        cnt[nxt] += cnt[x]
        if flag == 1:
            print(dist[k])
            print(cnt[k])
            break


bfs(n)
