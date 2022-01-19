import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n = int(input())
    ans = []

    def recursion(i, flag, res):
        if i > n:  # 탈출조건
            if flag == True:
                ans.append(res)  # res(부분집합 한 개)를 최종 답(ans)에 추가
            return
        if i != 0:  # 시작을 i = 0 으로 해서, 0은 제외하기 위함
            if flag == True:  # flag 가 True 일 때만 부분집합에 포함
                res += f"{i} "
        recursion(i + 1, True, res)  # True : 해당 수 포함
        recursion(i + 1, False, res)  # False : 해당 수 미 포함

    recursion(0, True, "")
    # print(ans) # ['1 2 3 ', '1 2 ', '1 3 ', '1 ', '2 3 ', '2 ', '3 ', '']

    for x in range(len(ans) - 1):  # 맨 마지막에는 공집합이 들어와서 그 전까지만 루프 실행
        print(ans[x])
    # 로직 끝
