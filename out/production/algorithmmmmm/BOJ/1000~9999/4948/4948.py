import sys

read = sys.stdin.readline

while True:
    n = int(read())
    if n == 0:
        break
    cnt = 0
    save = 0
    check = [0] * (2 * n + 1)
    for i in range(2, 2 * n + 1):
        if check[i] == 0:
            cnt += 1
            for j in range(i, 2 * n + 1, i):
                check[j] = 1
        if i == n:
            save = cnt
    print(cnt - save)
