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
    board = []
    for _ in range(n):
        board.append(list(map(int, read().split())))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    visited = [[0] * n for _ in range(n)]
    visited[n // 2][n // 2] = 1  # 정중앙 사각형부터 시작하므로 방문처리

    deq = deque()
    deq.append((n // 2, n // 2))  # 정중앙 사각형부터 시작
    L = 0  # 레벨(깊이)
    total = board[n // 2][n // 2]  # 누적합 변수

    while deq:
        # bfs 종료조건
        if L == n // 2:  # 상태트리의 깊이가 n//2 이면 break
            break

        size = len(deq)
        for _ in range(size):  # 레벨 체크용 for문 (일반적인 bfs 에서는 생략해도됨)
            v = deq.popleft()
            for i in range(4):  # 각 노드당 상,하,좌,우 탐색해야하므로 4번 반복
                x = v[0] + dx[i]
                y = v[1] + dy[i]
                if visited[x][y] == 0:  # 방문하지 않은 노드일때만 아래 로직 실행
                    total += board[x][y]  # 누적합에 더해줌
                    visited[x][y] = 1  # 방문처리
                    deq.append((x, y))  # 큐에 추가
        L += 1  # 한 레벨 끝났으므로 레벨 1 증가시켜줌
    print(total)

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
