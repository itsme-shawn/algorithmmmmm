# 냅색 알고리즘
# 이차원 dp 배열 (정방향 순회)

import sys
# sys.stdin = open("in.txt", "r")
read = sys.stdin.readline

n,k = map(int, read().split()) # 물품수, 가방의 한계무게
items = [list(map(int, read().split())) for _ in range(n)] # 무게, 가치
items.insert(0,0) # 1-index

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    weight = items[i][0]
    value = items[i][1]
    for j in range(1, k+1):
        if j - weight >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])