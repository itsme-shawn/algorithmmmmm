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
    arr = list(map(int, read().split()))
    arr.insert(0, 0)  # 인덱스 사용 편하게 하기 위해서 맨 앞에 0 삽입
    dp = [0] * (n + 1)  # 인덱스 사용 편하게 하기 위해서 사이즈 1 크게 생성
    dp[1] = 1  # base case
    res = 0  # 매 루프마다 최댓값 저장하는 변수
    for i in range(2, n + 1):
        maxx = 0
        # i 기준으로 왼쪽방향으로 진행
        for j in range(i - 1, 0, -1):
            # 증가수열이 가능한 경우 중에서 길이 최댓값 구함
            if arr[j] < arr[i] and dp[j] > maxx:
                maxx = dp[j]
        # dp[i] 는 가능한 증가수열 최대길이 + 1
        dp[i] = maxx + 1
        # 구한 dp[i] 와 res 를 비교
        if dp[i] > res:
            res = dp[i]

    print(res)

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
