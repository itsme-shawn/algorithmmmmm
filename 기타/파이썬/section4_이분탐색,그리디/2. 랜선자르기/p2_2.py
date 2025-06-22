import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    # for fileNum in range(6, 7):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작

    def Count(len):
        cnt = 0
        for x in Line:
            cnt += x // len
        return cnt

    k, n = map(int, input().split())
    Line = []
    res = 0
    largest = 0
    for i in range(k):
        tmp = int(input())
        Line.append(tmp)
        largest = max(largest, tmp)
    lt = 1
    rt = largest
    while lt <= rt:
        mid = (lt + rt) // 2
        if Count(mid) >= n:
            res = mid
            lt = mid + 1
        else:
            rt = mid - 1
    print(res)

    # 로직 끝

    print()
