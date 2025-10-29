# 일차원 dp 배열

import sys

read = sys.stdin.readline

n = int(read())

hp_list = list(map(int, read().split()))
good_list = list(map(int, read().split()))

dp = [0] * (100)
# dp[k] : k의 체력소모로 얻을 수 있는 최대 기쁨
# 정답 : dp[99]

for i in range(n):
    hp = hp_list[i]
    good = good_list[i]
    if hp >= 100:
        continue
    for j in range(99, hp-1,-1):
        dp[j] = max(dp[j], dp[j-hp]+good)

print(dp[99])
