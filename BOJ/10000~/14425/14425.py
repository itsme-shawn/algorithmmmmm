import sys

read = sys.stdin.readline

n, m = map(int, read().split())

s = []
tests = []

for _ in range(n):
    s.append(read().rstrip())

for _ in range(m):
    tests.append(read().rstrip())

cnt = 0

for test in tests:
    if test in s:
        cnt += 1

print(cnt)
