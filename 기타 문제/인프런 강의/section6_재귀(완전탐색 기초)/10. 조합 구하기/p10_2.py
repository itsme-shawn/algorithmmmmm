import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    n, m = map(int, sys.stdin.readline().split())
    visited = [0] * n  # 방문한 노드의 인덱스 저장
    res = [0] * m  # 답 저장
    nums = list(range(1, n + 1))  # [1,2,...n]
    cnt = 0

    def dfs(L):
        global cnt
        if L == m:
            print(" ".join(map(str, res)))
            cnt += 1
            return
        else:
            for i in range(len(nums)):
                if not visited[i] and nums[i] > res[L - 1]:
                    visited[i] = 1  # 해당 인덱스 방문처리
                    res[L] = nums[i]  # 결과에 push
                    dfs(L + 1)
                    visited[i] = 0  # 해당 인덱스 방문해제
                    res[L] = 0  #

    dfs(0)
    print(cnt)

    # 로직 끝
