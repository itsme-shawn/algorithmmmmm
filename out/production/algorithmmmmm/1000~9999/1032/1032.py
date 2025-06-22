import sys

read = sys.stdin.readline

n = int(read())
lst = [read().rstrip() for _ in range(n)]
res = []
for i in range(len(lst[0])):
    temp = lst[0][i]
    for j in range(1, len(lst)):
        if temp != lst[j][i]:
            res.append("?")
            break
    else:
        res.append(temp)

print("".join(res))
