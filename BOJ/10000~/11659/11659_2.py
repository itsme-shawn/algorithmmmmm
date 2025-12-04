# 정답풀이 (dp)

import sys

read = sys.stdin.readline

def solution():
    n, m = map(int, read().split())
    nums = list(map(int, read().split()))
    dp = [0] * (n+1)
    for i, num in enumerate(nums):
        dp[i+1] = dp[i] + num
    for _ in range(m):
        i, j = map(int, read().split())
        print(dp[j]-dp[i-1])
        
if __name__ == "__main__":
    solution()