import sys

read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().split()))

dp = [0] * (1000)
dp[0] = 1  # base case. 첫 숫자의 LIS 길이는 1

for i in range(1, n):  # 두 번째 숫자부터 진행 ( arr[1:n] )
    maxx = 0  # arr[0:i] 에서의 LIS 길이 를 구할 변수
    for j in range(i):  # i 기준 왼쪽에서만 진행 ( 0 <= j < i )
        # 증가수열이 가능하고, dp 값이 현재 LIS 길이의 최댓값보다 클 때 maxx 갱신
        if arr[j] < arr[i] and dp[j] > maxx:
            maxx = dp[j]
    dp[i] = maxx + 1  # dp[i] : arr[0:i] 에서의 LIS 길이 + 1

print(max(dp))
