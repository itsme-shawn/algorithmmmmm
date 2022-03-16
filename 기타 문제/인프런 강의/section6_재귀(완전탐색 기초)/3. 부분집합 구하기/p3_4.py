import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n = int(input())

    def dfs(v, cur):
        if v == n + 1:
            print(" ".join(map(str, cur)))
            return
        else:
            dfs(v + 1, cur + [v])
            dfs(v + 1, cur)

    dfs(1, [])
    # 로직 끝
