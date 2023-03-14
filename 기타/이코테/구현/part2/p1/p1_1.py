# 상하좌우
import sys

sys.stdin = open("in.txt", "rt")
read = sys.stdin.readline

n = int(read())
commands = read().split()
x, y = 1, 1

for cmd in commands:
    if cmd == "R":
        dx, dy = 0, 1
    elif cmd == "D":
        dx, dy = 1, 0
    elif cmd == "L":
        dx, dy = 0, -1
    elif cmd == "U":
        dx, dy = -1, 0

    if 1 <= x + dx <= n and 1 <= y + dy <= n:
        x += dx
        y += dy

print(x, y)
