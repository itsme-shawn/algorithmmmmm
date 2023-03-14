import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    # for fileNum in range(6, 7):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작

    k, n = map(int, sys.stdin.readline().split())
    wireList = [int(sys.stdin.readline()) for _ in range(k)]

    start = 1
    end = max(wireList)
    # lst = list(range(start, end + 1))
    # 사용하지 않는 위 문장 때문에 코드가 터졌다.
    # list 가 너무 크면 터지더라

    def isValid(l):
        total = 0
        for item in wireList:
            total += item // l
        if total >= n:
            return True
        else:
            return False

    while start <= end:
        mid = (start + end) // 2
        if isValid(mid):
            start = mid + 1
        else:
            end = mid - 1

    # 최종으로 나오는 mid 는 불가능한 경우 중 가장 작은 경우임. 따라서 -1을 해줘야함.
    # 이 이분탐색은 안되는 쪽에서 end 값을 줄이면서 계속 돌기 때문임.
    print(mid - 1)

    # 로직 끝

    print()
