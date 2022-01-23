nums = list(map(int, input()))
if (0 not in nums) or (sum(nums) % 3 != 0):
    print(-1)
else:
    nums.sort(reverse=True)
    print("".join(list(map(str, nums))))
