# dfs 백트래킹

import sys

read = sys.stdin.readline

n = int(read())

hp_list = list(map(int, read().split()))
good_list = list(map(int, read().split()))

result = 0

def dfs(L, cur_good, cur_hp):
    global result

    # 탈출조건 1: 남은 hp <= 0
    if cur_hp <= 0:
        return

    # 탈출조건 2 / 정답체크 : L == n (모든 사람 전부 탐색)
    if L == n:
        result = max(result, cur_good)
        return
    
    dfs(L+1, cur_good+good_list[L], cur_hp-hp_list[L]) # 선택
    dfs(L+1, cur_good, cur_hp) # 미선택
    
dfs(0,0,100)
print(result)