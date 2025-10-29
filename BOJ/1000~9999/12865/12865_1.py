# 냅색 알고리즘
# 일차원 dp 배열 (역방향 순회)

import sys
# sys.stdin = open("in.txt", "r")
read = sys.stdin.readline

n,k = map(int, read().split()) # 물품수, 가방의 한계무게
items = [list(map(int, read().split())) for _ in range(n)] # 무게, 가치

dp = [0] * (k+1)

for w,v in items:
    if w > k:
        continue
    for i in range(k, w-1, -1): # 역방향 순회 (k ~ w)
        dp[i] = max(dp[i], dp[i-w] + v)

print(dp[k])