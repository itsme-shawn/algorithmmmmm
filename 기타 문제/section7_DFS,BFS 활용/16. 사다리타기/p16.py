import sys
import time
from collections import deque

# 다시 풀어보기

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(3, 4):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline
    start_time = time.time()

    # 로직 시작
    board = [list(map(int, read().split())) for _ in range(10)]
    visited = [[0] * 10 for _ in range(10)]

    dx = [0, 0, 1]
    dy = [1, -1, 0]
    # 왼, 오 , 아래

    def dfs(x, y, start):
        if x == 9:
            if board[x][y] == 2:
                print(start)
                sys.exit()
            else:
                return
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < 10
                and 0 <= ny < 10
                and board[nx][ny] >= 1  # 1 아니면 2
                and visited[nx][ny] == 0
            ):
                # 왼쪽길 존재하면, 오른쪽,아래방향 아예 못가게끔 막기
                if i == 0:
                    for j in range(1, 3):
                        if 0 <= x + dx[j] < 10 and 0 <= y + dy[j] < 10:
                            visited[x + dx[j]][y + dy[j]] = -1
                elif i == 1:
                    for j in range(0, 3):
                        if j == 1:
                            continue
                        if 0 <= x + dx[j] < 10 and 0 <= y + dy[j] < 10:
                            visited[x + dx[j]][y + dy[j]] = -1
                else:
                    for j in range(0, 2):
                        if 0 <= x + dx[j] < 10 and 0 <= y + dy[j] < 10:
                            visited[x + dx[j]][y + dy[j]] = -1
                visited[nx][ny] = 1  # 해당노드 방문처리
                dfs(nx, ny, start)

    for i in range(10):
        visited = [[0] * 10 for _ in range(10)]  # 방문 초기화
        if board[0][i] == 1:
            visited[0][i] = 1
            dfs(0, i, i)

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
