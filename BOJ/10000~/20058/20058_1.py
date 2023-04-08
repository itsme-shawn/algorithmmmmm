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
new_board = [[0] * board_len for _ in range(board_len)]  # 회전한 Board 저장 용

total = 0
ice_size = []
retry = False


def tmp_print():
    print("")
    for i in range(board_len):
        print(new_board[i])


def bfs(x, y):
    deq = deque()
    deq.append((x, y))
    ice_temp = 0

    while deq:
        v = deq.popleft()
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if 0 <= nx < board_len and 0 <= ny < board_len:
                if visited[nx][ny] == 0 and new_board[nx][ny] > 0:
                    visited[nx][ny] = 1
                    ice_temp += 1
                    deq.append((nx, ny))
    ice_size.append(ice_temp)


for L in commands:
    if retry:
        board = copy.deepcopy(new_board)

    # 2^L 단위로 나뉜 격자를 시계방향 90도 회전
    # 회전
    if L > 0:
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
    temp = []

    # 체크 배열 값 할당
    for i in range(board_len):
        for j in range(board_len):
            ice_cnt = 0
            if new_board[i][j] == 0:
                continue  # 승우 추가
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < board_len and 0 <= ny < board_len:
                    if new_board[nx][ny] > 0:
                        ice_cnt += 1
            if ice_cnt < 3 and new_board[i][j] > 0:
                temp.append((i, j))

    for i, j in temp:
        if new_board[i][j] > 0:
            new_board[i][j] -= 1

    # tmp_print()

    retry = True

visited = [[0] * 2**n for _ in range(2**n)]
for i in range(board_len):
    for j in range(board_len):
        if new_board[i][j] and not visited[i][j]:
            # visited = [[0] * 2**n for _ in range(2**n)] 승우 수정 (위로 옮김)
            bfs(i, j)

for i in range(board_len):
    total += sum(new_board[i])

print(total)
if ice_size:
    print(max(ice_size))
else:
    print(0)
