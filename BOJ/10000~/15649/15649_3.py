import sys

input = sys.stdin.readline().rstrip

n, m = map(int, input().split())
res = [0] * m  # 일단 필요한 길이만큼 생성


# res 전역리스트 사용
def dfs(L):
    if L == m:
        for i in range(m):
            print(res[i], end=" ")
        print()
        return
    else:
        for num in range(1, n + 1):
            if num in res:
                continue
            else:
                res[L] = num  # 현재 값 push
                dfs(L + 1)
                res[L] = 0  # 현재 호출스택의 초기상태로 되돌려줌(pop)
        # dfs 호출 한 번이 끝났다는 것은 함수스택이 이전 스택으로 돌아온 것이므로
        # res 도 다시 이전 스택의 초기 상태로 돌려줘야 한다.


dfs(0)
