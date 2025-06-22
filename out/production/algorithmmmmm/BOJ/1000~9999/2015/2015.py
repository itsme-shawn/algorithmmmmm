# 시간초과 코드

import sys

read = sys.stdin.readline

n, k = map(int, read().split())

nums = list(map(int, read().split()))

psum = [0] * (n + 1)

cnt = 0

for i in range(n):
    psum[i + 1] = psum[i] + nums[i]

for i in range(n):
    for j in range(i, n):
        if psum[j + 1] - psum[i] == k:
            cnt += 1

print(cnt)
