import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    res = []  # 부분집합 리스트
    entire = sum(nums)  # 집합 전체 합

    def dfs(v, sub_total):
        global flag
        if flag == 1:  # flag 가 1로 설정되면 모든 스택들 바로바로 종료 (프로그램 종료와 비슷한 효과를 냄)
            return
        if v == n:  # 스택탈출
            if sub_total == entire - sub_total:
                print("YES")
                # sys.exit() # 프로그램 종료 제일 쉽게하는 방법. 이거 아니면 flag 써야함
                flag = 1
            return
        if sub_total > entire - sub_total:  # 이미 누적합이 전체의 절반보다 크다면, 현재 스택 종료
            return
        else:
            dfs(v + 1, sub_total + nums[v])
            if v != 0:  # 이 라인에서 v 값이 0 이 들어왔다는 것은 트리의 왼쪽 부분 탐색을 모두 마쳤다는 뜻이므로 멈춰도 된다.
                dfs(v + 1, sub_total)

    flag = 0  # flag 1 이면 프로그램 전체 종료
    dfs(0, 0)

    if flag == 0:
        print("NO")

    # 로직 끝
