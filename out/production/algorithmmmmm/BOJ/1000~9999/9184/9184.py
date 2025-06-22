import sys

read = sys.stdin.readline

dp = dict()  # 리스트는 mutable 이라서 key 불가능이지만, 튜플은 key 가능

while True:
    a, b, c = map(int, read().split())
    if (a, b, c) == (-1, -1, -1):
        break

    def dfs(a, b, c):
        if (a, b, c) in dp.keys():
            return dp[(a, b, c)]
        else:
            if a <= 0 or b <= 0 or c <= 0:
                dp[(a, b, c)] = 1
            elif a > 20 or b > 20 or c > 20:
                dp[(a, b, c)] = dfs(20, 20, 20)
            elif a < b and b < c:
                dp[(a, b, c)] = (
                    dfs(a, b, c - 1) + dfs(a, b - 1, c - 1) - dfs(a, b - 1, c)
                )
            else:
                dp[(a, b, c)] = (
                    dfs(a - 1, b, c)
                    + dfs(a - 1, b - 1, c)
                    + dfs(a - 1, b, c - 1)
                    - dfs(a - 1, b - 1, c - 1)
                )
            return dp[(a, b, c)]

    print(f"w({a}, {b}, {c}) = {dfs(a, b, c)}")
