import sys
import time
from collections import deque

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline
    start_time = time.time()

    # 로직 시작
    board = [list(map(int, read().split())) for _ in range(7)]
    visited = [[0] * 7 for _ in range(7)]
    visited[0][0] = 1
    cnt = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def dfs(x, y):
        global cnt
        if (x, y) == (6, 6):  # 좌표가 (6,6) 이면 dfs 종료 후 cnt 1 증가
            cnt += 1
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx <= 6
                and 0 <= ny <= 6
                and visited[nx][ny] == 0
                and board[nx][ny] == 0
            ):
                visited[nx][ny] = 1  # dfs 실행 전 방문 처리
                dfs(nx, ny)
                visited[nx][ny] = 0  # dfs 종료 후 방문 해제

    dfs(0, 0)
    print(cnt)

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
