import sys
import time

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(0, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline
    start_time = time.time()

    # 로직 시작
    n, c = map(int, read().split())
    pos = [int(read()) for _ in range(n)]

    pos.sort()

    def get_horse(dis):
        ep = pos[0]
        cnt = 1

        for i in range(1, len(pos)):
            if pos[i] - ep >= dis:
                ep = pos[i]
                cnt += 1
        return cnt

    lt = 1
    rt = pos[-1] - pos[0]

    while lt <= rt:
        mid = (lt + rt) // 2
        if get_horse(mid) >= c:
            res = mid
            lt = mid + 1
        else:
            rt = mid - 1

    print(res)

    # 로직 끝

    print(f"실행시간 : {time.time() - start_time}\n")
