import sys

n = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

minn = min(cost)
res = 0
i = 0
while i < len(cost) - 1:
    if cost[i] == minn:  # 현재도시 가격이 최소면, 남은도시 길이 한 번에 충전하고 끝
        res += cost[i] * sum(road[i:])
        break
    elif cost[i] <= cost[i + 1]:  # 현재도시 기름가격 <= 다음도시 기름가격 일 때
        j = i + 1
        # 현재도시 기름가격보다 비싼 도시 나올때까지 찾음
        while (j < len(cost) - 1) and cost[i] < cost[j]:
            j += 1
        # while 루프끝나면 j 가 현재보다 비싼도시
        res += cost[i] * sum(road[i:j])
        i = j
    elif cost[i] > cost[i + 1]:  # 현재도시 > 다음도시면 현재도시~다음도시 길이만큼만 충전
        res += cost[i] * road[i]
        i += 1
print(res)
