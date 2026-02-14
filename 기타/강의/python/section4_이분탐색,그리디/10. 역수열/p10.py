import sys
from collections import deque

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n = int(input())
    lst = list(map(int, sys.stdin.readline().split()))
    res = []

    for _ in range(len(lst)):
        idx = lst.index(0) # 값이 0 인 빠른 index 를 찾음
        if idx > -1:
            res.append(idx + 1)
            lst[idx] = -1 # 사용한 숫자는 -1 로 처리
            for i in range(idx): # idx 보다 작은 값들은 -1 씩 해줌
                lst[i] -= 1

    print(res)

    # 로직 끝

    print()
