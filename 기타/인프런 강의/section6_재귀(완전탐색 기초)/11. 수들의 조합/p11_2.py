import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(0, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    m = int(input())
    cur = []
    check = []
    cnt = 0

    def dfs(L):
        global cnt
        if L == k:
            if sum(cur) % m == 0:
                cnt += 1
            return
        else:
            for i in range(n):
                if not check or i > check[-1]:
                    check.append(i)
                    cur.append(nums[i])
                    dfs(L + 1)
                    check.pop()
                    cur.pop()

    dfs(0)
    print(cnt)

    # 로직 끝
