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
    nums = [0, 0] + [1] * (n - 1)  # 에라토스테네스 체
    # 0 : 소수 아님
    # 1 : 소수
    for i in range(2, n + 1):
        temp = i  # 인덱스
        if nums[i] == 1:
            temp += i
            while temp <= n:
                nums[temp] = 0
                temp += i
    print(sum(nums))

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
