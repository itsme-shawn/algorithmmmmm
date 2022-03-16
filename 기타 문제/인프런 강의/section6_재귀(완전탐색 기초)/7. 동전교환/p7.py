import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 7):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    change = int(sys.stdin.readline())

    coins.sort(reverse=True)

    def dfs(n, cur):
        if cur == 0:
            print(n)
            sys.exit()
        else:
            for coin in coins:
                if cur - coin < 0:
                    continue
                else:
                    dfs(n + 1, cur - coin)

    dfs(0, change)

    # 로직 끝
