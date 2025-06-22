import sys

sys.stdin = open("in.txt", "rt")
read = sys.stdin.readline

n, m = map(int, read().split())
weights = list(map(int, read().split()))
weights.sort()
cnt = 0
for i in range(len(weights) - 1):
    for j in range(i + 1, len(weights)):
        if weights[i] < weights[j]:
            cnt += 1

print(cnt)
