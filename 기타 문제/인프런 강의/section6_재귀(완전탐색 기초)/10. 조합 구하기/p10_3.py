import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n, m = map(int, sys.stdin.readline().split())
    nums = list(range(1, n + 1))
    cnt = 0

    def dfs(L, visited, cur):
        global cnt
        if L == m:
            print(" ".join(map(str, cur)))
            cnt += 1
            return
        else:
            for i in range(n):
                if i not in visited:
                    if cur and nums[i] < cur[-1]:
                        continue
                    else:
                        dfs(L + 1, visited + [i], cur + [nums[i]])

    dfs(0, [], [])
    print(cnt)

    # 로직 끝
