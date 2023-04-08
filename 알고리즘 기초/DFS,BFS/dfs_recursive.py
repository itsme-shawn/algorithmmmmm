# 재귀 이용

def dfs(v):
    # 현재 노드 방문처리
    visited[v] = 1
    print(v, end=" ")

    # 현재 노드와 인접한 노드들 체크
    for i in graph[v]:
        # 방문하지 않은 노드 일때만 dfs재귀
        if visited[i] == 0:
            dfs(i)


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

dfs(1)  # 1 2 7 6 8 3 4 5
