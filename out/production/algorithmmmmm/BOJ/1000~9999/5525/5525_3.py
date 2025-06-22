import sys

read = sys.stdin.readline

n = int(read())
m = int(read())
s = read().rstrip()

# 서브태스크2 통과
ans = 0
cnt = 0
i = 0

while i < m:
    if s[i : i + 3] == "IOI":
        cnt += 1
        if cnt == n:
            cnt -= 1
            ans += 1
        i += 2
    else:
        i += 1
        cnt = 0


print(ans)
