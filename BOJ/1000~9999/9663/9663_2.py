# 시간초과 해결

import sys

read = sys.stdin.readline

n = int(read())


queen_pos = []  # 인덱스가 행, 값이 열. ex. [2,4] : 0행 2열, 1행 4열에 퀸이 위치
# queen_pos[i] : i번째 행에서 퀸이 놓인 열의 위치
cnt = 0


def dfs(x):  # x : 행
    global cnt

    if x == n:
        cnt += 1
        return
    else:
        for y in range(n):  # x 행에서의 모든 열(y) 순회
            flag = True  # 초기값

            # (x,y) 에 퀸이 올때, 이전 행들의 퀸 (row, queen_pos[row]) 에 의해 안 죽는지 확인
            # 세로 : queen_pos[row] == y => 같은 열(세로)에 놓인 퀸임
            # 대각 : 가로길이 : x - row , 세로길이 : abs(y-queen_pos[row]) => 둘이 같다면 대각선에 놓인 퀸임
            for row in range(len(queen_pos)):
                if queen_pos[row] == y or x - row == abs(y - queen_pos[row]):
                    flag = False
                    break  # return 해주면 안됨! (현재 스택에서 남은 다른 열(y)도 검사해야함)

            # 이전 행들의 퀸에 의해 안 죽으므로 유망한 노드
            if flag:
                queen_pos.append(y)
                dfs(x + 1)
                queen_pos.pop()


dfs(0)
print(cnt)
