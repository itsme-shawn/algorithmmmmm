import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n, m = map(int, input().split())
    lst = list(map(int, sys.stdin.readline().split()))
    l = len(lst)

    lst.sort(reverse=True)

    lp = 0
    rp = l - 1
    cnt = 0

    while lp < rp:
        if lst[lp] + lst[rp] > m:
            cnt += 1
            lp += 1
        else:
            cnt += 1
            lp += 1
            rp -= 1

    if lp == rp:
        cnt += 1

    print(cnt)

    # 로직 끝

    print()
