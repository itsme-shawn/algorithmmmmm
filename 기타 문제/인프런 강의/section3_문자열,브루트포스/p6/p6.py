import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))

    rowSum = [0] * n
    colSum = [0] * n
    # rowSum = colSum = [0] * n 하면 주소값까지 같아져서 같은 객체가 되버림!
    dgSum = [0] * 2

    for i in range(n):
        rowSum[i] = sum(arr[i])

    for i in range(n):
        for j in range(n):
            colSum[i] += arr[j][i]

    for i in range(n):
        dgSum[0] += arr[i][i]
        dgSum[1] += arr[i][n - 1 - i]

    rowSumMax = max(rowSum)
    colSumMax = max(colSum)
    dgSumMax = max(dgSum)
    print(max(rowSumMax, colSumMax, dgSumMax))

    # 로직 끝

    print()
