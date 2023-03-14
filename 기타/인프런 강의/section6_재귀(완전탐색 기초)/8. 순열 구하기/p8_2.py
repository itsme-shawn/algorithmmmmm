import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n, m = map(int, sys.stdin.readline().split())
    cnt = 0
    cur = []

    def dfs(L):
        global cnt
        if L == m:
            print(" ".join(map(str, cur)))
            cnt += 1
            return
        else:
            for i in range(1, n + 1):
                if i in cur:
                    continue
                else:
                    cur.append(i)  # dfs 하기 전에 값 push
                    dfs(L + 1)
                    cur.pop()  # dfs 끝나면 이전스택값을 돌려줘야 하므로 pop

    dfs(0)
    print(cnt)

    # 로직 끝
