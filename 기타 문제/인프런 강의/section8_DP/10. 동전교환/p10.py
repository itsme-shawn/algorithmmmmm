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
    coins = list(map(int, read().split()))
    m = int(read())

    # dp[k] : k원을 거슬러 주는데 필요한 최소 동전 개수
    dp = [(i // coins[0]) for i in range(m + 1)]  # 첫 동전으로 나눠준 결과로 dp 배열 초기화

    # 동전 종류 개수만큼 for문
    for i in range(1, n):  # 처음에 초기화했으므로 두번째 코인부터 돌면 됨
        # dp 배열 coins[i]부터 끝까지 순회
        for j in range(coins[i], m + 1):
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)

    print(dp[m])

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
