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
    lst = list(map(int, read().split()))
    aver = round(sum(lst) / n)
    minn = 10e9
    res = 0

    for i in range(len(lst)):
        tmp = abs(lst[i] - aver)  # 점수와 평균의 차이
        if tmp < minn:  # 차이가 최소일 때
            minn = tmp  # minn 갱신
            res = i  # 학생번호 정답 갱신
        elif tmp == minn:  # 차이가 기존의 최소와 같을 떼 (평균과 가까운 점수가 여러 개)
            if lst[i] > lst[res]:  # 현재 점수가 기존의 정답점수보다 클 때
                res = i

    print(aver, res + 1)  # 인덱스 + 1

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
