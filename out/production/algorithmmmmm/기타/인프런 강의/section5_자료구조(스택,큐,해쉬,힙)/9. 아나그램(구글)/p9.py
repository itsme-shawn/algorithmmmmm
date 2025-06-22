import sys
from collections import Counter, deque

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    # for fileNum in range(6, 7):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    w1 = Counter(list(sys.stdin.readline().rstrip()))
    w2 = list(sys.stdin.readline().rstrip())
    for x in w2:
        if x in w1.keys():
            w1[x] -= 1
        else:
            break

    for val in w1.values():
        if val != 0:
            print("NO")
            break
    else:
        print("YES")

    # 로직 끝
