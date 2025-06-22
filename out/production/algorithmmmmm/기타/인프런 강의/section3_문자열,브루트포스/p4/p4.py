import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n = int(input())
    lst_1 = list(map(int, input().split()))

    m = int(input())
    lst_2 = list(map(int, input().split()))

    merge = []

    i = j = 0
    for _ in range(n + m):
        # lst_1 끝까지 간 경우
        if i == n:
            merge += lst_2[j:]
            break
        # lst_2 끝까지 간 경우
        elif j == m:
            merge += lst_1[i:]
            break
        elif lst_1[i] <= lst_2[j]:
            merge.append(lst_1[i])
            i += 1
        else:
            merge.append(lst_2[j])
            j += 1

    print(" ".join(map(str, merge)))

    # 로직 끝

    print()
