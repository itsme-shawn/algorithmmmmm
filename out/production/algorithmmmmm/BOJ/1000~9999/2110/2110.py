import sys

n, c = map(int, sys.stdin.readline().split())
lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))

lst.sort()
start = 1
end = max(lst)
res = 0


def check(distance):
    cnt = 1  # 맨 처음에 하나 주고 시작
    last = lst[0]
    for i in range(1, len(lst)):
        if lst[i] - last >= distance:
            cnt += 1
            last = lst[i]
    return cnt


while start <= end:
    mid = (start + end) // 2
    if check(mid) >= c:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)
