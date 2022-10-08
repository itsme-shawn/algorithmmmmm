import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline

    # 로직 시작
    n = int(read())
    nums1 = list(map(int, read().split()))
    m = int(read())
    nums2 = list(map(int, read().split()))

    nums = sorted((nums1 + nums2))

    print(" ".join(map(str, nums)))

    # 로직 끝

    print()
