import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    lst = [list(map(int, input().split())) for _ in range(7)]
    cnt = 0

    for i in range(7):
        for j in range(2, 5):
            # 행 체크
            for k in range(1, 3):
                if lst[i][j - k] != lst[i][j + k]:
                    break
            else:
                cnt += 1

            # 열 체크
            for k in range(1, 3):
                if lst[j - k][i] != lst[j + k][i]:
                    break
            else:
                cnt += 1

    print(cnt)

    # 로직 끝

    print()
