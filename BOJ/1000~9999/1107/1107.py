import sys

n = int(input())
m = int(input())
broken = []
if m != 0:
    broken = list(map(int, sys.stdin.readline().split()))
button = list(range(0, 10))

possible = list(set(button) - set(broken))

channel = list(str(n))


low_num = n
while low_num > 0:
    for x in list(map(int, str(low_num))):
        if x not in possible:
            low_num -= 1
            break
    else:
        break

high_num = n
while high_num <= 999999:
    for x in list(map(int, str(high_num))):
        if x not in possible:
            high_num += 1
            break
    else:
        break

low_cnt = len(str(low_num)) + (n - low_num)
high_cnt = len(str(high_num)) + (high_num - n)

print(min(abs(n - 100), low_cnt, high_cnt))
