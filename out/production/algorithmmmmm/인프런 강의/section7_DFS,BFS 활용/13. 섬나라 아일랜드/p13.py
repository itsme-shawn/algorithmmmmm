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

    # 상하좌우 + 대각선 : 8방향
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    res = []

    def bfs(x, y, cnt):
        deq = deque()
        deq.append((x, y))  # 큐에 시작노드 넣고 bfs 시작
        while deq:
            v = deq.popleft()  # 탐색할 노드 pop
            for i in range(8):  # 8방향 탐색
                nx = v[0] + dx[i]
                ny = v[1] + dy[i]
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:  # 방문가능
                    board[nx][ny] = 0  # 방문처리
                    cnt += 1  # 조건에 맞는 노드 탐색 횟수 증가시킴
                    deq.append((nx, ny))  # 방문한 노드 큐에 삽입
        # bfs 완료되면 cnt에 조건에 맞는 노드개수 저장됨
        res.append(cnt)

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                board[i][j] = 0  # 시작노드 방문해제 해줘야함
                bfs(i, j, 1)  # cnt 1부터 시작

    print(len(res))

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
