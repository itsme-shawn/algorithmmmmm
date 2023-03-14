import sys

sys.stdin = open("in5.txt", "rt")

n = int(input())
cnt = 0

for num in range(2, n + 1):
    flag = 1  # true
    for i in range(2, int(n ** (1 / 2)) + 1):
        if i == num:
            continue
        if num % i == 0:
            flag = 0
            break
    if flag == 1:
        cnt += 1


print(cnt)
