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
    res = []

    for _ in range(n):
        nums = list(map(int, read().split()))
        num_set = set(nums)
        price = 0
        if len(num_set) == 3:  # 모두 다른 눈
            price = max(num_set) * 100
        elif len(num_set) == 2:  # 같은 눈 2개
            for num in num_set:
                if nums.count(num) == 2:
                    price = 1000 + num * 100
        else:  # 같은 눈 3개
            price = 10000 + nums[0] * 1000
        res.append(price)

    print(max(res))

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
