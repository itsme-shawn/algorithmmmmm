import sys

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
k = int(input())
c = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]


for coordinate in c:
    i, j, x, y = (
        coordinate[0] - 1,
        coordinate[1] - 1,
        coordinate[2] - 1,
        coordinate[3] - 1,
    )
    total = 0
    for a in range(i, x + 1):
        total += sum(arr[a][j : y + 1])

    print(total)
