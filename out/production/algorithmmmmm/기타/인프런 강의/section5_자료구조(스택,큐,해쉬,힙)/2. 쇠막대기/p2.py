import sys
from collections import deque

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    # for fileNum in range(6, 7):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    lst = list(sys.stdin.readline().rstrip())
    cnt = 0  # 현재 열린 괄호 개수
    res = 0  # 답
    before = ""
    for item in lst:
        if item == "(":
            cnt += 1
        elif item == ")" and before == "(":
            cnt -= 1
            res += cnt
        elif item == ")" and before == ")":
            cnt -= 1
            res += 1
        before = item
    print(res)

    # 로직 끝
