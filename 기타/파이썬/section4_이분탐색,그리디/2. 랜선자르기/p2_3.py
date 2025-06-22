import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    # for fileNum in range(6, 7):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작

    n, m = map(int, input().split())
    lst = []
    for _ in range(n):
        lst.append(int(input()))

    start = 1
    end = max(lst)
    res = 0

    def get_lines(length):
        cnt = 0
        for x in lst:
            cnt += x // length
        return cnt

    while start <= end:
        mid = (start + end) // 2
        cnt = get_lines(mid)
        if cnt >= m:
            res = mid
            start = mid + 1
        else:
            end = mid - 1

    print(res)

    # 로직 끝

    print()
