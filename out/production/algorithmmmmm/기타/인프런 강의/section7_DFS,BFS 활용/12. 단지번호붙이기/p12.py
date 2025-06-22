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
    board = [list(map(int, read().rstrip())) for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    res = []

    # 따로 탈출조건은 없고 상하좌우에 1이 없을 때까지 dfs 실행하게 되면 알아서 빠져나온다.
    def dfs(x, y):
        global cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 1:  # 1 일때만 dfs 실행
                    board[nx][ny] = 0  # 방문 처리
                    cnt += 1
                    dfs(nx, ny)
                    # 방문 해제 하면 안 됨! (이 문제는 한 번 방문한 노드는 다른 호출스택에서도 방문하면 안 된다.)

    # board 전체 돌면서 dfs 실행
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:  # 1 일때만 dfs 실행
                cnt = 1  # 시작점도 집이므로 1 추가
                board[i][j] = 0  # 시작점 방문처리
                dfs(i, j)
                res.append(cnt)

    res.sort()
    print(len(res))
    print("\n".join(map(str, res)))

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
