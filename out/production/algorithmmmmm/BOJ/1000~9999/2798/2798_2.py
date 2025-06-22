import sys
from itertools import combinations

n, m = map(int, input().split())
lst = list(map(int, input().split()))

best = -1  # m에 최대한 가까운 합
lst.sort()

for pair in combinations(lst, 3):
    total = sum(pair)
    if total > m:  # m을 넘으면 continue 로 다음 루프로 넘어감
        continue
    else:
        best = max(best, total)

print(best)
