import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n, m = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))

    lst.sort()

    def binarySearch(lst, target, start=0, end=None):
        if end is None:
            end = len(lst) - 1
        if start > end:
            return False
        mid = (start + end) // 2

        if target < lst[mid]:
            return binarySearch(lst, target, start, mid - 1)
        elif target > lst[mid]:
            return binarySearch(lst, target, mid + 1, end)
        else:
            return mid

    print(binarySearch(lst, m) + 1)

    # 로직 끝

    print()
