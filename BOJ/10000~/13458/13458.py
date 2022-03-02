import sys

read = sys.stdin.readline

n = int(read())
persons = list(map(int, read().split()))
b, c = map(int, read().split())

res = n  # n으로 초기화

for i in range(n):
    persons[i] -= b  # 각 방에 총감독관 1명 배치

    # 부감독관 계산
    if persons[i] > 0:
        if persons[i] % c == 0:
            res += persons[i] // c
        else:
            res += (persons[i] // c) + 1

print(res)
