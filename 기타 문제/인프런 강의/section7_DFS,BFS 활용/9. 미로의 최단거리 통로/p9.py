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
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    deq = deque()
    deq.append((0, 0))
    visited = [[0] * 7 for _ in range(7)]
    res = [[0] * 7 for _ in range(7)]  # 현재 노드의 경로 수
    visited[0][0] = 1
    flag = 0

    while deq:
        v = deq.popleft()
        for i in range(4):
            x = v[0] + dx[i]
            y = v[1] + dy[i]
            if 0 <= x <= 6 and 0 <= y <= 6 and board[x][y] == 0 and visited[x][y] == 0:
                # x,y 둘다 격자안에 존재하고, 갈 수 있는 노드면서 미방문인 노드일때
                visited[x][y] = 1  # 방문처리
                res[x][y] = res[v[0]][v[1]] + 1  # 경로 수 = 부모노드 + 1
                deq.append((x, y))  # 큐에 추가
                if (x, y) == (6, 6):
                    flag = 1
                    print(res[6][6])
                    break
        if flag == 1:
            break
    else:  # 도착할 수 없는 경우
        print(-1)

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
