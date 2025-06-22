import sys
from collections import deque

read = sys.stdin.readline

n = int(read())

text = read().rstrip()  # 마지막 개행 제거


dic = dict()
deq = deque()

for i in range(n):
    dic[chr(i + ord("A"))] = int(read())
    # dic : {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}


for t in text:
    if t.isalpha():
        deq.append(dic[t])
    else:
        n2 = deq.pop()
        n1 = deq.pop()

        if t == "+":
            n3 = n1 + n2
        elif t == "-":
            n3 = n1 - n2
        elif t == "*":
            n3 = n1 * n2
        elif t == "/":
            n3 = n1 / n2

        deq.append(n3)

print("{:.2f}".format(deq[-1]))
