import sys

n, m = map(int, sys.stdin.readline().split())
a = []
b = []
for _ in range(n):
    a.append(sys.stdin.readline().rstrip())
for _ in range(m):
    b.append(sys.stdin.readline().rstrip())

c = list(set(a) & set(b))
print(len(c))
print("\n".join(sorted(c)))
