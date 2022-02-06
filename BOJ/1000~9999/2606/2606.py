# 시간초과
import sys

v = int(sys.stdin.readline())
e = int(sys.stdin.readline())

graph = [[0] * (v + 1) for _ in range(v + 1)]
path = [1]

for _ in range(e):
    i, j = map(int, sys.stdin.readline().split())
    graph[i][j] = 1
    graph[j][i] = 1  # 무방향그래프이므로 인접행렬에 쌍으로 추가


def dfs(n, visited):
    for i in range(1, v + 1):
        if graph[n][i] == 1 and i not in visited:
            path.append(i)
            # 재귀인자로 사용하면 이전스택으로 돌아갈 때 visited 가 자동으로 해제돼버림
            dfs(i, visited + [i])


dfs(1, [1])
print(path)  # 모든 경로가 다 출력됨
print(len(set(path)) - 1)  # 1 제외
