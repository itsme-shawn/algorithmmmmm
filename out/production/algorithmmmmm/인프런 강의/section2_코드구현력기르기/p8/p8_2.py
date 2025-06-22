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
    n = int(read())
    nums = list(map(int, read().split()))

    def reverse(x):
        x = str(x)
        lst = list(x)
        lst.reverse()
        return int("".join(lst))

    def isPrime(x):
        if x == 1:
            return 0
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return 0  # 소수 아님
        return 1  # 소수

    for num in nums:
        rev = reverse(num)
        if isPrime(rev):
            print(rev, end=" ")

    print()

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
