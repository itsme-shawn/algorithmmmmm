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
    n, w = map(int, read().split())
    jewel = []
    for _ in range(n):
        x, y = map(int, read().split())
        jewel.append((x, y))  # (무게,가치)
    jewel.sort()

    WEIGHT = 0
    PRICE = 1

    dp = [0] * (w + 1)  # dp[k] : 가방 무게가 k 일 때 담을 수 있는 보석 최대가치

    # 보석무게만큼 dp 배열 순회
    for i in range(jewel[0][WEIGHT], w + 1):  # 보석최소무게 ~ 구하려는 무게
        maxx = 0
        # dp[가방무게] = dp[가방무게-보석무게] + (보석 무게에 해당하는 보석의 가치)
        # 여러 후보들 중에서 가장 큰 값 구하기
        for j in range(n):
            if i - jewel[j][WEIGHT] >= 0:  # 인덱스는 0 이상이여야하므로
                temp = dp[i - jewel[j][WEIGHT]] + jewel[j][PRICE]
                if temp > maxx:
                    maxx = temp
        # 가장 큰 값이 dp 값이 됨
        dp[i] = maxx

    print(dp[w])

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
