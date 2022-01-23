import sys

s = list(map(int, list(sys.stdin.readline().rstrip())))

if s.count(0) == 0 or s.count(1) == 0:  # 모두 다 1 or 0 => 안 뒤집어도 됨
    print(0)
else:  # 연속되는 0 개수, 연속되는 1 개수 찾기
    c0 = 0
    c1 = 0
    for i in range(len(s) - 1):
        if s[i] == 0 and s[i + 1] == 1:  # 0 -> 1 전환 : 연속되는 0 개수 증가
            c0 += 1
        elif s[i] == 1 and s[i + 1] == 0:  # 1 -> 0 전환 : 연속되는 1 개수 증가
            c1 += 1
    # 마지막 하나 처리
    if s[-1] == 0:  # 마지막 0 이면 연속되는 0 개수 증가
        c0 += 1
    else:  # s[-1] == 1: 마지막 1 이면 연속되는 1 개수 증가
        c1 += 1

    if c0 > c1:
        print(c1)
    else:
        print(c0)
