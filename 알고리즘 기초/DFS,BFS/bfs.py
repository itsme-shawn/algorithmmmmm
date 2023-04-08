from collections import deque


def bfs(start):
    q = deque([start])  # 시작노드 큐에 넣고 시작
    visited[start] = 1  # 시작노드 방문처리
    while q:
        v = q.popleft()  # 큐에서 노드 하나 pop(실제 방문)
        print(v, end=" ")
        for node in graph[v]:  # pop한 노드와 인접한 노드들 체크
            if visited[node] == 0:  # 인접노드가 미방문노드일 때만
                q.append(node)  # 큐에 추가
                visited[node] = 1  # 방문처리


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [0] * 9

bfs(1)  # 1 2 3 8 7 4 5 6
