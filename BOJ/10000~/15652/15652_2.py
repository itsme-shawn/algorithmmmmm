import sys

read = sys.stdin.readline

n, m = map(int, read().split())

# 조합
def dfs(L, cur):
    if L == m:
        print(" ".join(map(str, cur)))
    else:
        for i in range(1, n + 1):
            if not cur or i >= cur[-1]:  # cur 배열이 비어있거나, 다음 수가 현재 값보다 크거나 같을 때만 dfs
                dfs(L + 1, cur + [i])


dfs(0, [])
