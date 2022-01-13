import sys

n, m = map(int, sys.stdin.readline().split())
money = [int(sys.stdin.readline()) for _ in range(n)]

start = max(money)  # 이분탐색 최솟값. 인출하는 돈은 money 리스트의 최솟값보다는 커야한다.
end = sum(money)


def check(price, lst):
    cnt = 1  # 맨 처음 한 번 인출하고 시작
    total = 0
    for item in lst:
        total += item
        if total > price:
            cnt += 1
            total = item
    return cnt


while start <= end:
    mid = (start + end) // 2
    if check(mid, money) <= m:  # 인출횟수가 주어진 횟수보다 적다는 것은 인출금액을 더 줄일 수 있다는 뜻
        res = mid
        end = mid - 1
    else:  # 이 경우는 인출금액을 늘려줘야함
        start = mid + 1

print(res)
