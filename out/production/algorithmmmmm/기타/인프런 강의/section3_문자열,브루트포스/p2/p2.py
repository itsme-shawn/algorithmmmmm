import sys


# 약수개수 구하는 함수
def findDivisor(n):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
    return cnt


# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    string = input()

    onlyNum = []  # 숫자만 추출한 리스트

    for item in string:
        if not item.isalpha():
            onlyNum.append(item)

    Num = int("".join(onlyNum))

    print(Num)
    print(findDivisor(Num))

    # 로직 끝
    print()
