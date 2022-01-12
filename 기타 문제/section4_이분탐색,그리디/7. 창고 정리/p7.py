import sys
from os import lchflags

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    l = int(input())
    lst = list(map(int, sys.stdin.readline().split()))
    m = int(input())

    lst.sort(reverse=True)

    for i in range(m):
        lst[0] -= 1
        lst[-1] += 1
        if lst[0] < lst[1]:
            lst.sort(reverse=True)
        if lst[-1] > lst[-2]:
            lst.sort(reverse=True)

    print(lst[0] - lst[-1])

    # 로직 끝

    print()
