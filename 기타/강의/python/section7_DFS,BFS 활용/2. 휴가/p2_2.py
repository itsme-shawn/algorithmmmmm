import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline

    # 로직 시작
    def DFS(L, sum):
        global res
        if L == n + 1:
            if sum > res:
                res = sum
            return
        else:
            if L + T[L] <= n + 1:
                DFS(L + T[L], sum + P[L])
            DFS(L + 1, sum)

    if __name__ == "__main__":
        n = int(input())
        T = list()
        P = list()
        for i in range(n):
            a, b = map(int, input().split())
            T.append(a)
            P.append(b)
        res = -2147000000
        T.insert(0, 0)
        P.insert(0, 0)
        DFS(1, 0)
        print(res)

    # 로직 끝
