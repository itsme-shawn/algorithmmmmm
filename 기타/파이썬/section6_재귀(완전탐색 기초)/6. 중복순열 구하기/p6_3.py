import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    N, M = map(int, input().split())

    nums = list(range(1, N + 1))
    check = [0] * M
    cnt = 0

    def dfs(L):
        global cnt
        if L == M:
            for c in check:
                print(nums[c], end=" ")
            print()
            cnt += 1
            return
        for i in range(len(nums)):
            check[L] = i
            dfs(L + 1)

    dfs(0)
    print(cnt)

    # 로직 끝
