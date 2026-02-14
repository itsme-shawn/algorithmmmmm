import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 2):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n = int(input())
    nums = list(range(1, n + 1))

    def dfs(v):
        if v == n:  # 스택탈출 조건
            for i in range(n):
                if check[i] == 1:
                    print(nums[i], end=" ")
            print()
            return
        else:
            # 왼쪽 서브트리 탐색
            check[v] = 1  # ch[v+1] 이 아님에 주의! 재귀호출에서 인자로 v+1 이 들어오므로 그냥 v 만 써주면 된다.
            dfs(v + 1)  # 계속 깊게 파고들어감
            # 오른쪽 서브트리 탐색
            check[v] = 0  # 자식노드 탐색끝나면 부모노드로 돌아가서 check 값 0으로 수정
            dfs(v + 1)

    check = [0] * n  # 부분집합에 포함할 nums 의 인덱스 담는 리스트
    dfs(0)
    # 로직 끝
