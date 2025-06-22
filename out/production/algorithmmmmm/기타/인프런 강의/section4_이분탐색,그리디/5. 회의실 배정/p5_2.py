import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline

    # 로직 시작
    n = int(read())

    schedule = [list(map(int, read().split())) for _ in range(n)]

    schedule.sort(key=lambda x: (x[-1], x[0]))

    cnt = 1
    cur_start = schedule[0][0]
    cur_end = schedule[0][1]

    for i in range(1, len(schedule)):
        if cur_end <= schedule[i][0]:
            cur_end = schedule[i][1]
            cnt += 1

    print(cnt)

    # 로직 끝

    print()
