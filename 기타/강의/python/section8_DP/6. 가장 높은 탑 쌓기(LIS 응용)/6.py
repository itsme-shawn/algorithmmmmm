import sys
import time

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline
    start_time = time.time()

    # 로직 시작
    n = int(read())
    arr = [list(map(int, read().split())) for _ in range(n)]
    arr.sort(reverse=True)  # 이 문제는 입력순서대로 뽑는 문제가 아니므로 정렬해야함.
    # 정렬을 함으로써 기준2개(밑면,무게)를 기준1개(무게)로만 판단해서 감소수열을 만들 수 있다.
    arr.insert(0, 0)  # 인덱스 사용 편하게 하기 위해서 맨 앞에 0 삽입
    dp = [0] * (n + 1)  # 인덱스 사용 편하게 하기 위해서 사이즈 1 크게 생성

    AREA = 0
    HEIGHT = 1
    WEIGHT = 2
    dp[1] = arr[1][HEIGHT]  # base case (첫 번째 데이터의 높이)
    res = arr[1][HEIGHT]  # 매 루프마다 최댓값 저장하는 변수
    # res 초기값을 0 으로 하면 안 된다. 나머지 벽돌들이 첫 번째 벽돌보다 모두 무거운 벽돌이라면, 첫 벽돌의 높이가 답이 되어야 하므로

    for i in range(2, n + 1):
        maxx = 0
        # i 기준으로 왼쪽방향으로 진행
        for j in range(i - 1, 0, -1):
            # 감소수열이 가능한 경우 중에서 높이 최댓값 구함
            if arr[j][WEIGHT] > arr[i][WEIGHT] and dp[j] > maxx:
                maxx = dp[j]
        # dp[i] = i-1 까지 가능한 감소수열 최대높이 + 현재높이
        dp[i] = maxx + arr[i][HEIGHT]
        # 구한 dp[i] 와 res 를 비교
        if dp[i] > res:
            res = dp[i]

    print(res)

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
