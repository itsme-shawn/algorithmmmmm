import sys
import time

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline
    start_time = time.time()

    # 로직 시작
    n, m = map(int, read().split())  # n : 행,열 길이, m : 피자집 선택개수

    board = [list(map(int, read().split())) for _ in range(n)]

    pizzas = []  # 피자가게 저장 리스트
    houses = []  # 집 저장 리스트
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                houses.append((i, j))
            if board[i][j] == 2:
                pizzas.append((i, j))

    combies = []  # 조합으로 뽑은 인덱스들이 담길 리스트
    # ex. [[0, 1, 2], [0, 1, 3], [0, 1, 4], [0, 1, 5], .... ]

    # 조합 리스트 생성 (combies)
    def dfs(L, cur, select):  # L : 레벨, cur : 현재 뽑은 수(인덱스), select : 뽑은 수 리스트
        if L == m:
            combies.append(select)
        else:
            for i in range(cur + 1, len(pizzas)):
                dfs(L + 1, i, select + [i])

    dfs(0, -1, [])  # for문에서 cur+1 때문에 초기값 -1 로 해줘야함

    res = float("inf")
    for combi in combies:  # combi : 피자가게 리스트에서 m 개 선택한 피자가게의 인덱스 ex. [0,1,2]
        dist = 0  # 현재 선택된 피자가게 리스트에서의 피자배달거리
        for house in houses:  # 집 리스트에서 집 하나씩 순회
            temp = float("inf")  # temp : 특정 집에서의 피자배달거리
            for idx in combi:  # 피자가게 루프 돌면서 특정 집에서의 피자배달거리(최소거리) 구함
                temp = min(
                    temp,
                    abs(house[0] - pizzas[idx][0]) + abs(house[1] - pizzas[idx][1]),
                )
            dist += temp  # 최종 피자배달거리에 특정 집의 배달거리 누적으로 더함

        # res(현재까지의 최소 피자배달거리) 와 dist(선택된 피자가게들에 대한 피자배달거리) 의 최소 구하기
        res = min(res, dist)

    print(res)

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
