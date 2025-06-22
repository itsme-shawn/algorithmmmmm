import sys
from collections import deque

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    # for fileNum in range(6, 7):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    string = list(sys.stdin.readline().rstrip())
    stack = deque()
    res = []

    for i in range(len(string)):
        if string[i].isdigit():
            stack.append(string[i])
        else:
            n2 = stack.pop()
            n1 = stack.pop()
            temp = n1 + string[i] + n2
            stack.append(str(eval(temp)))
    print(stack[0])

    # 로직 끝
