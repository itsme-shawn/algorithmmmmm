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

idx = -1
cnt = 0
while True:
    idx = s.find(p, idx + 1)
    if idx == -1:
        break
    cnt += 1
print(cnt)
