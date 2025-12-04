import sys
# sys.stdin = open("in.txt","r")
read = sys.stdin.readline

n = int(read())

mp,mf,ms,mv = map(int, read().split())

ingd = [list(map(int, read().split())) for _ in range(n)] # ingredients

result = float('inf')
min_set = []

def dfs(L, cp, cf, cs, cv, price, cur_ingd):
    global result, min_set
    if L == n:
        if cp>=mp and cf>=mf and cs>=ms and cv>=mv and price < result:
            result = price
            min_set = cur_ingd
        return
    if sum(ingd[L][0:5]): # 영양분이 존재하는 경우만 영양소 추가
        dfs(L+1, cp+ingd[L][0], cf+ingd[L][1], cs+ingd[L][2], cv+ingd[L][3], price+ingd[L][4], cur_ingd + [L+1]) # 0-index 출력형식 때문에 cur_ingd 에 L+1 을 추가
    dfs(L+1, cp, cf, cs, cv, price, cur_ingd)

dfs(0,0,0,0,0,0,[])

if len(min_set):
    print(result)
    print(" ".join(map(str,min_set)))
else:
    print(-1)


    




