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
    def digit_sum(x):
        x = str(x)
        lst = list(map(int, list(x)))
        return sum(lst)

    n = int(read())
    nums = list(map(int, read().split()))
    maxx = -(10e9)
    res = 0
    for num in nums:
        if digit_sum(num) > maxx:
            maxx = digit_sum(num)
            res = num

    print(res)

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
