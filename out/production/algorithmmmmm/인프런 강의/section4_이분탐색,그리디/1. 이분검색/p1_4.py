import bisect
import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(0, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline

    # 로직 시작
    n, m = map(int, read().split())
    nums = list(map(int, read().split()))

    nums.sort()

    start, end = 0, n - 1
    res = 0

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == m:
            res = mid
            break
        elif nums[mid] < m:
            start = mid + 1
        elif nums[mid] > m:
            end = mid - 1

    print(res + 1)

    # 로직 끝

    print()
