import sys

read = sys.stdin.readline

n = int(read())
nums = list(map(int, read().split()))
operator = list(map(int, read().split()))

maxx = float("-inf")
minn = float("inf")


def dfs(L, cur):
    global maxx, minn
    if L == n - 1:
        maxx = max(maxx, cur)
        minn = min(minn, cur)
        return
    else:
        for i in range(4):
            if operator[i] > 0:
                operator[i] -= 1
                if i == 0:
                    dfs(L + 1, cur + nums[L + 1])
                elif i == 1:
                    dfs(L + 1, cur - nums[L + 1])
                elif i == 2:
                    dfs(L + 1, cur * nums[L + 1])
                elif i == 3:
                    if cur > 0:
                        dfs(L + 1, cur // nums[L + 1])
                    else:
                        dfs(L + 1, -(-cur // nums[L + 1]))

                operator[i] += 1


dfs(0, nums[0])
print(maxx)
print(minn)
