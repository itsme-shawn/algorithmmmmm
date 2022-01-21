# 중복순열
import sys

n, m = map(int, sys.stdin.readline().split())


def dfs(L, cur):
    if L == m:
        print(" ".join(map(str, cur)))
        return
    else:
        for num in range(1, n + 1):
            dfs(L + 1, cur + [num])


dfs(0, [])
