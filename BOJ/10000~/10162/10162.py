import sys

t = int(sys.stdin.readline())
times = [300, 60, 10]
res = []
for time in times:
    cnt = 0
    cnt += t // time
    res.append(cnt)
    t = t % time
if t == 0:
    print(" ".join(map(str, res)))
else:
    print(-1)
