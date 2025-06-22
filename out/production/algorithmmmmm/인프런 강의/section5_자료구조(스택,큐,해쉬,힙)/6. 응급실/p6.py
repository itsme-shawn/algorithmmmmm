import sys
from collections import deque

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    # for fileNum in range(6, 7):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n, m = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    q = deque([0, lst[i]] for i in range(n))
    q[m][0] = 1  # 문제에서 주어진 환자, q : [[선택여부,위험도],...]
    temp = 0
    cnt = 0

    def get_max(q):  # q 가 이차원리스트이기 때문에 최대 위험도 찾는 함수 따로 생성
        maxx = -1
        for i in range(len(q)):
            if q[i][1] > maxx:
                maxx = q[i][1]
        return maxx

    while q:
        if q[0][1] < get_max(q):  # q 의 첫번째 원소가 최댓값보다 작다면
            q.append(q.popleft())  # 순서 뒤로 밀림
        else:  # 첫 원소가 q에서 최댓값이라면
            temp = q.popleft()  # pop(진료)
            cnt += 1
            if temp[0] == 1:  # 주어진 환자라면 break
                break
    print(cnt)

    # 로직 끝
