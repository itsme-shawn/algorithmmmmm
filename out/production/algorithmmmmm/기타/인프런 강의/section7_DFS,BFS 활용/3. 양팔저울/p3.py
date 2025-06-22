import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")
    read = sys.stdin.readline

    # 로직 시작
    k = int(read())
    weights = list(map(int, read().split()))
    # weights.sort(reverse=True) # 굳이 할 필요없음
    possible = set()  # 가능한 무게들 담을 집합

    def dfs(v, cur):
        if v == k:
            if cur > 0:  # 결과가 0보다 클때만 possible 에 추가
                possible.add(cur)
            return
        else:
            dfs(v + 1, cur + weights[v])  # 추 더하기
            dfs(v + 1, cur - weights[v])  # 추 빼기
            dfs(v + 1, cur)  # 추 아예 안넣기

    dfs(0, 0)
    S = set(range(1, sum(weights) + 1))  # 1~최대무게 집합
    print(len(S - possible))

    # 로직 끝
