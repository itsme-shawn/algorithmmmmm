import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(list(map(int, input().split())))

    m = int(input())
    for _ in range(m):
        rowN, direction, rotateN = map(int, input().split())

        if direction == 0:  # 왼쪽
            for _ in range(rotateN):
                lst[rowN - 1] = lst[rowN - 1][1:] + [lst[rowN - 1][0]]

        elif direction == 1:  # 오른쪽
            for _ in range(rotateN):
                lst[rowN - 1] = [lst[rowN - 1][-1]] + lst[rowN - 1][0:-1]

    total = 0
    for i in range(n):
        k = n // 2 - abs(n // 2 - i)
        total += sum(lst[i][k : n - k])

    print(total)

    # 로직 끝

    print()
