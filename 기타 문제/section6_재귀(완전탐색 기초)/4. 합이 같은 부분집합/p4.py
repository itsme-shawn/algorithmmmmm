import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 2):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    res = []  # 부분집합 리스트
    entire = sum(nums)  # 집합 전체 합

    def dfs(v):
        if v == n:
            temp = []  # 부분집합 한 개
            for i in range(n):
                if check[i] == 1:
                    temp.append(nums[i])
            res.append(temp)
            return
        else:
            # 왼쪽서브트리
            check[v] = 1
            dfs(v + 1)
            # 오른쪽서브트리
            if v != 0:  # 이 라인에서 v 값이 0 이 들어왔다는 것은 트리의 왼쪽 부분 탐색을 모두 마쳤다는 뜻이므로 멈춰도 된다.
                check[v] = 0
                dfs(v + 1)

    check = [0] * n  # nums 의 인덱스를 담는 스택
    dfs(0)
    # print(res)  # ex. [ [1,2,3],[1,2],[1,3],[1] ]
    for subset in res:
        total = sum(subset)
        if total == entire / 2:  # 부분집합의 합이 전체의 반절이면 YES
            print("YES")
            break
    else:
        print("NO")

    # 로직 끝
