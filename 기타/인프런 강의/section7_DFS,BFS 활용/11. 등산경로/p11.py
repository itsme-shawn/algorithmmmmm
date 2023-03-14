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
    n = int(read())
    board = [list(map(int, read().split())) for _ in range(n)]
    minn = float("inf")
    maxx = float("-inf")
    min_coord = (0, 0)  # 최솟값 좌표
    max_coord = (0, 0)  # 최댓값 좌표
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 최솟값좌표, 최댓값좌표 찾기
    for i in range(n):
        for j in range(n):
            if board[i][j] < minn:
                minn = board[i][j]
                min_coord = (i, j)
            if board[i][j] > maxx:
                maxx = board[i][j]
                max_coord = (i, j)

    visited = [[0] * n for _ in range(n)]
    visited[min_coord[0]][min_coord[1]] = 1
    cnt = 0

    def dfs(x, y):
        global cnt
        if (x, y) == max_coord:
            cnt += 1
            return
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (
                    0 <= nx < n
                    and 0 <= ny < n
                    and visited[nx][ny] == 0
                    and board[nx][ny] > board[x][y]  # 다음 구역 높이 > 현재 구역 높이 일때만
                ):
                    visited[nx][ny] = 1
                    dfs(nx, ny)
                    visited[nx][ny] = 0

    dfs(min_coord[0], min_coord[1])
    print(cnt)

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
