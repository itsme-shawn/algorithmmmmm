import sys
from collections import deque

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    # for fileNum in range(6, 7):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    num, delete_cnt = map(int, sys.stdin.readline().split())
    num = deque(str(num))
    cnt = 0
    res = []
    flag = 0
    l = len(num)
    for i in range(l):
        temp = num.popleft()  # num 에서 뽑고, res 스택에 들어갈 수
        for _ in range(len(res)):  # 전체 res 길이만큼 돈다.
            if temp > res[-1]:  # temp 가 스택의 마지막 수보다 크다면
                res.pop()
                cnt += 1  # 삭제한 횟수 1 증가
                if cnt == delete_cnt:  # 주어진 삭제횟수를 채운다면 break
                    flag = 1
                    break
        res.append(temp)
        if flag == 1:
            break
    res.extend(num)  # 남은 num 들 추가해줌
    res = res[: l - delete_cnt]  # 실제로 있어야 하는 개수만큼만 슬라이싱
    print("".join(res))

    # 로직 끝
