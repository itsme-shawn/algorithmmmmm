import sys

sys.setrecursionlimit(10**6)

read = sys.stdin.readline

n = int(read().rstrip())
home = [list(map(int, read().split())) for _ in range(n)]
home.insert(0, 0)
R = 0
G = 1
B = 2
dp = [[0] * 3 for _ in range(n + 1)]
dp[1] = home[1]


def dfs(n, color):
    if dp[n][color]:
        return dp[n][color]
    else:
        if color == R:
            dp[n][color] = min(dfs(n - 1, G), dfs(n - 1, B)) + home[n][color]
        elif color == G:
            dp[n][color] = min(dfs(n - 1, R), dfs(n - 1, B)) + home[n][color]
        elif color == B:
            dp[n][color] = min(dfs(n - 1, R), dfs(n - 1, G)) + home[n][color]
        return dp[n][color]


print(min(dfs(n, R), dfs(n, G), dfs(n, B)))
