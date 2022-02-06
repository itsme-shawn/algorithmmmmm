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
    n = int(read())
    moneys = []
    for _ in range(n):
        moneys.append(int(read()))
    result = {"A": 0, "B": 0, "C": 0}
    ans = float("inf")

    def dfs(L):
        global ans
        if L == n:
            temp = max(result.values()) - min(result.values())
            if temp < ans and len(set(result.values())) == 3:
                # 문제에서 세 사람의 총액이 모두 달라야한다고 했으므로
                ans = temp
            return
        else:
            for key in result.keys():  # key= 'A' , 'B', 'C'
                result[key] += moneys[L]
                dfs(L + 1)
                result[key] -= moneys[L]

    dfs(0)
    print(ans)

    # 로직 끝
    print(f"실행시간 : {time.time() - start}\n")
