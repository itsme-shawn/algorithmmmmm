import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n, m = map(int, input().split())
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        i, j = map(int, input().split())
        graph[i][j] = 1
    visited = [0] * (n + 1)  # 고정리스트
    cnt = 0
    visited[1] = 1  # 1번노드 방문처리 하고 시작
    path = []  # 경로 저장용
    path.append(1)  # 1번노드 경로에 추가하고 시작

    def dfs(v):
        global cnt
        if v == n:
            cnt += 1
            for x in path:
                print(x, end=" ")
            print()
        else:
            for i in range(1, n + 1):
                # 그래프가 이어져 있고, 방문하지 않은 노드 일때만 dfs 탐색
                if graph[v][i] == 1 and visited[i] == 0:
                    visited[i] = 1  # 방문처리
                    path.append(i)  # 경로에 추가
                    dfs(i)  # dfs 재귀로 깊게 들어감
                    # 모든 경로를 구해야하기 때문에 아래 작업 수행
                    # path.pop()  # dfs 끝난 후에는 경로에서 제거
                    # visited[i] = 0  # dfs 끝난 후에는 방문처리 해제

    dfs(1)
    print(cnt)

    # 로직 끝
