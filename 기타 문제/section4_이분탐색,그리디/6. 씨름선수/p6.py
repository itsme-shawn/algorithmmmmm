import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n = int(input())

    lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    lst.sort(key=lambda x: (-x[0], x[1]))
    selected_height = -1
    selected_weight = -1
    cnt = 0

    for h, w in lst:
        if w > selected_weight:
            selected_weight = w
            cnt += 1

    print(cnt)

    # 로직 끝

    print()
