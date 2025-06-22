import sys

sys.stdin = open("in5.txt", "rt")

n, m = map(int, input().split())

res = {}

# res : { 합 : 빈도수 , ...} 딕셔너리
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # (i+j) 값이 res 딕셔너리 안에 있을 때 (기존에 존재할 때)
        if i + j in res:
            res[i + j] += 1
        else:
            res[i + j] = 0

# 빈도수 최대값
maxFreq = max(res.values())

lst = list(res.items())
for i in range(len(lst)):
    if lst[i][1] == maxFreq:
        print(lst[i][0], end=" ")
print()
