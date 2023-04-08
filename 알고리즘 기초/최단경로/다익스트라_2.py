# visited 리스트를 사용해서 최단거리를 계산한 노드는 무시하는 코드

import heapq as hq
import sys

read = sys.stdin.readline

v, e = map(int, read().split())  # 정점개수, 간선개수
start = int(read())  # 시작 정점
graph = dict()  # 이차원배열로 해도 무방

for i in range(1, v + 1):
    graph[i] = []

for _ in range(e):
    a, b, w = map(int, read().split())  # 시작,도착,가중치
    graph[a].append((b, w))

MAX = int(1e9)
distance = [MAX] * (v + 1)  # 최단거리 테이블 무한대로 초기화
visited = [False] * (v + 1)


def dijkstra(start):
    q = []  # (시작정점으로부터의 거리, 노드번호) 를 저장할 최소 힙
    # pop 시 거리가 작은 순으로 pop 됨

    # 시작점 세팅
    distance[start] = 0  # 시작점의 거리는 0
    hq.heappush(q, (0, start))  # 힙에 시작점 (거리,시작노드번호) push

    while q:
        dist, cur = hq.heappop(q)  # 최소 힙에서 (거리,노드번호) pop

        # 현재 노드의 최단거리가 계산되지 않은 경우에만 수행

        if visited[cur]:  # 현재 노드가 이미 처리된 적이 있는 노드이면 무시
            continue

        visited[cur] = True  # 여기서 방문처리!

        for i in graph[cur]:  # i[0] : 인접노드번호, i[1] : 거리
            cost = dist + i[1]  # 현재노드를 거쳐갈 경우의 거리 계산
            if cost < distance[i[0]]:  # 새롭게 계산한 거리가 작을때만 갱신
                distance[i[0]] = cost  # 거리테이블 갱신
                hq.heappush(q, (cost, i[0]))  # 갱신 노드의 거리와 노드번호를 heap 에 push


dijkstra(start)

for i in range(1, v + 1):
    if distance[i] == MAX:
        print("INF")
    else:
        print(distance[i])

"""
>> input
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1 
5 3 1 
5 6 2

>> output
0
2
3
1
2
4
"""
