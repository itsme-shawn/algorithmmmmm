import sys

sys.stdin = open("in1.txt", "rt")

n, k = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

sum = []

for a in range(len(lst) - 2):
    for b in range(a + 1, len(lst) - 1):
        for c in range(b + 1, len(lst)):
            sum.append(lst[a] + lst[b] + lst[c])

sum = list(set(sum))
sum.sort(reverse=True)

print(sum[k - 1])
