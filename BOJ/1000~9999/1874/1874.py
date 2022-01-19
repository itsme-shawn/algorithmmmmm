import sys

n = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(n)]
stack = []
res = []
nxt = 1  # 다음 번에 스택에 담을 숫자
flag = 0

for x in lst:
    while nxt <= x: 
        stack.append(nxt) # nxt 부터 x 까지 스택에 append
        res.append("+")
        nxt += 1 # nxt 1 증가

    if stack[-1] == x: # pop 가능
        stack.pop()
        res.append("-")
    else:
        print("NO")
        break
else:
    for v in res:
        print(v)
