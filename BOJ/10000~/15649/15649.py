import sys

input = sys.stdin.readline().rstrip

n, m = map(int, input().split())
res = [0] * m

# res 전역리스트 사용
def dfs(L):
    if L == m:
        for i in range(m):
            print(res[i], end=" ")
        print()
        return
    else:
        for num in range(1, n + 1):
            if num in res:
                continue
            else:
                res[L] = num
                dfs(L + 1)
                res[L] = 0


dfs(0)
