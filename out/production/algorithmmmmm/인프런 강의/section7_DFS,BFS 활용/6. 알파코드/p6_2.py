import sys
import time
from math import inf

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline
    start = time.time()

    # 로직 시작
    def DFS(L, P):  # L : code 에서 현재 가리키는 인덱스, P : res 인덱스
        global cnt
        if L == n:
            cnt += 1
            for j in range(P):
                print(chr(res[j] + 64), end="")
            print()
        else:
            for i in range(1, 27):
                if code[L] == i:
                    res[P] = i
                    DFS(L + 1, P + 1)
                elif i >= 10 and code[L] == i // 10 and code[L + 1] == i % 10:
                    res[P] = i
                    DFS(L + 2, P + 1)

    if __name__ == "__main__":
        code = list(map(int, input()))
        n = len(code)
        code.insert(n, -1)
        res = [0] * n
        cnt = 0
        DFS(0, 0)
        print(cnt)

    # 로직 끝
    print(f"실행시간 : {time.time() - start}\n")
