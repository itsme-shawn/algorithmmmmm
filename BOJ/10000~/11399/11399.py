import sys

N = int(sys.stdin.readline())

time = list(map(int, sys.stdin.readline().split()))

time.sort(reverse=True)
result = 0
for idx in range(len(time)):
    result += (idx + 1) * time[idx]

print(result)
