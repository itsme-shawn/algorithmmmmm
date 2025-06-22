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
    visited = [[0] * n for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    res = []

    def bfs(x, y, rain):
        global cnt
        deq = deque()
        deq.append((x, y))
        while deq:
            v = deq.popleft()
            for i in range(4):
                nx = v[0] + dx[i]
                ny = v[1] + dy[i]
                if (
                    0 <= nx < n
                    and 0 <= ny < n
                    and board[nx][ny] > rain  # 강수량보다 높이가 높아야함
                    and visited[nx][ny] == 0  # 미 방문노드여야함
                ):
                    visited[nx][ny] = 1  # 방문 처리
                    deq.append((nx, ny))  # 탐색노드 큐에 추가
        cnt += 1  # bfs 종료 -> 영역 1 증가

    # rain 만큼 반복
    for rain in range(0, 101):
        cnt = 0
        # rain 마다 전 영역 탐색으로 새롭게 하기 때문에 기존 방문여부 초기화해줘야함!!!
        visited = [[0] * n for _ in range(n)]
        # 주어진 강수량(rain)으로 전 영역 bfs
        for i in range(n):
            for j in range(n):
                if board[i][j] > rain and visited[i][j] == 0:
                    visited[i][j] = 1
                    bfs(i, j, rain)

        if cnt == 0:  # cnt(안전영역)이 0이라는 것은 모두 잠겼다는 뜻이므로 rain 을 더 볼 필요없이 break
            break

        # 전 영역에 대해 bfs 반복문이 끝나면 cnt 에 고립된 영역 갯수가 저장됨
        res.append(cnt)

    print(max(res))

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
