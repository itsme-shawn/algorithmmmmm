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
    high = ["*", "/"]
    low = ["+", "-"]

    for i in range(len(string)):
        if string[i].isdigit():
            res.append(string[i])
        else:
            if string[i] in high:
                while stack and stack[-1] in high:
                    res.append(stack.pop())
                stack.append(string[i])
            elif string[i] in low:
                while stack and (stack[-1] in high or stack[-1] in low):
                    res.append(stack.pop())
                stack.append(string[i])
            elif string[i] == "(":
                stack.append(string[i])
            elif string[i] == ")":
                while stack and stack[-1] != "(":
                    res.append(stack.pop())
                stack.pop()

    while stack:
        temp = stack.pop()
        if temp != "(" and temp != ")":
            res.append(temp)

    print("".join(res))

    # 로직 끝
