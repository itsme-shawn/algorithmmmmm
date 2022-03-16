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
    start, end = map(int, read().split())
    MAX = 10000
    visited = [0] * (MAX + 1)  # 방문 여부 리스트
    depth = [0] * (MAX + 1)  # 루트노드부터의 거리 계산

    visited[start] = 1  # 시작지점 방문처리
    depth[start] = 0  # 시작지점(루트노드)은 깊이 0

    deq = deque()
    deq.append(start)

    # bfs
    while deq:
        # 큐에서 pop 한 원소 확인
        cur = deq.popleft()  # 큐에서 하나 뽑음
        if cur == end:  # 뽑은 원소가 찾는 값이면 break
            break

        # pop한 원소의 자식노드를 큐에 append 하는 로직
        for nxt in (cur - 1, cur + 1, cur + 5):  # 자식노드값은 현재값-1/+1/+5
            if 0 <= nxt <= MAX:
                if visited[nxt] == 0:  # 자식노드가 방문하지 않은 노드일때만 아래 코드 실행
                    deq.append(nxt)  # 큐에 append
                    visited[nxt] = 1  # 방문처리
                    depth[nxt] = depth[cur] + 1  # 부모노드보다 루트노드까지의 깊이 1 증가

    print(depth[end])

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
