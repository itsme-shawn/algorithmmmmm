import sys

n, m = map(int, sys.stdin.readline().split())
money = [int(sys.stdin.readline()) for _ in range(n)]

start = max(money)
end = sum(money)


def check(price, lst):
    cnt = 1
    total = 0
    for item in lst:
        total += item
        if total > price:
            cnt += 1
            total = item
    return cnt


while start <= end:
    mid = (start + end) // 2
    if check(mid, money) <= m:
        res = mid
        end = mid - 1
    else:
        start = mid + 1

print(res)
