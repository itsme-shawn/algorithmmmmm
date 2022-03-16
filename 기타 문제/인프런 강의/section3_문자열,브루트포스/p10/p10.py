import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    lst = [list(map(int, input().split())) for _ in range(9)]

    flag = 0  # 1이면 통과, 0이면 false

    # 행 검사
    for i in range(9):
        # set 형 변환 후 원소개수가 9개 그대로 나와야함
        if len(list(set(lst[i]))) == 9:
            flag = 1
        else:
            flag = 0
            break

    if flag == 1:
        # 열 검사
        for i in range(9):
            temp = []
            for j in range(9):
                temp.append(lst[j][i])
            if len(list(set(temp))) == 9:
                flag = 1
            else:
                flag = 0
                break

    if flag == 1:
        # 정사각형 검사
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if (
                    len(
                        list(
                            set(
                                lst[i][j : j + 3]
                                + lst[i + 1][j : j + 3]
                                + lst[i + 2][j : j + 3]
                            )
                        )
                    )
                    == 9
                ):
                    flag = 1
                else:
                    flag = 0
                    break

    if flag == 1:
        print("YES")
    else:
        print("NO")
    # 로직 끝

    print()
