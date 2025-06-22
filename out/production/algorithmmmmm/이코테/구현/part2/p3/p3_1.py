# 실전) 왕실의 나이트
import sys

sys.stdin = open("in.txt", "rt")
read = sys.stdin.readline

dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]
cnt = 0

pos = list(read())
y, x = ord(pos[0]) - ord("a") + 1, int(pos[1])

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        cnt += 1

print(cnt)
