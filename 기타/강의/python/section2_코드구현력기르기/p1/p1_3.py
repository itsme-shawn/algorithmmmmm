import math
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
    n, k = map(int, read().split())
    print(n, k)

    i = 1

    result = []

    while i <= n:
        if n % i == 0:
            result.append(i)
        i += 1

    print(result)

    if k > len(result):
        print(-1)
    else:
        print(result[k - 1])

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
