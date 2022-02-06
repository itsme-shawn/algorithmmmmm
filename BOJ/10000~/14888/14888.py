import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
oper = list(map(int, sys.stdin.readline().split()))
maxx = -2147000000
minn = 2147000000


def dfs(L, cur):
    global maxx, minn
    if L == n - 1:
        if cur > maxx:
            maxx = cur
        if cur < minn:
            minn = cur
        return
    else:
        for i in range(len(oper)):
            if oper[i]:
                oper[i] -= 1
                if i == 0:
                    dfs(L + 1, cur + a[L + 1])
                if i == 1:
                    dfs(L + 1, cur - a[L + 1])
                if i == 2:
                    dfs(L + 1, cur * a[L + 1])
                if i == 3:
                    if cur > 0:
                        dfs(L + 1, cur // a[L + 1])
                    else:
                        dfs(L + 1, -((-cur) // a[L + 1]))
                oper[i] += 1


dfs(0, a[0])
print(maxx)
print(minn)
