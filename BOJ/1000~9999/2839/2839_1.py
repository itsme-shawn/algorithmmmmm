# 재귀를 이용한 DP (top-down)

import sys

n = int(sys.stdin.readline())


def dp(n):
    cache[3] = cache[5] = 1
    cache[1] = cache[2] = cache[4] = -1

    if n not in cache:
        if n % 5 == 0:
            cache[n] = dp(n - 5) + 1
        elif n % 3 == 0:
            cache[n] = dp(n - 3) + 1
        elif dp(n - 5) > 0 and dp(n - 3) > 0:
            cache[n] = min(dp(n - 5), dp(n - 3)) + 1
        else:
            cache[n] = -1

    return cache[n]


cache = {}
print(dp(n))
