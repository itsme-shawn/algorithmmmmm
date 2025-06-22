import sys

sys.stdin = open("in.txt", "rt")
read = sys.stdin.readline

n = int(read())
coins = list(map(int, read().split()))
res = []

# 완전탐색
def dfs(L, cur):
    if L == n:
        res.append(cur)
        return
    else:
        dfs(L + 1, cur + coins[L])
        dfs(L + 1, cur)


dfs(0, 0)
U = set(range(1, sum(coins) + 1))  # 모든 경우 전체집합
res = set(res)  # 만들 수 있는 경우 집합
print(min(U - res))
