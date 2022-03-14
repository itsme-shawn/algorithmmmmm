import sys

read = sys.stdin.readline


n = int(read())
board = [list(map(int, read().split())) for _ in range(n)]

res = []
min_diff = float("inf")


def dfs(L, cur):
    global min_diff
    if L == n // 2:
        team_a = res  # res 는 조합으로 뽑힌 배열
        team_b = list(set(range(1, n + 1)) - set(res))
        # ex. n = 4 일 때 team_a == [1,3] , team_b : == [2,4] 이런 식으로 됨

        sum_a, sum_b = 0, 0
        for i in range(len(team_a)):
            for j in range(i + 1, len(team_b)):
                sum_a += (
                    board[team_a[i] - 1][team_a[j] - 1]
                    + board[team_a[j] - 1][team_a[i] - 1]
                )
                sum_b += (
                    board[team_b[i] - 1][team_b[j] - 1]
                    + board[team_b[j] - 1][team_b[i] - 1]
                )
        min_diff = min(min_diff, abs(sum_a - sum_b))

        return
    else:
        for i in range(cur + 1, n + 1):
            res.append(i)
            dfs(L + 1, i)
            res.pop()


dfs(0, 0)
print(min_diff)
