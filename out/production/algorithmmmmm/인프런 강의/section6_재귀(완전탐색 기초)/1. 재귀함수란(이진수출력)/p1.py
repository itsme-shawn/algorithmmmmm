import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    # for fileNum in range(6, 7):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    def recursion(n):
        if n > 0:
            recursion(n // 2)
            print(n % 2, end="")

    n = int(input())
    recursion(n)
    print()

    # 로직 끝
