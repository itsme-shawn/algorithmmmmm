# 스택 이용

def dfs(v):
    stack = [v]  # 현재 노드 스택에 추가

    while stack:
        cur = stack.pop()
        if visited[cur] == 0:  # 방문하지 않은 노드일 때
            visited[cur] = 1  # 방문처리
            print(cur, end=" ")
            # 인접노드들 뒤집어서 extend (작은노드들부터 먼저 방문하기 위해)
            stack.extend(graph[cur][::-1])


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
