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
    T = int(read())
    for i in range(1, T + 1):
        N, s, e, k = map(int, read().split())
        lst = list(map(int, read().split()))
        lst = lst[s - 1 : e]
        lst.sort()
        print(f"#{i} {lst[k - 1]}")

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
