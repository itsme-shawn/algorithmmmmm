import sys
import time

# 다시 풀어보기

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline
    start_time = time.time()

    # 로직 시작
    board = [list(map(int, read().split())) for _ in range(10)]
    visited = [[0] * 10 for _ in range(10)]

    dx = [0, 0, 1]
    dy = [-1, 1, 0]
    # 왼,오,아래 => 사다리는 아래보다 왼,오래가 우선순위가 높으므로 이 순서 지켜줘야함!

    def dfs(x, y, start):
        global flag
        if flag == 1:  # 이미 끝까지 도달했는데 도착지점이 1이였던 경우 -> 바로 return 으로 들어오자마자 끝내버림
            return
        if x == 9:
            if board[x][y] == 2:
                print(start)
            else:
                flag = 1  # dfs 가 백트랙해서 2에 도달하는 경우 방지용 flag
                return
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < 10
                and 0 <= ny < 10
                and board[nx][ny] >= 1
                and visited[nx][ny] == 0
            ):  # 1 아니면 2
                visited[nx][ny] = 1
                dfs(nx, ny, start)

    for i in range(10):
        visited = [[0] * 10 for _ in range(10)]  # 방문 초기화
        if board[0][i] == 1:
            visited[0][i] = 1
            flag = 0  # flag 도 매 dfs 마다 0 으로 초기화
            dfs(0, i, i)

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
