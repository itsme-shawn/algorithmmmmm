import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n, m = map(int, sys.stdin.readline().split())
    score = [0] * n
    time = [0] * n
    for i in range(n):
        score[i], time[i] = map(int, sys.stdin.readline().split())
    maxx = -1

    def dfs(L, cur_score, cur_time):
        global maxx
        if cur_time > m:  # L == n 보다 위에서 분기처리 해줘야함
            return
        if L == n:
            if cur_score > maxx:
                maxx = cur_score
            return
        else:
            dfs(L + 1, cur_score + score[L], cur_time + time[L])
            dfs(L + 1, cur_score, cur_time)

    dfs(0, 0, 0)
    print(maxx)

    # 로직 끝
