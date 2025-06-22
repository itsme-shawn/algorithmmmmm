import sys
from collections import deque

read = sys.stdin.readline

n = int(read())  # 보드크기
k = int(read())  # 사과개수

apples = []
for _ in range(k):
    x, y = map(int, read().split())
    apples.append((x, y))

L = int(read())  # 방향전환횟수
turns = deque()
for _ in range(L):
    temp = read().split()
    turns.append((int(temp[0]), temp[1]))

board = [[0] * (n + 1) for _ in range(n + 1)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

d = 0  # 방향 ( 0 : 오, 1 : 아래, 2: 왼, 3: 위 )
t = 0  # 시간(초)
snake = deque([(1, 1)])  # 뱀 몸통 좌표
while True:
    t += 1  # 시간 증가
    # 다음 위치
    x = snake[-1][0] + dx[d]  # snake[-1] 은 뱀의 머리좌표
    y = snake[-1][1] + dy[d]

    if (x, y) in snake:  # 탈출조건1 : 다음 좌표가 뱀의 몸통과 겹치면 break
        print(t)
        break

    if x == 0 or y == 0 or x > n or y > n:  # 탈출조건2 : 벽을 뚫으면 break
        print(t)
        break

    snake.append((x, y))  # 머리 이동

    if (x, y) not in apples:  # 다음 칸에 사과가 없으면
        snake.popleft()  # 꼬리 제거
    if (x, y) in apples:  # 다음 칸에 사과를 먹었으면 사과 제거
        idx = apples.index((x, y))
        del apples[idx]

    # 회전방향 설정
    if turns and t == turns[0][0]:
        if turns[0][1] == "D":  # 오른쪽 전환
            d = (d + 1) % 4
        else:  # 왼쪽 전환
            d = (d + 3) % 4
        turns.popleft()
