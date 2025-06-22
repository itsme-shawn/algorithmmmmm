# 시간초과

import sys

read = sys.stdin.readline

n = int(read())


dx = [1, 1, 1]
dy = [-1, 0, 1]
cnt = 0


def dfs(x, y):
    global cnt
    # 탈출조건 1 : 가면 안되는 곳(죽는 곳)일 때
    if (x, y) in check:
        return
    # 탈출조건 2 : 정상 종료
    if x == n - 1:  # x 가 마지막 행이라면 종료 (행 번호 0부터 시작하므로 -1 해줘야함)
        cnt += 1
        return
    else:
        check_cnt = 0
        for i in range(3):  # 방향 3개 (왼대각,아래,오른대각)
            for times in range(1, n):  # 한 칸만 보는게 아니라 끝까지 체크해야함 ( times : 곱하는 횟수 )
                nx = x + dx[i] * times
                ny = y + dy[i] * times
                if 0 <= nx < n and 0 <= ny < n:
                    check.append((nx, ny))
                    check_cnt += 1  # 현재 스택에서 추가한 check 좌표

        for j in range(n):
            dfs(x + 1, j)  # 다음 행에 있는 모든 열 dfs

        for _ in range(check_cnt):  # 현재 스택에서만 추가한 좌표만큼만 지워야함
            check.pop()


# 첫 번째 열(0열)에 있는 모든 열 dfs 해줌
for i in range(0, n):
    check = []
    dfs(0, i)

print(cnt)
