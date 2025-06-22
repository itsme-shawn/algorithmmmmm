import sys

read = sys.stdin.readline

n = int(read())
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1
for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    print(dp[n])
