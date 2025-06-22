import sys

n, m = map(int, input().split())
lst = list(map(int, input().split()))

best = -1  # m에 최대한 가까운 합
lst.sort()

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if lst[i] + lst[j] + lst[k] > m:  # m을 넘으면 break 로 다음 루프로 넘어감
                break
            else:
                best = max(best, lst[i] + lst[j] + lst[k])

print(best)
