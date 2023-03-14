# 큰 수의 법칙
import sys

sys.stdin = open("in.txt", "rt")
read = sys.stdin.readline

n, m, k = map(int, read().split())  # 배열크기, 숫자더하는횟수, 같은 수 연속횟수제한
nums = list(map(int, read().split()))
nums.sort(reverse=True)

res = nums[0] * k * (m // k) + nums[1] * (m % k)
print(res)
