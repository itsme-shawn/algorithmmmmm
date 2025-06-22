n, m = map(int, input().split())


def dfs(n, m):
    stack = [(0, 1, [])]
    ans = []

    while stack:
        print("stack", stack)
        L, num, cur = stack.pop()

        if L == m:
            print(cur)
            ans.append(cur)
            continue
        for i in range(num, n + 1):
            stack.append((L + 1, i + 1, cur + [i]))

    return ans


ans = dfs(n, m)

print(ans)
