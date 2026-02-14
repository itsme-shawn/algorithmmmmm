"""
그래프 탐색 기본기.
- 인접 리스트 입력 -> BFS 최단거리, DFS 방문 순서
"""

from collections import deque
from typing import List


def build_graph(n: int, edges: List[tuple[int, int]]) -> List[List[int]]:
    graph = [[] for _ in range(n + 1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    for adj in graph:
        adj.sort()
    return graph


def bfs(start: int, graph: List[List[int]]) -> List[int]:
    """무가중치 최단거리. 방문하지 못하는 노드는 -1."""

    dist = [-1] * len(graph)
    dist[start] = 0
    q = deque([start])
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)
    return dist


def dfs(start: int, graph: List[List[int]]) -> List[int]:
    """재귀 대신 스택 사용. 방문 순서를 리턴."""

    order = []
    stack = [start]
    visited = [False] * len(graph)
    visited[start] = True
    while stack:
        cur = stack.pop()
        order.append(cur)
        for nxt in reversed(graph[cur]):  # 작은 번호 먼저 꺼내려면 역순 push
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)
    return order


if __name__ == "__main__":
    n = 5
    edges = [(1, 2), (1, 3), (2, 4), (3, 5)]
    g = build_graph(n, edges)
    print(bfs(1, g))  # [ -1,0,1,1,2,2 ] (index 0 unused)
    print(dfs(1, g))  # 1 2 4 3 5
