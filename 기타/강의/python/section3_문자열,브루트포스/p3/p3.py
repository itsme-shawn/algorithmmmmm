import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    lst = list(range(1, 21))
    for _ in range(10):
        start, end = map(int, input().split())
        tmp = lst[start - 1 : end]
        lst[start - 1 : end] = tmp[::-1]
    print(lst)
    # 로직 끝

    print()
