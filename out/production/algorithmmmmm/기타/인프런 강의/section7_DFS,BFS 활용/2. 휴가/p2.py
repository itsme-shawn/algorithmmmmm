import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline

    # 로직 시작
    n = int(read())
    day = [0]
    cost = [0]
    for _ in range(n):
        a, b = map(int, read().split())
        day.append(a)
        cost.append(b)
    maxx = -1

    def dfs(v, cur_cost):
        global maxx
        # 탈출조건 1 : 현재 날짜 기준으로 상담하면 딱 휴가날짜가 딱 맞을때
        if v + day[v] == n + 1:
            cur_cost += cost[v]
            if cur_cost > maxx:
                maxx = cur_cost
            return
        # 탈출조건 2 : 휴가날짜초과
        if v > n:
            return
        else:
            if cur_cost > maxx:  # 최댓값 확인
                maxx = cur_cost
            # 현재 날 상담하기 (부분집합 포함)
            if v <= n and v + day[v] <= n + 1:  # 인덱스 초과가 떠서 조건문으로 처리해줬음
                dfs(v + day[v], cur_cost + cost[v])
            # 현재 날 pass (부분집합 제외)
            if v + 1 <= n:  # 인덱스 초과 때문에 조건문 처리
                dfs(v + 1, cur_cost)

    dfs(1, 0)
    print(maxx)

    # 로직 끝
