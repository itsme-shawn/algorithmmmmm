import sys


# 리턴값 : (-1 : 실패) , (0 : 이동완료), (1 : 성공)
def tilt_up(rx, ry, bx, by):
    global cnt
    cnt += 1  # 기울인 횟수
    while True:
        # 탈출조건 1 : 둘 다 벽 또는 장애물에 도달 시
        if board[rx - 1][ry] == "#" and board[bx - 1][by] == "#":
            break

        # R 이동
        rx -= 1

        # B 이동
        bx -= 1

        # R이 빠졌는지 체크
        check_r = board[rx][ry] == "0"

        # B가 빠졌는지 체크
        check_b = board[bx][by] == "0"

        # R은 빠지고 B 는 안 빠지면 성공 (1,0)
        if check_r and (not check_b):
            return (1, (rx, ry, bx, by))
        # 둘 다 안 빠졌으면 한 번 더 이동 (0,0)
        elif not check_r and not check_b:
            continue
        # B 가 빠지면 실패인 경우 (0,1), (1,1)
        else:
            return (-1, (rx, ry, bx, by))
    return (0, (rx, ry, bx, by))


# 리턴값 : (-1 : 실패) , (0 : 이동완료), (1 : 성공)
def tilt_down(rx, ry, bx, by):
    global cnt
    cnt += 1  # 기울인 횟수
    while True:
        # 탈출조건 1 : 둘 다 벽 또는 장애물에 도달 시
        if board[rx + 1][ry] == "#" and board[bx + 1][by] == "#":
            break

        # R 이동
        rx += 1

        # B 이동
        bx += 1

        # R이 빠졌는지 체크
        check_r = board[rx][ry] == "0"

        # B가 빠졌는지 체크
        check_b = board[bx][by] == "0"

        # R은 빠지고 B 는 안 빠지면 성공 (1,0)
        if check_r and (not check_b):
            return (1, (rx, ry, bx, by))
        # 둘 다 안 빠졌으면 한 번 더 이동 (0,0)
        elif not check_r and not check_b:
            continue
        # B 가 빠지면 실패인 경우 (0,1), (1,1)
        else:
            return (-1, (rx, ry, bx, by))
    return (0, (rx, ry, bx, by))


# 리턴값 : (-1 : 실패) , (0 : 이동완료), (1 : 성공)
def tilt_left(rx, ry, bx, by):
    global cnt
    cnt += 1  # 기울인 횟수
    while True:
        # 탈출조건 1 : 둘 다 벽 또는 장애물에 도달 시
        if board[rx][ry - 1] == "#" and board[bx][by - 1] == "#":
            break

        # R 이동
        ry -= 1

        # B 이동
        by -= 1

        # R이 빠졌는지 체크
        check_r = board[rx][ry] == "0"

        # B가 빠졌는지 체크
        check_b = board[bx][by] == "0"

        # R은 빠지고 B 는 안 빠지면 성공 (1,0)
        if check_r and (not check_b):
            return (1, (rx, ry, bx, by))
        # 둘 다 안 빠졌으면 한 번 더 이동 (0,0)
        elif not check_r and not check_b:
            continue
        # B 가 빠지면 실패인 경우 (0,1), (1,1)
        else:
            return (-1, (rx, ry, bx, by))
    return (0, (rx, ry, bx, by))


# 리턴값 : (-1 : 실패) , (0 : 이동완료), (1 : 성공)
def tilt_right(rx, ry, bx, by):
    global cnt
    cnt += 1  # 기울인 횟수
    while True:
        # 탈출조건 1 : 둘 다 벽 또는 장애물에 도달 시
        if board[rx][ry + 1] == "#" and board[bx][by + 1] == "#":
            break

        # R 이동
        ry += 1

        # B 이동
        by += 1

        # R이 빠졌는지 체크
        check_r = board[rx][ry] == "0"

        # B가 빠졌는지 체크
        check_b = board[bx][by] == "0"

        # R은 빠지고 B 는 안 빠지면 성공 (1,0)
        if check_r and (not check_b):
            return (1, (rx, ry, bx, by))
        # 둘 다 안 빠졌으면 한 번 더 이동 (0,0)
        elif not check_r and not check_b:
            continue
        # B 가 빠지면 실패인 경우 (0,1), (1,1)
        else:
            return (-1, (rx, ry, bx, by))
    return (0, (rx, ry, bx, by))


def dfs(rx, ry, bx, by):
    global flag

    if cnt == 10:
        flag = 1
        print(-1)
        return

    if flag == 1:
        return

    for i in range(4):
        if i == 0:
            # 위
            res, (nrx, nry, nbx, nby) = tilt_up(rx, ry, bx, by)
            if res == -1:
                flag = 1
                return
            elif res == 0:  # 이동완료
                dfs(nrx, nry, nbx, nby)
            elif res == 1:  # 성공
                print(cnt)
                flag = 1
                return
        elif i == 1:
            # 오
            res, (nrx, nry, nbx, nby) = tilt_right(rx, ry, bx, by)
            if res == -1:
                flag = 1
                return
            elif res == 0:  # 이동완료
                dfs(nrx, nry, nbx, nby)
            elif res == 1:  # 성공
                print(cnt)
                flag = 1
                return
        elif i == 2:
            # 아래
            res, (nrx, nry, nbx, nby) = tilt_down(rx, ry, bx, by)
            if res == -1:
                flag = 1
                return
            elif res == 0:  # 이동완료
                dfs(nrx, nry, nbx, nby)
            elif res == 1:  # 성공
                print(cnt)
                flag = 1
                return
        elif i == 3:
            # 왼
            res, (nrx, nry, nbx, nby) = tilt_left(rx, ry, bx, by)
            if res == -1:
                flag = 1
                return
            elif res == 0:  # 이동완료
                dfs(nrx, nry, nbx, nby)
            elif res == 1:  # 성공
                print(cnt)
                flag = 1
                return


# 위, 오, 아래, 왼
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
direction = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
cnt = 0
flag = 0

rx, ry, bx, by = 0, 0, 0, 0


for i in range(N):
    for j in range(M):
        if board[i][j] == "B":
            bx, by = i, j
        elif board[i][j] == "R":
            rx, ry = i, j

dfs(rx, ry, bx, by)
