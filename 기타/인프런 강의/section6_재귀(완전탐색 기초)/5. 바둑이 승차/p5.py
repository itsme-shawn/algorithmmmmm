import sys
from decimal import MAX_EMAX

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    c, n = map(int, sys.stdin.readline().split())
    weights = [int(sys.stdin.readline()) for _ in range(n)]

    def dfs(v, total, all_sum):
        # total 은 선택한 값만 누적합한 것, all_sum 은 선택여부와 상관없이 탐색한 노드들의 값들을 모두 더한 값
        global maxx
        if v == n:  # 탈출조건
            if maxx < total < c:
                maxx = total
            if total == c:  # 가지치기 1 : leaf node 에서 total == c 이면 출력하고 프로그램을 종료
                maxx = total
                print(maxx)
                sys.exit()  # 프로그램 바로 종료
            return
        if total > c:  # 가지치기 2 : 탐색 중에 이미 c 보다 커지면 해당스택 종료
            return
        if total + (entire - all_sum) < maxx:
            # 가지치기 3 , total : 현재 선택한 노드의 누적합 , entire - all_sum : 남은 노드들의 전체 합
            # total + (entire - all_sum) : 현재 노드에서 모든 노드를 택할 때의 합 (현재 노드 기준 가능한 합의 최댓값)
            # 가능한 최댓값 이 현재의 최댓값 보다도 작다면 굳이 탐색할 필요없으므로 종료
            return
        else:
            dfs(v + 1, total + weights[v], all_sum + weights[v])
            dfs(v + 1, total, all_sum + weights[v])

    maxx = 0
    entire = sum(weights)  # 무게 리스트의 총 합
    dfs(0, 0, 0)
    print(maxx)

    # 로직 끝
