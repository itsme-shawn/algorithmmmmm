# 2차원 dp 배열

import sys

read = sys.stdin.readline

n = int(read())

hp_list = list(map(int, read().split()))
good_list = list(map(int, read().split()))
hp_list.insert(0,0)
good_list.insert(0,0)

dp = [[0]*100 for _ in range(n+1)]
# dp[i][j] : i번째 루프에서 j 체력으로 얻을 수 있는 최대 기쁨

for i in range(1, n+1):
    hp = hp_list[i]
    good = good_list[i]
    for j in range(1,100):
        if j >= hp: 
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-hp]+good)
        else: # 이 조건 빼먹었었음
            dp[i][j] = dp[i-1][j]

print(dp[n][99])
