import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n, m = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))

    start = max(lst)
    end = sum(lst)

    def check(size):
        total = 0
        cnt = 1  # cd 갯수
        for item in lst:
            total += item
            if total > size:
                cnt += 1
                total = item
        return cnt

    while start <= end:
        mid = (start + end) // 2
        if check(mid) <= m:
            ans = mid
            end = mid - 1  # 이미 가능하면 크기를 더 줄일수있는 방향으로
        else:
            start = mid + 1  # 지금 안되므로 크기 더 키워야함

    print(ans)

    # 로직 끝

    print()
