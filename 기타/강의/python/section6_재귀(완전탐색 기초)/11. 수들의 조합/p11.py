import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n, k = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    cnt = 0

    def dfs(L, cur):
        global cnt
        if L == k:
            if sum(cur) % m == 0:
                cnt += 1
            return
        else:
            for num in nums:
                if cur and num <= cur[-1]:
                    continue
                else:
                    dfs(L + 1, cur + [num])

    dfs(0, [])
    print(cnt)

    # 로직 끝
