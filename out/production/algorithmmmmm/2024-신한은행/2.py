n, m = map(int, input().split())


def dfs(L, num, cur):
    if L == m:
        ans.append(cur)
        return

    for i in range(num, n + 1):
        dfs(L + 1, i + 1, cur + [i])


ans = []
dfs(0, 1, [])

print(ans)

# def solution(n, q, ans):
