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

    start = 1
    end = max(lines)

    def get_lines(mid):
        cnt = 0
        for line in lines:
            cnt += line // mid
        return cnt

    while start <= end:
        mid = (start + end) // 2
        if get_lines(mid) >= n:
            res = mid
            start = mid + 1
        else:
            end = mid - 1

    print(res)

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
