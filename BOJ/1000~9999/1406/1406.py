import sys
from collections import deque

string = list(input())
N = int(sys.stdin.readline())

deq = deque()
temp = deque()

deq.extend(string)

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "L":
        if len(deq) != 0:
            temp.appendleft(deq.pop())
    elif command[0] == "D":
        if len(temp) != 0:
            deq.append(temp.popleft())
    elif command[0] == "B":
        if len(deq) != 0:
            deq.pop()
    elif command[0] == "P":
        deq.append(command[1])

print("".join(deq) + "".join(temp))
