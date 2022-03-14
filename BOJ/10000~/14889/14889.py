import sys
from itertools import combinations, permutations

read = sys.stdin.readline

# print(list(combinations(range(1, 5), 2))) [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

n = int(read())
board = [list(map(int, read().split())) for _ in range(n)]

combi = list(combinations(range(1, n + 1), n // 2))

res = float("inf")

for i in range(len(combi) // 2):
    a = combi[i]
    b = combi[len(combi) - i - 1]
    a_sum, b_sum = 0, 0
    # a팀, b팀에서 2명씩 순열로 뽑아서 능력치 계산
    for r, c in permutations(a, 2):
        a_sum += board[r - 1][c - 1]
    for r, c in permutations(b, 2):
        b_sum += board[r - 1][c - 1]
    res = min(res, abs(a_sum - b_sum))

print(res)
