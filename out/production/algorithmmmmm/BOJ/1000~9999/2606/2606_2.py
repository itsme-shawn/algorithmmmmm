# 정답풀이
import sys

v = int(sys.stdin.readline())
e = int(sys.stdin.readline())

graph = [[] for _ in range(v + 1)]  # 인접 리스트
cnt = 0
# visited 는 함수스택에서 인자로 쓰는 게 아니라, 이렇게 전역리스트로 체크만 하는 용도가 더 적합함.
visited = [0] * (v + 1)
visited[1] = 1

for _ in range(e):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)


def dfs(n):
    global cnt
    for i in graph[n]:  # 인접 리스트에서 각 노드랑 연결된 노드들만 for문 순회
        if visited[i] == 0:
            visited[i] = 1  # 방문처리
            cnt += 1  # 방문노드횟수 1 증가
            dfs(i)
            # dfs 끝나고 방문해제처리하면 안 됨. 가능한 모든 경로를 찾는 문제가 아니라 모든 노드를 한 번씩만 탐색하면 되기 때문임.


dfs(1)
print(cnt)
