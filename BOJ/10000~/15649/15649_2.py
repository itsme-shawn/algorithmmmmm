import sys

input = sys.stdin.readline().rstrip

n, m = map(int, input().split())

# 함수스택의 지역변수(매개변수) 이용
def dfs(L, cur):
    if L == m:
        for i in range(m):
            print(cur[i], end=" ")
        print()
        return
    else:
        for num in range(1, n + 1):
            if num in cur:
                continue
            else:
                temp = cur + [num]
                dfs(L + 1, temp)  # dfs(L+1, cur+[num]) 도 가능

                # 그런데 이상하게도 아래처럼 하면 안 됨. 왜 그럴까? 위랑 완전 똑같은 코드라 생각하는데... 재귀 인자를 넘겨줄 때, 변수에 변화를 줬어도 변수명이 같으면 안되는건가?
                # cur.append(num)
                # dfs(L+1, cur)


dfs(0, [])
