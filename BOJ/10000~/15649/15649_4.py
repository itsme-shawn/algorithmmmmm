import sys

input = sys.stdin.readline().rstrip

n, m = map(int, input().split())
res = []

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
                res.append(num)
                dfs(L + 1)
                res.pop()


dfs(0)
