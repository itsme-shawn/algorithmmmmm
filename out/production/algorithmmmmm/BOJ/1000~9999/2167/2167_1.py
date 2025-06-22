import sys

n, m = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
k = int(input())
case = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

dp = [[0] * (m + 1) for _ in range(n + 1)]

# dp 테이블 채우기 (바텀업)
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + arr[i - 1][j - 1]
        # arr[][] 의 인덱스는 행,열 번호에서 1씩 빼줘야함

# dp 테이블 사용해서 값 구하기
for i, j, x, y in case:
    ans = dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1]
    print(ans)
