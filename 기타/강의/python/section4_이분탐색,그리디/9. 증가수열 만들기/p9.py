import sys
from collections import deque

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n = int(input())
    deq = deque(map(int, sys.stdin.readline().split()))

    last = 0  # 제일 마지막에 뽑은 수
    cnt = 0
    res = []

    while True:
        if last < deq[0] or last < deq[-1]:
            if deq[-1] < last < deq[0]:
                last = deq.popleft()
                res.append("L")
            if deq[0] < last < deq[-1]:
                last = deq.pop()
                res.append("R")
            if last < deq[0] and last < deq[-1]:
                if deq[0] < deq[-1]:
                    last = deq.popleft()
                    res.append("L")
                else:
                    last = deq.pop()
                    res.append("R")
        else:
            break

    print(len(res))
    print(res)

    # 로직 끝

    print()
