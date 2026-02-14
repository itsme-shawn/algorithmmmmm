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
    cnt = 0  # 약수 개수 카운트
    num = 1  # 나누는 수

    while cnt != k:
        if n % num == 0:
            cnt += 1
        if n == num and cnt < k:  # 예외처리
            num = 0
            break
        num += 1

    print(num - 1)

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
