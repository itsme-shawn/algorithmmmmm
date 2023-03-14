# 숫자 카드 게임
import sys

sys.stdin = open("in2.txt", "rt")
read = sys.stdin.readline

n, m = map(int, read().split())
board = [list(map(int, read().split())) for _ in range(n)]
maxx = int(-1e9)
for row in board:
    maxx = max(maxx, min(row))

print(maxx)
