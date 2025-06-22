import sys

read = sys.stdin.readline

n = int(read())
m = int(read())
s = read().rstrip()

# p_n 생성
p = "I"
for _ in range(n):
    p += "OI"

# cf. count 는 non-overlapping
# 서브태스크 2 에서 시간초과

idx = 0
cnt = 0
while idx < m:
    if s[idx : idx + len(p)] == p:
        cnt += 1
        idx += 2
    else:
        idx += 1

print(cnt)
