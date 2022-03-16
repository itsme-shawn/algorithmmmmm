n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    i, j, w = map(int, input().split())
    graph[i][j] = w

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(graph[i][j], end=" ")
    print()

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
