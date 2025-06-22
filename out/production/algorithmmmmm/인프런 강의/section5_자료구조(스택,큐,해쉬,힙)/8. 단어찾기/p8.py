import sys
from collections import Counter, deque

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    # for fileNum in range(6, 7):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n = int(input())
    word = dict()
    # 딕셔너리 만들기
    for _ in range(n):
        x = sys.stdin.readline().rstrip()
        if x not in word:
            word[x] = 1
        else:
            word[x] += 1

    # 딕셔너리에서 키에 해당하는 현재 값 1 감소
    for _ in range(n - 1):
        word[sys.stdin.readline().rstrip()] -= 1

    # 딕셔너리 순회하면서 값 1 인것 출력
    for key, val in word.items():
        if val == 1:
            print(key)

    # 로직 끝
