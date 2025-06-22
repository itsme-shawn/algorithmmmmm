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
    n, m = map(int, read().split())
    n_list = list(range(1, n + 1))
    m_list = list(range(1, m + 1))
    sum_dict = {}
    maxx = -(10e9)

    for i in n_list:
        for j in m_list:
            tmp = i + j
            if tmp not in sum_dict:
                sum_dict[tmp] = 1
            else:
                sum_dict[tmp] += 1
                if sum_dict[tmp] > maxx:
                    maxx = sum_dict[tmp]

    for key, val in sum_dict.items():
        if val == maxx:
            print(key, end=" ")
    print()

    # 로직 끝
    print(f"실행시간 : {time.time() - start_time}\n")
