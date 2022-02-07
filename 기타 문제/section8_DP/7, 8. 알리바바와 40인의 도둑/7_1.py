import sys
import time

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline
    start_time = time.time()

    # 로직 시작
    n = int(read())
    board = [list(map(int, read().split())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if (i, j) == (0, 0):
                dp[i][j] = board[0][0]
            elif i == 0:
                dp[i][j] = dp[i][j - 1] + board[i][j]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + board[i][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + board[i][j]

    print(dp[n - 1][n - 1])

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
