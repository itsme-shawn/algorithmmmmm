import sys

sys.setrecursionlimit(10**6)


read = sys.stdin.readline

n = int(read())

dp = [0] * (1000001)
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, n + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        if dp[i // 2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1

    if i % 3 == 0:
        if dp[i // 3] + 1 < dp[i]:
            dp[i] = dp[i // 3] + 1

print(dp[n])


# def dfs(n):
#     if dp[n]:
#         return dp[n]
#     else:
#         if n % 6 == 0:
#             dp[n] = min(dfs(n // 3), dfs(n // 2), dfs(n - 1)) + 1
#         elif n % 3 == 0:
#             dp[n] = min(dfs(n // 3), dfs(n - 1)) + 1
#         elif n % 2 == 0:
#             dp[n] = min(dfs(n // 2), dfs(n - 1)) + 1
#         else:
#             dp[n] = dfs(n - 1) + 1
#         return dp[n]


# print(dfs(n))
