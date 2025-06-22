import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(0, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline

    # 로직 시작

    K, N = map(int, read().split())
    wires = [int(read()) for _ in range(K)]

    start, end = 1, max(wires)
    res = 0

    def get_total(mid):
        cnt = 0
        for wire in wires:
            cnt += wire // mid
        return cnt

    while start <= end:
        mid = (start + end) // 2

        if get_total(mid) >= N:
            res = mid
            start = mid + 1
        else:  # get_total(mid) < N
            end = mid - 1
    print(res)
    # 로직 끝

    print()
