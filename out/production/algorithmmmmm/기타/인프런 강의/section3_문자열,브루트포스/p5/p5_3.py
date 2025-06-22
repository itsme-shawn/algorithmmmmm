import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(6, 7):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline

    # 로직 시작
    n, m = map(int, read().split())
    lst = list(map(int, read().split()))
    cnt = 0
    summ = 0
    i = 0

    # 틀린 풀이
    # for j in range(0, n):
    #     summ += lst[j]
    #     if summ < m:
    #         continue
    #     if summ == m:
    #         cnt += 1
    #         summ -= lst[i]
    #         i += 1
    #     if summ > m:
    #         summ -= lst[i]
    #         i += 1
    #         if summ == m:
    #             cnt += 1

    print(cnt)

    # 로직 끝

    print()
