import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 7):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    subsum = [0] * n
    subsum[0] = lst[0]
    for i in range(1, len(lst)):
        subsum[i] = subsum[i - 1] + lst[i]
    cnt = 0

    for i in range(len(subsum)):
        if subsum[i] == m:
            cnt += 1
            continue
        for j in range(i + 1, len(subsum)):
            if subsum[j] - subsum[i] == m:
                cnt += 1
                break

    print(cnt)

    # 로직 끝

    print()
