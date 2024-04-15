# 삼성 2022-하반기-오전-1

import sys

read = sys.stdin.readline

X = 0
Y = 1
DIRECTION = 2
STAT = 3
GUN = 4

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
arrow = ["⬆️", "➡️", "⬇️", "⬅️"]

n, m, k = map(int, read().split())  # 격자크기, 플레이어 수, 라운드 수

board = []
score = [0] * (m + 1)

# 총 정보 3차원배열 입력
for i in range(n):
    row = list(map(int, read().split()))
    temp = []
    for gun in row:
        temp.append([gun])
    board.append(temp)


players = [[0, 0, 0, 0, 0] for _ in range(m + 1)]


def print_board():
    print("---board---")
    for row in board:
        print(row)
    print()


def print_players():
    print("---players---")
    print(players)
    print()


def print_score():
    print("---score---")
    print(score)
    print()


for i in range(1, m + 1):
    x, y, d, s = map(int, read().split())
    players[i] = [x - 1, y - 1, d, s, 0]
    # 플레이어 x좌표, 플레이어 y좌표, 방향, 초기능력치, 현재 공격력(총)


def move():
    d = players[player_num][DIRECTION]
    nx = players[player_num][X] + dx[d]
    ny = players[player_num][Y] + dy[d]
    # print("before d", arrow[d], d)

    # 격자 벗어나는 경우는 정반대 방향으로 설정
    if not (0 <= nx < n and 0 <= ny < n):
        players[player_num][DIRECTION] = (d + 2) % 4  # 방향 전환
        # print("after d", arrow[players[player_num][DIRECTION]], players[player_num][DIRECTION])
        nx = players[player_num][X] + dx[players[player_num][DIRECTION]]
        ny = players[player_num][Y] + dy[players[player_num][DIRECTION]]

    # 이동
    players[player_num][X] = nx
    players[player_num][Y] = ny

    return nx, ny


def get_gun(player_num, nx, ny):
    max_gun = -1
    idx = 0

    # 기존 총이 더 공격력이 큰 경우
    if players[player_num][GUN] >= max(board[nx][ny]):
        max_gun = players[player_num][GUN]
        return max_gun
    else:
        for i in range(len(board[nx][ny])):
            if board[nx][ny][i] > max_gun:
                max_gun = board[nx][ny][i]
                idx = i
                # print("총 줍기 board[nx][ny][i]", nx, ny, i)
    if players[player_num][GUN]:  # 기존에 총이 있던 경우는 해당 총을 내려놓는다
        # print("총 내려놓기")
        board[nx][ny][idx] = players[player_num][GUN]
    else:  # 총이 없던 경우는 그냥 가져간다
        # print("총 그냥 가져가기")
        board[nx][ny][idx] = 0

    return max_gun


def fight(i):
    cur_player = players[player_num][STAT] + players[player_num][GUN]
    new_player = players[i][STAT] + players[i][GUN]
    winner_num = 0
    loser_num = 0

    if cur_player > new_player:
        point = cur_player - new_player
        score[player_num] += point
        winner_num, loser_num = player_num, i
    elif cur_player < new_player:
        point = new_player - cur_player
        score[i] += point
        winner_num, loser_num = i, player_num
    else:
        if players[player_num][STAT] > players[i][STAT]:
            point = cur_player - new_player
            score[player_num] += point
            winner_num, loser_num = player_num, i
        else:
            point = new_player - cur_player
            score[i] += point
            winner_num, loser_num = i, player_num

        # print("---after fight---")
        # print_board()
        # print_players()
        # print_score()

    return winner_num, loser_num


# 이동할 방향에 플레이어 있는지 확인
def is_player_exist(me, nx, ny):
    for i in range(1, m + 1):
        if i == me:
            continue
        if players[i][X] == nx and players[i][Y] == ny:
            return True
    return False


