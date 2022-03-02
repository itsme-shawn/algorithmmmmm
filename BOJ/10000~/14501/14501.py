import sys

read = sys.stdin.readline

n = int(read())
days = [0]
moneys = [0]
for _ in range(n):
    a, b = map(int, read().split())
    days.append(a)
    moneys.append(b)

res = 0


def dfs(day, money):
    global res
    # 탈출조건1 : res 최신화
    if day == n + 1:
        if money > res:
            res = money
        return
    # 탈출조건2 : 상담날짜가 초과되는 경우는 바로 return
    if day > n + 1:
        return
    else:
        dfs(day + days[day], money + moneys[day])  # 해당날짜 상담
        dfs(day + 1, money)  # 상담안하고 다음날로 건너뜀


dfs(1, 0)
print(res)
