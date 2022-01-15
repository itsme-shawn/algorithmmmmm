import sys

n = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(n)]
max_idx = lst.index(max(lst))
for i in range(max_idx + 1):
    flag = 0
    temp = lst[i]
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            if temp < lst[j]:
                flag = 1  # 안 되는 경우
                break
            temp = lst[j]
    if flag == 1:
        print("NO")


if flag == 0:
    res = ["+"] * lst[0] + ["-"]
    maxx = 0
    for i in range(1, max_idx + 1):
        if lst[i - 1] > lst[i]:
            res += ["-"] * (lst[i - 1] - lst[i])
        else:
            res += ["+"] * (lst[i] - maxx) + ["-"]
        if lst[i] > maxx:
            maxx = lst[i]
    res += ["-"] * (len(lst) - max_idx - 1)

    print("\n".join(res))
