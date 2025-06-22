import sys

nums = list(sys.stdin.readline().rstrip())
print("".join(sorted(nums, reverse=True)))
