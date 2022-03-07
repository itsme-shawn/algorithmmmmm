import sys
from collections import deque

read = sys.stdin.readline

n = int(read())
dic = dict()

for _ in range(n - 1):
    a, b = map(int, read().split())
    if a not in dic.keys():
        dic[a] = [b]
    else:
        dic[a].append(b)
    if b not in dic.keys():
        dic[b] = [a]
    else:
        dic[b].append(a)

q = deque([1])
visited = [0] * (n + 1)
parent = [0] * (n + 1)


while q:
    x = q.popleft()
    visited[x] = 1
    for node in dic[x]:
        if visited[node] == 0:
            parent[node] = x
            q.append(node)

for i in range(2, n + 1):
    print(parent[i])
