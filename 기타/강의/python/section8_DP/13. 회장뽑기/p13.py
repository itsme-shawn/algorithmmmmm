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
    n = int(read())
    MAX = 100

    dist = [[MAX] * (n + 1) for _ in range(n + 1)]  # 거리 최대값으로 초기화

    # 대각성분(자기자신)은 0 할당
    for i in range(1, n + 1):
        dist[i][i] = 0

    # 그래프 생성
    while True:
        a, b = map(int, read().split())
        if (a, b) == (-1, -1):
            break
        dist[a][b] = 1
        dist[b][a] = 1

    # 플로이드-와샬
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # 각 후보의 점수 리스트 (인덱스 편의를 위해 0 하나 삽입)
    scores = [0]
    for i in range(1, n + 1):
        scores.append(max(dist[i][1:]))

    # 회장 당선 점수
    min_score = min(scores[1:])
    # 후보 리스트
    hubo = []

    # 점수리스트 돌면서 회장 후보 저장
    for i in range(1, n + 1):
        if scores[i] == min_score:
            hubo.append(i)

    print(min_score, len(hubo))
    print(" ".join(map(str, hubo)))

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
