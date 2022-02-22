import sys
from collections import deque

read = sys.stdin.readline

n, m = map(int, read().split())  # n : 학생수(노드수), m : 비교횟수(간선 수)

# graph = [[0] * (n + 1) for _ in range(n + 1)]  # 그래프 => 이차원배열로하면 메모리 초과 뜸
graph = dict()  # 딕셔너리 방식으로 그래프 구현
in_degree = [0] * (n + 1)  # 각 노드들의 진입차수

# 그래프와 진입차수 생성
for _ in range(m):
    a, b = map(int, read().split())
    # graph[a] = graph.get(a, []).append(b) => append 로 하면 안 됨! append 의 리턴값은 None 이기 때문
    graph[a] = graph.get(a, []) + [b]  # get 을 이용한 딕셔너리 그래프 구현

    # 똑같은 로직
    # if a not in graph:
    #     graph[a] = [b]
    # else:
    #     graph[a].append(b)
    in_degree[b] += 1


q = deque()
res = []

# 초기 큐 세팅 (진입차수가 0인 노드들 큐에 삽입)
for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append(i)


while q:
    node = q.popleft()
    res.append(node)
    if node in graph:
        for x in graph[node]:
            in_degree[x] -= 1
            if in_degree[x] == 0:  # 진입차수가 0 이라면(=작업해도 되는 노드라면) 큐에 append
                q.append(x)


print(" ".join(map(str, res)))
