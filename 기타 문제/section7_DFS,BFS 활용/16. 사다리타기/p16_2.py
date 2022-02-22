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
    dx = [0, 0, -1]
    dy = [-1, 1, 0]

    def DFS(x, y):
        ch[x][y] = 1
        if x == 0:
            print(y)
        else:
            for i in range(3):
                nx = x + dx[i]
                ny = y + dy[i]
                if (
                    0 <= nx < 10
                    and 0 <= ny < 10
                    and board[nx][ny] == 1
                    and ch[nx][ny] == 0
                ):
                    DFS(nx, ny)

    board = [list(map(int, input().split())) for _ in range(10)]
    ch = [[0] * 10 for _ in range(10)]
    for y in range(10):
        if board[9][y] == 2:
            DFS(9, y)

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
