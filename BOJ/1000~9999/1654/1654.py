import sys

k, n = map(int, sys.stdin.readline().split())
lst = []
for _ in range(k):
    lst.append(int(sys.stdin.readline()))

start = 1
end = max(lst)


def check(l):
    total = 0
    for wire in lst:
        total += wire // l
    return total


while start <= end:
    mid = (start + end) // 2
    if check(mid) >= n:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)
