import sys

n = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(n)]
stack = []
res = []
cur = 1  # 조심
flag = 0

for x in lst:
    while cur <= x:
        stack.append(cur)
        res.append("+")
        cur += 1

    if stack[-1] == x:
        stack.pop()
        res.append("-")
    else:
        print("NO")
        break
else:
    for v in res:
        print(v)
