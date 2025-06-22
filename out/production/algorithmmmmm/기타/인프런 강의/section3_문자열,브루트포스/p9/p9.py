import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n = int(input())
    temp = [list(map(int, input().split())) for _ in range(n)]

    # lst = [[0] * (n + 2)] * (n + 2) # 안됨 ! 얕은복사일어남
    lst = [[0] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            lst[i + 1][j + 1] = temp[i][j]

    cnt = 0
    for i in range(n):
        for j in range(n):
            if lst[i + 1][j + 1] > max(
                lst[i][j + 1],
                lst[i + 1][j],
                lst[i + 1][j + 2],
                lst[i + 2][j + 1],
            ):
                cnt += 1
    print(cnt)

    # 로직 끝

    print()
