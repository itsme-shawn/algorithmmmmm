import sys

n, m = map(int, sys.stdin.readline().split())
site = dict()
for _ in range(n):
    url, pw = map(str, sys.stdin.readline().split())
    site[url] = pw

find = [sys.stdin.readline().rstrip() for _ in range(m)]

for x in find:
    print(site[x])
