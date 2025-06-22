INF = int(1e9)

n = int(input())  # 노드 개수
m = int(input())  # 간선 개수

# 2차원 리스트(최단거리 그래프) 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0 으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A 에서 B 로 가는 비용은 C 라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드-워셜
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INF", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()

"""
>> input
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

>> output
0 4 8 6 
3 0 7 9 
5 9 0 4 
7 11 2 0 
"""
