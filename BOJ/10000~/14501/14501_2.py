import sys

read = sys.stdin.readline

n = int(read())
days = [0]
moneys = [0]
for _ in range(n):
    a, b = map(int, read().split())
    days.append(a)
    moneys.append(b)

dp = [0] * (n + 2)
# dp[i] : i번째 날 이상에 대해 받을 수 있는 최대금액 (i번째 미만 날은 고려안함)

# 뒤에서부터 dp 테이블을 채운다.
for i in range(n, 0, -1):
    # 현재 날에 상담을 못하면 다음 날 dp 값 가져옴
    if i + days[i] > n + 1:
        dp[i] = dp[i + 1]
    # moneys[i] + dp[i + days[i]] : 현재 날짜 상담 금액 + 상담 끝난 후 보상
    # dp[i + 1] : 상담을 안할 때의 보상
    else:
        dp[i] = max(moneys[i] + dp[i + days[i]], dp[i + 1])

print(dp[1])
