import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(5, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n, m = map(int, sys.stdin.readline().split())
    combi = []

    def factorial(n):
        res = 1
        while n > 0:
            res *= n
            n = n - 1
        return res

    for i in range(0, n):
        combi.append(factorial(n - 1) // (factorial(n - 1 - i) * factorial(i)))

    def dfs(L, cur):
        if L == n:
            total = 0
            for i in range(n):
                total += cur[i] * combi[i]
            if total == m:
                print(" ".join(map(str, cur)))
                sys.exit()
            else:
                return
        else:
            for j in range(1, n + 1):
                if j in cur:
                    continue
                else:
                    dfs(L + 1, cur + [j])

    dfs(0, [])

    # 로직 끝
