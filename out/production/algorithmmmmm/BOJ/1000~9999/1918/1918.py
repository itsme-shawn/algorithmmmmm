import sys
from collections import deque
from curses.ascii import isalpha

string = list(sys.stdin.readline().rstrip())
stack = deque()
res = []
high = ["*", "/"]
low = ["+", "-"]

for i in range(len(string)):
    if isalpha(string[i]):
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
