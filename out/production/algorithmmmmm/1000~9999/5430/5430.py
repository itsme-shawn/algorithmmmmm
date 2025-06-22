import sys
from collections import deque

t = int(input())

for _ in range(t):
    p = list(sys.stdin.readline().rstrip())
    n = int(input())
    lst = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    # ['1', '2', '3', '4']
    r_cnt = 0  # reverse 횟수

    for f in p:
        if f == "R":
            r_cnt += 1
        elif f == "D":  # D
            if (not lst) or n == 0:
                print("error")
                break
            if r_cnt % 2 == 0:  # 짝수면 왼쪽에서 팝
                lst.popleft()
            else:  # 홀수면 오른쪽에서 팝
                lst.pop()
    else:
        if r_cnt % 2 == 1:
            lst.reverse()
        print("[", end="")
        if len(lst) != 0:
            for i in range(len(lst) - 1):
                print(lst[i], end=",")
            print(lst[-1], end="")
        print("]")
