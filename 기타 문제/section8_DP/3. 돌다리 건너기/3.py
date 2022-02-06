import sys

read = sys.stdin.readline

n = int(read())
dp = [0] * (n + 2)

dp[1] = 1
dp[2] = 2

for i in range(3, n + 2):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n + 1])
