import sys

N, M = map(int, sys.stdin.readline().split())

result = (N-1) + (N * (M-1))

print(result)