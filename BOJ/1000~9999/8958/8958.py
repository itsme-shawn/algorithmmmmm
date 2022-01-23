import sys

t = int(input())

for _ in range(t):
    case = list(sys.stdin.readline().rstrip())

    res = 0
    cnt = 0  # O 누적횟수

    for ch in case:
        if ch == "O":
            res += 1
            res += cnt
            cnt += 1
        elif ch == "X":
            cnt = 0

    print(res)
