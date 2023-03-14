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
    dp = [0] * (n + 1)

    # base case
    dp[1] = 1
    dp[2] = 2

    def dfs(i):
        # 부분문제를 이미 풀었다면 정답 바로 return
        if dp[i]:
            return dp[i]
        # 처음 등장한 부분문제라면, 재귀로 해결하고 메모배열(dp)에 답 저장
        else:
            dp[i] = dfs(i - 1) + dfs(i - 2)
            return dp[i]

    print(dfs(n))

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
