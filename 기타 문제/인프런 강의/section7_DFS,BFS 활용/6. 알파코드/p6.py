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
    code = read().rstrip()
    cnt = 0

    def dfs(n, cur):
        global cnt
        if n == len(code):
            cnt += 1
            return
        else:
            a = int(code[n])  # 한 자리 수 저장
            b = 0  # 두 자리 수 저장
            if a == 0:  # 현재 가리키는 수가 0이면 dfs 종료함
                return  # dfs 를 실행하는 블록 안에서도 return 으로 dfs 종료시킬수 도 있음!
            if n < len(code) - 1:  # 두 자리 수 가져올 수 있을 때
                b = int(code[n : n + 2])

            if 1 <= a <= 9:  # 사실 이 조건은 안 써줘도 되는데 그냥 구색맞추기용
                dfs(n + 1, cur + chr(a + 64))
            if 10 <= b <= 26:  # b 는 26보다 클 수 있으므로 이 조건문 있어야함
                dfs(n + 2, cur + chr(b + 64))

    dfs(0, "")
    print(cnt)

    # 로직 끝
    print(f"실행시간 : {time.time() - start}\n")
