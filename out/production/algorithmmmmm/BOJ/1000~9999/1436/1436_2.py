import sys

n = int(sys.stdin.readline())

ans = 666  # 현재 제목
cnt = 1  # 현재 횟수 카운트

while cnt != n:
    ans += 1
    temp = ans
    while temp != 0 or temp >= 666:
        if temp % 1000 == 666:  # 1000으로 나눴을 때 666이면 ok
            cnt += 1
            break
        else:
            temp //= 10  # 일의자리수 삭제

print(ans)
