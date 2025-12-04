# 시간초과 풀이

import sys

read = sys.stdin.readline

def solution():
    n, m = map(int, read().split())
    nums = list(map(int, read().split()))
    for _ in range(m):
        i, j = map(int, read().split())
        print(sum(nums[i-1:j]))


if __name__ == "__main__":
    solution()