import sys
from collections import deque

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    # for fileNum in range(6, 7):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    order = deque(sys.stdin.readline())  # 필수과목순서 원본
    n = int(sys.stdin.readline())
    for i in range(n):
        order_copy = order.copy()  # 필수과목순서 복사본 (복사한 이유는 pop을 할 것이기 때문이다.)
        check = deque(sys.stdin.readline())  # 체크할 수업계획
        possible = [order_copy.popleft()]  # 현재 들어도 되는 필수과목
        while check:
            temp = check.popleft()  # 수업계획에서 한 과목 pop
            if temp in order:  # pop 한 과목이 필수과목이고
                if order_copy and temp in possible:  # 들어도 되는 필수과목이면
                    possible.append(order_copy.popleft())  # 들어도되는 과목리스트에 다음과목을 추가
                elif temp not in possible:  # 필수과목인데도 들을수 없는 과목이면 NO
                    print("NO")
                    break
        else:
            print("YES")

    # 로직 끝
