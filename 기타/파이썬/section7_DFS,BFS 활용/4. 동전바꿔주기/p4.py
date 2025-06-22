import sys
import time

# sys.setrecursionlimit(1000000)

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

    # 현재 기준, 남은 동전들을 모두 선택할 때의 금액
    def get_left(cur):
        res = 0
        for i in range(k):
            if coins[i] <= cur[-1]:
                res += coins[i] * nums[i]
        return res

    def dfs(cur):
        global cnt
        total = sum(cur)
        if cur and total + get_left(cur) < t:
            # 가지치기 1 : 남은 동전들을 모두 선택했는데도 불구하고 t보다 작다면 불가능한 케이스
            return
        if total > t:
            # 가지치기 2 : 현재까지 합이 t 보다 크면 불가능한 케이스
            return
        if total == t:
            # 정답케이스
            cnt += 1
            return
        else:
            for i in range(len(coins)):
                if cur and coins[i] > cur[-1]:
                    # 중복조합이랑 비슷하게 현재값이 cur[-1] 보다 크면 건너뜀
                    continue
                if nums[i] > 0:  # 동전이 존재할 때만 다음 dfs 실행할 수 있음
                    nums[i] -= 1  # dfs 시작 전에 동전 감소
                    dfs(cur + [coins[i]])
                    nums[i] += 1  # dfs 끝나면 다시 동전 증가

    dfs([])
    print(cnt)

    # 로직 끝
    print(f"실행시간 : {time.time() - start}\n")
