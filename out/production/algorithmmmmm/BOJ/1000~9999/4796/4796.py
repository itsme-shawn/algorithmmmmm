import sys

i = 0

while True:
    l, p, v = map(int, sys.stdin.readline().split())
    if (l, p, v) == (0, 0, 0):
        break
    i += 1
    res = (v // p) * l + min(l, v % p)
    print(f"Case {i}: {res}")
    # print("Case %d: %d" % (i, res))
