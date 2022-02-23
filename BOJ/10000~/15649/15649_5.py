import sys

read = sys.stdin.readline

n, m = map(int, read().split())


def dfs(L, cur):
    if L == m:
        print(" ".join(map(str, cur)))
    else:
        for i in range(1, n + 1):
            if i in cur:
                continue
            else:
                dfs(L + 1, cur + [i])


dfs(0, [])
