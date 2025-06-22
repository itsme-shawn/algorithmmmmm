import sys

n, m = map(int, input().split())
lst = list(map(int, input().split()))

best = -1  # m에 최대한 가까운 합

lst.sort()
flag = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            tmp = lst[i] + lst[j] + lst[k]  # 현재 루프에서의 합
            if tmp == m:  # 조건1: 같으면 루프 모두 탈출
                best = m
                flag = 1
                break
            elif (tmp < m) and (m - tmp < m - best):  # 조건2
                best = tmp
            elif tmp > m:  # 조건3 : tmp 가 m보다 크면 탈출
                break
        if flag == 1:
            break
    if flag == 1:
        break
print(best)
