import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n, target = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    # print(nums)

    start = 0
    end = len(nums) - 1
    res = -1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            res = mid
            break
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    if res != -1:
        print(res + 1)
    else:
        print("not found")

    # 로직 끝

    print()
