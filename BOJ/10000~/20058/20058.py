import copy
import sys
from collections import deque

read = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


n, q = map(int, read().split())
visited = [[0] * 2**n for _ in range(2**n)]
board = [list(map(int, read().split())) for _ in range(2**n)]


commands = list(map(int, read().split()))
board_len = 2**n  # 전체 한 변 길이
new_board = copy.deepcopy(board)  # 회전한 Board 저장 용

total = 0
ice_total = 0
max_ice_area = 0
ice_area = 0
retry = False


def bfs(x, y):
    global ice_total, max_ice_area, ice_area
    deq = deque()
    deq.append((x, y))
    visited[x][y] = 1

    while deq:
        v = deq.popleft()
        ice_total += new_board[v[0]][v[1]]
        ice_area += 1
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if 0 <= nx < board_len and 0 <= ny < board_len:
                if visited[nx][ny] == 0 and new_board[nx][ny] > 0:
                    visited[nx][ny] = 1
                    deq.append((nx, ny))
    max_ice_area = max(max_ice_area, ice_area)


for L in commands:
    if L != 0:
        if retry:
            board = copy.deepcopy(new_board)

        # 2^L 단위로 나뉜 격자를 시계방향 90도 회전
        # 회전
        sub_len = 2**L  # 격자 한 변 길이

        for y in range(0, board_len, sub_len):  # 격자 시작 좌표 y축
            for x in range(0, board_len, sub_len):  # 격자 시작 좌표 x축
                for i in range(sub_len):
                    for j in range(sub_len):
                        new_board[y + j][x + sub_len - i - 1] = board[y + i][x + j]

        # for row in new_board:
        #     print("회전 후", row)
        # print()

        # 감소할 얼음 정보 배열
        melt = []

        # 감소하는 얼음 찾기
        for i in range(board_len):
            for j in range(board_len):
                ice_cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < board_len and 0 <= ny < board_len:
                        if new_board[nx][ny] > 0:
                            ice_cnt += 1
                if ice_cnt < 3 and new_board[i][j] > 0:
                    melt.append((i, j))

        # print(melt)

        for i, j in melt:
            if new_board[i][j]:
                new_board[i][j] -= 1

        # for row in new_board:
        #     print("얼음제거", row)
        # print()
    else:
        if new_board[0][0]:
            new_board[0][0] -= 1
        if new_board[0][-1]:
            new_board[0][-1] -= 1
        if new_board[-1][0]:
            new_board[-1][0] -= 1
        if new_board[-1][-1]:
            new_board[-1][-1] -= 1

        # for row in new_board:
        #     print("0일 때 제거", row)
        # print()

    retry = True


for i in range(board_len):
    for j in range(board_len):
        if new_board[i][j] and not visited[i][j]:
            ice_area = 0
            bfs(i, j)

print(ice_total)
print(max_ice_area)
