import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n = int(input())

    def dfs(v):
        if v == n + 1:
            for i in range(1, n + 1):
                if check[i] == 1:
                    print(i, end=" ")
            print()
            return
        else:
            check[v] = 1
            dfs(v + 1)
            check[v] = 0
            dfs(v + 1)

    check = [0] * (n + 1)
    dfs(1)
    # 로직 끝
