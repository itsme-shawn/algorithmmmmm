import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline

    # 로직 시작
    lst = list(read())
    nums = []
    for ch in lst:
        if ch.isdecimal():
            nums.append(ch)

    num = int("".join(nums))
    print(num)

    cnt = 0

    for i in range(1, num + 1):
        if num % i == 0:
            cnt += 1

    print(cnt)

    # 로직 끝
    print()
