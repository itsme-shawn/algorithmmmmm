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
    cnt = 0

    def dfs(v, visited):
        global cnt
        if v == n:
            cnt += 1
            for x in visited:
                print(x, end=" ")
            print()
        else:
            for i in range(1, n + 1):
                # 그래프가 이어져 있고, 방문하지 않은 노드 일때만 dfs 탐색
                if graph[v][i] == 1 and i not in visited:
                    dfs(i, visited + [i])  # dfs 재귀로 깊게 들어감

    dfs(1, [1])  # visited 에 1 집어넣고 시작
    print(cnt)

    # 로직 끝
