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

    # top down

    def dfs(i, j):
        # 이미 푼 부분문제라면 바로 리턴
        if dp[i][j]:
            return dp[i][j]
        else:
            if (i, j) == (0, 0):
                dp[i][j] = board[0][0]
            elif i == 0:
                dp[i][j] = dfs(i, j - 1) + board[i][j]
            elif j == 0:
                dp[i][j] = dfs(i - 1, j) + board[i][j]
            else:
                dp[i][j] = min(dfs(i - 1, j), dfs(i, j - 1)) + board[i][j]
            # 위에서 구한 dp 값을 리턴
            return dp[i][j]

    print(dfs(n - 1, n - 1))

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
