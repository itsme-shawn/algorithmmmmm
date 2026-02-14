import sys
from collections import deque

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    # for fileNum in range(6, 7):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n, k = map(int, sys.stdin.readline().split())
    q = deque(range(1, n + 1))
    while len(q) != 1:
        for _ in range(k - 1):
            q.append(q.popleft())
        q.popleft()
    print(q[0])

    # 로직 끝
