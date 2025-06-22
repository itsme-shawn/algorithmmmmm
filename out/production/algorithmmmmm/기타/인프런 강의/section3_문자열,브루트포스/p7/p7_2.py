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

    total = 0

    for i in range(n):
        k = abs(n // 2 - i)
        total += sum(lst[i][k : n - k])
    print(total)

    # 로직 끝

    print()
