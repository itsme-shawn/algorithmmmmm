import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline

    # 로직 시작
    nums = list(range(1, 21))

    for _ in range(10):
        s, e = map(int, read().split())
        temp = nums[s - 1 : e]
        nums[s - 1 : e] = temp[::-1]

    print(nums)

    # 로직 끝

    print()
