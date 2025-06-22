import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 7):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline

    # 로직 시작
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    lt = 0
    rt = 1
    tot = a[0]
    cnt = 0
    while True:
        if tot < m:
            if rt < n:
                tot += a[rt]
                rt += 1
            else:
                break
        elif tot == m:
            cnt += 1
            tot -= a[lt]
            lt += 1
        else:
            tot -= a[lt]
            lt += 1
    print(cnt)

    # 로직 끝

    print()
