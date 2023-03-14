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
    letters = read().rstrip()
    res = []
    for letter in letters:
        if letter.isnumeric():
            res.append(letter)
    num = int("".join(res))
    print(num)
    cnt = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cnt += 1
    print(cnt)

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
