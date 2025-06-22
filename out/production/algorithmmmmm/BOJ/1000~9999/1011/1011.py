import sys

sys.setrecursionlimit(10**8)

read = sys.stdin.readline

T = int(read())


def dfs(cur, y, move, cnt):
    global minn
    if cur == y and move[-1] == 1:
        minn = min(minn, cnt)
        return
    if cur > y:
        return

    for nxt_move in (move[-1] - 1, move[-1], move[-1] + 1):
        if nxt_move > 0:
            dfs(cur + nxt_move, y, move + [nxt_move], cnt + 1)


for _ in range(T):
    x, y = map(int, read().split())
    minn = float("inf")
    dfs(x, y, [0], 0)
    print(minn)
