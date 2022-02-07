import sys

read = sys.stdin.readline

n = int(read())
res = 0

dp = [[0] * 10 for _ in range(n + 1)]
for i in range(0, 10):
    dp[1][i] = 1


def dfs(level, num):
    if dp[level][num]:
        return dp[level][num]
    else:
        if num == 0:
            dp[level][num] = dfs(level - 1, 1)
        elif num == 9:
            dp[level][num] = dfs(level - 1, 8)
        else:
            dp[level][num] = dfs(level - 1, num + 1) + dfs(level - 1, num - 1)

        return dp[level][num]


res = 0
for i in range(1, 10):
    res += dfs(n, i) % 1000000000

print(res % 1000000000)
