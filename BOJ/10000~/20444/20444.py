import sys

read = sys.stdin.readline

n, k = map(int, read().split())

start = 0
end = n


def check(mid):
    return (mid + 1) * (n - mid + 1)


while start <= end:
    mid = (start + end) // 2

    if check(mid) < k:
        # start = mid + 1
        end = mid - 1
    elif check(mid) > k:
        # end = mid - 1
        start = mid + 1
    else:
        print("YES")
        break
else:
    print("NO")
