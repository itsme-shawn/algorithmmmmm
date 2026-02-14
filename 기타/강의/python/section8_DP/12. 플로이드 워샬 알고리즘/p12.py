import sys
import time

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline
    start_time = time.time()

    # 로직 시작
    n, m = map(int, input().split())
    MAX = 10**8  # 무한대 상수 설정
    dis = [[MAX] * (n + 1) for _ in range(n + 1)]  # 무한대로 2차원배열 초기화
    for i in range(1, n + 1):
        dis[i][i] = 0  # 대각성분은 0 으로 초기화

    # 그래프 생성
    for i in range(m):
        a, b, c = map(int, input().split())  # a : 시작노드, b : 도착노드, c : 가중치
        dis[a][b] = c

    # 플로이드-와샬
    for k in range(1, n + 1):  # k : 중간노드
        for i in range(1, n + 1):  # i : 시작노드(행)
            for j in range(1, n + 1):  # j : 도착노드(열)
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

    # 출력
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dis[i][j] == MAX:  # 갈 수 없는 경우
                print("M", end=" ")
            else:
                print(dis[i][j], end=" ")
        print()

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
