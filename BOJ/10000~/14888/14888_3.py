import sys
from itertools import permutations

read = sys.stdin.readline

n = int(read())
nums = list(map(int, read().split()))
operator = list(map(int, read().split()))
temp = ["+", "-", "*", "//"]
op = []

for i in range(4):
    for _ in range(operator[i]):
        op.append(temp[i])

maxx = float("-inf")
minn = float("inf")

for oper in permutations(op, n - 1):
    total = nums[0]
    for j in range(len(oper)):
        if oper[j] == "+":
            total += nums[j + 1]
        elif oper[j] == "-":
            total -= nums[j + 1]
        elif oper[j] == "*":
            total *= nums[j + 1]
        else:
            if total > 0:
                total //= nums[j + 1]
            else:
                total = -(-total // nums[j + 1])

    maxx = max(maxx, total)
    minn = min(minn, total)

print(maxx)
print(minn)