# 2-2-2. 진 플레이어는 총을 그 자리에 내려놓고, 원래 방향대로 한 칸 이동
# 이동하려는 칸에 다른 플레이어가 있거나 격자 밖이면 오른쪽으로 90도 회전하면서 빈 칸이 보이는 순간 이동
# 해당 칸에 총이 있으면 공격력 가장 높은 총 획득
def lose_player_action(loser_num):
    # 총 내려 놓기
    if players[loser_num][GUN] > 0:
        board[players[loser_num][X]][players[loser_num][Y]].append(players[loser_num][GUN])
        players[loser_num][GUN] = 0

    d = players[loser_num][DIRECTION]

    # 플레이어가 있거나 격자 벗어나는 경우는 오른쪽 90도로 돌면서 확인
    for i in range(0, 4):
        players[loser_num][DIRECTION] = (d + i) % 4  # 방향 전환
        nx = players[loser_num][X] + dx[players[loser_num][DIRECTION]]
        ny = players[loser_num][Y] + dy[players[loser_num][DIRECTION]]
        if is_player_exist(loser_num, nx, ny) or not (0 <= nx < n and 0 <= ny < n):
            continue
        else:
            # 이동
            players[loser_num][X] = nx
            players[loser_num][Y] = ny

            # 총이 있으면 획득
            if max(board[nx][ny]) > 0:
                # print("===진 플레이어가 이동하면서 총 획득===")
                players[loser_num][GUN] = get_gun(loser_num, nx, ny)

            break


# 2-2-3. 이긴 플레이어는 떨어진 총과 원래 총 중 공격력 높은 총 획득 후 나머지 총은 격자에 모두 내려놓기
def win_player_action(winner_num):
    players[winner_num][GUN] = get_gun(winner_num, players[winner_num][X], players[winner_num][Y])


# 0. k 라운드 진행
for _ in range(k):
    # print(f"-----round {_+1}-----")
    for player_num in range(1, m + 1):
        # print("player_num", player_num, "\n")

        # 1-1. 플레이어 한 명씩 이동
        # 격자 벗어나면 정반대방향으로 1 이동
        nx, ny = move()
        # print("nx,ny", nx, ny)
        # print("===after move===")
        # print_board()
        # print_players()

        # 2-1. 이동한 방향에 플레이어가 없고 총이 있는 경우
        # max(가지고 있는 총, 놓여 있는 총들)
        # 나머지 총은 격자에 내려 놓음

        if not is_player_exist(player_num, nx, ny):
            if max(board[nx][ny]) > 0:
                players[player_num][GUN] = get_gun(player_num, nx, ny)

                # print("===after get gun===")
                # print_board()
                # print_players()

        # 2-2-1. (전투) 이동한 방향에 플레이어가 있는 경우
        # 초기능력치 + 총 공격력 합 비교
        # 이기면 초기능력치 + 공격력 차이만큼 포인트 획득
        else:
            for i in range(1, m + 1):
                if i == player_num:
                    continue
                if players[i][X] == players[player_num][X] and players[i][Y] == players[player_num][Y]:
                    winner_num, loser_num = fight(i)

                    # 2-2-2. 진 플레이어는 총을 그 자리에 내려놓고, 원래 방향대로 한 칸 이동
                    # 이동하려는 칸에 다른 플레이어가 있거나 격자 밖이면 오른쪽으로 90도 회전하면서 빈 칸이 보이는 순간 이동
                    # 해당 칸에 총이 있으면 공격력 가장 높은 총 획득
                    lose_player_action(loser_num)

                    # print("---after lose_player_action---")
                    # print_board()
                    # print_players()

                    # 2-2-3. 이긴 플레이어는 떨어진 총과 원래 총 중 공격력 높은 총 획득
                    win_player_action(winner_num)

                    # print("---after win_player_action---")
                    # print_board()
                    # print_players()

                    break

    # print_score()

    # 1~n번 플레이어까지 모두 진행하면 1라운드 종료

print(" ".join(map(str, score[1:])))
