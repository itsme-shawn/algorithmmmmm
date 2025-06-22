import sys

read = sys.stdin.readline

t = int(read())

dp = [0] * (101)
dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for _ in range(t):
    n = int(read())
    for i in range(6, n + 1):
        dp[i] = dp[i - 5] + dp[i - 1]
    print(dp[n])
