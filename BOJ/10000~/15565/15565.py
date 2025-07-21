import sys

read = sys.stdin.readline

N, K = map(int, read().split())
dolls = list(map(int, read().split()))
# 1: 라이언, 2 : 어피치

idx = []

for i in range(len(dolls)):
    if dolls[i] == 1:
        idx.append(i)
        
minn = N

if len(idx) < K:
    print(-1)
else:
    for j in range(0, len(idx)):
        lt = j
        rt = j + (K-1)
        if rt >= len(idx):
            break
        cur = (idx[rt] - idx[lt]) + 1 
        if cur < minn:
            minn = cur     
    print(minn)
        