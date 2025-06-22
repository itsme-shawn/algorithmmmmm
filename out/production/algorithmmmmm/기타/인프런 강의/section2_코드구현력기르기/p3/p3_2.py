import sys
import time
from itertools import combinations

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline
    start_time = time.time()

    # 로직 시작
    n, k = map(int, read().split())
    lst = list(map(int, read().split()))
    res = []

    for combi in combinations(lst, 3):
        res.append(sum(combi))
    res = list(set(res))
    res.sort(reverse=True)
    print(res[k - 1])

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
