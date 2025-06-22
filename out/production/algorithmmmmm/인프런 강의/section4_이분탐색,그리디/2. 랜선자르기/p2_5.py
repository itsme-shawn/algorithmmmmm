import sys
import time

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(0, 7):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline
    start_time = time.time()

    # 로직 시작
    k, n = map(int, read().split())
    lines = []
    for _ in range(k):
        lines.append(int(read()))

    lt = 0
    rt = max(lines)

    def cut(length):
        cnt = 0
        for line in lines:
            cnt += line // length
        return cnt

    while lt <= rt:
        mid = (lt + rt) // 2

        if cut(mid) < n:
            rt = mid - 1
        elif cut(mid) >= n:
            res = mid
            lt = mid + 1

    print(res)

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
