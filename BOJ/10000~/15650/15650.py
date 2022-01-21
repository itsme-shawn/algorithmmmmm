# 조합
import sys

n, m = map(int, sys.stdin.readline().split())


def dfs(L, cur):
    if L == m:
        print(" ".join(map(str, cur)))
        return
    else:
        for num in range(1, n + 1):
            if cur and num <= cur[-1]:  # num이 cur 의 마지막 값보다 작으면 dfs 할 필요없음
                continue
            else:
                dfs(L + 1, cur + [num])


dfs(0, [])
