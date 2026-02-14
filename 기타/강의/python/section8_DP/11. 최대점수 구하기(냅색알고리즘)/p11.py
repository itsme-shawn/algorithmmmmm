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
    n, m = map(int, read().split())

    # dp 2차원 배열 (행: 문제(n), 열 : 시간(m))
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # (문제점수, 걸리는 시간) 한 쌍씩 입력받고 dp 배열 한 줄씩 채워나간다.
    for i in range(1, n + 1):  # dp 행
        score, t = map(int, read().split())
        for j in range(t, m + 1):  # dp 열
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - t] + score)
            # dp[i-1][j] : 직전 행의 값을 그대로 물려받음 (이번 문제는 안 품)
            # dp[i - 1][j - t] + score : 직전 행 기준에서 이번 문제 걸리는 시간 뺀 점수 + 이번 문제 점수

    print(dp[n][m])

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
