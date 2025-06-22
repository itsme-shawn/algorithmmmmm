import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n, m = map(int, sys.stdin.readline().split())
    nums = list(range(1, n + 1))
    cnt = 0
    select = [0] * m  # m 개 선택되므로 m 개만 생성

    def dfs(L):
        global cnt
        if L == m:  # m 개 선택되면 종료
            print(" ".join(map(str, select)))
            cnt += 1
            return
        else:
            for i in range(n):  # 각 레벨 당 탐색할 자식노드가 n 개씩 생김 => 노드 당 dfs n번 해야함
                select[L] = nums[i]  # select 의 현재 레벨 인덱스에 선택된 숫자를 덮어씌움
                dfs(L + 1)

    dfs(0)
    print(cnt)

    # 로직 끝
