# 순회결과를 절반씩 쪼개가면 레벨별로 트리저장

import sys
# sys.stdin = open("in.txt", "r")
read = sys.stdin.readline

k = int(read())
inorders = list(map(int, read().split())) # 중위순회로 방문한 순서 (입력값)

levels = [[] for _ in range(k)] # 각 레벨 별 노드 저장할 정답 배열

i = 0

def build(L, start, end):
    if L == k:
        return
    mid = (start+end) // 2
    levels[L].append(inorders[mid])
    # print(f"{L=} {start=} {end=} {mid=} {inorders[mid]}")
    build(L+1, start, mid-1)
    build(L+1, mid+1, end)

build(0,0,2**k-2)

for level in levels:
    print(*level)