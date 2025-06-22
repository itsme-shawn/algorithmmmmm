import sys

sys.stdin = open("in5.txt", "rt")

n = int(input())

lst = list(map(int, input().split()))


def digit_sum(x):
    result = 0
    i = len(str(x)) - 1  # 자릿수-1
    while i >= 0:
        tmp = x // (10 ** i)
        x -= tmp * (10 ** i)
        result += tmp
        i -= 1
    return result


result = []
for i in range(n):
    result.append(digit_sum(lst[i]))

M = max(result)
for i in range(n):
    if result[i] == M:
        print(lst[i], end=" ")
print()
