import sys
import time

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline
    start_time = time.time()

    # 로직 시작
    n, m = map(int, read().split())
    songs = list(map(int, read().split()))

    lt = max(songs)
    rt = sum(songs)

    def get_cd(capa):
        cnt = 1  # 초기값 0이 아니라 1임에 주의!
        temp = 0
        for song in songs:
            temp += song
            if temp <= capa:
                continue
            else:
                cnt += 1
                temp = song
        return cnt

    while lt <= rt:
        mid = (lt + rt) // 2
        if get_cd(mid) <= m:
            res = mid
            rt = mid - 1
        else:
            lt = mid + 1

    print(res)

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
