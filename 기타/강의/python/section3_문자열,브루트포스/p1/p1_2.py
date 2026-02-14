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
    for i in range(1, n + 1):
        word = read().rstrip().lower()
        rev_word = word[::-1]
        if word == rev_word:
            print(f"#{i} YES")
        else:
            print(f"#{i} NO")

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
