import sys

sys.stdin = open("in5.txt", "rt")

n = int(input())
lst = []

for _ in range(n):
    lst.append(list(map(int, input().split())))

prize = [0] * len(lst)

for i in range(len(lst)):
    numSet = list(set(lst[i]))
    l = len(numSet)

    # 다 같은 경우
    if l == 1:
        prize[i] = 10000 + numSet[0] * 1000
    # 다 다른 경우
    elif l == 3:
        prize[i] = max(numSet) * 100
    # 2개 같고 하나 다른 경우
    else:
        if lst[i][0] == lst[i][1]:
            prize[i] = 1000 + lst[i][0] * 100
        elif lst[i][0] == lst[i][2]:
            prize[i] = 1000 + lst[i][0] * 100
        else:
            prize[i] = 1000 + lst[i][1] * 100

print(max(prize))
