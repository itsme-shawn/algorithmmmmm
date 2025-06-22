import sys
import time

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline
    start = time.time()

    # 로직 시작
    t = int(read())  # 바꿔야하는 지폐 금액
    k = int(read())  # 동전가짓수
    coins = list()  # 동전 금액리스트
    nums = list()  # 동전 개수리스트
    cnt = 0

    for _ in range(k):
        a, b = map(int, read().split())
        coins.append(a)
        nums.append(b)

    def dfs(L, cur):
        global cnt
        if cur > t:
            return
        if L == k:
            if cur == t:  # 구하는 케이스
                cnt += 1
            return
        else:
            for i in range(nums[L] + 1):  # 해당 동전 0개~최대개수 까지 가지수 생성
                dfs(L + 1, cur + (coins[L] * i))  # 동전종류 * 개수

    dfs(0, 0)
    print(cnt)

    # 로직 끝
    print(f"실행시간 : {time.time() - start}\n")
