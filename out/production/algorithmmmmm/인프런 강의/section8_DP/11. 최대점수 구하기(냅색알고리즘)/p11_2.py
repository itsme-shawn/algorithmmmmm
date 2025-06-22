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

    # dp 1차원 배열 (시간)
    dp = [0] * (m + 1)

    # (문제점수, 걸리는 시간) 한 쌍씩 입력받고 dp 배열 새롭게 갱신한다.
    # 이때, 앞에서 풀었던 문제는 다시 풀 수 없으므로 역방향으로 루프를 진행한다.
    # 정방향으로 루프를 돌면 점수가 계속 중복으로 누적됨
    for _ in range(n):  # 시행횟수 == 문제 개수
        score, t = map(int, read().split())
        for j in range(m, t - 1, -1):  # 역방향 진행!
            dp[j] = max(dp[j], dp[j - t] + score)
            # dp[j] : 직전 값을 그대로 물려받음 (이번 문제는 안 품)
            # dp[j - t] + score : 직전 시행 기준에서 이번 문제 걸리는 시간 뺀 점수 + 이번 문제 점수

    print(dp[m])

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
