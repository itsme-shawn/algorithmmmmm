import sys

n = int(sys.stdin.readline())
i = 1
while True:
    res = (i * (i + 1)) // 2
    if res > n:
        print(i - 1)
        break
    i += 1
