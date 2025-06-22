import sys

n, m = map(int, sys.stdin.readline().split())
wood = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(wood)
res = 0


def check(height, wood):
    total = 0
    for item in wood:
        if item > height:
            total += item - height
    return total


while start <= end:
    mid = (start + end) // 2
    if check(mid, wood) >= m:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)
