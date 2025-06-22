import sys

n = int(input())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
lst.sort(key=lambda x: (x[1], x[0]))

end = 0
cnt = 0
for s, e in lst:
    if end <= s:
        cnt += 1
        end = e

print(cnt)
