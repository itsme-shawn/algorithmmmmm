# 정답코드 DP

# N <= 1000 이므로 완탐은 불가하다는 거 생각해야했음

import sys
# sys.stdin = open("in.txt", "r")
input = sys.stdin.readline

N = int(input())
milk = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]

if milk[0][0] == 0:
    dp[0][0] = 1

for i in range(N):
    for j in range(N):
        # 왼쪽, 위 중 최댓값으로 DP 값 전이
        if i > 0:
            dp[i][j] = dp[i-1][j]
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i][j-1])

        if milk[i][j] == dp[i][j] % 3: # 현재 마신우유갯수 % 3 이 이번에 마실 우유
            dp[i][j] += 1

print(dp[N-1][N-1])