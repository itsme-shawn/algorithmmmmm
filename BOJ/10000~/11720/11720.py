import sys

n = int(sys.stdin.readline())

nums = map(int, list(sys.stdin.readline().rstrip()))

total = 0
for num in nums:
    total += num

print(total)
