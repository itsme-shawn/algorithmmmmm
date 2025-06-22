import sys

sys.stdin = open("in.txt", "rt")
read = sys.stdin.readline

nums = list(map(int, read().rstrip()))
res = nums[0]
for i in range(len(nums) - 1):
    # 현재 수(res) 가 0 또는 1 이거나, 다음 수(nums[i+1])가 0 또는 1 이면 더해야함.
    if res == 0 or res == 1 or nums[i + 1] == 0 or nums[i + 1] == 1:
        res += nums[i + 1]
    # 나머지 경우는 곱셈
    else:
        res *= nums[i + 1]

print(res)
