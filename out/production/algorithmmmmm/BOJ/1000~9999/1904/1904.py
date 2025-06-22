import sys

read = sys.stdin.readline

n = int(read())
cur = 1
before = 1
for i in range(1, n):
    cur, before = (cur + before) % 15746, cur % 15746

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    print(cur)
