import sys

n, m = map(int, sys.stdin.readline().split())
a = []
b = []
for _ in range(n):
    a.append(sys.stdin.readline().rstrip())
for _ in range(m):
    temp = sys.stdin.readline().rstrip()
    if temp in a:
        b.append(temp)

b.sort()
print(len(b))
print("\n".join(b))
