import sys
read = sys.stdin.readline

n = int(read())
cnt = 0
for _ in range(n):
    string = read().rstrip()
    stk = [string[0]]
    for s in string[1:]:
        if s != stk[-1]:
            if s not in stk:
                stk.append(s)
            else:
                break
    else:
        cnt += 1

print(cnt)
