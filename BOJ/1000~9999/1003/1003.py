import sys

t = int(sys.stdin.readline())
cnt_zero = 0
cnt_one = 0


def fibo(n):
    global cnt_zero, cnt_one
    if n == 0:
        cnt_zero += 1
        return 0
    elif n == 1:
        cnt_one += 1
        return 1
    return fibo(n - 1) + fibo(n - 2)


for _ in range(t):
    cnt_zero = 0
    cnt_one = 0
    fibo(int(sys.stdin.readline()))
    print(cnt_zero, cnt_one)
