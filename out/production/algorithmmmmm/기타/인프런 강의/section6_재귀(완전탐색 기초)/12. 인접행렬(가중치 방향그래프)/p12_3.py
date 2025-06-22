# 인접리스트 방식 (딕셔너리사용)

n, m = map(int, input().split())
graph = {}
for _ in range(m):
    i, j, w = map(int, input().split())
    graph[i] = graph.get(i, []) + [(j, w)]  # (j,w) == (도착노드, 가중치)

for i in graph.keys():
    print(f"{i} : {graph[i]}")

"""
6 9
1 2 7
1 3 4
2 1 2
2 3 5
2 5 5
3 4 5
4 2 2
4 5 5
6 4 5
"""
