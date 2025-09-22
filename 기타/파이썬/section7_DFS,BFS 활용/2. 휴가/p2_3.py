import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline

    # 로직 시작
    n = int(read())

    lists = list(list(map(int, read().split())) for _ in range(n))
    lists.insert(0, [0,0])
    print(lists)
    res = 0

    def dfs(L, sum):
        # print("L",L,"sum",sum)
        global res
        if L == n+1:
            if sum>res:
                res = sum
                print("res", res)
            return
        else:
            if L + (lists[L][0] - 1) <= n:
                dfs(L+(lists[L][0]), sum+lists[L][1])
            dfs(L+1, sum)

    dfs(1,0)
    print(res)

    # 로직 끝
