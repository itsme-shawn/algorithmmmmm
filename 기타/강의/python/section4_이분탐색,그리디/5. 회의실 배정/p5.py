import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n = int(input())
    lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    lst.sort(key=lambda x: x[1])

    cnt = 0
    end = -1

    for t1, t2 in lst:
        if end <= t1:
            cnt += 1
            end = t2

    print(cnt)

    # 로직 끝

    print()
