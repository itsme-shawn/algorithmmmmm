import sys

N = int(sys.stdin.readline())

numbers = set(list(map(int, sys.stdin.readline().split())))

for item in sorted(numbers):
    print(item, end=" ")
